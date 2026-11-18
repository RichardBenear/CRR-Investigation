import sys; sys.path.insert(0,'.')
from crrstyle import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
setup()
steps=[("A partner interaction (wake)","D3-5","trailing receiver slows in pairs, never in solo worlds"),
("Deposited history, not the partner's current state","D3-6","leader introduced first: 24/24 respond; solos 0/96;\nremoving the pre-receiver relation restores speed 41/41"),
("A persistent remnant, not a propagating signal","D3-7A–C","persists 143/143; leader's later events reach the receiver 0/413;\nhead-on approach: no response before contact 0/32"),
("One source slot, changed in two ways","D3-7G–I","additive or subtractive (8/8 ledger); no simple conservation;\ncapture, no closed exchange cycle (0/8)"),
("Not the fossil, not the start site, not the scheduler","D3-7J–N","fossil deleted: still 8/8; start-site boundary surgery: no effect;\nonset unchanged under three random streams (24/24)"),
("A worldline encounter at the leader's formation site","D3-7O–Q","predicted before running: 8/8, then 72/72;\nnormalizing the source slot removes the response 24/24"),
("Preparation-dependent formation memory","D3-7R","identical mature leader from two preparations (24/24),\nbut remnants differ in 4/24; inherited law holds 17/24")]
fig=plt.figure(figsize=(7.2,6.0)); ax=fig.add_axes([0,0,1,1]); ax.axis("off")
n=len(steps); ax.set_xlim(0,10); ax.set_ylim(-0.4,n+0.4)
for i,(interp,st,ev) in enumerate(steps):
    y=n-1-i+0.2; x0=0.15+i*0.22
    last=i==n-1
    ax.add_patch(FancyBboxPatch((x0,y-0.3),4.0,0.6,boxstyle="round,pad=0,rounding_size=0.08",
        fc=C["light"] if not last else "white",ec=C["act"] if last else C["core"],lw=1.5 if last else 0.9))
    ax.text(x0+0.12,y,interp,va="center",fontsize=7.6,fontweight="bold" if last else "normal")
    ax.text(x0+4.15,y+0.13,st,va="center",fontsize=7,color=C["soft"])
    ax.text(x0+4.15,y-0.12,ev,va="center",fontsize=6.9,linespacing=1.25)
    if not last:
        ax.annotate("",xy=(x0+0.42,y-0.55),xytext=(x0+0.42,y-0.3),arrowprops=dict(arrowstyle="->",color=C["soft"],lw=0.8))
ax.text(0.15,n+0.1,"interpretation supported at each step  →  evidence that forced the next step",fontsize=8,color=C["soft"])
save(fig,"F11_D37_reclassification_ladder")
