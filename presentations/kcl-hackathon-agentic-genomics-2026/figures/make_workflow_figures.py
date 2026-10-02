#!/usr/bin/env python3
"""Three native dark-theme workflow graphs (Fig 1 design, Fig 2 result, Fig 3
paradox) to replace the white paper PNGs in the KCL agentic-genomics deck.
All numbers are the real reported aggregates from the bioRxiv preprint."""
import os
DIR = os.path.dirname(os.path.abspath(__file__))

CARD="#161b22"; BORDER="#30363d"; TX="#e6edf3"; MUT="#adbac7"; DIM="#6e7681"
GREEN="#56d364"; BLUE="#58a6ff"; RED="#ffa198"; HOT="#f85149"; ORANGE="#e3b341"
FONT="font-family='Segoe UI, system-ui, sans-serif'"
COND=[("Free-prompted","#e06c5e"),("Retrieval-augmented","#e3b341"),
      ("Skill-reasoning","#58a6ff"),("Skill-execution","#1f6feb"),
      ("Answer-supplied","#56d364")]
X=chr(0x00d7); MID=chr(0x00b7); TRI=chr(0x25b2)

def T(s,x,y,t,fill=TX,size=15,w="400",a="start",it=False):
    st=" font-style='italic'" if it else ""
    s.append(f"<text x='{x:.1f}' y='{y:.1f}' fill='{fill}' font-size='{size}' font-weight='{w}' text-anchor='{a}'{st}>{t}</text>")
