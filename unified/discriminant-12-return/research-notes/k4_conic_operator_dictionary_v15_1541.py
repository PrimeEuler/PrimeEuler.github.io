import sympy as s
h,b,d,y,z,t=s.symbols('h b d y z t',positive=True)
P=y**2/(2*h)
assert s.diff(P,y,2)==1/h
A=s.integrate(b**2/(2*h)-P,(y,-b,b))
assert s.simplify(A/(b**3/h))==s.Rational(2,3)
Ap=A.subs(b,s.sqrt(2*h*d))
assert s.simplify(d*s.diff(Ap,d)/Ap)==s.Rational(3,2)
# curvature center of graph (y,P(y))
p=s.diff(P,y); pp=s.diff(P,y,2)
E=s.simplify(y-p*(1+p*p)/pp); F=s.simplify(P+(1+p*p)/pp)
assert s.simplify(E+y**3/h**2)==0
assert s.simplify(F-h-3*y*y/(2*h))==0
assert s.simplify(27*h*E**2-8*(F-h)**3)==0
# dimensionless cap functions A/h^2, width half-span b/h
wH=s.sqrt(z*(2+z)); wC=s.sqrt(z*(2-z))
AH=(1+z)*wH-s.acosh(1+z)
AC=s.acos(1-z)-(1-z)*wC
assert s.simplify(s.diff(AH,z)-2*wH)==0
assert s.simplify(s.diff(AC,z)-2*wC)==0
# expansions via integral of the widths; exact leading corrections
for sign in (1,-1):
 w=s.sqrt(2*z)*s.sqrt(1+sign*z/2)
 a=s.integrate(2*s.series(w,z,0,4).removeO(),z)
 ratio=s.series(a/(2*z*w),z,0,3)
 print('sign',sign,'ratio',ratio)
 assert s.simplify(ratio.removeO().coeff(z,1)+sign/s.Integer(15))==0
print('parabola area',Ap,'evolute',E,F)
for zz in (.01,.1,.5,1.):
 print('depth/radius',zz,'hyperbola',float((AH/(2*z*wH)).subs(z,zz)),'parabola',2/3,'circle',float((AC/(2*z*wC)).subs(z,zz)))
print('PASS')
