import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}",
})

# Geometric mod-12 unit-shell data.
data = [
    dict(K4=1,  c=0, R=1, color="#b3211a"),
    dict(K4=5,  c=2, R=3, color="#e07b1a"),
    dict(K4=7,  c=3, R=4, color="#e8a324"),
    dict(K4=11, c=5, R=6, color="#f0c419"),
]
Rmax = 6
theta = np.linspace(0, 2*np.pi, 400)
W_SHELL=.65; W_COLOR=1.55; W_BLUE=1.; W_BLACK=.7; W_AXIS=.55; W_CONE=.75

fig = plt.figure(figsize=(20.5, 6.4))
gs = fig.add_gridspec(1, 4, width_ratios=[1,1,1,1.08], wspace=.24)

# (a) T-Circle
ax = fig.add_subplot(gs[0,0]); ax.set_title("(a) T-Circle", fontsize=11)
for d in data:
    ax.plot(d["R"]*np.cos(theta), d["R"]*np.sin(theta), color=".25", lw=W_SHELL)
for d in data:
    c,r,R,col=d["c"],d["K4"],d["R"],d["color"]; h=np.sqrt(r)
    for x in ([c,-c] if c else [0]):
        ax.plot([x,x],[-h,h],color=col,lw=W_COLOR,zorder=3)
        ax.plot([x],[h],"o",color=col,ms=4); ax.plot([x],[-h],"o",color=col,ms=4)
for k in range(1,13):
    T=np.linspace(k/2,Rmax,200); Y=np.sqrt(k*(2*T-k))
    for X in (k-T,T-k):
        ax.plot(X,Y,color="#2f6fb0",lw=.7,alpha=.28)
        ax.plot(X,-Y,color="#2f6fb0",lw=.7,alpha=.28)
Tp=np.linspace(.5,Rmax,300); Y1=np.sqrt(2*Tp-1); Xp=Tp-1; Xm=1-Tp
for X in (Xp,Xm):
    ax.plot(X,Y1,color="#2f6fb0",lw=W_BLUE,alpha=.85)
    ax.plot(X,-Y1,color="#2f6fb0",lw=W_BLUE,alpha=.85)
for d in data:
    if d["c"]:
        c=d["c"]; h=np.sqrt(d["K4"])
        ax.plot([-c,c],[h,h],color="black",lw=W_BLACK)
        ax.plot([-c,c],[-h,-h],color="black",lw=W_BLACK)
ax.axhline(0,color=".5",lw=W_AXIS); ax.axvline(0,color=".5",lw=W_AXIS)
ax.set(xlim=(-6.6,6.6),ylim=(-6.6,6.6)); ax.set_xticks(range(-6,7)); ax.set_yticks([]); ax.set_aspect("equal")
for s in ["top","right","left"]: ax.spines[s].set_visible(False)

# (b) X-Triangle
axB=fig.add_subplot(gs[0,1]); axB.set_title("(b) X-Triangle",fontsize=11)
axB.plot([-6,0,6],[6,0,6],color=".55",lw=W_CONE)
for k in range(-12,13):
    axB.plot([k,k-6],[0,6],color=".88",lw=.6)
    axB.plot([-k,6-k],[0,6],color=".88",lw=.6)
for R in [1,3,4,6]:
    axB.plot([-R,R],[R,R],color=".25",lw=W_SHELL)
tt=np.linspace(.5,6,300)
axB.plot(tt-1,tt,color="#2f6fb0",lw=1.2,alpha=.85)
axB.plot(1-tt,tt,color="#2f6fb0",lw=1.2,alpha=.85)
for d in data:
    c,r,R,col=d["c"],d["K4"],d["R"],d["color"]
    for x in ([c,-c] if c else [0]):
        axB.plot([x,x],[abs(x),R],color=col,lw=W_COLOR,zorder=3)
        axB.plot([x],[abs(x)],"o",color=col,ms=4,mfc="white",mew=1)
        axB.plot([x],[R],"s",color=col,ms=4)
