import sys; sys.path.insert(0,'.')
from crrstyle import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
setup()
lanes=[("Canonical binary rule",0.0,["recurrent translating\nstructure","fragile under\nbackground contact","no repair\n(0/142 census)"],"fails the tested\nfixed-support architecture",C["ctrl"]),
("Ternary rule search",1.2,["77,314 rules\nsearched","80 with a closed\nparticle class","rule 55744\n≈97% survival"],"existence result;\ngeometry not physical",C["ctrl"]),
("FBCL/Y33 carriers",2.4,["DS001 exact\nrecurrence","seven R5/R6\ncomposites","bond automaton;\n$z_{\\max}=2$"],"persistent\nparticle-like structures",C["core"]),
("Autonomous kinematics",3.6,["covariant engine\n(Y148)","environmental\nspeed control","reversible,\nrepeatable (44/44)"],"autonomous recurrence;\ntriggers external",C["core"]),
("Mass-energy program",4.8,["curvature proxy\ntopology-blind","no conserved\nstate scalar","38/38 contrast,\nenvironmental dressing","no safe rest\ncoupling (C3)"],"$E_0$, $M_i$ operationally\nundefined",C["act"]),
("Two-particle program",6.0,["apparent\nwake","worldline\nencounter","formation\nremnant"],"preparation-dependent\nformation memory",C["act"])]
fig=plt.figure(figsize=(7.2,5.4)); ax=fig.add_axes([0,0,1,1]); ax.axis("off")
ax.set_xlim(-0.2,10.4); ax.set_ylim(6.7,-0.9)
for name,y,ms,verdict,vc in lanes:
    ax.text(-0.1,y,name,va="center",fontsize=8,fontweight="bold")
    x0=2.35; step=(6.6-x0)/max(len(ms)-1,1) if len(ms)>1 else 0
    xs=[x0+i*step for i in range(len(ms))]
    ax.plot([xs[0],7.35],[y,y],color=C["vac"],lw=1.5,zorder=0)
    for x,m in zip(xs,ms):
        ax.plot(x,y,"o",ms=6,color=C["core"],zorder=2)
        ax.text(x,y+0.17,m,ha="center",va="top",fontsize=6.7,linespacing=1.2)
    ax.add_patch(FancyBboxPatch((7.45,y-0.33),2.85,0.66,boxstyle="round,pad=0,rounding_size=0.08",fc="white",ec=vc,lw=1.2))
    ax.text(8.875,y,verdict,ha="center",va="center",fontsize=7.2,linespacing=1.2)
# connectors
ax.annotate("",xy=(2.35,1.13),xytext=(2.35,0.78),arrowprops=dict(arrowstyle="->",color=C["soft"],lw=0.8))
ax.annotate("",xy=(2.35,2.33),xytext=(2.35,1.98),arrowprops=dict(arrowstyle="->",color=C["soft"],lw=0.8))
ax.text(2.5,2.13,"Rule 55584 was a separate Stage-W hit; the later Y33/Y47 law",fontsize=6.3,color=C["soft"],va="center")
ax.text(2.5,2.29,"shared 0/8 outputs with it and was named FBCL at Y50",fontsize=6.3,color=C["soft"],va="center")
for y in (3.6,4.8,6.0):
    ax.text(-0.1,y+0.27,"built on FBCL/Y33",va="center",fontsize=6.8,color=C["soft"])
ax.text(-0.1,-0.65,"three broad rule lineages; the Rule-55584 branch is the historical bridge into the later co-designed FBCL/Y33 law",fontsize=7.0,color=C["soft"])
save(fig,"F1_program_roadmap")
