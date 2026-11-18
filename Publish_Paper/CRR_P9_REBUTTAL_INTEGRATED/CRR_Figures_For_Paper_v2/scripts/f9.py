import sys,csv; sys.path.insert(0,'.')
from crrstyle import *
import numpy as np, matplotlib.pyplot as plt
setup()
R=list(csv.DictReader(open('D/CRR_Figure_Data_Package_Primary/F9_Y158_channel_actions_primary.csv')))
fig=plt.figure(figsize=(7.2,3.3))
# a: bond-local action under two accounting rules
ax=fig.add_axes([0.07,0.16,0.27,0.72]); panel(ax,"a",x=-0.28)
Y154={"D2R5":119/6,"D2R6":199/24}
for i,sp in enumerate(["D2R5","D2R6"]):
    col=C["R5"] if sp=="D2R5" else C["R6"]
    ax.bar(i-0.18,Y154[sp],0.32,color=col,alpha=0.9)
    vals=[float(r["M_BOND_total"]) for r in R if r["species"]==sp]
    ax.bar(i+0.18,0.0001,0.32,color=col)
    ax.plot([i+0.18]*len(vals),vals,"o",ms=3.5,mfc="white",mec=col,mew=1.1,zorder=4)
    ax.text(i-0.18,Y154[sp]+0.5,{"D2R5":"119/6","D2R6":"199/24"}[sp],ha="center",fontsize=7.5)
    ax.text(i+0.18,0.6,"0",ha="center",fontsize=7.5)
ax.set_xticks([0,1],["D2R5","D2R6"]); ax.set_ylim(0,26); ax.set_xlim(-0.55,1.6); ax.set_ylabel("bond-local action")
ax.text(0.14,25.5,"filled: current-incidence\naccounting (Y154)\nopen: producer-owned\nbond action (Y158),\neach of 8 contexts",fontsize=7,va="top",ha="left",color=C["ink"],linespacing=1.3)
# b: who produced the cross-core relations
bx=fig.add_axes([0.45,0.16,0.2,0.72]); panel(bx,"b",x=-0.36)
traffic={"D2R5":(190,1),"D2R6":(86,9)}
for i,sp in enumerate(["D2R5","D2R6"]):
    col=C["R5"] if sp=="D2R5" else C["R6"]
    env,car=traffic[sp]
    bx.bar(i,env,0.5,color=C["vac"],edgecolor=C["soft"],lw=0.6)
    bx.bar(i,car,0.5,bottom=env,color=col)
    bx.text(i,env+car+5,f"{env} + {car}",ha="center",fontsize=7.5)
bx.set_xticks([0,1],["D2R5","D2R6"]); bx.set_ylim(0,230)
bx.set_ylabel("entries into bond sector, per case")
bx.text(1.48,165,"gray: environment\n(vacuum-produced)\ncolor: carrier-produced",fontsize=7,va="top",ha="right")
bx.set_xlim(-0.5,1.5)
# c: accounting identity
cx=fig.add_axes([0.80,0.16,0.19,0.72]); panel(cx,"c",x=-0.42)
mig={"D2R5":376,"D2R6":331}
for i,sp in enumerate(["D2R5","D2R6"]):
    col=C["R5"] if sp=="D2R5" else C["R6"]
    cx.bar(i,2*mig[sp],0.55,color=col,alpha=0.85)
    cx.text(i,2*mig[sp]+15,f"{2*mig[sp]}\n= 2 × {mig[sp]}",ha="center",fontsize=7)
cx.set_xticks([0,1],["D2R5","D2R6"]); cx.set_ylim(0,900)
cx.set_ylabel("excess counted edits")
save(fig,"F9_Y158_reinterpretation")
