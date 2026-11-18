import sys,csv,json; sys.path.insert(0,'.')
from crrstyle import *
import numpy as np, matplotlib.pyplot as plt
setup()
d=json.load(open('Y160/raw/Y160_D2_D2R5_P_p.json'))
br={it['branch']['kind']:it['branch'] for it in d}
def sp(b): return [sum(abs(x) for x in r['displacement'])/len(r['displacement']) for r in b['rounds']]
fig=plt.figure(figsize=(7.2,5.4))
ax=fig.add_axes([0.08,0.6,0.38,0.34]); panel(ax,"a",x=-0.16)
r=np.arange(1,17)
ax.step(r,sp(br['CONTROL']),where="mid",color=C["ctrl"],lw=1.6)
ax.step(r,sp(br['PULSE']),where="mid",color=C["act"],lw=1.4,ls=(0,(3,2)))
ax.step(r,sp(br['CLAMP']),where="mid",color=C["act"],lw=1.8)
ax.text(16.4,1.0,"untouched",va="center",fontsize=7.5,color=C["ctrl"])
ax.text(16.4,1.5,"one deletion",va="center",fontsize=7.5,color=C["act"])
ax.text(16.4,2.0,"two rounds\nof deletion",va="center",fontsize=7.5,color=C["act"])
ax.plot([1],[0.86],marker="v",color=C["act"],ms=5,mfc="white",mew=1)
ax.text(1.6,0.86,"one deletion (before round 1)",fontsize=7,color=C["act"],va="center")
ax.plot([1,2],[0.76,0.76],marker="v",ls="",color=C["act"],ms=5)
ax.text(2.6,0.76,"deletions in rounds 1 and 2",fontsize=7,color=C["act"],va="center")
ax.set_yticks([1,1.5,2],["$v_1$","3/2","$v_2$"]); ax.set_ylim(0.68,2.2); ax.set_xlim(0.5,16.3)
ax.set_xlabel("round"); ax.set_ylabel("mean speed per round")
ax.text(0.6,2.17,"same trajectory in 28/28 cases per branch",fontsize=7.5,color=C["soft"],va="top")
# panel b: Y163 four-leg round trip
R=list(csv.DictReader(open('D/CRR_Figure_Data_Package_Primary/F10_Y163_roundtrip_and_control_primary.csv')))
iv=[x for x in R if x['branch']=='intervention']; ct=[x for x in R if x['branch']!='intervention']
bx=fig.add_axes([0.08,0.1,0.9,0.34]); panel(bx,"b",x=-0.07)
g=np.array([int(x['global_round']) for x in iv]); v=np.array([float(x['mean_abs_speed']) for x in iv])
for leg in range(1,5):
    lo,hi=(leg-1)*64+0.5,leg*64+0.5
    if leg%2==0: bx.axvspan(lo,hi,color=C["light"],lw=0,zorder=0)
    tgt="$v_2$" if leg%2 else "$v_1$"
    bx.text((lo+hi)/2,2.32,f"leg {leg}: to {tgt}",ha="center",fontsize=7.5)
bx.step(g,v,where="mid",color=C["core"],lw=1.4,zorder=3)
gc=np.array([int(x['global_round']) for x in ct]); vc=np.array([float(x['mean_abs_speed']) for x in ct])
bx.step(gc,vc-0.04,where="mid",color=C["ctrl"],lw=1.2,zorder=2)
bx.text(257,0.94,"untouched control",fontsize=7.5,color=C["ctrl"],ha="right",va="top")
for x in iv:
    if x['operation_this_round']=='DELETE': bx.plot(int(x['global_round']),0.76,"v",color=C["act"],ms=4.5)
    if x['operation_this_round']=='E': bx.plot(int(x['global_round']),0.76,"^",mfc="white",mec=C["act"],ms=4.5,mew=1)
for leg in range(1,5):
    L=[x for x in iv if int(x['leg'])==leg]; m=int(L[0]['first_reference_match_round_in_leg'])
    gr=(leg-1)*64+m; bx.plot(gr,float(L[m-1]['mean_abs_speed'])+0.14,"D",ms=4,color=C["R5"])
bx.text(30,2.08,"dressing first matches reference",fontsize=7,color=C["R5"])
bx.text(5,0.62,"▼ sector-relation deletion   △ occupancy-guarded source insertion",fontsize=7,color=C["act"])
bx.set_yticks([1,1.5,2],["$v_1$","3/2","$v_2$"]); bx.set_ylim(0.55,2.45); bx.set_xlim(0,258)
bx.set_xlabel("round"); bx.set_ylabel("mean speed per round")
bx.text(258,2.6,"N5R5555, one of 44/44 N5 cases",ha="right",fontsize=7.5,color=C["soft"])
# panel c: settling note
cx=fig.add_axes([0.6,0.6,0.38,0.34]); cx.axis("off"); panel(cx,"c",x=0.0)
cx.text(0,0.92,"How the staircase arises",fontsize=8.5,fontweight="bold",va="top")
cx.text(0,0.78,("Each carrier update reads the graph as it was\n"
"before that update. A deletion therefore cannot\n"
"change the step already taken; it changes what\n"
"the next update reads. Speed moves one step\n"
"per round: $v_1 \\to 3/2 \\to v_2$.\n\n"
"After two rounds of deletion the faster sector\n"
"maintains itself with no further intervention.\n"
"A single deletion instead settles on the\n"
"period-2 orbit (mean speed 3/2)."),fontsize=7.6,va="top",linespacing=1.4)
save(fig,"F10_environmental_speed_control")
