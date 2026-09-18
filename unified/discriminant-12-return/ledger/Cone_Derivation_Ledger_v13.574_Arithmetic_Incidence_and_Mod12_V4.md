# Cone Derivation Ledger v13.574 — Arithmetic Incidence Theorem and Certified Mod-12 V4 Action

**Renumbering note:** originally filed as v13.573, which collided with the already-pushed `Cone_Derivation_Ledger_v13.573_External_Audit_Round_52.md`. Renumbered to v13.574 during External Audit Round 53. Mathematical content is unchanged.

## Status
Exact algebraic/arithmetic theorem. This entry combines the AM-GM cone factor-hyperbola coordinates with the classical divisor summatory identity, then maps the resulting factor/root involutions onto the already-certified projective reflection correspondence of v13.557. No new identification of cone coordinates with the character basis is made.

## 1. Fixed-n factor-hyperbola incidence

Let n be a positive integer and let u in {1,...,n}. On the factor hyperbola ab=n take the continuous row sample

a=u,  b=n/u.

Under the Paper-A AM-GM coordinates

T=(a+b)/2,
X=(b-a)/2,
Y^2=ab,

define

T_n(u) = (u+n/u)/2,
X_n(u) = (n/u-u)/2.

Then exactly

T_n(u)^2 - X_n(u)^2 = n,
Y^2=n.

Thus every positive row sample of ab=n lifts to the same fixed-n cone hyperbola. The two root lifts and factor-exchanged lifts form

O_n(u) = {(+/- X_n(u), +/- sqrt(n), T_n(u))}.

Define the reflected full separation

g_n(u) = 2 X_n(u) = n/u-u = (n-u^2)/u.

The factor 2 is geometrically the full separation between the two factor-exchanged incidences across X=0.

## 2. Divisor incidences and the square fixed locus

If u divides n, then n/u is an integer and (u,n/u) is an integer factor pair. Its cone coordinates satisfy

(T_n(u),X_n(u)) in (1/2 Z)^2.

Factor exchange (u,n/u) <-> (n/u,u) sends X -> -X and fixes T and Y^2.

The factor-exchange fixed-point condition is

X_n(u)=0
<=> n/u=u
<=> n=u^2.

Therefore squares are exactly the arithmetic fixed points of factor exchange.

For a pronic n=m(m+1), the closest factor pair gives

X_n(m)=+1/2,

with the exchanged incidence at X=-1/2. Hence pronics give the nearest nontrivial reflected arithmetic orbit to the square fixed locus.

## 3. Positive unfloored sampling, divisor count, and residual

The positive unfloored row samples satisfy

sum_{u=1}^n n/u = n H_n.

The integer lattice count below the same factor hyperbola is the divisor summatory function

D(n) = sum_{u=1}^n floor(n/u)
     = #{(a,b) in Z_{>0}^2 : ab <= n}.

Using

n/u = floor(n/u) + {n/u}

and summing gives the exact identity

n H_n = D(n) + sum_{u=1}^n {n/u},

hence

n H_n - D(n) = sum_{u=1}^n {n/u}.

If u divides n then {n/u}=0, so equivalently

n H_n - D(n)
= sum_{1<=u<=n, u not dividing n} {n/u}.

Because u is integral,

{g_n(u)} = {n/u-u} = {n/u}.

Therefore the same residual is encoded by the reflected separation:

n H_n - D(n)
= sum_{u=1}^n {g_n(u)}
= sum_{u=1}^n {2 X_n(u)}.

This is an exact equality for the ordinary fractional-part convention {x}=x-floor(x).

Important distinction: the signed reflected pair g_n(u)+(-g_n(u)) vanishes identically for every u and is NOT n H_n. The positive unfloored sum n H_n and the signed reflection cancellation are different constructions.

## 4. Symmetric half-hyperbola form of D(n)

Let m=floor(sqrt(n)). For 1<=u<=m, g_n(u)>=0 and

floor(g_n(u)) = floor(n/u)-u.

Therefore

sum_{u=1}^m [2 floor(g_n(u))+1]
= 2 sum_{u=1}^m floor(n/u) - m^2
= D(n),

the classical Dirichlet hyperbola identity.

Thus the reflection factor 2 has an exact geometric meaning: it counts the two X-reflected sides, while the +1 is the symmetry-axis contribution for each sampled row in the rearranged count.

## 5. Native arithmetic involutions

Define on cone incidence coordinates

F(X,Y,T)=(-X,Y,T),
S(X,Y,T)=(X,-Y,T).

Then

F^2=S^2=I,
FS=SF,

so

V_inc={I,F,S,FS} ~= V4.

Their arithmetic meanings are:

F: factor exchange / row-column exchange,
S: root-sheet exchange +sqrt(n) <-> -sqrt(n),
FS: simultaneous factor and root-sheet exchange.

For a generic incidence p=(X,+sqrt(n),T),

I p  = ( X,+sqrt(n),T),
F p  = (-X,+sqrt(n),T),
S p  = ( X,-sqrt(n),T),
FS p = (-X,-sqrt(n),T).

