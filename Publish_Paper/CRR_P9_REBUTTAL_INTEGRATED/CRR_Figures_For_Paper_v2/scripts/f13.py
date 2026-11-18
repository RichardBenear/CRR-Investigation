import sys; sys.path.insert(0,'.')
from crrstyle import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
setup()
fig=plt.figure(figsize=(7.2,4.6))
# a: gate overlap
ax=fig.add_axes([0.02,0.42,0.42,0.5]); ax.axis("off"); panel(ax,"a",x=0.0,y=1.02)
ax.set_xlim(-0.5,8.5); ax.set_ylim(-3.2,2.4); ax.set_aspect("equal")
for i in range(5): ax.add_patch(Circle((i,1.6),0.22,fc=C["core"],ec=C["core"]))
ax.add_patch(FancyBboxPatch((-0.4,1.3),4.8,0.6,boxstyle="round,pad=0,rounding_size=0.15",fc="none",ec=C["core"],lw=1.2))
ax.text(5.0,1.6,"native rest gate\n(the unique next update)",va="center",fontsize=7.5)
for i in range(1,5): ax.add_patch(Circle((i,0.5),0.22,fc=C["core"],ec=C["act"],lw=1.4))
ax.add_patch(Circle((5,0.5),0.22,fc="white",ec=C["act"],lw=1.4))
ax.add_patch(FancyBboxPatch((0.6,0.2),4.8,0.6,boxstyle="round,pad=0,rounding_size=0.15",fc="none",ec=C["act"],lw=1.2,ls=(0,(3,2))))
ax.text(5.6,0.5,"rival gate",va="center",fontsize=7.5,color=C["act"])
ax.text(2.5,-0.05,"shares 4 of 5 vertices; uses a fresh one",ha="center",va="top",fontsize=7.2,color=C["act"])
ax.text(-0.4,-0.75,"Firing the rival consumes support the native gate needs.\nIn all 6 phases with a rival, the next rest update was lost\n(no valid rest-role assignment). 2 phases had no rival.\nViable phases: 0/8. The untouched control completed\ntwo full rest cycles.",va="top",fontsize=7.2,linespacing=1.35)
# b: requirement matrix
bx=fig.add_axes([0.5,0.06,0.49,0.88]); bx.axis("off"); panel(bx,"b",x=-0.02,y=0.99)
req=["local and future-blind","acts outside the unique next gate","independent environment-side state",
     "balanced signed exchange ledger","no direct speed or phase command","recurrence intact before and after","available at rest"]
cols=["C3 rival\ngate","sector\nrelation","rest\nreservoir"]
# 1 meets, 0 fails, None untested
M=[[1,1,1],[0,1,None],[0,1,1],[None,None,None],[1,1,None],[0,1,None],[1,0,1]]
nr=len(req); bx.set_xlim(0,10); bx.set_ylim(-0.8,nr+1.3)
for j,c in enumerate(cols): bx.text(6.0+j*1.45,nr+0.55,c,ha="center",va="center",fontsize=7.4)
for i,r in enumerate(req):
    y=nr-1-i+0.2
    bx.text(0.05,y,r,va="center",fontsize=7.4)
    if i%2==0: bx.add_patch(FancyBboxPatch((0,y-0.38),9.95,0.76,boxstyle="square,pad=0",fc=C["light"],ec="none",zorder=0))
    for j in range(3):
        v=M[i][j]; x=6.0+j*1.45
        if v==1: bx.plot(x,y,"o",ms=8,color=C["core"])
        elif v==0: bx.plot(x,y,"x",ms=8,mew=2,color=C["act"])
        else: bx.plot(x,y,"o",ms=8,mfc="white",mec=C["ctrl"],mew=1.3)
bx.plot(0.2,-0.45,"o",ms=7,color=C["core"]); bx.text(0.45,-0.45,"established",va="center",fontsize=7)
bx.plot(2.6,-0.45,"x",ms=7,mew=2,color=C["act"]); bx.text(2.85,-0.45,"fails",va="center",fontsize=7)
bx.plot(4.1,-0.45,"o",ms=7,mfc="white",mec=C["ctrl"],mew=1.3); bx.text(4.35,-0.45,"not yet tested (C4)",va="center",fontsize=7)
save(fig,"F13_rest_coupling_requirements")
