import matplotlib as mpl
import matplotlib.pyplot as plt
C = dict(R5="#C8811A", R6="#1F6F78", core="#3A4250", vac="#C9CED4",
         act="#B23A48", ctrl="#8C949E", ink="#22262B", soft="#6B737D", light="#EEF1F4")
def setup():
    mpl.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9, "axes.titlesize": 9.5,
        "axes.labelsize": 9, "xtick.labelsize": 8, "ytick.labelsize": 8,
        "axes.edgecolor": C["soft"], "axes.labelcolor": C["ink"], "text.color": C["ink"],
        "xtick.color": C["soft"], "ytick.color": C["soft"], "axes.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "legend.frameon": False, "legend.fontsize": 8,
        "savefig.dpi": 300, "savefig.bbox": "tight", "svg.fonttype": "none"})
def panel(ax, letter, x=-0.12, y=1.04):
    ax.text(x, y, letter, transform=ax.transAxes, fontsize=11, fontweight="bold", va="bottom", ha="left")
def save(fig, name):
    for ext in ("png", "svg"):
        import os; os.makedirs("out",exist_ok=True); fig.savefig(f"out/{name}.{ext}")
    plt.close(fig)

import numpy as np
def pentagon(ax, cx, cy, r, ec=None, lw=1.1, vs=4.2, labels=False, fs=7, z=5):
    """DS001 glyph: five core vertices c0-c4 on a pentagon, direction marker h at the center."""
    ec = ec or C["core"]
    ang = np.pi/2 + np.arange(5)*2*np.pi/5   # c0 at top, then c1 (left) ... counter-clockwise
    order = [0,1,2,3,4]
    xs = cx + r*np.cos(ang); ys = cy + r*np.sin(ang)
    ax.plot(list(xs)+[xs[0]], list(ys)+[ys[0]], color=ec, lw=lw, zorder=z, solid_capstyle="round")
    for x,y in zip(xs,ys):
        ax.plot([cx,x],[cy,y], color=C["soft"], lw=0.6, ls=(0,(2,1.6)), zorder=z-1)
    ax.plot(xs, ys, "o", ms=vs, color=ec, zorder=z+1)
    ax.plot(cx, cy, "o", ms=vs*0.8, mfc="white", mec=C["soft"], mew=0.9, zorder=z+1)
    if labels:
        names=["$c_0$","$c_1$","$c_2$","$c_3$","$c_4$"]
        for x,y,n,a in zip(xs,ys,names,ang):
            ax.text(cx+(r*1.32)*np.cos(a), cy+(r*1.32)*np.sin(a), n, ha="center", va="center", fontsize=fs)
        ax.text(cx+r*0.22, cy-r*0.2, "$h$", fontsize=fs, ha="left", va="top", color=C["soft"])
    return xs, ys
