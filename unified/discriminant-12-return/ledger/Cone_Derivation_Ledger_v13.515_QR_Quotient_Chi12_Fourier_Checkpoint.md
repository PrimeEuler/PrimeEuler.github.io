# Cone Derivation Ledger v13.515 — QR Quotient / χ12 Fourier Checkpoint

**Renumbering note:** originally filed as v13.512 (and misplaced outside `ledger/`), which collided with the concurrently-created `Cone_Derivation_Ledger_v13.512_M16001_Transcripted_Gamma_Replay_Instrumentation.md` (created 6 seconds earlier). Renumbered to v13.515 and moved into `ledger/` during External Audit Round 40. Mathematical content is unchanged.

**Status:** exact/proven finite algebraic checkpoint. Spectral interpretation remains exploratory.

## 1. Signed-state carrier

Use

\[
G=\mathbf F_2^3,
\qquad
(a,b,c)\longleftrightarrow r=5^a7^b(-1)^c\pmod{24}.
\]

Thus the eight signed roots \(\{\pm1,\pm5,\pm7,\pm11\}\) form

\[
G\cong U(24)\cong C_2^3=V_4\times C_2.
\]

For the signed affine factor-line coordinates

\[
X=(r-1)/2,\qquad T=(r+1)/2,
\]

same-root sign reversal \(r\mapsto-r\) is

\[
(a,b,c)\mapsto(a,b,c+1),
\qquad
(X,T)\mapsto(-T,-X).
\]

**Guardrail:** this signed extension is an exact affine / split-quadratic-form construction. For negative \(r\), \(Y^2=r\) has no real positive-AM–GM-cone interpretation, so this is not by itself a real Lorentz symmetry of the positive cone.

## 2. QR double labeling and its quotient

On the positive \(c=0\) sheet,

\[
r=1,5,7,11,
\qquad
X=0,2,3,5,
\qquad
T=1,3,4,6.
\]

Squaring modulo 12 gives two bijections onto

\[
QR(12)=\{0,1,4,9\}:
\]

\[
Q_X=X^2\bmod12:
00\mapsto0,\;10\mapsto4,\;01\mapsto9,\;11\mapsto1,
\]

\[
Q_T=T^2\bmod12:
00\mapsto1,\;10\mapsto9,\;01\mapsto4,\;11\mapsto0.
\]

If \(h=(1,1)\), then

\[
Q_T(v)=Q_X(v+h).
\]

Ordinary multiplication on \(QR(12)\) is **not** the \(V_4\) law: e.g. \(4^2=4\), \(9^2=9\pmod{12}\). XOR appears only after transporting the \(\mathbf F_2^2\) law through either QR bijection.

For the full signed cube,

\[
Q_X(a,b,c)=q(a+c,b+c),
\qquad
Q_T(a,b,c)=q(a+c+1,b+c+1),
\]

where \(q=Q_X|_{c=0}\). Hence both QR labels factor through

\[
P:G\to\mathbf F_2^2,
\qquad
P(a,b,c)=(a+c,b+c).
\]

Its kernel is

\[
K=\ker P=\langle111\rangle=\{000,111\}.
\]

Therefore

\[
G/K\cong\mathbf F_2^2.
\]

The QR-indistinguishable signed pairs are

\[
\{1,-11\},\quad\{5,-7\},\quad\{7,-5\},\quad\{11,-1\}.
\]

## 3. Distinguish the two involutions

This distinction is binding for concurrent threads.

1. **Same-root sign involution:** multiplication by \(-1\), label \(001\):
   \[
   r\mapsto-r,
   \qquad
   (X,T)\mapsto(-T,-X),
   \qquad
   (Q_X,Q_T)\mapsto(Q_T,Q_X).
   \]

2. **Reduction-kernel / U(24)→U(12) sheet direction:** generator \(111\), corresponding to \(13\pmod{24}\). It is the kernel of \(P\) and leaves the ordered QR pair unchanged.

These are different elements/permutations of the eight-state carrier.

## 4. Character annihilator and quotient H4

Write full \(G\)-characters as

\[
\chi_\lambda(v)=(-1)^{\lambda\cdot v},
\qquad \lambda\in\mathbf F_2^3.
\]

A character descends to \(G/K\) iff it is trivial on \(111\):

\[
\lambda\cdot111=0.
\]

Thus

\[
K^\perp=\{000,110,101,011\}\cong\mathbf F_2^2.
\]

Let \(\sigma=(-1)^c=\chi_{001}\). With the established mod-12 notation

\[
\chi_{-3}=\chi_{100},\qquad
\chi_{-4}=\chi_{010},\qquad
\chi_{12}=\chi_{110},
\]

the quotient-compatible quartet is

\[
K^\perp=\{1,\chi_{12},\sigma\chi_{-3},\sigma\chi_{-4}\}.
\]

