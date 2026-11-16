# Cone Derivation Ledger v15.1053 — Confocal secant/circle coordinates and T/X sign-sector quotient

Date: 2026-11-16 Eastern. Track: Gravity/Cone. Status: [D] exact geometric equalities and inversion; [N] no derived physical coupling or quarter-boundary projector. Additive continuation of v15.1052; reproducer committed earlier as 8c59a04c72b4e137503438cee9c97e75dd5bb459. Prior v13.196 and v13.691 establish rapidity-circle normalization; v13.409 identifies secant/divisor cone shell; v15.1049–1052 establish V4 mirror, null hinge, and rank-two obstruction. No foundation, Suzuki or other lane objects changed.

## Gate 853 — secant-to-circle exact compactification
For n>0, k>0, define T=(k+n/k)/2, X=(k-n/k)/2, R=sqrt(n). The previous GeoGebra ordinate (n-k²)/(2k) equals -X. Then T²-X²=n. At any positive chosen circle radius A, define
x=A X/T=A(k²-n)/(k²+n), y=A R/T=2Ak sqrt(n)/(k²+n).
Exactly x²+y²=A²; the positive-product shell maps to the open upper semicircle. Parameter s=log(k/sqrt(n)) gives x/A=tanh(s), y/A=sech(s), agreeing with v13.691 up to circle-axis convention. This is real compactification, NOT the analytic continuation s -> i theta.

## Gate 854 — exactly uniform circle abscissae require NONuniform k
For outer diameter n+1 set A=(n+1)/2, and define circle ladder x_j=j-A, y_j=sqrt[j(n+1-j)] for 1<=j<=n. Then x_j²+y_j²=A², and x_{j+1}-x_j=1.
Solving x(k)=x_j yields uniquely
k_j²=n*j/(n+1-j), k_j=sqrt[n*j/(n+1-j)].
At j=1, k_1=1; at j=n, k_n=n. In general k_j != j and consecutive k_j are NOT equally spaced, so the earlier half-step labels and unit-spaced circle ladder must not be identified without a reparameterization. Example n=11, A=6: k=2 produces x=-14/5, whereas second unit-spaced circle abscissa x_2=-4 occurs at k_2=sqrt(11/5), not k=2. The derivative dx/dk=4Ank/(k²+n)² is not constant. This is a strong spacing control, not a negative result for the existence of the map.

## Gate 855 — T/X compactifications agree but forget the sign-sector bit
For u>0 and v !=0, set w=|v| and R=sqrt(u w). For the T-cone (v>0), T=(u+w)/2, X=(u-w)/2, and the circle map is (x,y)=(A X/T,A R/T). For the X-cone (v<0), T=(u-w)/2, X=(u+w)/2, and the analogous X-normalized map (x,y)=(A T/X,A R/X). BOTH reduce to
(x,y)=(A(u-w)/(u+w), 2A sqrt(u w)/(u+w)).
Thus equal |v| on opposite sign sheets gives exactly the same circle point: projection is two-to-one in sign v. At the null hinge w=0, both reach (A,0). For the v_p(t)=-(2t-1)^p path of v15.1052, the projected arc travels to (A,0) and back to the same original circle point. No positive fixed-n shell with n>0 itself reaches the hinge at finite k: crossing varies product uv and necessarily leaves that shell.

## Gate 856 — algebraic obstruction retained
The common circle is a quotient coordinate forgetting sign(v). It cannot alone encode a sign-sector transition, determine a time orientation, select the two source boundary states of the established q2 open ladder, or recover T_q†T_q=2E_L (rank two) versus full V4 sign map (rank four). Recovering the sign requires an additional sheet label epsilon=sgn(v), so a genuine transition must act on a two-sheet carrier rather than the common circle alone. No physical action or source has been found to generate sheet flips; this gate does not predict G, frequency or EM/gravitational transfer.

## Gate 857 — arithmetic symmetry and next test
Pell scaling k -> lambda*k at fixed n acts on the normalized horizontal circle coordinate q=x/A through
q'=[lambda²(1+q)-(1-q)]/[lambda²(1+q)+(1-q)].
It is a fractional-linear (Möbius) action, generally NOT a rigid rotation of the unit circle and NOT an equal-step translation. The next source-first task is to ask whether an independently supplied physical boundary term on the doubled-circle carrier produces a self-adjoint sheet-off-diagonal operator with the open-quarter ladder's two amplitudes sqrt[(L+1)/4] without imposing a projector by hand. Absent this, the circle bridge remains geometric and its induced sign map remains rank-four on four V4 points.

Reproducibility: the prior v15.1053 SymPy script checks circle identity, T/X mirror, nonuniform spacing, Möbius action and hinge endpoints. Additional exact SymPy checks for this ledger tested x(k_j)=j-(n+1)/2, y(k_j)²=j(n+1-j), and the sign-folded circle identity. Independent Audit pending.
