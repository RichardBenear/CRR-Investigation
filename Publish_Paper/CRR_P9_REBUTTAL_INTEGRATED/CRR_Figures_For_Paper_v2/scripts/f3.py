import sys; sys.path.insert(0,'.')
from crrstyle import *
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
setup()
fig=plt.figure(figsize=(7.2,3.2))
# a: relation-floor obstruction schematic
ax=fig.add_axes([0.06,0.18,0.47,0.70]); panel(ax,"a",x=-0.08,y=1.06)
ax.set_xlim(0,10); ax.set_ylim(-0.2,3.1)
ax.spines[['top','right','left']].set_visible(False); ax.set_yticks([]); ax.set_xticks([])
ax.plot([0.7,3.8],[2.3,2.3],color=C["core"],lw=2)
ax.plot([4.8,9.3],[1.25,1.25],color=C["act"],lw=2)
ax.annotate("",xy=(4.65,1.35),xytext=(3.95,2.22),arrowprops=dict(arrowstyle="->",lw=1.2,color=C["act"]))
ax.text(2.25,2.55,r"recurrent floor $\rho$",ha="center",fontsize=8,color=C["core"])
ax.text(7.05,1.52,r"after destructive contact: floor $\leq \rho-1$",ha="center",fontsize=7.6,color=C["act"])
ax.text(7.05,0.82,"native dynamics cannot raise the floor",ha="center",fontsize=7.4,color=C["soft"])
ax.text(0.7,0.05,r"$\rho_{next}\leq\rho_{current}$; a recurrent return requires the original floor",fontsize=7.4,color=C["ink"])
ax.text(0.7,-0.18,"structural obstruction for the tested fixed-support architecture",fontsize=7,color=C["soft"])
# b: complete census
bx=fig.add_axes([0.61,0.17,0.35,0.72]); bx.axis("off"); panel(bx,"b",x=-0.08,y=1.04)
n=142; cols=12
for i in range(n):
    r,c=divmod(i,cols); bx.add_patch(Rectangle((c,-r),0.82,0.82,fc="white",ec=C["act"],lw=0.7))
bx.set_xlim(-0.3,12.3); bx.set_ylim(-13.2,1.6)
bx.text(6,1.15,"142 destructive branches",ha="center",fontsize=8)
bx.text(6,-12.65,"0 / 142 return to the recurrence cycle\ncomplete fixed-size predictive quotient",ha="center",va="top",fontsize=7.5,color=C["act"])
save(fig,"F3_canonical_fixed_support_nogo")
