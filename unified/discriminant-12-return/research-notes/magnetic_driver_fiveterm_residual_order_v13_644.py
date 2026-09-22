#!/usr/bin/env python3
"""Independent high-precision five-term endpoint residual audit."""
import mpmath as mp
mp.mp.dps=70
pi=mp.pi
def one_period(g):
    def f(t,y):
        a,b,c,d=y; ep=mp.exp(2j*t); em=1/ep
        hp=-g*(1+ep)/4; hm=-g*(1+em)/4
        return (-1j*hp*c,-1j*hp*d,-1j*hm*a,-1j*hm*b)
    sol=mp.odefun(f,0,(1,0,0,1),tol=mp.mpf('1e-58'),degree=40)
    y=sol(pi)
    return mp.matrix([[y[0],y[1]],[y[2],y[3]]])
def mpow(M,n):
    R=mp.eye(2)
    while n:
        if n&1: R=R*M
        M=M*M; n//=2
    return R
def coeffs(j):
    cp=[j/4,
        j*(50-3*pi)/3072,
        j*(4676-810*pi+15*pi**2)/7864320,
        -j*(75004+69678*pi-3024*pi**2+63*pi**3)/12683575296,
        j*(-470860912-5604840*pi+1485540*pi**2-119880*pi**3+2025*pi**4)/mp.mpf(166988328468480)]
    ci=[j/32,
        j*(pi**2+152-16*j)/32768,
        j*(64*j**2-(1824+12*pi**2)*j+5536+39*pi**2)/12582912,
        -j*(4608*j**3-(262656+1728*pi**2)*j**2+(2841984+27648*pi**2+54*pi**4)*j-3759104-26622*pi**2-9*pi**4)/115964116992,
        j*(82944*j**4-(7879680+51840*pi**2)*j**3+(184032000+1982880*pi**2+4860*pi**4)*j**2-(1019911680+11681820*pi**2+32400*pi**4)*j+647183200+4596345*pi**2+5265*pi**4)/mp.mpf(333976656936960)]
    return cp,ci
print("eps j Rphi/eps^11 RP/eps^12")
for es in ('.2','.1','.05','.025'):
    e=mp.mpf(es); N=int(mp.nint(1/e)); U=one_period(e)
    Uh=mpow(U,N); Uf=mpow(U,2*N)
    b,d=Uh[0,1],Uh[1,1]
    base=mp.atan2(mp.sin(mp.arg(b)-mp.arg(d)-pi/2),mp.cos(mp.arg(b)-mp.arg(d)-pi/2))
    p=abs(Uf[0,1])**2
    for js in ('.5','1','1.5'):
        j=mp.mpf(js); cp,ci=coeffs(j)
        rph=2*j*base-sum(cp[k]*e**(2*k+1) for k in range(5))
        rip=1-p**(2*j)-sum(ci[k]*e**(2*k+2) for k in range(5))
        print(es,js,mp.nstr(rph/e**11,20),mp.nstr(rip/e**12,20))
