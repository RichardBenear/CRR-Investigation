import sys; sys.path.insert(0,'.')
from crrstyle import *
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
setup()
species=[("DS001",[0],{},None),("D2R5",[0,5],{(0,1):4},97),("D2R6",[0,6],{(0,1):1},99),
 ("T3R65",[0,6,11],{(0,1):1,(1,2):4},155),("T4R656",[0,6,11,17],{(0,1):1,(1,2):4,(2,3):1},219),
 ("N5R5555",[0,5,10,15,20],{(0,1):4,(1,2):4,(2,3):4,(3,4):4},283)]
RS=4.1; R=1.15
fig=plt.figure(figsize=(7.2,8.2))
ax=fig.add_axes([0.02,0.36,0.96,0.6]); ax.set_aspect("equal"); ax.axis("off")
ax.set_xlim(-6.5,28.5); ax.set_ylim(-2.4,len(species)*RS+0.6)
panel(ax,"a",x=0.0,y=1.0)
for row,(name,pos,edges,halo) in enumerate(species):
    y=(len(species)-1-row)*RS+0.6
    ax.text(-6.4,y+0.2,name,ha="left",va="center",fontsize=9,fontweight="bold")
    occ=set()
    for p in pos: occ|=set(range(p,p+5))
    base=y-R-0.55
    for s_ in range(0,max(pos)+5):
        if s_ in occ: ax.plot(s_,base,"o",ms=2.8,color=C["core"])
        else: ax.plot(s_,base,"o",ms=3.2,mfc="white",mec=C["vac"],mew=1)
    for p in pos:
        ax.plot([p-0.2,p+4.2],[base+0.32]*2,color=C["vac"],lw=0.8)
        pentagon(ax,p+2,y+0.2,R)
    for (i,j),n in edges.items():
        a=pos[i]+2+R*0.95; b=pos[j]+2-R*0.95; mid=(a+b)/2; w=b-a
        col=C["R5"] if n==4 else C["R6"]
        for k in range(n):
            ax.add_patch(Arc((mid,y+0.2),w,0.5+0.38*k,theta1=0,theta2=180,color=col,lw=1.25,zorder=3))
    if halo: ax.text(28.4,y+0.2,f"halo {halo}",ha="right",va="center",fontsize=8,color=C["soft"])
yb=-2.2
for s_ in range(0,25,5): ax.text(s_,yb,str(s_),ha="center",fontsize=7.5,color=C["soft"])
ax.text(27.6,yb,"old-vacuum site",ha="right",fontsize=7.5,color=C["soft"])
top=len(species)*RS+0.2
ax.plot([5.2,6.4],[top]*2,color=C["R5"],lw=2); ax.text(6.7,top,"R5 contact: supports adjacent, 4 cross-core relations at rest",va="center",fontsize=8,color=C["R5"])
ax.plot([5.2,6.4],[top-0.85]*2,color=C["R6"],lw=2); ax.text(6.7,top-0.85,"R6 contact: one empty site between supports, 1 cross-core relation",va="center",fontsize=8,color=C["R6"])
# glyph key
kx=fig.add_axes([0.03,0.22,0.17,0.12]); kx.set_aspect("equal"); kx.axis("off"); kx.set_xlim(-2,2); kx.set_ylim(-1.9,1.9)
pentagon(kx,0,0,1.15,labels=True,vs=5,fs=7.5)
fig.text(0.115,0.21,"DS001 constituent:\nfive core vertices and\ndirection marker $h$",ha="center",va="top",fontsize=7.2)
# panel b
bx=fig.add_axes([0.3,0.08,0.27,0.22]); panel(bx,"b",x=-0.3,y=1.02)
for x,y,c,fill in [(1,2,C["R5"],True),(0,1,C["R6"],False),(1,0,C["R6"],False),(1,1,C["R6"],True)]:
    bx.plot(x,y,"o",ms=11,mfc=c if fill else "white",mec=c,mew=1.6,zorder=3)
bx.annotate("",xy=(0.93,0.97),xytext=(0.1,0.99),arrowprops=dict(arrowstyle="->",color=C["R6"],lw=1))
bx.annotate("",xy=(0.97,0.91),xytext=(0.98,0.1),arrowprops=dict(arrowstyle="->",color=C["R6"],lw=1))
bx.text(1.13,2,"R5: one state in every\nsector, relay occupancy 3",va="center",fontsize=7.2,color=C["R5"])
bx.text(1.13,1,"R6 at $v_2$:\nrelay occupancy 2",va="center",fontsize=7.2,color=C["R6"])
bx.text(-0.15,1.28,"R6 at rest, $v_1$:\nrelay occupancy 1",ha="left",va="bottom",fontsize=7.2,color=C["R6"])
bx.set_xlim(-0.35,2.6); bx.set_ylim(-0.45,2.55); bx.set_xticks([0,1]); bx.set_yticks([0,1,2])
bx.set_xlabel("$n_X$"); bx.set_ylabel("$n_W$")
bx.spines["bottom"].set_bounds(0,1); bx.spines["left"].set_bounds(0,2)
# panel c
cx=fig.add_axes([0.62,0.05,0.37,0.27]); cx.set_aspect("equal"); cx.axis("off"); panel(cx,"c",x=0.0,y=1.0)
cx.set_xlim(-8.5,12.5); cx.set_ylim(-2.6,9.6)
for s_ in range(-6,11): cx.plot(s_,-1.0,"o",ms=2.6,mfc="white",mec=C["vac"],mew=0.9)
for s_ in range(0,5): cx.plot(s_,-1.0,"o",ms=2.8,color=C["core"])
pentagon(cx,2,0.6,1.05,vs=3.5)
for off,y in [(-5,3.6),(-6,6.6),(5,3.6),(6,6.6)]:
    col=C["R5"] if abs(off)==5 else C["R6"]
    pentagon(cx,off+2,y,0.95,ec=col,vs=3.2,lw=1.0)
    cx.plot([off-0.1,off+4.1],[y-1.45]*2,color=col,lw=1.6,solid_capstyle="round")
    cx.text(off+(-0.6 if off<0 else 4.6),y,f"{off:+d}",ha="right" if off<0 else "left",va="center",fontsize=7.5,color=col)
cx.text(-3.5,9.4,"same side: share\n4 of 5 sites",ha="center",va="top",fontsize=6.8,color=C["soft"])
cx.text(7.5,9.4,"same side: share\n4 of 5 sites",ha="center",va="top",fontsize=6.8,color=C["soft"])
cx.text(2,-1.7,"at most one neighbor per side, so $z_{\\max}=2$",ha="center",va="top",fontsize=7.8)
save(fig,"F14_structure_gallery")
