import sys,csv; sys.path.insert(0,'.')
from crrstyle import *
import numpy as np, matplotlib.pyplot as plt
setup()
P=list(csv.DictReader(open('Y155/Y155_SAME_N_PAIRWISE.csv')))
k=277/48
rows=[]
for x in P:
    s=1 if int(x['dnR5'])>0 else -1
    rows.append((int(x['N']),abs(int(x['dnR5'])),s*float(x['DeltaM']),s*k*float(x['DeltaF']),-s*k*float(x['DeltaB']),s*float(x['DeltaMi']),x['a'],x['b']))
rows.sort(key=lambda r:(r[0],r[1],r[6],r[7]))
fig=plt.figure(figsize=(7.2,5.6))
ax=fig.add_axes([0.08,0.56,0.9,0.38]); panel(ax,"a",x=-0.06)
xs=np.arange(len(rows))
ax.axhline(0,color=C["vac"],lw=0.8,zorder=0)
for i,r in enumerate(rows):
    ax.plot(i,r[2],"o",ms=7,color=C["R5"],zorder=3)
    ax.plot(i,r[3],"o",ms=11,mfc="none",mec=C["ink"],mew=0.9,zorder=4)
    ax.plot(i,r[4],"+",ms=9,color=C["ink"],mew=1.3,zorder=5)
    ax.plot(i,r[5],"s",ms=4,color=C["ctrl"],zorder=3)
# group labels
small=[i for i,r in enumerate(rows) if r[0]<5]; big=[i for i,r in enumerate(rows) if r[0]==5]
for ii,lab in [(small,"N = 2, 3, 4"),(big,"N = 5 (eleven chains)")]:
    a,b=min(ii),max(ii)
    ax.plot([a-0.3,b+0.3],[-5.2,-5.2],color=C["soft"],lw=0.8)
    ax.text((a+b)/2,-6.3,lab,ha="center",va="top",fontsize=8)
ax.set_xlim(-1,len(rows)); ax.set_ylim(-8,27)
ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
ax.set_ylabel("same-N contrast")
ax.set_yticks([0,277/24,277/12],["0","277/24","277/12"])
for y,lab in [(277/24,"one R5 substitution (32 pairs)"),(277/12,"two R5 substitutions (6 pairs)")]:
    ax.text(len(rows)-0.5,y+1.3,lab,ha="right",fontsize=7.5,color=C["soft"])
from matplotlib.lines import Line2D
h=[Line2D([],[],marker="o",ls="",color=C["R5"],ms=7,label="measured transition action, $\\Delta M_{\\rm adm}$"),
   Line2D([],[],marker="o",ls="",mfc="none",mec=C["ink"],ms=10,label="$\\kappa\\,\\Delta\\mathcal{F}_{\\rm flux}$ (causal rest content)"),
   Line2D([],[],marker="+",ls="",color=C["ink"],ms=9,mew=1.3,label="$-\\kappa\\,\\Delta B_{\\rm proj}$ (halo content)"),
   Line2D([],[],marker="s",ls="",color=C["ctrl"],ms=4,label="Y81 curvature proxy, $\\Delta M_{\\rm curv}$")]
ax.legend(handles=h,loc="upper left",ncol=2,fontsize=7.5,bbox_to_anchor=(0.0,1.12),columnspacing=1.2,handletextpad=0.3)
# panel b
Pop=list(csv.DictReader(open('Y155/Y155_COMPARATOR_POPULATION.csv')))
bx=fig.add_axes([0.08,0.08,0.5,0.36]); panel(bx,"b",x=-0.11)
F=np.array([float(p['F_flux']) for p in Pop]); M=np.array([float(p['M_adm']) for p in Pop])
N=np.array([int(p['N']) for p in Pop]); R5=np.array([int(p['nR5']) for p in Pop])
a_fit=(F*M).sum()/(F*F).sum()
xx=np.linspace(0,115,10); bx.plot(xx,a_fit*xx,ls="--",color=C["soft"],lw=1)
for n in sorted(set(N)):
    m=N==n
    cols=[C["core"] if n==1 else (C["R5"] if r>0 else C["R6"]) for r in R5[m]]
    bx.scatter(F[m],M[m],s=28,c=cols,edgecolor="white",lw=0.5,zorder=3)
    if n<5: bx.text(F[m].min()-2,M[m].min()-1,f"N={n}",ha="right",va="top",fontsize=7.5,color=C["soft"])
    else: bx.text(F[m].max()+2,M[m].min()-2,"N=5",ha="left",va="top",fontsize=7.5,color=C["soft"])
bx.text(110,4,"orange: contains R5\nteal: all-R6",ha="right",fontsize=7,color=C["soft"])
bx.annotate("DS001: no bond-local action",xy=(20,0),xytext=(32,-9),fontsize=7.5,arrowprops=dict(arrowstyle="-",color=C["soft"],lw=0.7))
bx.text(48,a_fit*48+6,"best zero-intercept fit",fontsize=7.5,color=C["soft"],rotation=33)
bx.set_xlabel("causal rest content $\\mathcal{F}_{\\rm flux}$"); bx.set_ylabel("$M_{\\rm adm}$")
bx.set_xlim(0,122); bx.set_ylim(-14,88)
cx=fig.add_axes([0.66,0.08,0.32,0.36]); cx.axis("off"); panel(cx,"c",x=0.0)
txt=("Same-N contrasts agree exactly in all 38 pairs\n"
     "($\\kappa = 277/48$, fixed by the D2 pair alone).\n\n"
     "Total values do not: the all-R6 baselines differ,\n"
     "$M_{\\rm adm}=\\frac{199}{24}(N-1)+\\frac{277}{24}n_{R5}$,\n"
     "$\\mathcal{F}_{\\rm flux}=20N+2n_{R5}$,\n"
     "so no single factor maps one onto the other\n"
     "(0/7 development, 0/11 N5 rows).\n\n"
     "Later (Y158) the action is traced to environmental\n"
     "relay dressing, not bond-produced structure.")
cx.text(0,0.95,txt,va="top",fontsize=7.6,linespacing=1.45)
save(fig,"F8_Y155_topology_contrast")
