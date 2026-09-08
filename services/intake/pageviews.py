"""Opt-in daily totals. No visitor IDs, raw request logs or private-page collection."""
import json
import threading
import time
import urllib.request
from datetime import timedelta
from pathlib import Path

from flask import Response, abort, g, render_template, request

SCHEMA = '''
CREATE TABLE IF NOT EXISTS public_pageviews (
 day TEXT NOT NULL, path TEXT NOT NULL, views INTEGER NOT NULL CHECK(views>0),
 PRIMARY KEY(day,path)
);
'''
ORIGINS = {'https://airr.science', 'https://www.airr.science'}
MANIFEST_URL = 'https://airr.science/analytics-pages.json'


def validate_manifest(value):
    if not isinstance(value, dict) or not 1 <= len(value) <= 10000:
        raise ValueError('Invalid public page catalogue')
    for path, title in value.items():
        if (not isinstance(path, str) or not path.startswith('/') or not path.endswith('/')
                or len(path) > 250 or '//' in path or any(c in path for c in '?#\\\r\n')
                or path.startswith(('/admin/', '/case/', '/editor/', '/api/'))
                or not isinstance(title, str) or not 1 <= len(title) <= 400):
            raise ValueError('Invalid public page entry')
    return value


def migrate(db):
    db.executescript(SCHEMA)
    db.commit()


def sweep(db, today):
    db.execute('DELETE FROM public_pageviews WHERE day < ?',
               ((today - timedelta(days=399)).isoformat(),))


def install(app, a):
    lock = threading.Lock()
    state = {'pages': {}, 'refresh_at': 0., 'minute': -1, 'requests': 0, 'swept': ''}
    try:
        state['pages'] = validate_manifest(json.loads(Path(app.config['ANALYTICS_MANIFEST']).read_text(encoding='utf-8')))
    except (OSError, ValueError):
        pass

    def catalogue():
        with lock:
            if app.config['TESTING'] or time.monotonic() < state['refresh_at']:
                return dict(state['pages'])
            state['refresh_at'] = time.monotonic() + 600
        # Only this fixed public URL is fetched; no user-controlled URL or private data.
        try:
            with urllib.request.urlopen(MANIFEST_URL, timeout=2) as response:
                if response.geturl() != MANIFEST_URL:
                    raise ValueError('Unexpected catalogue redirect')
                raw = response.read(1_000_001)
            if len(raw) > 1_000_000:
                raise ValueError('Catalogue too large')
            pages = validate_manifest(json.loads(raw))
            with lock:
                state['pages'] = pages
        except (OSError, ValueError):
            pass  # Keep the bundled/last good public catalogue; never store arbitrary paths.
        return dict(state['pages'])

    @app.route('/api/v1/pageviews', methods=['POST', 'OPTIONS'])
    def collect_pageview():
        if not app.config['ANALYTICS_ENABLED']:
            abort(503)
        origin = request.headers.get('Origin', '')
        if origin not in ORIGINS:
            abort(403)
        response = Response(status=204)
        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Vary'] = 'Origin'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        if request.method == 'OPTIONS':
            return response
        if request.content_length is None or request.content_length > 512:
            abort(413)
        if request.mimetype != 'application/json':
            abort(415)
        payload = request.get_json(silent=True)
        if (not isinstance(payload, dict) or set(payload) != {'path', 'consent'}
                or payload['consent'] != 'aggregate-v1' or not isinstance(payload['path'], str)):
            abort(400)
        # A global, per-worker burst limit does not create or retain visitor identifiers.
        with lock:
            minute = int(time.monotonic() // 60)
            if minute != state['minute']:
                state.update(minute=minute, requests=0)
            state['requests'] += 1
            if state['requests'] > 120:
                abort(429)
        if payload['path'] not in catalogue():
            abort(400)
        day = a.now().date().isoformat()
        db = a.get_db()
        db.execute('''INSERT INTO public_pageviews(day,path,views) VALUES(?,?,1)
          ON CONFLICT(day,path) DO UPDATE SET views=views+1''', (day, payload['path']))
        if state['swept'] != day:
            sweep(db, a.now().date())
        db.commit()
        state['swept'] = day
        return response

    @app.get('/admin/statistics')
    @a.login_required
    def pageview_dashboard():
        if g.user['role'] != 'operator' or not g.user['totp_secret']:
            abort(403)
        try:
            days = int(request.args.get('days', '30'))
        except ValueError:
            abort(400)
        if days not in {7, 30, 90, 365}:
            abort(400)
        today = a.now().date()
        since = (today - timedelta(days=days - 1)).isoformat()
        db = a.get_db()
        daily = dict(db.execute('SELECT day,SUM(views) FROM public_pageviews WHERE day>=? GROUP BY day', (since,)))
        series = [{'day': (today-timedelta(days=offset)).isoformat(),
                   'views': daily.get((today-timedelta(days=offset)).isoformat(), 0)}
                  for offset in range(days-1, -1, -1)]
        titles = catalogue()
        top = [{'path': row['path'], 'views': row['views'], 'title': titles.get(row['path'], row['path'])}
               for row in db.execute('SELECT path,SUM(views) AS views FROM public_pageviews WHERE day>=? GROUP BY path ORDER BY views DESC,path LIMIT 40', (since,))]
        return render_template('statistics.html', days=days, series=series, top=top,
                               total=sum(daily.values()), today=daily.get(today.isoformat(), 0),
                               maximum=max([row['views'] for row in series]+[1]),
                               enabled=app.config['ANALYTICS_ENABLED'])
