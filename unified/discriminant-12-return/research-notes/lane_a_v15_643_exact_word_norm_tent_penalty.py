from fractions import Fraction as F
from math import isqrt
from itertools import combinations, product
P=10**35
N=160
QS=(2,3,4,5,7)
FREQ={2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),5:(0,0,1,0),7:(0,0,0,1)}
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[1],a[1]-b[0])
def mul(a,b):
 v=[x*y for x in a for y in b]
 return min(v),max(v)
def scale(a,s):return mul(a,(F(s),F(s)))
def div(a,b):assert b[0]>0;return mul(a,(1/b[1],1/b[0]))
def neg(a):return -a[1],-a[0]
def absi(a):return (0,max(-a[0],a[1])) if a[0]<=0<=a[1] else a if a[0]>0 else neg(a)
def logbound(q):
 x=F(q-1,q+1)
 s=sum((2*x**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
 e=2*x**(2*N+1)/((2*N+1)*(1-x*x))
 return s,s+e
def sqrtbound(q):
 k=isqrt(q*P*P);return F(k,P),F(k+1,P)
Ls={q:logbound(q) for q in QS}
alpha={q:div(Ls[q],scale(sqrtbound(q),2)) for q in QS}
def mod2(a):
 assert a[0]//2==a[1]//2,(float(a[0]),float(a[1]))
 return sub(a,scale((F(2),F(2)),a[0]//2))
def saw(a):return sub((F(1),F(1)),mod2(a))
def D(x,s,L):return sub(saw(sub(x,scale(L,s))),saw(x))
def G(x,s,t,A,B):
 y=add(x,scale(A,s));z=sub(x,scale(B,t))
 return add(mul(D(y,s,A),D(y,t,B)),mul(D(z,-t,B),D(z,-s,A)))
def certified_word(q,r,s,t):
 A,B=Ls[q],Ls[r]
 cuts=[(F(0),F(0)),(F(2),F(2)),mod2(scale(A,-s)),mod2(scale(B,t)),mod2(sub(scale(B,t),scale(A,s)))]
 cuts=sorted(cuts,key=lambda a:a[0])
 for a,b in zip(cuts,cuts[1:]):assert a[1]<b[0],(q,r,s,t,[(float(z[0]),float(z[1])) for z in cuts])
 vals=[]
 for a,b in zip(cuts,cuts[1:]):
  x=(a[1]+b[0])/2;x=(x,x)
  vals.append(G(x,s,t,A,B))
 return (max(a[0] for a in vals),max(a[1] for a in vals)),[(float(a),float(b)) for a,b in vals]
def label(q,r,s,t):
 return tuple(t*(FREQ[r][i])-s*FREQ[q][i] for i in range(4))
def w(n,R):return max(0,R+1-abs(n))
def corr(k,R):
 a=sum(w(n,R)**2 for n in range(-R,R+1));b=sum(w(n,R)*w(n-k,R) for n in range(-2*R,2*R+1));return F(b,a)
def tent(g,R):
 v=F(1)
 for x in g:v*=corr(x,R)
 return v
if __name__=='__main__':
 for R in (8,16,32):
  totlo=totup=F(0)
  for q,r in combinations(QS,2):
   for s,t in product((-1,1),repeat=2):
    g=label(q,r,s,t); factor=1-tent(g,R)
    I,v=certified_word(q,r,s,t)
    term=mul(alpha[q],alpha[r]);lo,up=mul(term,I);totlo+=lo*factor;totup+=up*factor
  print('R=',R,'improved',float(totlo),float(totup))
 for q,r in combinations(QS,2):
  print((q,r),[(s,t,round(float(certified_word(q,r,s,t)[0][1]),8)) for s,t in product((-1,1),repeat=2)])
