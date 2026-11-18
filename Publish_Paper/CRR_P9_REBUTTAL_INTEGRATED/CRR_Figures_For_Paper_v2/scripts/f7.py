import sys; sys.path.insert(0,'.')
from crrstyle import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
setup()
K={"neg":("exact negative",C["act"],True),"circ":("circular",C["ctrl"],False),
   "reint":("reinterpreted",C["core"],False),"unav":("no coupling available",C["act"],False)}
rows=[("Y81 inertial-curvature proxy, $N\\cdot\\frac{5}{8}\\ln 2$","same-N topology test","exactly topology-blind","neg","Y81, Y149"),
("Candidate A rest content, $6N\\ln 2$","fit to the proxy","fits, but built from the same machinery","circ","Y88, Y149"),
("Causal rest content $\\mathcal{F}$ and Candidate B","proportionality to the proxy","structurally impossible on same-N pairs","neg","Y99, Y100, Y149"),
("$\\mathcal{F}$ as a state quantity","rest/motion branch test","trajectory action, not a state function","reint","Y108"),
("Conserved state scalar, 80-motif basis","grammar-derived search","only constituent number survives","neg","Y109–Y112"),
("Admissible transition action $M_{\\rm adm}$","same-N and total-value tests","38/38 contrasts; totals fail; environmental dressing","reint","Y154–Y158"),
("Rest-local exchange channel","eligibility screen; minimal extension","none eligible; rival gate destroys recurrence","unav","Y165-D0, C3")]
fig=plt.figure(figsize=(7.2,5.2)); ax=fig.add_axes([0,0,1,1]); ax.axis("off")
ax.set_xlim(0,10); ax.set_ylim(-1.6,len(rows)+0.6)
for x,lab in [(1.85,"candidate"),(4.85,"test"),(7.55,"outcome")]: ax.text(x,len(rows)+0.25,lab,ha="center",fontsize=8,color=C["soft"])
for i,(cand,test,out,cat,st) in enumerate(rows):
    y=len(rows)-1-i+0.3
    w=3.6
    ax.add_patch(FancyBboxPatch((1.85-w/2,y-0.32),w,0.64,boxstyle="round,pad=0,rounding_size=0.08",fc=C["light"],ec=C["core"],lw=0.9))
    ax.text(1.85,y+0.06,cand,ha="center",va="center",fontsize=7.3)
    ax.text(1.85,y-0.2,st,ha="center",va="center",fontsize=6.4,color=C["soft"])
    ax.text(4.85,y,test,ha="center",va="center",fontsize=7.3,color=C["ink"])
    name,col,fill=K[cat]
    ax.plot(6.35,y,"o" if cat!="unav" else "s",ms=8,mfc=col if fill else "white",mec=col,mew=1.4)
    ax.text(6.6,y+0.1,out,va="center",fontsize=7.3)
    ax.text(6.6,y-0.17,name,va="center",fontsize=6.6,color=col)
ax.annotate("",xy=(1.85,-0.55),xytext=(1.85,-0.05),arrowprops=dict(arrowstyle="->",color=C["core"],lw=1))
ax.add_patch(FancyBboxPatch((0.25,-1.45),9.5,0.8,boxstyle="round,pad=0,rounding_size=0.1",fc="white",ec=C["act"],lw=1.3))
ax.text(5.0,-1.05,"Within the tested architecture, rest energy $E_0$ and an independently calibrated inertial mass are operationally\nundefined, so $M_i=\\alpha E_0$ cannot yet be tested. This is not a finding that either is zero.",
        ha="center",va="center",fontsize=7.8)
save(fig,"F7_mass_energy_decision_map")
