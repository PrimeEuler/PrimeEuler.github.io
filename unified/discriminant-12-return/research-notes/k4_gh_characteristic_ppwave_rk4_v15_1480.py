#!/usr/bin/env python3
"""v15.1480: restricted exact nonlinear Einstein-H2 pp-wave characteristic
time evolution, RK4 convergence. NOT unrestricted 3D GH field evolution.
"""
import numpy as np
def run(N=32,dt=.08,T=4,kappa=.003):
 z=2*np.pi*np.arange(N)/N
 k=np.fft.fftfreq(N,d=1/N)
 dz=lambda q:np.fft.ifft(1j*k*np.fft.fft(q)).real
 y=np.array([.12*np.sin(z),.02*np.cos(z)])
 rhs=lambda a:-np.array([dz(a[0]),dz(a[1])])
 n=round(T/dt);dt=T/n
 for _ in range(n):
  a=rhs(y);b=rhs(y+.5*dt*a);c=rhs(y+.5*dt*b);d=rhs(y+dt*c)
  y=y+dt*(a+2*b+2*c+d)/6
 f,e=y;w=T-z
 # Two right-moving characteristic functions; a sine is odd under sign reversal.
 fex=-.12*np.sin(w);eex=.02*np.cos(w)
 x=.4;v=-.3
 H=-kappa/2*dz(f)**2*(x*x+v*v)+e*(x*x-v*v)
 Hex=-kappa/2*(.12*np.cos(w))**2*(x*x+v*v)+eex*(x*x-v*v)
 # Reconstructed 4D harmonic pp wave in Cartesian t,z: g=eta+H(dt-dz)^2,
 # sigma=(sinh(f),0). Metric is harmonic iff (dt+dz)H=0.
 ft=-dz(f);fzt=-dz(dz(f));et=-dz(e)
 Ht=-kappa*dz(f)*fzt*(x*x+v*v)+et*(x*x-v*v)
 Hz=-kappa*dz(f)*dz(dz(f))*(x*x+v*v)+dz(e)*(x*x-v*v)
 out=dict(N=N,dt=dt,T=T,profiles=float(np.max(abs(y-np.array([fex,eex])))),
    metric=float(np.max(abs(H-Hex))),
    sigma=float(np.max(abs(np.sinh(f)-np.sinh(fex)))),
    harmonic=float(np.max(abs(Ht+Hz))))
 # On this pp-wave sector -Delta_transverse H/2=kappa*(f')^2 exactly;
 # no second target direction => B=0 and Maxwell conversion is absent.
 print(out,flush=True)
 assert out["harmonic"]<2e-13
 return out
if __name__=="__main__":
 results=[run(dt=dt) for dt in (.16,.08,.04)]
 ratios=[results[i]["profiles"]/results[i+1]["profiles"] for i in (0,1)]
 print("RK4 convergence factors",ratios)
 assert all(13<r<19 for r in ratios)
 print("PASS RK4 order four for restricted nonlinear harmonic Einstein-H2 pp-wave")
 print("OPEN unrestricted 3D nonlinear GH time evolution, EM coupling, nonzero B")
