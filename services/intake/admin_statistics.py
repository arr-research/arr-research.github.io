"""Read-only operator reporting over existing aggregates and account records."""
import csv
import io
import json
import re
import threading
import time
import urllib.request
from datetime import date, datetime, timedelta

from flask import abort

METRICS_URL = 'https://airr.science/metrics.json'
PDF_LABEL = re.compile(r'^/(papers|notes)/[^/]+/versions/[^/]+/pdf/$')
STATUS_LABELS = {
    'quarantined': 'En cuarentena', 'eligible': 'Pendiente de evaluación',
    'under_assessment': 'En evaluación', 'changes_requested': 'Cambios solicitados',
    'awaiting_independent_decision': 'Pendiente de decisión independiente',
    'accepted_for_publication': 'Aceptado para publicación', 'declined': 'Rechazado',
    'withdrawn': 'Retirado', 'removed': 'Eliminado', 'legal_hold': 'Conservación legal',
    'superseded': 'Sustituido por otra versión', 'appeal_pending': 'Recurso pendiente',
}


def reporting_range(args, today):
    earliest = today - timedelta(days=399)
    try:
        if 'start' in args or 'end' in args:
            start, end = date.fromisoformat(args['start']), date.fromisoformat(args['end'])
        elif args.get('period') == 'month':
            start, end = today.replace(day=1), today
        else:
            days = int(args.get('days', '30'))
            if days not in {7, 30, 90, 365}:
                raise ValueError()
            start, end = today - timedelta(days=days - 1), today
        if not earliest <= start <= end <= today:
            raise ValueError()
    except (ValueError, KeyError, TypeError):
        abort(400, 'Elige fechas válidas dentro de los últimos 400 días, sin fechas futuras.')
    return start, end


def validate_downloads(value):
    if not isinstance(value, dict) or value.get('schema_version') != '1.0':
        raise ValueError('Unknown metrics schema')
    if not isinstance(value.get('downloads'), dict) or value['downloads'].get('provider') != 'GitHub Releases':
        raise ValueError('Unknown download source')
    stamp = value.get('generated_at')
    if not isinstance(stamp, str) or len(stamp) > 50 or datetime.fromisoformat(stamp).tzinfo is None:
        raise ValueError('Invalid timestamp')
    papers = value.get('papers')
    if not isinstance(papers, dict) or len(papers) > 10000:
        raise ValueError('Invalid paper metrics')
    rows = []
    for paper_id, metrics in papers.items():
        if not re.fullmatch(r'ARR-\d{4}-[A-Z0-9]{16}', paper_id) or not isinstance(metrics, dict):
            raise ValueError('Invalid paper identifier')
        count = metrics.get('pdf_downloads')
        if type(count) is not int or not 0 <= count <= 10**12:
            raise ValueError('Invalid download count')
        rows.append({'paper_id': paper_id, 'downloads': count})
    return {'generated_at': stamp, 'total': sum(r['downloads'] for r in rows),
            'rows': sorted(rows, key=lambda r: (-r['downloads'], r['paper_id']))[:20]}


def install_download_reader(app):
    # Only the public snapshot is fetched, on dashboard requests. No new job,
    # credential, browser tracking or private data transfer is introduced.
    lock = threading.Lock()
    cache = {'value': None, 'retry_at': 0, 'failed': False}

    def read():
        with lock:
            if app.config['TESTING']:
                fixture = app.config.get('ADMIN_DOWNLOADS_SNAPSHOT')
                return (validate_downloads(fixture) if fixture else None), False
            if time.monotonic() >= cache['retry_at']:
                cache['retry_at'] = time.monotonic() + 600
                try:
                    with urllib.request.urlopen(METRICS_URL, timeout=2) as response:
                        if response.geturl() != METRICS_URL:
                            raise ValueError('Unexpected metrics redirect')
                        raw = response.read(2_000_001)
                    if len(raw) > 2_000_000:
                        raise ValueError('Metrics too large')
                    cache['value'] = validate_downloads(json.loads(raw))
                    cache['failed'] = False
                except (OSError, ValueError, TypeError):
                    cache['failed'] = True
            return cache['value'], cache['failed']
    return read


def daily_series(db, start, end):
    values = {}
    day = start
    while day <= end:
        values[day.isoformat()] = {'day': day.isoformat(), 'views': 0, 'pdfs': 0,
                                  'accounts': 0, 'submissions': 0}
        day += timedelta(days=1)
    for day, path, count in db.execute(
            'SELECT day,path,views FROM public_pageviews WHERE day BETWEEN ? AND ?',
            (start.isoformat(), end.isoformat())):
        values[day]['pdfs' if PDF_LABEL.match(path) else 'views'] += count
    for table, metric in [('private_accounts', 'accounts'), ('submissions', 'submissions')]:
        for day, count in db.execute(
                f'SELECT substr(created_at,1,10),COUNT(*) FROM {table} '
                'WHERE created_at>=? AND created_at<? GROUP BY substr(created_at,1,10)',
                (start.isoformat(), (end + timedelta(days=1)).isoformat())):
            values[day][metric] = count
    return list(values.values())


