"""Typeset the consolidated manuscript using ReportLab and 480 dpi mathematics."""
from pathlib import Path
from html import escape
import hashlib, re, json, importlib.util, os
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['mathtext.fontset']='dejavuserif'
from matplotlib import mathtext
from matplotlib.font_manager import FontProperties
from PIL import Image as PILImage
from reportlab.platypus import SimpleDocTemplate, Paragraph, Flowable, Table, TableStyle, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'paper.md'
OUTPUT=ROOT/'paper.pdf'
TMP=ROOT/'tmp/pdfs/inertia_revision3'
TMP.mkdir(parents=True,exist_ok=True)
OUTPUT.parent.mkdir(parents=True,exist_ok=True)
os.environ.setdefault('SOURCE_DATE_EPOCH','1788588538')
PAGE=(595.28,841.89); MARGIN=52; WIDTH=PAGE[0]-2*MARGIN
INK=HexColor('#20252B'); GRAY=HexColor('#59616B')
FONTDIR=Path(matplotlib.get_data_path())/'fonts/ttf'
for name,file in [('Serif','DejaVuSerif.ttf'),('SerifBold','DejaVuSerif-Bold.ttf'),('SerifItalic','DejaVuSerif-Italic.ttf'),('Sans','DejaVuSans.ttf'),('SansBold','DejaVuSans-Bold.ttf'),('Mono','DejaVuSansMono.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONTDIR/file)))
pdfmetrics.registerFontFamily('Serif',normal='Serif',bold='SerifBold',italic='SerifItalic',boldItalic='SerifBold')
BODY=ParagraphStyle('body',fontName='Serif',fontSize=10.3,leading=16.1,spaceAfter=7.2,textColor=INK,autoLeading='max',allowWidows=0,allowOrphans=0)
HEAD=ParagraphStyle('head',fontName='SansBold',fontSize=12,leading=16,spaceBefore=14,spaceAfter=8,keepWithNext=True,textColor=INK)
SUB=ParagraphStyle('sub',parent=HEAD,fontSize=10.5,leading=14,spaceBefore=10,spaceAfter=7)
TITLE=ParagraphStyle('title',fontName='SerifBold',fontSize=21,leading=26,spaceAfter=14,textColor=INK)
META=ParagraphStyle('meta',fontName='Sans',fontSize=9,leading=13,spaceAfter=13,textColor=GRAY)
SMALL=ParagraphStyle('small',parent=BODY,fontSize=8.6,leading=12.3,spaceAfter=6)
CELL=ParagraphStyle('cell',parent=BODY,fontSize=9.2,leading=14,spaceAfter=0,alignment=1)

# An exact copy of the previous Mathtext compatibility routine is packaged with the source.
spec=importlib.util.spec_from_file_location('math_compat',ROOT/'typeset/math_compat.py')
compat=importlib.util.module_from_spec(spec);spec.loader.exec_module(compat)
clean_math=compat.clean_math
cache={}; ledger=[]

def equation(tex,size=10.3):
    tex=clean_math(tex)
    key=(tex,size)
    if key not in cache:
        path=TMP/(hashlib.sha256((tex+str(size)).encode()).hexdigest()+'.png')
        mathtext.math_to_image('$'+tex+'$',path,dpi=480,prop=FontProperties(family='DejaVu Serif',size=size),color='#20252b')
        with PILImage.open(path) as im:w,h=[v*72/480 for v in im.size]
        cache[key]=(path,w,h)
    return cache[key]

def inline(s,size=10.3):
    out=[];pos=0
    for m in re.finditer(r'\$([^$]+)\$|`([^`]+)`|\[([^\]]+)\]\((https?://[^)]+)\)',s):
        out.append(escape(s[pos:m.start()]))
        if m.group(1) is not None:
            p,w,h=equation(m.group(1).replace(r'\sum',r'\Sigma'),size)
            out.append(f'<img src="{p}" width="{w:.3f}" height="{h:.3f}" valign="middle"/>')
        elif m.group(2) is not None:out.append('<font name="Mono" size="8.3">'+escape(m.group(2))+'</font>')
        else:out.append('<link href="'+escape(m.group(4),quote=True)+'" color="#28506D">'+escape(m.group(3))+'</link>')
        pos=m.end()
    out.append(escape(s[pos:]));value=''.join(out)
    value=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',value)
    value=re.sub(r'\*([^*]+)\*',r'<i>\1</i>',value)
    return re.sub(r'(<img [^>]+/>)([.,;:])',r'<nobr>\1\2</nobr>',value)

class Display(Flowable):
    def __init__(self,raw):
        super().__init__();self.tag=str(len(ledger)+1)
        chunks=[s.strip() for s in raw.split(r'\\') if s.strip()]
        # Split independent definitions/conditions before shrinking mathematical type.
        if len(chunks)==1 and equation(raw,12.2)[1]>WIDTH-34 and r'\qquad' in raw:
            chunks=[s.strip() for s in raw.split(r'\qquad') if s.strip()]
        self.lines=[equation(t,12.2) for t in chunks]
        self.scale=min(1,(WIDTH-34)/max(w for _,w,_ in self.lines))
        self.width=WIDTH;self.height=sum(h*self.scale for _,_,h in self.lines)+6*(len(chunks)-1)+14
        self.spaceBefore=1;self.spaceAfter=6
        ledger.append({'tag':self.tag,'tex':raw,'lines':len(chunks),'scale':self.scale})
    def draw(self):
        y=self.height-7
        for p,w,h in self.lines:
            w*=self.scale;h*=self.scale;y-=h
            self.canv.drawImage(str(p),(WIDTH-26-w)/2,y,width=w,height=h,mask='auto');y-=6
        self.canv.setFont('Serif',9)
        self.canv.drawRightString(WIDTH-1,self.height/2-3,'('+self.tag+')')

def footer(c,doc):
    c.saveState();c.setFont('Sans',7.4);c.setFillColor(GRAY)
    c.drawString(MARGIN,29,'Lluis Eriksson | Sharp inertia ceilings and optimal stability | Review revision 3')
    c.drawRightString(PAGE[0]-MARGIN,29,str(doc.page));c.restoreState()

def main():
    text=SOURCE.read_text(encoding='utf-8')
    for c in '\u2010\u2011\u2012\u2013\u2014':text=text.replace(c,'-')
    lines=text.splitlines();flow=[];i=0;refs=False
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('# '):flow.append(Paragraph(escape(line[2:]),TITLE));i+=1;continue
        if line.startswith('Lluis Eriksson |'):
            flow.append(Paragraph('Lluis Eriksson<br/>Independent researcher | 5 September 2026<br/>Consolidated review revision 3',META));i+=1;continue
        if line.startswith('### '):flow.append(Paragraph(escape(line[4:]),SUB));i+=1;continue
        if line.startswith('## '):
            name=line[3:];refs=name=='References'
            if refs:flow.append(PageBreak())
            flow.append(Paragraph(escape(name),HEAD));i+=1;continue
        if line==r'\[':
            eq=[];i+=1
            while i<len(lines) and lines[i].strip()!=r'\]':eq.append(lines[i]);i+=1
            assert i<len(lines);flow.append(Display(' '.join(eq)));i+=1;continue
        if line.startswith('| '):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('| '):
                row=lines[i].strip().strip('|').split('|');i+=1
                if all(re.fullmatch(r'[\s:-]+',v) for v in row):continue
                rows.append([Paragraph(inline(v.strip(),9.4),CELL) for v in row])
            table=Table(rows,colWidths=[65,250,80,WIDTH-395],repeatRows=1,hAlign='CENTER')
            table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('BACKGROUND',(0,0),(-1,0),HexColor('#EEF1F4')),('LINEBELOW',(0,0),(-1,0),.6,GRAY),('LINEBELOW',(0,-1),(-1,-1),.6,GRAY)]))
            table.spaceAfter=12;flow.append(table);continue
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith('#') and lines[i].strip()!=r'\[' and not lines[i].startswith('| '):
            if lines[i].startswith('- '):break
            para.append(lines[i].strip());i+=1
        s=' '.join(para).removeprefix('- ')
        flow.append(Paragraph(inline(s,8.6 if refs else 10.3),SMALL if refs else BODY))
    for idx in range(len(flow)-1):
        f=flow[idx]
        if isinstance(f,Paragraph) and isinstance(flow[idx+1],(Display,Table)):f.keepWithNext=True
        elif isinstance(f,Paragraph) and f.getPlainText().endswith(':'):f.keepWithNext=True
    doc=SimpleDocTemplate(str(OUTPUT),pagesize=PAGE,leftMargin=MARGIN,rightMargin=MARGIN,topMargin=44,bottomMargin=51,
        title='Sharp inertia ceilings and optimal stability for inverse self-commutators',author='Lluis Eriksson',
        subject='Consolidated review: optimal stability including balanced multiplicity three',invariant=1)
    doc.build(flow,onFirstPage=footer,onLaterPages=footer)
    report={'source':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'pdf':str(OUTPUT),'pdf_sha256':hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
            'display_equations':len(ledger),'math_fragments':len(cache),'equations':ledger}
    (TMP/'build_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='equations'},indent=2))
    print('Shrunk equations:',[(z['tag'],round(z['scale'],3)) for z in ledger if z['scale']<.85])

if __name__=='__main__':main()
