import sys,csv; sys.path.insert(0,'.')
from crrstyle import *
import numpy as np, matplotlib.pyplot as plt
from collections import defaultdict
setup()
R=list(csv.DictReader(open('D/CRR_Figure_Data_Package_Primary/F12_D37Q_worldline_encounter_primary.csv')))
g=defaultdict(list)
for x in R: g[x['case']].append(x)
cases=[("D37Q_seed1_d40_p_PAIR_NATIVE","d = 40, moving +","additive: locks to $v_1$"),
       ("D37Q_seed1_d44_p_PAIR_NATIVE","d = 44, moving +","subtractive: locks to $v_2$"),
       ("D37Q_seed1_d40_m_PAIR_NATIVE","d = 40, moving −","additive: one phase slip")]
fig=plt.figure(figsize=(7.2,5.6))
for ci,(cid,title,mech) in enumerate(cases):
    v=g[cid][:12]; s=int(v[0]['sign']); near=float(v[0]['formation_near_edge'])
    delta=[s*(float(x['receiver_position'])-near) for x in v]
    k=[int(x['receiver_k']) for x in v]; mag=[int(x['receiver_native_mag_after_event']) for x in v]
    ek=int(v[0]['encounter_receiver_k']); sep=float(v[0]['leader_receiver_separation_at_encounter'])
    ax=fig.add_axes([0.08+ci*0.31,0.42,0.25,0.5])
    panel(ax,"abc"[ci],x=-0.22)
    ax.axvspan(0,4,color=C["light"],lw=0,zorder=0)
    ax.text(2,0.55,"formation\nsupport",ha="center",va="bottom",fontsize=7,color=C["soft"])
    ax.plot(delta,k,color=C["vac"],lw=1,zorder=1)
    for d_,k_,m_ in zip(delta,k,mag):
        ax.plot(d_,k_,"o",ms=6,mfc=C["core"] if m_==2 else "white",mec=C["core"],mew=1.1,zorder=3)
    ed=delta[ek-1]; ax.plot(ed,ek,"o",ms=12,mfc="none",mec=C["act"],mew=1.6,zorder=4)
    ax.text(ed+1.0,ek+(0.9 if ek<3 else 0),"encounter",va="center",fontsize=7.5,color=C["act"])
    ax.set_ylim(13.4,-0.6); ax.set_xlim(-8,22)
    ax.text(-7.5,-0.35,title,fontsize=8.5,fontweight="bold",va="bottom")
    ax.text(21.5,1.6,f"leader {sep:.0f} units\nahead →",ha="right",fontsize=7,color=C["soft"])
    ax.text(-7.5,13.15,mech,fontsize=7.5,color=C["act"])
    ax.set_xlabel("position relative to formation site")
    if ci==0: ax.set_ylabel("receiver event")
    else: ax.set_yticklabels([])
# legend
lx=fig.add_axes([0.08,0.31,0.9,0.04]); lx.axis("off")
lx.plot([0.0],[0.5],"o",ms=6,mfc=C["core"],mec=C["core"]); lx.text(0.012,0.5,"fast sector after event",va="center",fontsize=7.5)
lx.plot([0.21],[0.5],"o",ms=6,mfc="white",mec=C["core"],mew=1.1); lx.text(0.222,0.5,"slow sector after event",va="center",fontsize=7.5)
lx.text(0.44,0.5,"before the encounter the receiver alternates sectors (period-2 orbit)",va="center",fontsize=7.5,color=C["soft"])
lx.set_xlim(-0.01,1); lx.set_ylim(0,1)
# panel d: period-3 phase law
dx=fig.add_axes([0.08,0.07,0.56,0.18]); panel(dx,"d",x=-0.1)
pos={0:(4.0,"add"),1:(1.5,"sub"),2:(2.0,"add")}; neg={0:(0.0,"add"),1:(2.0,"add"),2:(2.5,"sub")}
for tab,col,lab,ls in [(pos,C["core"],"moving +","-"),(neg,C["ctrl"],"moving −","--")]:
    ds=list(range(40,49)); ys=[tab[(d-40)%3][0] for d in ds]
    dx.plot(ds,ys,color=col,lw=0.9,ls=ls,zorder=1)
    for d,y in zip(ds,ys):
        m=tab[(d-40)%3][1]
        dx.plot(d,y,"o" if m=="add" else "s",ms=6,mfc=col if m=="add" else "white",mec=col,mew=1.2,zorder=3)
    dx.text(48.35,ys[-1]+(0.45 if lab=="moving −" else -0.45),lab,va="center",fontsize=7.5,color=col)
dx.set_ylim(-0.5,4.6); dx.set_yticks([0,2,4]); dx.set_ylabel("offset into support")
dx.set_xticks(range(40,49)); dx.set_xlabel("formation displacement d"); dx.set_xlim(39.6,49.4)
nx=fig.add_axes([0.68,0.07,0.31,0.18]); nx.axis("off")
nx.text(0,1.0,"Encounter offset and mechanism repeat every\n3 units of d (all 72 comparisons, 4 vacua).\n\n● additive: partner relation fills the slot\n□ subtractive: needed relation removed",va="top",fontsize=7.5,linespacing=1.4)
save(fig,"F12_D37_worldline_encounter")
