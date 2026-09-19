# Cone Derivation Ledger v13.595 — Resonant Magnetic-Driver Weighted Multiplet

Date: 2026-09-19

Status labels: [S] standard SU(2) fact, [D] exact derived, [Audit] explicitly checked, [G] structural interpretation, [O] open.

## Coordination / collision check

Immediately before this write, the live ledger reached v13.594, occupied by External Audit Round 61. v13.595 was free.

The LQG / quantum-tetrahedron lane remains a coordinated parallel path. This checkpoint returns to the magnetic-driver lane and does not import any LQG conclusion.

A repository search found no existing ledger entry containing the full resonant multiplet / rotating-frame / Rabi-path calculation below.

---

## 1. [S][D] Magnetic driver and circular basis

Take

\[
H(t)=H_0+H_\perp(t),\qquad H_0=\Omega_0J_z,\qquad \Omega_0=-\gamma B_0.
\]

For the rotating transverse field

\[
B_x=B_1\cos\omega t,\qquad B_y=B_1\sin\omega t,
\]

define

\[
B_\pm=B_x\pm iB_y,
\]

so

\[
B_-=B_1e^{-i\omega t},\qquad B_+=B_1e^{+i\omega t}.
\]

Using

\[
B_xJ_x+B_yJ_y=\frac12(B_-J_+ + B_+J_-),
\]

the transverse interaction is

\[
\boxed{
H_\perp(t)
=
-\frac{\gamma B_1}{2}
\left(
e^{-i\omega t}J_+
+
e^{+i\omega t}J_-
\right).
}
\]

The factor \(1/2\) is exact.

For an edge \(q\to q+1\),

\[
J_+|j,q\rangle=Y_q|j,q+1\rangle,
\qquad
Y_q=\sqrt{(j-q)(j+q+1)}.
\]

With

\[
X_q=q+\frac12,\qquad T=j+\frac12,
\]

the previously certified centered identity is

\[
\boxed{Y_q^2=T^2-X_q^2.}
\]

---

## 2. [D][Audit] Edge rotating-frame convention

In the ordered edge basis

\[
\mathcal B_q=(|q\rangle,|q+1\rangle),
\]

the centered rotating-frame Hamiltonian is

\[
\boxed{
H_{r,q}
=
\frac12
\begin{pmatrix}
\Delta&-\gamma B_1Y_q\\
-\gamma B_1Y_q&-\Delta
\end{pmatrix},
}
\]

with the convention

\[
\boxed{\Delta=\omega-\Omega_0.}
\]

Therefore

\[
H_{r,q}^2
=
\frac14
\left(
\Delta^2+\gamma^2B_1^2Y_q^2
\right)I_2.
\]

The dressed edge splitting is

\[
\Omega_{\rm eff,q}
=
\sqrt{\Delta^2+\gamma^2B_1^2Y_q^2}.
\]

At resonance \(\Delta=0\),

\[
\boxed{
\Omega_{R,q}=|\gamma|B_1Y_q.
}
\]

Guardrail: the off-diagonal Hamiltonian matrix element has magnitude

\[
\boxed{
|H_{12}|=\frac{|\gamma|B_1Y_q}{2}
=\frac{\Omega_{R,q}}2.
}
\]

Thus the factor of two between the Hamiltonian matrix element and the resonant population-oscillation angular frequency is explicit.

---

## 3. [D][Audit] Low-spin edge checks

### j=1/2

There is one edge, \(q=-1/2\to+1/2\), with

\[
Y=1.
\]

Hence

\[
H_r^{(1/2)}
=
\frac12
\begin{pmatrix}
\Delta&-\gamma B_1\\
-\gamma B_1&-\Delta
\end{pmatrix},
\]

and at resonance

\[
\boxed{\Omega_R=|\gamma|B_1.}
\]

### j=1

The two edges have

\[
Y_{-1}=Y_0=\sqrt2.
\]

Each restricted edge block has

\[
H_{r,q}^{(1)}
=
\frac12
\begin{pmatrix}
\Delta&-\sqrt2\gamma B_1\\
-\sqrt2\gamma B_1&-\Delta
\end{pmatrix},
\]

with resonant edge scale

\[
\boxed{\Omega_{R,q}=\sqrt2|\gamma|B_1.}
\]

### j=3/2

The three edge weights are

\[
\boxed{\sqrt3,\ 2,\ \sqrt3.}
\]

The outer restricted blocks have resonant scale

\[
\boxed{\Omega_{R,\rm outer}=\sqrt3|\gamma|B_1,}
\]

and the center restricted block has

\[
\boxed{\Omega_{R,\rm center}=2|\gamma|B_1.}
\]

These are exact restricted-edge coupling scales. For \(j>1/2\), they are not independent two-level dynamics when all Zeeman edges are simultaneously resonant.

---

## 4. [S][D][Audit] Full resonant multiplet

At exact resonance,

\[
\Delta=0,
\]