def csv_daily(series):
    stream = io.StringIO(newline='')
    writer = csv.writer(stream)
    writer.writerow(['date_utc', 'consenting_page_views', 'consenting_pdf_opens',
                     'registered_workspaces', 'private_submissions'])
    for row in series:
        writer.writerow([row[k] for k in ('day', 'views', 'pdfs', 'accounts', 'submissions')])
    return stream.getvalue()


def dashboard_data(db, start, end, today, titles, account_page=1):
    days = (end - start).days + 1
    series = daily_series(db, start, end)
    previous_start, previous_end = start - timedelta(days=days), start - timedelta(days=1)
    first, last = db.execute('SELECT MIN(day),MAX(day) FROM public_pageviews').fetchone()
    comparison_available = bool(first and previous_start.isoformat() >= first and
                                previous_start >= today - timedelta(days=399))
    previous = daily_series(db, previous_start, previous_end) if comparison_available else []
    totals = {key: sum(row[key] for row in series) for key in ('views', 'pdfs', 'accounts', 'submissions')}
    previous_totals = {key: sum(row[key] for row in previous) for key in totals}
    by_path = db.execute('SELECT path,SUM(views) AS views FROM public_pageviews '
                         'WHERE day BETWEEN ? AND ? GROUP BY path ORDER BY views DESC,path',
                         (start.isoformat(), end.isoformat())).fetchall()
    rows = [{'path': path, 'views': count, 'title': titles.get(path, path)} for path, count in by_path]
    charts = []
    for key, label in [('views', 'Visitas registradas'), ('pdfs', 'Aperturas de PDF'),
                       ('accounts', 'Nuevas cuentas privadas'), ('submissions', 'Envíos recibidos')]:
        maximum = max([row[key] for row in series] + [1])
        # The same series also appears as an accessible table and CSV. SVG adds
        # no third-party script and remains usable under the existing CSP.
        points = ' '.join(f'{12 + i * 576 / max(days-1, 1):.2f},{132-row[key]*112/maximum:.2f}'
                          for i, row in enumerate(series))
        charts.append({'key': key, 'label': label, 'points': points, 'maximum': maximum,
                       'total': totals[key], 'previous': previous_totals[key],
                       'change': totals[key] - previous_totals[key]})
    account_count = db.execute('SELECT COUNT(*) FROM users').fetchone()[0]
    account_pages = max(1, (account_count + 49) // 50)
    if not 1 <= account_page <= account_pages:
        abort(400, 'Página de cuentas fuera de rango.')
    # Explicit fields: never pass credential hashes, recovery material, email
    # addresses or token values into a template or export.
    accounts = [dict(row) for row in db.execute('''
      SELECT u.id,COALESCE(i.name,p.alias,u.display_name) AS name,u.role,u.active,
             u.created_at,p.last_seen_at,p.identity_kind,i.id AS agent_id,
             i.state AS agent_state,i.expires_at AS agent_expires_at,
             (SELECT COUNT(*) FROM submissions s WHERE s.user_id=u.id) AS submissions
      FROM users u LEFT JOIN private_accounts p ON p.user_id=u.id
      LEFT JOIN independent_agents i ON i.user_id=u.id
      ORDER BY u.created_at DESC,u.id DESC LIMIT 50 OFFSET ?''', ((account_page-1)*50,))]
    workspace_counts = {row[0]: row[1] for row in db.execute(
        'SELECT identity_kind,COUNT(*) FROM private_accounts GROUP BY identity_kind')}
    submissions = dict(db.execute('SELECT status,COUNT(*) FROM submissions GROUP BY status'))
    recent = [dict(row) for row in db.execute(
        'SELECT id,title,status,created_at FROM submissions WHERE created_at>=? AND created_at<? '
        'ORDER BY created_at DESC,id DESC LIMIT 12',
        (start.isoformat(), (end+timedelta(days=1)).isoformat()))]
    return dict(days=days, start=start.isoformat(), end=end.isoformat(), series=series,
                total=totals['views'], pdf_total=totals['pdfs'], totals=totals,
                today=next((r['views'] for r in series if r['day']==today.isoformat()), 0),
                pdf_today=next((r['pdfs'] for r in series if r['day']==today.isoformat()), 0),
                top=[r for r in rows if not PDF_LABEL.match(r['path'])][:40],
                top_pdfs=[r for r in rows if PDF_LABEL.match(r['path'])][:40],
                maximum=max([r['views'] for r in series]+[1]), charts=charts,
                previous_start=previous_start.isoformat(), previous_end=previous_end.isoformat(),
                comparison_available=comparison_available, includes_today=end==today,
                earliest=(today-timedelta(days=399)).isoformat(), today_date=today.isoformat(),
                first_recorded=first, last_recorded=last, accounts=accounts,
                account_count=account_count, account_page=account_page, account_pages=account_pages,
                workspaces=sum(workspace_counts.values()), workspace_counts=workspace_counts,
                staff=db.execute("SELECT COUNT(*) FROM users WHERE role IN ('operator','independent_editor')").fetchone()[0],
                submitters=db.execute('SELECT COUNT(DISTINCT user_id) FROM submissions').fetchone()[0],
                submission_count=sum(submissions.values()), statuses=submissions,
                status_labels=STATUS_LABELS, recent_submissions=recent)
