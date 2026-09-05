"""Typeset reviewed Markdown manuscripts with ReportLab and 480 dpi math.

Usage: python build_pdf.py SOURCE OUTPUT --footer SHORT_TITLE
The source is never rewritten. Explicit TeX tags are preserved; untagged
equations remain unnumbered. Requires reportlab, matplotlib and Pillow.
"""
from pathlib import Path
from html import escape
import argparse, hashlib, json, os, re
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['mathtext.fontset']='dejavuserif'
from matplotlib import mathtext
from matplotlib.font_manager import FontProperties
from PIL import Image as PILImage
from reportlab.platypus import SimpleDocTemplate, Paragraph, Flowable, Table, TableStyle, Preformatted
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from math_compat import clean_math as prior_clean

ap=argparse.ArgumentParser();ap.add_argument('source',type=Path);ap.add_argument('output',type=Path);ap.add_argument('--footer',required=True)
args=ap.parse_args()
SOURCE=args.source.resolve();OUTPUT=args.output.resolve()
TMP=OUTPUT.parent/'qa'/OUTPUT.stem;TMP.mkdir(parents=True,exist_ok=True)
os.environ.setdefault('SOURCE_DATE_EPOCH','1788613200')
PAGE=(595.28,841.89);MARGIN=52;WIDTH=PAGE[0]-2*MARGIN
INK=HexColor('#20252B');GRAY=HexColor('#59616B')
FONTDIR=Path(matplotlib.get_data_path())/'fonts/ttf'
for name,file in [('Serif','DejaVuSerif.ttf'),('SerifBold','DejaVuSerif-Bold.ttf'),('SerifItalic','DejaVuSerif-Italic.ttf'),('Sans','DejaVuSans.ttf'),('SansBold','DejaVuSans-Bold.ttf'),('Mono','DejaVuSansMono.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONTDIR/file)))
pdfmetrics.registerFontFamily('Serif',normal='Serif',bold='SerifBold',italic='SerifItalic',boldItalic='SerifBold')
BODY=ParagraphStyle('body',fontName='Serif',fontSize=10.3,leading=16.1,spaceAfter=7.2,textColor=INK,autoLeading='max',allowWidows=0,allowOrphans=0)
HEAD=ParagraphStyle('head',fontName='SansBold',fontSize=12,leading=16,spaceBefore=14,spaceAfter=8,keepWithNext=True,textColor=INK)
SUB=ParagraphStyle('sub',parent=HEAD,fontSize=10.5,leading=14,spaceBefore=10,spaceAfter=7)
TITLE=ParagraphStyle('title',fontName='SerifBold',fontSize=20,leading=26,spaceAfter=14,textColor=INK)
META=ParagraphStyle('meta',fontName='Sans',fontSize=9,leading=13,spaceAfter=10,textColor=GRAY)
SMALL=ParagraphStyle('small',parent=BODY,fontSize=8.6,leading=12.3,spaceAfter=6)
CELL=ParagraphStyle('cell',parent=BODY,fontSize=8.1,leading=12,spaceAfter=0)
CODE=ParagraphStyle('code',fontName='Mono',fontSize=7.7,leading=11,spaceBefore=5,spaceAfter=9,textColor=INK)
cache={};ledger=[]

def clean_math(s):
    s=prior_clean(s)
    s=re.sub(r'\\le(?![A-Za-z])',r'\\leq',s);s=re.sub(r'\\ge(?![A-Za-z])',r'\\geq',s)
    s=re.sub(r'\\(?:displaystyle|textstyle)\b','',s)
    s=re.sub(r'\\bmod(?![A-Za-z])',r'\\,\\mathrm{mod}\\,',s)
    s=re.sub(r'\\lVert\b|\\rVert\b',r'\\Vert',s)
    s=re.sub(r'\\lvert\b|\\rvert\b','|',s)
    s=re.sub(r'\\rm\s+([A-Za-z]+)',r'\\mathrm{\1}',s)
    s=s.replace(r'\mathscr',r'\mathcal')
    s=re.sub(r'\\binom([0-9])([0-9])',r'\\binom{\1}{\2}',s)
    s=re.sub(r'\\sqrt\s*([A-Za-z0-9])',r'\\sqrt{\1}',s)
    return prior_clean(s)

def equation(tex,size=10.3):
    tex=clean_math(tex);key=(tex,size)
    if key not in cache:
        path=TMP/(hashlib.sha256((tex+str(size)).encode()).hexdigest()+'.png')
        try:mathtext.math_to_image('$'+tex+'$',path,dpi=480,prop=FontProperties(family='DejaVu Serif',size=size),color='#20252b')
        except Exception as exc:raise ValueError('Cannot typeset: '+tex) from exc
        with PILImage.open(path) as im:w,h=[v*72/480 for v in im.size]
        cache[key]=(path,w,h)
    return cache[key]

def inline(s,size=10.3):
    out=[];pos=0
    for m in re.finditer(r'\$([^$]+)\$[.,;:]?|`([^`]+)`|\[([^\]]+)\]\((https?://[^)]+)\)',s):
        out.append(escape(s[pos:m.start()]))
        if m.group(1) is not None:
            punctuation=m[0][-1] if m[0][-1] in '.,;:' else ''
            p,w,h=equation(m.group(1).replace(r'\sum',r'\Sigma')+punctuation,size)
            out.append(f'<img src="{p}" width="{w:.3f}" height="{h:.3f}" valign="middle"/>')
        elif m.group(2) is not None:out.append('<font name="Mono" size="7.8">'+escape(m.group(2))+'</font>')
        else:out.append('<link href="'+escape(m.group(4),quote=True)+'" color="#28506D">'+escape(m.group(3))+'</link>')
        pos=m.end()
    out.append(escape(s[pos:]));value=''.join(out)
    value=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',value)
    value=re.sub(r'\*([^*]+)\*',r'<i>\1</i>',value)
    return re.sub(r'(<img [^>]+/>)([.,;:])',r'<nobr>\1\2</nobr>',value)

class Display(Flowable):
    def __init__(self,raw):
        super().__init__();tags=re.findall(r'\\tag\{([^}]+)\}',raw)
        assert len(tags)<=1,raw
        self.tag=tags[0] if tags else None
        raw=re.sub(r'\\tag\{[^}]+\}','',raw).strip()
        chunks=[s.strip() for s in raw.split(r'\\') if s.strip()]
        available=WIDTH-(34 if self.tag else 8)
        if len(chunks)==1 and equation(raw,12.2)[1]>available and r'\qquad' in raw:
            chunks=[s.strip() for s in raw.split(r'\qquad') if s.strip()]
        self.lines=[equation(t,12.2) for t in chunks]
        self.scale=min(1,available/max(w for _,w,_ in self.lines))
        self.width=WIDTH;self.height=sum(h*self.scale for _,_,h in self.lines)+6*(len(chunks)-1)+14
        self.spaceBefore=1;self.spaceAfter=6
        ledger.append({'tag':self.tag,'tex':raw,'lines':len(chunks),'scale':self.scale})
    def draw(self):
        y=self.height-7;available=WIDTH-(26 if self.tag else 0)
        for p,w,h in self.lines:
            w*=self.scale;h*=self.scale;y-=h
            self.canv.drawImage(str(p),(available-w)/2,y,width=w,height=h,mask='auto');y-=6
        if self.tag:
            self.canv.setFont('Serif',9);self.canv.drawRightString(WIDTH-1,self.height/2-3,'('+self.tag+')')

def footer(c,doc):
    c.saveState();c.setFont('Sans',7.2);c.setFillColor(GRAY)
    c.drawString(MARGIN,29,'Lluis Eriksson | '+args.footer+' | ARR v1')
    c.drawRightString(PAGE[0]-MARGIN,29,str(doc.page));c.restoreState()

def main():
    text=SOURCE.read_text(encoding='utf-8-sig')
    for c in '\u2010\u2011\u2012\u2013\u2014':text=text.replace(c,'-')
    lines=text.splitlines();flow=[];i=0;refs=False;title=None
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('# '):title=line[2:];flow.append(Paragraph(escape(title),TITLE));i+=1;continue
        if line=='Lluis Eriksson' or line.startswith('Independent researcher.'):
            flow.append(Paragraph(escape(line),META));i+=1;continue
        if line.startswith('### '):flow.append(Paragraph(inline(line[4:],10.5),SUB));i+=1;continue
        if line.startswith('## '):
            name=line[3:];refs=name.lower()=='references' or name.startswith(('8. Antecedents,','10. Antecedents and'))
            flow.append(Paragraph(inline(name,12),HEAD));i+=1;continue
        if line==r'\[':
            eq=[];i+=1
            while i<len(lines) and lines[i].strip()!=r'\]':eq.append(lines[i]);i+=1
            assert i<len(lines);flow.append(Display(' '.join(eq)));i+=1;continue
        if line.startswith('```'):
            block=[];i+=1
            while i<len(lines) and not lines[i].strip().startswith('```'):block.append(lines[i]);i+=1
            flow.append(Preformatted('\n'.join(block),CODE,maxLineLength=93));i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=lines[i].strip().strip('|').split('|');i+=1
                if all(re.fullmatch(r'[\s:-]+',v) for v in row):continue
                rows.append([Paragraph(inline(v.strip(),8.1),CELL) for v in row])
            n=len(rows[0]);widths=[WIDTH/n]*n
            if n==3:widths=[WIDTH*.23,WIDTH*.36,WIDTH*.41]
            if n==2:widths=[WIDTH*.35,WIDTH*.65]
            table=Table(rows,colWidths=widths,repeatRows=1,hAlign='CENTER')
            table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('BACKGROUND',(0,0),(-1,0),HexColor('#EEF1F4')),('LINEBELOW',(0,0),(-1,0),.6,GRAY),('LINEBELOW',(0,-1),(-1,-1),.6,GRAY)]))
            table.spaceAfter=12;flow.append(table);continue
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith('#') and lines[i].strip()!=r'\[' and not lines[i].lstrip().startswith(('|','```','- ','* ')):
            para.append(lines[i].strip());i+=1
        s=' '.join(para)
        if s.startswith(('- ','* ')):s='• '+s[2:]
        flow.append(Paragraph(inline(s,8.6 if refs else 10.3),SMALL if refs else BODY))
    for idx in range(len(flow)-1):
        f=flow[idx]
        if isinstance(f,Paragraph) and isinstance(flow[idx+1],(Display,Table)):f.keepWithNext=True
        elif isinstance(f,Paragraph) and f.getPlainText().endswith(':'):f.keepWithNext=True
    doc=SimpleDocTemplate(str(OUTPUT),pagesize=PAGE,leftMargin=MARGIN,rightMargin=MARGIN,topMargin=44,bottomMargin=51,title=title,author='Lluis Eriksson',subject='Final research manuscript - ARR v1',invariant=1)
    doc.build(flow,onFirstPage=footer,onLaterPages=footer)
    report={'source':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'pdf':str(OUTPUT),'pdf_sha256':hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),'display_equations':len(ledger),'math_fragments':len(cache),'equations':ledger}
    (TMP/'build_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='equations'},indent=2))
    print('Shrunk equations:',[(z['tag'],round(z['scale'],3)) for z in ledger if z['scale']<.85])

if __name__=='__main__':main()
