#!/usr/bin/env python3
"""High-precision exact-dynamics residual test after four known endpoint terms."""
import mpmath as mp
mp.mp.dps=70
pi=mp.pi
def rhs(g):
    def f(t,y):
        a,b,c,d=y; ep=mp.e**(2j*t); em=1/ep
        # H=[[-g/4? rotating expression diagonal zero], offdiagonal]
        hp=-g/4*ep-g/4 # Jx contribution -g/2 Jx = offdiag -g/4
        hm=-g/4*em-g/4
        return [-1j*hp*c,-1j*hp*d,-1j*hm*a,-1j*hm*b]
    return f
# use Taylor ODE exact evolution; endpoints are stroboscopic for reciprocal integer eps
def U(g,t):
    sol=mp.odefun(rhs(g),0,(1,0,0,1),tol=mp.mpf('1e-55'),degree=40)
    return sol(t)
def coeffs(j):
    c1=j/4
    c3=j*(50-3*pi)/3072
    c5=j*(4676-810*pi+15*pi**2)/7864320
    c7=-j*(75004+69678*pi-3024*pi**2+63*pi**3)/12683575296
    p2=j/32
    p4=j*(pi**2+152-16*j)/32768
    p6=j*(64*j**2-(1824+12*pi**2)*j+5536+39*pi**2)/12582912
    p8=-j*(4608*j**3-(262656+1728*pi**2)*j**2+(2841984+27648*pi**2+54*pi**4)*j-3759104-26622*pi**2-9*pi**4)/115964116992
    return c1,c3,c5,c7,p2,p4,p6,p8
print("eps,j,Rphi/eps^9,RP/eps^10")
for eps in map(mp.mpf,('0.2','0.1','0.05')):
    uh=U(eps,pi/eps); uf=U(eps,2*pi/eps)
    # initial down=(0,1): column 2 = (b,d)
    b,d=uh[1],uh[3]; p=abs(uf[1])**2
    base=mp.arg(b)-mp.arg(d)-pi/2
    base=mp.atan2(mp.sin(base),mp.cos(base))
    for js in ('0.5','1','1.5'):
        j=mp.mpf(js); C=coeffs(j)
        phase=2*j*base
        rp=phase-(C[0]*eps+C[1]*eps**3+C[2]*eps**5+C[3]*eps**7)
        inf=1-p**(2*j)
        ri=inf-(C[4]*eps**2+C[5]*eps**4+C[6]*eps**6+C[7]*eps**8)
        print(mp.nstr(eps,4),js,mp.nstr(rp/eps**9,18),mp.nstr(ri/eps**10,18))