The factor hyperbola T^2-X^2=n, the fixed-T circle X^2+Y^2=T^2, and the scalar quantities n, D(n), nH_n, and nH_n-D(n) are invariant under this incidence action. The signed separation is F-anti-invariant:

F: g_n(u) -> -g_n(u).

The counts are invariant while the incidences carrying them form V4 orbits.

## 6. Certified v13.557 projective correspondence

Ledger v13.557 established, by exact finite-group/matrix computation, the determinant-one kernel

K={I,K_5,K_7,K_11}

with

K_5  = -R_X,
K_7  = R_X R_Y,
K_11 = -R_Y,

where

R_X=diag(-1,+1,+1),
R_Y=diag(+1,-1,+1).

It further established from the v13.545 equivariant cyclic-order labeling

T_5  <-> K_5  = -R_X,
T_7  <-> K_7  = R_XR_Y,
T_11 <-> K_11 = -R_Y.

Projectively,

T_5  <-> [R_X],
T_7  <-> [R_XR_Y],
T_11 <-> [R_Y].

Since the arithmetic involutions are exactly

F=R_X,
S=R_Y,
FS=R_XR_Y,

the label-preserving arithmetic interpretation of the certified v13.557 correspondence is

T_5  <-> F  = factor exchange,
T_7  <-> FS = factor exchange + root-sheet exchange,
T_11 <-> S  = root-sheet exchange.

Together with T_1 <-> I, this gives the projective incidence dictionary

1  -> I,
5  -> F,
7  -> FS,
11 -> S.

The multiplication agrees element-by-element:

5*11 = 7 mod 12  <->  F S = FS,
5*7  = 11 mod 12 <->  F(FS)=S,
7*11 = 5 mod 12  <->  (FS)S=F.

Thus the certified mod-12 translation V4 acts projectively as the factor/root incidence V4 on the cone.

## 7. n=11 / T=6 incidence

For n=11 and u=1,

X_11(1)=5,
T_11(1)=6,
Y^2=11.

The four incidence lifts are

(+5,+sqrt(11),6),
(-5,+sqrt(11),6),
(+5,-sqrt(11),6),
(-5,-sqrt(11),6).

All lie on

X^2+Y^2=36

and

T^2-X^2=11.

Their certified projective V4 action is:

T_5:  horizontal factor-exchange edge X <-> -X,
T_11: vertical root-sheet edge Y <-> -Y,
T_7:  simultaneous exchange, taking opposite corners.

Hence the rectangle visible in the flat V4 cone picture is a Cayley square for the certified mod-12 translation action, with the horizontal black fixed-n factor-hyperbola projection carrying the factor-exchange edges.

## 8. Theorem statement

Arithmetic Incidence / Mod-12 V4 Theorem.

For every positive integer n, the AM-GM image of the continuous factor-hyperbola samples (u,n/u) is

(T_n(u),X_n(u),Y^2)
=
((u+n/u)/2,(n/u-u)/2,n),

with T_n(u)^2-X_n(u)^2=n. Integer factor pairs are precisely divisor-aligned samples. Their factor exchange is X->-X; root-sheet exchange is Y->-Y. These commuting involutions generate a native incidence V4.

The positive unfloored samples, their integer lattice count, and their residual satisfy exactly

sum_{u=1}^n n/u = nH_n,

D(n)=sum_{u=1}^n floor(n/u),

nH_n-D(n)
=sum_{u=1}^n {n/u}
=sum_{u=1}^n {2X_n(u)}.

Under the already-certified v13.557 projective generator correspondence, the incidence involutions carry the existing mod-12 labels

T_5 <-> factor exchange,
T_11 <-> root-sheet exchange,
T_7 <-> their product.

Thus the scalar divisor/harmonic quantities are invariants of the same projective V4 whose nonidentity elements exchange the geometric incidence representatives.

## Guardrails

- Exact: all coordinate identities, divisor-summatory identities, reflection relations, and the reduction to the v13.557 certified projective dictionary.
- Do not state K=V_inc literally in GL_3(C). The determinant-one kernel uses -R_X and -R_Y; equality with the native incidence reflections is projective.
- Do not identify cone coordinates (X,Y,T) with the character basis (chi_-4,chi_-3,chi_12). v13.557 explicitly warns that the numerically similar diagonal sign matrices live in different coordinate spaces; v13.554 supplies a nontrivial intertwiner.
- Preserve the v13.557 labels: T_5 is factor exchange projectively, T_11 is root-sheet exchange projectively, and T_7 is their product.
- The identity {g_n(u)}={n/u} uses the ordinary fractional-part convention. A separate mod-1/2 residue sum requires its own representative/sign convention and is not promoted here.
- Divisors certainly vanish under reduction modulo 1/2 because g_n(u) is integral when u|n; the converse is not asserted.
- The signed reflected pair sum is zero and must not be conflated with the positive unfloored sum nH_n.