for d in data:
    if d["c"]:
        x=np.linspace(-d["c"],d["c"],220)
        axB.plot(x,np.sqrt(x*x+d["K4"]),color="black",lw=W_BLACK)
axB.set(xlim=(-6.8,6.8),ylim=(-.3,6.5)); axB.set_xticks([]); axB.set_yticks([]); axB.set_aspect("equal")
for s in axB.spines.values(): s.set_visible(False)

# (c) Y-Triangle
axC=fig.add_subplot(gs[0,2]); axC.set_title("(c) Y-Triangle",fontsize=11)
axC.plot([-6,0,6],[6,0,6],color=".55",lw=W_CONE)
for k in range(1,13):
    y=np.linspace(-6,6,500); t=(k*k+y*y)/(2*k); m=t<=6
    axC.plot(y[m],t[m],color=".88",lw=.6)
for R in [1,3,4,6]:
    axC.plot([-R,R],[R,R],color=".25",lw=W_SHELL)
yu=np.linspace(-np.sqrt(11),np.sqrt(11),400)
axC.plot(yu,(1+yu*yu)/2,color="#2f6fb0",lw=1.2,alpha=.85)
for d in data:
    c,r,R,col=d["c"],d["K4"],d["R"],d["color"]; h=np.sqrt(r)
    y=np.linspace(-h,h,220); t=np.sqrt(c*c+y*y)
    axC.plot(y,t,color=col,lw=W_COLOR,zorder=3)
    axC.plot([-h,h],[R,R],"s",color=col,ms=4)
    if c: axC.plot([0],[c],"o",color=col,ms=4,mfc="white",mew=1)
for d in data:
    if d["c"]:
        h=np.sqrt(d["K4"]); R=d["R"]
        axC.plot([h,h],[h,R],color="black",lw=W_BLACK)
        axC.plot([-h,-h],[h,R],color="black",lw=W_BLACK)
axC.set(xlim=(-6.8,6.8),ylim=(-.3,6.5)); axC.set_xticks([]); axC.set_yticks([]); axC.set_aspect("equal")
for s in axC.spines.values(): s.set_visible(False)

# (d) 3D Cone
ax3=fig.add_subplot(gs[0,3],projection="3d"); ax3.set_title("(d) 3D Cone",fontsize=11)
for R in [1,3,4,6]:
    ax3.plot(R*np.cos(theta),R*np.sin(theta),R,color=".2",lw=.7)
for d in data:
    c,r,R,col=d["c"],d["K4"],d["R"],d["color"]
    for x in ([c,-c] if c else [0]):
        Y=np.linspace(0,np.sqrt(r),80); T=np.sqrt(Y*Y+x*x); X=np.full_like(Y,x)
        ax3.plot(X,Y,T,color=col,lw=1.45)
        ax3.plot(X,-Y,T,color=col,lw=1.45)
for k in range(1,13):
    T=np.linspace(k/2,6,150); Y=np.sqrt(k*(2*T-k))
    for X in (k-T,T-k):
        ax3.plot(X,Y,T,color="#2f6fb0",lw=.6,alpha=.22)
        ax3.plot(X,-Y,T,color="#2f6fb0",lw=.6,alpha=.22)
for X in (Xp,Xm):
    ax3.plot(X,Y1,Tp,color="#2f6fb0",lw=1,alpha=.85)
    ax3.plot(X,-Y1,Tp,color="#2f6fb0",lw=1,alpha=.85)
for d in data:
    if d["c"]:
        x=np.linspace(-d["c"],d["c"],220); t=np.sqrt(x*x+d["K4"])
        y=np.full_like(x,np.sqrt(d["K4"]))
        ax3.plot(x,y,t,color="black",lw=.7)
        ax3.plot(x,-y,t,color="black",lw=.7)
ax3.set_box_aspect((2,2,1))
ax3.set(xlim=(-6,6),ylim=(-6,6),zlim=(0,6))
ax3.set_axis_off()
ax3.view_init(elev=18,azim=-60)

output_path = Path(__file__).with_name("mod12_v4_cone_triple.png")
fig.savefig(output_path,dpi=200,bbox_inches="tight",facecolor="white")
print("done")
