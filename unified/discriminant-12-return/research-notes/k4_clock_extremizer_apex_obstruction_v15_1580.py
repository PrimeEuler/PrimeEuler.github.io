import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
for e,d in [(.1,.05),(.1,.2),(.3,.05),(.5,.01),(.5,.2)]:
 C=(1-e)*(1+d)
 def K(c):return (C*e/c-1+C*C/c)/C
 def j(x,c):return 1+K(c)*x-x*x/c
 c=brentq(lambda c:np.log(e)+quad(lambda x:x/(c*j(x,c)),0,C)[0],1e-8,100,xtol=1e-14)
 k=K(c); gap=np.hypot(c*k,2*np.sqrt(c)); xp=(c*k+gap)/2; xm=-c/xp
 p=xp/gap
 L=quad(lambda x:2/(np.sqrt(c)*j(x,c)),0,C)[0]; g=np.hypot(np.pi,L)/L
 amp=np.hypot(k/np.sqrt(c),2*g/c)
 assert 0<p<1 and xp>C
 # exact integrated area radius, normalized v(0)=1
 def v(x):return ((xp-x)/xp)**p*((x-xm)/(-xm))**(1-p)
 assert abs(v(C)-e)<1e-9
 t=xp*np.array([1e-4,1e-5,1e-6]); x=xp-t
 slope=np.diff(np.log(v(x)))/np.diff(np.log(t))
 curv=amp/(t*(x-xm)/c)**2
 assert abs(slope[-1]-p)<1e-5
 assert abs(curv[-1]*t[-1]**2-amp*c*c/gap**2)<1e-4
 print(f'{e} {d} p={p:.10f} backward_extension={xp-C:.10g} curvature_coefficient={amp*c*c/gap**2:.10g} slope={slope[-1]:.10f}')