The complementary Fourier coset is

\[
\sigma K^\perp=\{\sigma,\sigma\chi_{12},\chi_{-3},\chi_{-4}\}.
\]

Multiplication by \(\sigma\) pairs the eight characters:

\[
1\leftrightarrow\sigma,
\quad
\chi_{12}\leftrightarrow\sigma\chi_{12},
\quad
\sigma\chi_{-3}\leftrightarrow\chi_{-3},
\quad
\sigma\chi_{-4}\leftrightarrow\chi_{-4}.
\]

## 5. Original H4 versus quotient H4

The original mod-12 character plane is

\[
P_0=\{(p,q,0):p,q\in\mathbf F_2\}
=\{1,\chi_{-3},\chi_{-4},\chi_{12}\}.
\]

The quotient dual plane is

\[
P_Q=K^\perp=\{(p,q,s):s=p+q\}.
\]

The character-label change is the linear shear

\[
L(p,q)=(p,q,p+q)=P^T(p,q).
\]

Hence

\[
1\mapsto1,
\qquad
\chi_{-3}\mapsto\sigma\chi_{-3},
\qquad
\chi_{-4}\mapsto\sigma\chi_{-4},
\qquad
\chi_{12}\mapsto\chi_{12}.
\]

Their intersection is exactly

\[
P_0\cap P_Q=\{000,110\}=\{1,\chi_{12}\}.
\]

Thus \(\chi_{12}\) is the unique nonprincipal character shared unchanged by these two independently defined \(H_4\) planes.

## 6. Exact Fourier intertwining

Let the unnormalized Hadamard character tables be

\[
(H_8)_{\lambda,v}=(-1)^{\lambda\cdot v},
\qquad
(H_4)_{\mu,u}=(-1)^{\mu\cdot u}.
\]

Then

\[
H_8^2=8I_8,
\qquad
H_4^2=4I_4.
\]

Let \(J\) be the \(8\times4\) incidence/pullback matrix

\[
J_{v,u}=1\iff P(v)=u.
\]

Each quotient fiber has size 2, so

\[
J^TJ=2I_4.
\]

Let \(R\) be the \(8\times4\) character-selection matrix embedding quotient character \(\mu\) as \(P^T\mu\in K^\perp\). Then

\[
R^TR=I_4.
\]

The basic duality identity

\[
(P^T\mu)\cdot v=\mu\cdot P(v)
\]

gives the exact unnormalized intertwining formulas

\[
H_8J=2RH_4,
\qquad
H_8R=JH_4.
\]

With normalized transforms

\[
\mathcal F_8=\frac1{\sqrt8}H_8,
\qquad
\mathcal F_4=\frac12H_4,
\qquad
\mathcal P=\frac1{\sqrt2}J,
\]

these become

\[
\boxed{\mathcal F_8\mathcal P=R\mathcal F_4},
\qquad
\boxed{\mathcal F_8R=\mathcal P\mathcal F_4}.
\]

Equivalently, if

\[
\Pi_K=\mathcal P\mathcal P^T,
\qquad
\Pi_{K^\perp}=RR^T,
\]

then

\[
\boxed{\mathcal F_8\Pi_K=\Pi_{K^\perp}\mathcal F_8}.
\]

In state coordinates,

\[
(\Pi_Kf)(v)=\frac12\bigl(f(v)+f(v+111)\bigr).
\]

Thus averaging over the QR-kernel direction is Fourier-dual to retaining precisely the four \(K\)-even characters.

## 7. Bounded claim for Pell / χ12 / Suzuki threads

The QR quotient gives an exact finite-algebraic explanation for why \(\chi_{12}\) survives unchanged in this construction:

\[
\boxed{P_0\cap K^\perp=\{1,\chi_{12}\}.}
\]

Equivalently, \(\chi_{12}\) is trivial on the QR-kernel direction \(K=\langle111\rangle\), while \(\chi_{-3}\) and \(\chi_{-4}\) require a sheet-character twist to descend to the quotient.

This compatibility is exact at the signed-state / QR / finite Fourier-Hadamard level.

### Guardrail

This does **not** establish:

- that the QR quotient occurs in the Suzuki operator;
- that \(\Pi_K\) or \(\Pi_{K^\perp}\) intertwines a Suzuki operator, Schur complement, or terminal unresolved plane;
- that Pell dynamics induces this quotient;
- that the survival of \(\chi_{12}\) has spectral consequences;
- any new Suzuki index bound;
- any zero-location, critical-line, RH, or GRH statement.

Any Pell/Suzuki bridge must be demonstrated independently by propagating an authentically defined source/operator quantity through the existing Suzuki pipeline and showing a downstream invariant not forced by this finite \(V_4/H_8\) algebra alone.

**Checkpoint status:** exact/proven finite algebraic result; safe for other threads to reuse subject to the above guardrail.
