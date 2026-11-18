import sys; sys.path.insert(0,'.')
from crrstyle import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
setup()
rows=[("External speed command","Speed read from current structure (native sector memory)","Y136–Y140"),
("Relay as a separately scheduled event","One atomic compound event (no race)","Y141"),
("Successor by vertex-number arithmetic","Causal-spine successor (relabel-covariant)","Y142"),
("Numeric gate orientation (u < v)","Structural guard orientation","Y143"),
("Rest marker shaped like a motion signal","Covariant rest marker (RST1)","Y144"),
("External rest phase counter","Phase read from current structure","Y145–Y146"),
("Cleanup lookup tables","Transient provenance token, inert to all gates","Y147")]
fig=plt.figure(figsize=(7.2,5.0))
ax=fig.add_axes([0.0,0.38,1.0,0.6]); ax.axis("off"); panel(ax,"a",x=0.02,y=1.0)
ax.set_xlim(0,10); ax.set_ylim(-1.0,len(rows)+0.3)
ax.text(1.95,len(rows)-0.05,"removed scaffold",ha="center",fontsize=8,color=C["soft"])
ax.text(7.3,len(rows)-0.05,"intrinsic replacement",ha="center",fontsize=8,color=C["core"])
for i,(a,b,st) in enumerate(rows):
    y=len(rows)-1-i-0.35
    ax.add_patch(FancyBboxPatch((0.2,y-0.3),3.5,0.6,boxstyle="round,pad=0,rounding_size=0.08",fc="white",ec=C["ctrl"],lw=0.9,ls=(0,(3,2))))
    ax.text(1.95,y,a,ha="center",va="center",fontsize=7.6,color=C["soft"])
    ax.add_patch(FancyBboxPatch((5.0,y-0.3),4.6,0.6,boxstyle="round,pad=0,rounding_size=0.08",fc=C["light"],ec=C["core"],lw=1))
    ax.text(7.3,y,b,ha="center",va="center",fontsize=7.6,color=C["ink"])
    ax.annotate("",xy=(4.95,y),xytext=(3.75,y),arrowprops=dict(arrowstyle="->",color=C["core"],lw=0.9))
    ax.text(4.35,y+0.13,st,ha="center",va="bottom",fontsize=6.8,color=C["soft"])
# b: validation
bx=fig.add_axes([0.32,0.03,0.42,0.27]); panel(bx,"b",x=-0.55,y=1.02)
val=[("arbitrary relabelings, relay (Y142)",11520),("long-run rest periods (Y148)",640),("arbitrary relabelings, rest engine",560),
("unique ancestry successor, full period",352),("rest → motion handoffs",28),("motion → rest handoffs",14)]
for i,(lab,n) in enumerate(val):
    y=len(val)-1-i
    bx.barh(y,1,0.55,color=C["core"])
    bx.text(-0.03,y,lab,ha="right",va="center",fontsize=7.4)
    bx.text(1.03,y,f"{n:,}/{n:,}",ha="left",va="center",fontsize=7.4)
bx.set_xlim(0,1.35); bx.set_ylim(-0.6,len(val)-0.4); bx.axis("off")
bx.text(0.5,len(val)-0.15,"all gates passed; scope: tested manifold",ha="center",fontsize=7.2,color=C["soft"])
save(fig,"F5_autonomous_engine")