the full rotating-frame Hamiltonian is

\[
\boxed{
H_{\rm rot}^{(j)}=-\gamma B_1J_x.
}
\]

In the ordered \(J_z\) basis \(q=-j,-j+1,\ldots,j\),

\[
\boxed{
H_{\rm rot}^{(j)}
=
-\frac{\gamma B_1}{2}
\begin{pmatrix}
0&Y_{-j}&0&\cdots&0\\
Y_{-j}&0&Y_{-j+1}&\ddots&\vdots\\
0&Y_{-j+1}&0&\ddots&0\\
\vdots&\ddots&\ddots&\ddots&Y_{j-1}\\
0&\cdots&0&Y_{j-1}&0
\end{pmatrix}.
}
\]

Thus the magnetic driver realizes one connected weighted path, not a direct sum of independent two-state systems.

Writing \(M=2j+1\) and \(r=j+q+1\),

\[
\boxed{
Y_r=\sqrt{r(M-r)},\qquad r=1,\ldots,M-1.
}
\]

The previously derived arithmetic / SU(2) path weights are therefore literally the resonant magnetic hopping amplitudes, up to the common factor \(-\gamma B_1/2\).

---

## 5. [D][Audit] Full j=1 Hamiltonian

In the basis

\[
(|-1\rangle,|0\rangle,|1\rangle),
\]

\[
J_x
=
\frac1{\sqrt2}
\begin{pmatrix}
0&1&0\\
1&0&1\\
0&1&0
\end{pmatrix},
\]

hence

\[
\boxed{
H_{\rm rot}^{(1)}
=
-\frac{\gamma B_1}{\sqrt2}
\begin{pmatrix}
0&1&0\\
1&0&1\\
0&1&0
\end{pmatrix}.
}
\]

Its exact spectrum is

\[
\boxed{
E_{m_x}=-\gamma B_1m_x,
\qquad m_x=-1,0,1.
}
\]

The antisymmetric endpoint state

\[
|D\rangle
=
\frac1{\sqrt2}(|-1\rangle-|1\rangle)
\]

obeys

\[
\boxed{J_x|D\rangle=0.}
\]

This coherent dark eigenstate cannot be obtained by treating the two shared-state edge blocks as independent systems.

---

## 6. [D][Audit] Exact j=1 exponential check

Set

\[
\theta=\gamma B_1t.
\]

Because \(H_{\rm rot}=-\gamma B_1J_x\),

\[
U(t)=e^{-iH_{\rm rot}t}=e^{+i\theta J_x}.
\]

For \(j=1\), using the minimal polynomial \(J_x(J_x^2-I)=0\),

\[
U_1(t)
=
I+i\sin\theta\,J_x+(\cos\theta-1)J_x^2.
\]

Explicitly,

\[
\boxed{
U_1(t)=
\begin{pmatrix}
\frac{1+\cos\theta}{2}&\frac{i\sin\theta}{\sqrt2}&\frac{\cos\theta-1}{2}\\
\frac{i\sin\theta}{\sqrt2}&\cos\theta&\frac{i\sin\theta}{\sqrt2}\\
\frac{\cos\theta-1}{2}&\frac{i\sin\theta}{\sqrt2}&\frac{1+\cos\theta}{2}
\end{pmatrix}.
}
\]

Starting from \(|-1\rangle\),

\[
U_1(t)|-1\rangle
=
\frac{1+\cos\theta}{2}|-1\rangle
+
\frac{i\sin\theta}{\sqrt2}|0\rangle
+
\frac{\cos\theta-1}{2}|1\rangle.
\]

Equivalently,

\[
\boxed{
P_{-1}=\cos^4\frac\theta2,
\qquad
P_0=\frac12\sin^2\theta,
\qquad
P_{+1}=\sin^4\frac\theta2.
}
\]

The probabilities sum identically to one.

At \(\theta=\pi\),

\[
\boxed{
|-1\rangle\longrightarrow-|+1\rangle,
}
\]

with the intermediate state populated during the evolution. This is full spin-1 rotation through the connected path, not an isolated two-state Rabi oscillation on either edge.

---

## 7. [D][Audit] Full j=3/2 Hamiltonian

In the basis

\[
(|-3/2\rangle,|-1/2\rangle,|+1/2\rangle,|+3/2\rangle),
\]

\[
J_x
=
\frac12
\begin{pmatrix}
0&\sqrt3&0&0\\
\sqrt3&0&2&0\\
0&2&0&\sqrt3\\
0&0&\sqrt3&0
\end{pmatrix},
\]

hence

\[
\boxed{
H_{\rm rot}^{(3/2)}
=
-\frac{\gamma B_1}{2}
\begin{pmatrix}
0&\sqrt3&0&0\\
\sqrt3&0&2&0\\
0&2&0&\sqrt3\\
0&0&\sqrt3&0
\end{pmatrix}.
}
\]

Its exact spectrum is

