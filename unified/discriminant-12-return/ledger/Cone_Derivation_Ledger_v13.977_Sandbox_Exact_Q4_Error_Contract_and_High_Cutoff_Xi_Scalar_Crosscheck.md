# Cone Derivation Ledger v13.977 — Sandbox: Exact Q4 Error Contract and High-Cutoff Xi-Scalar Cross-Check

**Date:** 2026-10-03  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] exact numerical-KKT to exact-Q4 error theorem; [D] no global ground-state inverse; [N] independent high-cutoff energy/phase cross-check from the frozen v13.974 + KKT payload; [N] strong cutoff flow away from the N=96 near-one scalar; [G] no exact finite-a scalar interval yet; [O] certify remote transformed residuals and exact-P4 replacement errors  
**Authorization:** Jeremy, 2026-10-03 ("awesome continue")  
**Parents:** v13.801, v13.823–836, v13.965–976  
**Audit context:** External Audit Round 150 independently confirms v13.973–975.  
**Payloads:** frozen P4 carrier at v13.974; KKT payload under \`research-notes/p4_payload_kkt/{even-v,odd-v}/\`.  
**Collision check:** v13.977 was absent immediately before this write.

---

## 0. Purpose

Two questions are now separable.

1. How does a frozen-carrier KKT solve compare with the true exact-\(Q_4\) nonresonant response?
2. What does the newly uploaded high-cutoff numerical carrier predict for the Xi scalar before exact error propagation?

The first question has an exact answer.

The second receives a new numerical cross-check, with strict guardrails.

---

# Part I. Exact \(Q_4\) error contract

## 1. Exact and numerical projectors [D]

Let

\[
P=P_4,\qquad Q=I-P,
\]

where

\[
P=\mathbf 1_{(-0.02,0.02)}(J_T)
\]

is the exact four-channel spectral projector.

Let the normalized frozen numerical carrier be

\[
\widehat Y,\qquad \widehat Y^*\widehat Y=I_4,
\]

with

\[
\widehat P=\widehat Y\widehat Y^*,
\qquad
\widehat Q=I-\widehat P.
\]

Assume the certified projector error

\[
\boxed{
\|P-\widehat P\|
\le
\varepsilon_P.
}
\tag{1}
\]

The later block-energy refinement applies to the unchanged v13.974 carrier whenever its hypotheses are retained.

---

## 2. Exact nonresonant response [D]

For any transformed tail right-hand side

\[
g,
\]

the exact nonresonant response is

\[
\boxed{
y
=
Q(J_Q)^{-1}Qg,
}
\tag{2}
\]

where

\[
J_Q=QJ_TQ
\]

on \(\operatorname{Ran}Q\).

From the exact \(0.10\) spectral moat,

\[
\boxed{
\|J_Q^{-1}\|<10.
}
\tag{3}
\]

---

## 3. Frozen-carrier KKT pair [D]

Let the numerical KKT solution and multiplier satisfy

\[
\boxed{
J_T\widehat y
+
\widehat Y\lambda
=
g-e,
}
\tag{4}
\]

with orthogonality defect

\[
\boxed{
\eta
=
\|\widehat Y^*\widehat y\|.
}
\tag{5}
\]

For an exact solve with an exactly normalized carrier,

\[
e=0,\qquad \eta=0.
\]

---

## 4. Project onto exact \(Q\) [D]

Apply \(Q\) to (4):

\[
QJ_T\widehat y
+
Q\widehat Y\lambda
=
Qg-Qe.
\]

Since \(P\) is a spectral projector of \(J_T\),

\[
QJ_TP=0.
\]

Therefore

\[
QJ_T\widehat y
=
J_Q(Q\widehat y),
\]

and hence

\[
J_Q(Q\widehat y-y)
=
-Qe-Q\widehat Y\lambda.
\]

Using (3),

\[
\boxed{
\|Q\widehat y-y\|
\le
10
\left(
\|e\|
+
\|Q\widehat Y\lambda\|
\right).
}
\tag{6}
\]

---

## 5. Projector-angle leakage [D]

Because

\[
Q\widehat Y
=
(\widehat P-P)\widehat Y,
\]

\[
\boxed{
\|Q\widehat Y\|
\le
\varepsilon_P.
}
\tag{7}
\]

Thus

\[
\boxed{
\|Q\widehat y-y\|
\le
10
\left(
\|e\|
+
\varepsilon_P\|\lambda\|
\right).
}
\tag{8}
\]

Also

\[
P\widehat y
=
(P-\widehat P)\widehat y
+
\widehat P\widehat y,
\]

so

\[
\boxed{
\|P\widehat y\|
\le
\varepsilon_P\|\widehat y\|
+
\eta.
}
\tag{9}
\]

Combining (8) and (9),

\[
\boxed{
\|y-\widehat y\|
\le
10
\left(
\|e\|
+
\varepsilon_P\|\lambda\|
\right)
+
\varepsilon_P\|\widehat y\|
+
\eta.
}
\tag{10}
\]

This is the main exact-complement error theorem.

---

## 6. Original-coordinate residual [D]

For the original tail-coordinate KKT solve,

\[
A_Tx+B_TZ\lambda=b,
\]

define

\[
r=b-A_Tx-B_TZ\lambda.
\]

Then

\[
\widehat y=B_T^{1/2}x,
\]

and

\[
\boxed{
e=B_T^{-1/2}r.
}
\tag{11}
\]

Therefore

\[
\boxed{
\|e\|
=
\|B_T^{-1/2}r\|.
}
\tag{12}
\]

Any certified smooth-bulk floor

\[
B_T\succeq\beta I
\]

implies the safe conversion

\[
\boxed{
\|e\|
\le
\beta^{-1/2}\|r\|.
}
\tag{13}
\]

Sharper block-energy estimates remain preferable.

---

## 7. Core-coupling and source consequences [D]

For the two core-coupling right-hand sides, define

\[
\Delta_j
=
10
\left(
\|e_j\|
+
\varepsilon_P\|\lambda_j\|
\right)
+
\varepsilon_P\|\widehat y_j\|
+
\eta_j,
\qquad j=1,2.
\]

Then

\[
\|y_j-\widehat y_j\|
\le
\Delta_j.
\]

If

\[
C=B_T^{-1/2}A_{TC},
\]

the exact versus numerical nonresonant self-energy satisfies

\[
\boxed{
\|\Sigma_Q-\widehat\Sigma_Q\|
\le
\|C\|
\sqrt{\Delta_1^2+\Delta_2^2}.
}
\tag{14}
\]

For the source solve,

\[
\Delta_f
=
10
\left(
\|e_f\|
+
\varepsilon_P\|\lambda_f\|
\right)
+
\varepsilon_P\|\widehat y_f\|
+
\eta_f,
\]

and

\[
\boxed{
\|C^*y_f-C^*\widehat y_f\|
\le
\|C\|\Delta_f.
}
\tag{15}
\]

No tiny full-operator ground energy appears anywhere in these bounds.

---

# Part II. Frozen high-cutoff numerical cross-check

## 8. Uploaded KKT midpoint data [N]

The sandbox KKT payload freezes, for each parity:

- \(G_B\);
- \(K_0\);
- \(X_C\);
- \(x_f\);
- \(\widehat H_C(0)\);
- \(\widehat f_6\);
- three saddle multipliers;
- finite saddle residual diagnostics.

The B-orthogonality defects are tiny:

\[
\boxed{
\|G_{B,e}-I\|
\approx6.43\times10^{-14},
}
\]

\[
\boxed{
\|G_{B,o}-I\|
\approx2.90\times10^{-14}.
}
\]

The finite saddle residuals are at approximately

\[
10^{-14}\text{--}10^{-16}.
\]

These are finite midpoint residuals only; remote-tail continuation remains separate.

---

## 9. Renormalized core matrices [N]

The frozen numerical renormalized cores are

\[
\widehat H_{C,e}(0)
\approx
\begin{pmatrix}
2.14472654\times10^{-7}
&
6.34416023\times10^{-7}
\\
6.34416023\times10^{-7}
&
1.87662412\times10^{-6}
\end{pmatrix},
\]

and

\[
\widehat H_{C,o}(0)
\approx
\begin{pmatrix}
2.11780161\times10^{-5}
&
4.31142062\times10^{-5}
\\
4.31142062\times10^{-5}
&
8.77726210\times10^{-5}
\end{pmatrix}.
\]

After reinserting the four numerical Ritz channels, the resulting two-dimensional Schur collapses are approximately

even-v:

\[
\boxed{
-1.72\times10^{-12},
\qquad
6.34\times10^{-8},
}
\tag{16}
\]

odd-v:

\[
\boxed{
-3.19\times10^{-10},
\qquad
5.40\times10^{-7}.
}
\tag{17}
\]

This is dramatically different from the \(N=96\) tiny Schur levels reported in v13.801.

The change is numerical cutoff flow, not yet an exact-operator conclusion.

---

## 10. Static source-energy scalar [N]

Using the frozen midpoint \(6\times6\) systems gives nominal source energies

\[
\boxed{
E_e^{\rm nom}
\approx
1.1936890484\times10^{13},
}
\tag{18}
\]

\[
\boxed{
E_o^{\rm nom}
\approx
1.3863419915\times10^{12}.
}
\tag{19}
\]

Hence

\[
\boxed{
\frac{E_o^{\rm nom}}{E_e^{\rm nom}}
\approx
0.1161392905,
}
\tag{20}
\]

and

\[
\boxed{
\kappa_{\rm energy}^{\rm nom}
=
\frac{E_e^{\rm nom}-E_o^{\rm nom}}
{E_e^{\rm nom}+E_o^{\rm nom}}
\approx
0.79189104535.
}
\tag{21}
\]

This is a numerical frozen-carrier value only.

---

## 11. Independent phase reconstruction [N]

Using v13.985, reconstruct the two parity coefficient vectors from the same static solves and evaluate

\[
F(t)=E(t)+iO(t).
\]

The two real characteristic carriers are

\[
R(t)=tE(t)+O(t),
\]

\[
I(t)=tO(t)-E(t).
\]

A direct independent real-axis scan through

\[
T=100
\]

finds the first non-common roots approximately

\[
I(t)=0:
\quad
1.31893135,\ 
4.27059604,\ 
8.88585636,\ldots
\]

and

\[
R(t)=0:
\quad
1.59224590,\ 
4.74579046,\ 
14.13472514,\ldots
\]

After this low-height restructuring, both characteristics continue to show the familiar near-common Xi-like root locations around

\[
14.13472514,\ 
21.02203964,\ 
25.01085758,\ldots
\]

but the sign phase has already accumulated a large negative contribution below the first Xi zero.

Using the exact phase weights of v13.985 gives

\[
\boxed{
\kappa_{\rm phase}^{\rm nom}(100)
\approx
0.79187932504.
}
\tag{22}
\]

The universal phase tail is

\[
\boxed{
\frac1{1+100^2}
\approx
9.9990\times10^{-5}.
}
\tag{23}
\]

Therefore the frozen numerical phase observable lies in the nominal tail band

\[
\boxed{
0.79177934
\lesssim
\kappa_{\rm phase}^{\rm nom}
\lesssim
0.79197932,
}
\tag{24}
\]

before any exact-operator model error is added.

The static energy value (21) lies inside this phase-tail band.

Thus two independent scalar representations agree.

---

## 12. Interpretation of the cutoff flow [N/I]

v13.801 reported

\[
\kappa_{0,96}
\approx
0.9999287562.
\]

The new high-cutoff frozen-carrier model gives instead

\[
\kappa^{\rm nom}
\approx
0.7919.
\]

The energy and phase routes agree independently, so the shift is not explained by a Fourier-sign convention error.

The correct conclusion is:

\[
\boxed{
\textbf{the old near-one }N=96\textbf{ scalar was strongly pre-asymptotic in the current cutoff model.}
}
\]

This is not yet a theorem about the exact \(a=1\) operator because:

- the frozen numerical \(P_4\) differs from exact \(P_4\);
- the KKT solves have not yet been propagated through the infinite remote tail;
- the nominal \(6\times6\) matrix is highly ill-conditioned.

---

## 13. Correct next proof gate [O]

The immediate certification target is now sharply numerical.

For each of the six KKT solves:

1. certify the full transformed residual
   \[
   \|e\|=\|B_T^{-1/2}r\|;
   \]
2. record
   \[
   \|\lambda\|,\quad
   \|\widehat y\|,\quad
   \eta;
   \]
3. apply (10);
4. propagate the resulting exact-Q error to
   \[
   H_C,\quad f_6,\quad F(t);
   \]
5. use the adaptive sign-box theorem of v13.985.

Only after those steps may an exact interval for

\[
\kappa_{a=1}^{\Xi}
\]

be promoted.

---

## 14. Result

The frozen-carrier KKT solves admit the exact comparison

\[
\boxed{
\|y-\widehat y\|
\le
10
\left(
\|e\|
+
\varepsilon_P\|\lambda\|
\right)
+
\varepsilon_P\|\widehat y\|
+
\eta.
}
\]

Independently, the new high-cutoff numerical model gives mutually consistent energy and phase scalars near

\[
\boxed{
0.7919.
}
\]

This is a major cutoff-flow diagnostic, but **not yet the certified exact finite-a scalar**.
