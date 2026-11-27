import sympy as S
s,r=S.symbols('s r',real=True)
w=lambda s:s*(1-s)/2
k=s*(r-s)*(1-r)/2
d=s*s*(1-r)**2/2
I=lambda f,a,b,c,e:S.integrate(S.integrate(f,(s,a,b)),(r,c,e))
norm=2*I(k*k,0,r,0,1)
wnorm=S.integrate(w(s)**2,(s,0,1))
kw=S.factor(S.integrate(k*w(r),(r,s,1))-S.integrate(r*(s-r)*(1-s)/2*w(r),(r,0,s)))
kwnorm=S.integrate(kw**2,(s,0,1))
proj=S.factor(norm-2*kwnorm/wnorm)
assert (norm,wnorm,kwnorm,proj)==(S.Rational(1,10080),S.Rational(1,120),S.Rational(31,79833600),S.Rational(1,166320))
bound=S.sqrt(proj/2)
h=S.Rational(1,2)
P=2*I(k,0,h,h,1)
H=2*(I(d,0,r,0,h)+I(d,h,r,h,1))
assert (P,H)==(S.Rational(1,192),S.Rational(11,2880))
n=8; h=S.Rational(1,n)
z=[S.Rational(49,1000)*(x+S.I*y) for x,y in [(2,-20),(7,-19),(8,-3),(5,-1),(5,1),(8,3),(7,19),(2,20)]]
P=H=0
for i in range(n):
    a=i*h; b=a+h
    H+=2*I(d,a,r,a,b)*S.Abs(z[i])**2
    for j in range(i+1,n):
        c=j*h; e=c+h; C=S.conjugate(z[i])*z[j]
        P+=2*S.im(C)*I(k,a,b,c,e)
        H+=2*S.re(C)*I(d,a,b,c,e)
cap=max(S.Abs(x)**2 for x in z)
assert (P,H,cap)==(S.Rational(578641,307200000),S.Rational(355350401,368640000000),S.Rational(98441,100000))
assert P>bound and H<S.Rational(1,1000) and cap<1
print(norm,wnorm,kw,kwnorm,proj,bound)
print(P,H,cap,'threshold',S.N(bound*H/P,16))