\[
\boxed{
E_{m_x}=-\gamma B_1m_x,
\qquad
m_x=-\frac32,-\frac12,+\frac12,+\frac32.
}
\]

Thus the nonuniform \(J_z\)-basis weights \(\sqrt3,2,\sqrt3\) produce the uniformly spaced \(J_x\) spectrum.

An independent-edge treatment would instead suggest unrelated splittings \(\sqrt3|\gamma|B_1,2|\gamma|B_1,\sqrt3|\gamma|B_1\), which is not the spectrum of the four-dimensional Hamiltonian.

---

## 8. [D][Audit] Exact j=3/2 exponential check

Again let

\[
\theta=\gamma B_1t,
\qquad
c=\cos\frac\theta2,
\qquad
s=\sin\frac\theta2.
\]

For an initial lowest-weight state, the exact spin-3/2 rotation gives

\[
\boxed{
U_{3/2}(t)|-3/2\rangle
=
c^3|-3/2\rangle
+i\sqrt3\,c^2s|-1/2\rangle
-\sqrt3\,cs^2|+1/2\rangle
-i s^3|+3/2\rangle.
}
\]

Therefore

\[
\boxed{
P_{-3/2}=c^6,
\quad
P_{-1/2}=3c^4s^2,
\quad
P_{+1/2}=3c^2s^4,
\quad
P_{+3/2}=s^6.
}
\]

Their sum is exactly

\[
(c^2+s^2)^3=1.
\]

At \(\theta=\pi\),

\[
\boxed{
|-3/2\rangle\longrightarrow i\,|-i|? 
}
\]

The phase-only endpoint statement is more safely written as

\[
\boxed{
P_{+3/2}(\theta=\pi)=1,
}
\]

because the global endpoint phase depends on the rotation-sign convention. With the convention above, the amplitude is \(-i\).

Hence

\[
\boxed{
|-3/2\rangle\longrightarrow -i|+3/2\rangle
}
\]

for the stated \(U=e^{+i\theta J_x}\) convention.

This again exhibits coherent transport through the entire weighted chain.

---

## 9. [D][G] Cone interpretation of the full driver

Every off-diagonal entry obeys

\[
\boxed{
(H_{\rm rot})_{q,q+1}
=
-\frac{\gamma B_1}{2}
\sqrt{T^2-X_q^2}.
}
\]

Thus the fixed-shell circle

\[
X_q^2+Y_q^2=T^2
\]

does not merely describe isolated transition strengths. It fixes the complete hopping profile of the resonantly driven spin multiplet.

The exact hierarchy is

\[
\boxed{
\text{centered cone edge}
\to
Y_q
\to
\text{weighted }J_z\text{-basis path}
\to
J_x
\to
\text{full coherent multiplet rotation}.
}
\]

This gives the previously certified weighted SU(2) path a direct magnetic-driver realization.

---

## 10. Guardrails

1. For \(j>1/2\), an edge-restricted 2x2 Hamiltonian is an exact matrix restriction and correctly records that edge's coupling strength, but it is not an autonomous two-level dynamical subsystem when all adjacent Zeeman transitions are degenerate and resonantly driven.

2. The full resonant Hamiltonian is \(-\gamma B_1J_x\); shared basis states make the edge amplitudes interfere coherently.

3. The quantities \(|\gamma|B_1Y_q\) are valid resonant edge coupling / two-state Rabi scales. They must not be mistaken for independent dressed splittings of the full multiplet.

4. The full spectrum is always \(-\gamma B_1m_x\), with \(m_x=-j,-j+1,\ldots,j\).

5. No LQG conclusion is used here. The quantum-tetrahedron lane remains coordinated but logically separate.

6. No new arithmetic-to-electromagnetic operator equality is claimed. The exact statement is that the already-derived SU(2) weighted path is realized as the matrix of the resonant magnetic driver in the \(J_z\) basis.

---

## 11. Promoted conclusion

The magnetic-driver audit now promotes the exact statement

\[
\boxed{
H_{\rm rot}^{(j)}(\Delta=0)
=
-\gamma B_1J_x
=
-\frac{\gamma B_1}{2}A_j,
}
\]

where \(A_j\) is the weighted path adjacency matrix with edge weights

\[
\boxed{
Y_q=\sqrt{(j-q)(j+q+1)}
=\sqrt{T^2-X_q^2}.
}
\]

For \(j=1\) and \(j=3/2\), direct matrix exponentiation / exact spin rotation confirms coherent population transport across the whole path and explicitly rules out interpreting the simultaneously resonant edges as independent two-level systems.

## Open next gate

Add detuning to the full multiplet rather than to isolated edges. Determine the exact full rotating-frame Hamiltonian for arbitrary \(j\),

\[
H_{\rm rot}=\text{(detuning term)}-\gamma B_1J_x,
\]

audit its sign in the same basis convention used here, and identify the corresponding tilted effective-field rotation and its relation to the centered cone coordinates.