def B(s,x,y,w,h,fill,stroke=None,rx=8,sw=1.5):
    st=f" stroke='{stroke}' stroke-width='{sw}'" if stroke else ""
    s.append(f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='{rx}' fill='{fill}'{st}/>")
def harrow(s,x1,y,x2,col=DIM,wd=2):
    s.append(f"<line x1='{x1:.1f}' y1='{y:.1f}' x2='{x2:.1f}' y2='{y:.1f}' stroke='{col}' stroke-width='{wd}'/>")
    s.append(f"<path d='M{x2:.1f} {y:.1f} l-9 -5 l0 10 z' fill='{col}'/>")
def line(s,x1,y1,x2,y2,col,wd=1):
    s.append(f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{col}' stroke-width='{wd}'/>")
def check(s,cx,cy,col=GREEN):
    s.append(f"<path d='M{cx-7:.1f} {cy:.1f} l5 6 l10 -14' stroke='{col}' stroke-width='2.8' fill='none' stroke-linecap='round' stroke-linejoin='round'/>")
def write(name,w,h,s):
    s=[f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' {FONT}>"]+s+["</svg>"]
    open(os.path.join(DIR,name),"w").write("\n".join(s)); print("wrote",name)

def fig_design():
    s=[]; W=1200
    T(s,40,34,"THE SCALE",DIM,13,"700")
    parts=[("110","CPIC Level A cases"),("9","frontier LLMs"),("3","ancestries EUR/AMR/AFR"),("3","replicates")]
    bx,by,bw,bh,gap=40,50,196,66,34
    for i,(n,lab) in enumerate(parts):
        x=bx+i*(bw+gap); B(s,x,by,bw,bh,CARD,BORDER)
        T(s,x+bw/2,by+34,n,BLUE,26,"800","middle"); T(s,x+bw/2,by+54,lab,MUT,12.5,"400","middle")
        if i<3: T(s,x+bw+gap/2,by+42,X,DIM,22,"700","middle")
    eqx=bx+4*(bw+gap)-gap+16
    T(s,eqx-4,by+42,"=",DIM,22,"700","middle"); B(s,eqx+10,by,244,bh,"#0f2a16",GREEN)
    T(s,eqx+132,by+32,"44,550",GREEN,28,"800","middle"); T(s,eqx+132,by+53,"scored evaluations",MUT,12.5,"400","middle")
    T(s,40,176,f"THE WORKFLOW {MID} a five-condition constraint gradient",DIM,13,"700")
    cy,ch=196,96; cw=200; cgap=15; total=5*cw+4*cgap; cx0=(W-total)/2
    subs=["reasons from prior","reasons over CPIC text","applies skill rules","skill computes in code","deterministic control"]
    for i,(name,col) in enumerate(COND):
        x=cx0+i*(cw+cgap); B(s,x,cy,cw,ch,col,None,10)
        T(s,x+cw/2,cy+42,name,"#0d1117",16.5,"800","middle"); T(s,x+cw/2,cy+66,subs[i],"#0d1117",12,"600","middle")
        if i<4: harrow(s,x+cw+1,cy+ch/2,x+cw+cgap-2,DIM,2)
    by2=cy+ch+30
    line(s,cx0,by2,cx0+total,by2,BORDER,2); s.append(f"<path d='M{cx0+total} {by2} l-10 -5 l0 10 z' fill='{BORDER}'/>")
    T(s,cx0,by2+22,"correctness in the stochastic model","#e06c5e",13.5,"600"); T(s,cx0,by2+40,"stochastic, unauditable",DIM,12,"400","start",True)
    T(s,cx0+total,by2+22,"correctness in the executed skill",GREEN,13.5,"600","end"); T(s,cx0+total,by2+40,"deterministic, auditable, model-invariant",DIM,12,"400","end",True)
    T(s,40,398,f"TWO ARMS {MID} does curated accuracy transfer to real genomes?",DIM,13,"700")
    ay,ah=414,200; lx,lw=50,470
    B(s,lx,ay,lw,ah,CARD,BORDER,12)
    T(s,lx+lw/2,ay+36,"Curated analytical benchmark",TX,17,"700","middle"); T(s,lx+lw/2,ay+58,f"known CPIC ground truth {MID} balanced lethal-class coverage",MUT,12.5,"400","middle")
    for i,(_,col) in enumerate(COND): s.append(f"<circle cx='{lx+lw/2-2*46+i*46:.1f}' cy='{ay+106}' r='15' fill='{col}'/>")
    T(s,lx+lw/2,ay+152,"isolates WHERE correctness must reside",MUT,13,"600","middle"); T(s,lx+lw/2,ay+176,"curated accuracy reaches ~96%",GREEN,14,"700","middle")
    mx=lx+lw+18; harrow(s,mx,ay+ah/2,mx+40,DIM,2.5)
    rx=mx+56; rw=576; B(s,rx,ay,rw,ah,CARD,"#3a2a2a",12)
    T(s,rx+rw/2,ay+36,"Real-genome validation",TX,17,"700","middle"); T(s,rx+rw/2,ay+58,f"PyPGx diplotypes {MID} >7,000 individuals {MID} 3 cohorts",MUT,12.5,"400","middle")
    coh=[("72%","European","Corpas family",GREEN),("51%","Latin American","Peruvian Genome",ORANGE),("40%","East African","Uganda Genome",RED)]
    cohw=168; cohgap=14; cx1=rx+(rw-(3*cohw+2*cohgap))/2
    for i,(pct,anc,c,col) in enumerate(coh):
        x=cx1+i*(cohw+cohgap); B(s,x,ay+76,cohw,88,"#0d1117",BORDER,8)
        T(s,x+cohw/2,ay+118,pct,col,30,"800","middle"); T(s,x+cohw/2,ay+140,anc,TX,13,"600","middle"); T(s,x+cohw/2,ay+158,c,DIM,11.5,"400","middle")
    T(s,rx+rw/2,ay+186,"it does not transfer; it degrades by ancestry",RED,13.5,"700","middle")
    write("design-workflow.svg",W,640,s)

def fig_result():
    s=[]; W=1200
    T(s,40,34,"A  PHENOTYPE ACCURACY  (aggregate over 9 frontier models)",DIM,13,"700")
    accs=[80.6,89.5,95.5,93.3,100.0]; x0,x1=92,1110; ytop,ybot=66,248; lo,hi=60,100
    yv=lambda v: ybot-(v-lo)/(hi-lo)*(ybot-ytop)
    for g in range(lo,hi+1,10):
        y=yv(g); line(s,x0,y,x1,y,"#21262d",1); T(s,x0-12,y+4,f"{g}",DIM,11,"400","end")
    T(s,x0-12,ytop-6,"%",DIM,11,"400","end")
    colw=(x1-x0)/5; bw=112
    for i,((name,col),v) in enumerate(zip(COND,accs)):
        cx=x0+colw*i+colw/2; B(s,cx-bw/2,yv(v),bw,ybot-yv(v),col,None,6)
        T(s,cx,yv(v)-10,f"{v:.1f}",TX,17,"800","middle"); T(s,cx,ybot+24,name,MUT,12.5,"600","middle")
    T(s,40,300,"B  CLINICAL-GRADE GUARANTEES BY CONDITION",DIM,13,"700")
    props=["Comparable|accuracy","Deterministic|mapping","Auditable|","Model|invariant","Population|invariant"]
    rows=[("Free-prompt",[0,0,0,0,0]),("RAG",[0,0,0,0,0]),("Skill-reasoning",[1,0,0,0,0]),
          ("Skill-execution",[1,1,1,1,1]),("Control (answer supplied)",[1,1,1,1,1])]
    lblw=240; mx0=60+lblw; mtot=W-40-mx0; pcolw=mtot/5; hy=318
    for j,p in enumerate(props):
        cx=mx0+pcolw*j+pcolw/2; a,b=p.split("|")
        if b: T(s,cx,hy+16,a,MUT,12.5,"600","middle"); T(s,cx,hy+32,b,MUT,12.5,"600","middle")
        else: T(s,cx,hy+24,a,MUT,12.5,"600","middle")
    ry0=hy+48; rh=48
    for r,(name,vals) in enumerate(rows):
        y=ry0+r*rh; hot=name.startswith("Skill-execution")
        if hot: B(s,54,y+4,W-40-54,rh-6,"#0f2a16",GREEN,8,2)
        T(s,60,y+rh/2+5,name,TX if hot else MUT,14,"700" if hot else "500")
        for j,v in enumerate(vals):
            cx=mx0+pcolw*j+pcolw/2; cy=y+rh/2
            if v: check(s,cx,cy,GREEN)
            else: line(s,cx-9,cy,cx+9,cy,DIM,2)
    write("result-workflow.svg",W,ry0+5*rh+18,s)

def fig_paradox():
    s=[]; W=1200
    T(s,40,34,"LETHAL-CLASS SAFETY ERROR RATE BY CONDITION  (aggregate over 9 frontier models)",DIM,13,"700")
    errs=[24.6,36.6,8.5,15.3,0.0]; names=["Free-prompt","RAG","Skill-reasoning","Skill-execution","Control"]
    def dcol(v):
        if v==0: return GREEN
        if v>=30: return HOT
        if v>=20: return "#e06c5e"
        if v>=10: return ORANGE
        return "#d4a72c"
    x0,x1=92,1110; ytop,ybot=84,432; lo,hi=0,40
    yv=lambda v: ybot-(v-lo)/(hi-lo)*(ybot-ytop)
    for g in range(0,hi+1,10):
        y=yv(g); line(s,x0,y,x1,y,"#21262d",1); T(s,x0-12,y+4,f"{g}%",DIM,11,"400","end")
    colw=(x1-x0)/5; bw=120
    for i,(nm,v) in enumerate(zip(names,errs)):
        cx=x0+colw*i+colw/2; col=dcol(v)
        if v==0:
            line(s,cx-bw/2,ybot,cx+bw/2,ybot,GREEN,5); T(s,cx,ybot-14,"0%",GREEN,18,"800","middle")
        else:
            B(s,cx-bw/2,yv(v),bw,ybot-yv(v),col,None,6); T(s,cx,yv(v)-12,f"{v:.1f}%",TX,17,"800","middle")
        T(s,cx,ybot+26,nm,MUT,12.5,"600","middle")
    rcx=x0+colw*1+colw/2; T(s,rcx,yv(36.6)-34,f"{TRI} worst",HOT,12.5,"800","middle")
    T(s,W/2,ybot+60,"Retrieval-augmenting with the correct guideline RAISED lethal errors (+12.0 pp).",RED,14.5,"700","middle")
    T(s,W/2,ybot+82,"Executing the validated skill as code drives them toward zero. Correctness must be executed, not retrieved.",MUT,13,"400","middle")
    write("paradox-workflow.svg",W,ybot+102,s)

fig_design(); fig_result(); fig_paradox()
