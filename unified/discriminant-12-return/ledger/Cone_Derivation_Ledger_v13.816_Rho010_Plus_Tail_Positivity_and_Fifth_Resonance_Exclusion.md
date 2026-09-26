# Cone Derivation Ledger v13.816 — Exact \(\rho=0.10\) Plus-Tail Positivity and Sectorwise Four-Resonance Exclusion

Date: 2026-09-25 local / 2026-09-26 UTC.

Lane: A.

Status: [C] \(\rho=0.10\) plus tail endpoint certified strictly positive in both parity sectors; [C] together with audited v13.812–815 minus endpoint, sectorwise endpoint inertia difference equals four; [H] plus certificate self-audited with deliberately widened caps before promotion; [G] theorem remains scoped to the bulk-subtracted parity tails, excluding the separately retained two-mode low core.

Parents: v13.804–815.

Research artifacts:

- research-notes/suzuki_endpoint_M3999_midpoint_effective_core.py
  - commit 5ab4bf1276ce5077b9f8ad8cce9dd9e284d273a1
  - endpoint sign parameterized with default \(s=-1\), leaving all audited minus-endpoint calls unchanged;

- research-notes/suzuki_endpoint_M3999_terminal_remote_gram_certificate.py
  - commit a53c8140aa56c706609c592912eea4cc7a0be0cf
  - analytic far-generator proof now explicitly includes the endpoint shift magnitude \(\rho\pi/2\);

- research-notes/suzuki_endpoint_M3999_plus_frozen_L0.py
  - commit 71225577b1623241c408051e01a0b87b009e35de;

- research-notes/suzuki_endpoint_M3999_plus_terminal_certificate.py
  - commits 38a67af0f13719e7bdf40f2827da2c957c9e1902 and abe6b90eefe65924de3a55580bc71c878a97ebf9.

No GitHub workflow/status run is attached to the plus-endpoint commits. External Audit Round 105 (v13.815) independently confirmed the preceding minus-endpoint chain v13.812–814 before this plus-endpoint work began.

## 1. Endpoint and scope

The plus endpoint is

\[
F^+_{0.10}
=
A+0.10B_{\rm sm},
\qquad
B_{\rm sm}=D_{\log}-H.
\]

The theorem is on the bulk-subtracted parity tails

\[
n=5,7,9,\ldots
\quad\text{(even-v)}
\]

and

\[
n=6,8,10,\ldots
\quad\text{(odd-v)}.
\]

The separately retained first two parity modes are not part of this tail theorem.

## 2. Exact endpoint generator shift

For

\[
F_\rho^{(s)}=A+s\rho B_{\rm sm},
\qquad s=\pm1,
\]

the source-faithful rank-two generator obeys

\[
\boxed{
Z_n^{(s)}
=
Z_n+\frac{s\rho\pi}{2}.
}
\]

The midpoint builder is now parameterized by \(s\), with \(s=-1\) preserved as the default for the already-audited minus certificates.

The plus endpoint uses

\[
\boxed{
Z_n^+
=
Z_n+\frac{0.10\pi}{2}.
}
\]

## 3. Far-generator proof hygiene correction

The v13.812 terminal minus verifier bounded the unshifted source generator when proving the coarse far-tail hypothesis \(|Z_n|<8\).

The actual endpoint generator differs by \(\rho\pi/2\).

Commit a53c8140aa56c706609c592912eea4cc7a0be0cf corrects the proof by using

\[
|Z_n^{(s)}|
\le
2\sum_q\frac{\Lambda(q)}{\sqrt q}
+
\left(
\frac{\pi}{2}+\frac{1}{y}
\right)
+
\frac{4e^{-1}}{n\pi(1-e^{-4})}
+
\frac{\rho\pi}{2}.
\]

At \(n\ge2,000,001\), the corrected interval bound remains below

\[
7.581<8.
\]

Thus the v13.812 conclusion is unchanged, but the committed proof now bounds the generator actually used by the endpoint residual expansion.

## 4. Fresh \(M=3999/4000\) plus midpoint

Use the same ten-mode cores and structured buffers:

even-v:
\[
C_e=\{5,7,\ldots,23\},
\qquad
F_e=\{25,27,\ldots,3999\};
\]

odd-v:
\[
C_o=\{6,8,\ldots,24\},
\qquad
F_o=\{26,28,\ldots,4000\}.
\]

After eliminating the finite high buffers, the ten-dimensional plus effective-core spectra are:

### even-v

\[
\boxed{
\begin{aligned}
0.010744619159242,&\\
0.051150032719724,&\\
0.099919643977803,&\\
0.138415891967599,&\\
0.553916828810520,&\\
1.232564164514229,&\\
1.824390169325218,&\\
2.081945686493961,&\\
2.607341662683209,&\\
2.767100055830946.&
\end{aligned}
}
\]

### odd-v

\[
\boxed{
\begin{aligned}
0.030663376134136,&\\
0.068210275666904,&\\
0.107331145538637,&\\
0.155019779032483,&\\
1.036615236384518,&\\
1.631267112265340,&\\
1.899602547019206,&\\
2.329592638328114,&\\
2.623400629767544,&\\
2.773133461146966.&
\end{aligned}
}
\]

Hence the midpoint plus effective cores are strictly positive in all ten directions.

## 5. Frozen standard-core preconditioners

No eigenspace is frozen.

The core basis is exactly the standard coordinate basis \(I_{10}\).

Only the midpoint Cholesky factors \(L_{0,\pm}\) are frozen as exact IEEE-754 dyadics.

Even-v payload SHA-256:

\[
\boxed{
\texttt{488ed62ca2d6d4ba6eea4bd12bf80c10156a93cff6075fd32d34a6f3b9621742}.
}
\]

Odd-v payload SHA-256:

\[
\boxed{
\texttt{638f8e97a051aa97b17f9c2f147ab49810f1c5166600fef64fd3bca56015140d}.
}
\]

The verifier checks these hashes and all ten positive Cholesky diagonals at runtime.

## 6. Fresh plus-buffer conditioning

The pole-free minimum LDL pivots are

\[
0.861456802259748
\quad\text{(even-v)},
\]

\[
0.980178259102018
\quad\text{(odd-v)}.
\]

The completed structured-factor residual bounds are approximately

\[
6.64\times10^{-11}
\]

in each parity.

Outward inverse-factor bounds give nominal buffer floors

\[
\boxed{
\mu_e^+>0.01911367739829,
}
\]

\[
\boxed{
\mu_o^+>0.01482935415427.
}
\]

The corrected odd negative-pole Sherman-Morrison denominator is

\[
\boxed{
>0.99104819094854.
}
\]

After the common exact-vs-nominal operator budget

\[
\epsilon_F=2.1\times10^{-13},
\]

both exact plus buffers remain safely positive.

## 7. Ten-RHS finite-side audit

The actual frozen standard-core couplings are

\[
\|F_{FC}\|_F
\approx1.07718948017
\quad\text{(even-v)},
\]

\[
\approx0.80488257651
\quad\text{(odd-v)}.
\]

The fail-closed caps are widened to

\[
1.10,\qquad0.82.
\]

The outward ten-RHS residuals are

\[
1.478\times10^{-15}
\quad\text{(even-v)},
\]

\[
1.123\times10^{-15}
\quad\text{(odd-v)},
\]

under widened caps

\[
1.70\times10^{-15},
\qquad
1.30\times10^{-15}.
\]

The outward frozen-reference defects are approximately

\[
6.64\times10^{-16},
\qquad
4.88\times10^{-16},
\]

under caps

\[
8.0\times10^{-16},
\qquad
6.0\times10^{-16}.
\]

The actual preconditioner inverse norms are

\[
\|L_{0,e}^{-1}\|_2\approx9.6473<10,
\]

\[
\|L_{0,o}^{-1}\|_2\approx5.7108<6.
\]

The normalized dressed-plane norms are likewise below the same wide caps.

Thus no plus-endpoint theorem constant depends on sub-percent cap headroom.

## 8. Rigorous finite plus-core margins

The fixed-\(I_{10}\) Schur perturbation budgets are bounded by approximately

\[
7.21\times10^{-10}
\quad\text{(even-v)},
\]

\[
6.67\times10^{-10}
\quad\text{(odd-v)}.
\]

Therefore the exact finite plus-core restrictions satisfy the safe normalized bounds

\[
\boxed{
C_e^+>0.9999999279\,I,
}
\]

\[
\boxed{
C_o^+>0.9999999760\,I.
}
\]

The corresponding raw finite lower margins remain above approximately

\[
0.0107446184,
\qquad
0.0306633754.
\]

## 9. Outward plus remote-tail floors

For the plus endpoint,

\[
F^+_{0.10}
=
1.1\,B_{\rm sm}
+
B_{\rm prime}
+
K_{\rm cusp}
+
K_{\rm arch}
+
K_{\rm pole}.
\]

Using the same independently enclosed constants as v13.810 gives

\[
\boxed{
\gamma_e^+(4001)
>
3.82049621074657,
}
\]

\[
\boxed{
\gamma_o^+(4002)
>
3.82066116500621.
}
\]

The odd bound includes the adverse corrected \(-2dd^T\) pole allowance.

Combining with the finite normalized bounds gives

\[
\boxed{
\gamma_e^+C_e^+
>
3.8204959352887932\,I,
}
\]

\[
\boxed{
\gamma_o^+C_o^+
>
3.8206610733103420\,I.
}
\]

## 10. Plus remote residual Grams

Using the standard ten-core dressed graph and the endpoint generator shift \(+\rho\pi/2\), accumulate directly through \(16001/16000\) and by the eight-level inverse-power expansion through two million.

The point normalized Gram maxima are

\[
\boxed{
\lambda_{\max}(H_{e,2M}^{+,\rm point})
\approx
0.0363945641395357,
}
\]

\[
\boxed{
\lambda_{\max}(H_{o,2M}^{+,\rm point})
\approx
0.0190882947321762.
}
\]

The analytic far-tail envelopes are approximately

\[
7.79\times10^{-5}
\quad\text{(even-v)},
\]

\[
4.08\times10^{-5}
\quad\text{(odd-v)}.
\]

After adversarial cap review, the verifier deliberately uses much wider point/far caps:

even-v:
\[
0.0365,\qquad10^{-4};
\]

odd-v:
\[
0.0192,\qquad6\times10^{-5}.
\]

Thus

\[
H_{e,\rm point}^+<0.0366\,I,
\]

\[
H_{o,\rm point}^+<0.01926\,I.
\]

## 11. Residual-operator perturbation

The normalized dressed-plane perturbation estimate, propagated through the same crude remote cross cap \(20\), gives derived total residual-operator uncertainties of approximately

\[
1.35\times10^{-7}
\quad\text{(even-v)},
\]

\[
1.02\times10^{-7}
\quad\text{(odd-v)}.
\]

The plus terminal verifier rounds both all the way up to

\[
\boxed{
\|\Delta Y_\pm^+\|<10^{-6}.
}
\]

Using

\[
\|H_{\rm exact}-H_{\rm point}\|
\le
2\|Y_{\rm point}\|\|\Delta Y\|
+
\|\Delta Y\|^2,
\]

with

\[
\|Y_{e,\rm point}\|<0.192,
\qquad
\|Y_{o,\rm point}\|<0.139,
\]

gives

\[
\boxed{
H_e^+<0.036600384001\,I,
}
\]

\[
\boxed{
H_o^+<0.019260278001\,I.
}
\]

## 12. Terminal plus-endpoint positivity

Even-v:

\[
\boxed{
\gamma_e^+C_e^+-H_e^+
>
3.7838955512877932\,I.
}
\]

Odd-v:

\[
\boxed{
\gamma_o^+C_o^+-H_o^+
>
3.8014007953093420\,I.
}
\]

Equivalently,

\[
\boxed{
C_e^+-(\gamma_e^+)^{-1}H_e^+
>
0.9904199199\,I,
}
\]

\[
\boxed{
C_o^+-(\gamma_o^+)^{-1}H_o^+
>
0.9949588909\,I.
}
\]

Therefore

\[
\boxed{
F^+_{0.10,e,\rm tail}\succ0,
\qquad
F^+_{0.10,o,\rm tail}\succ0.
}
\]

So

\[
\boxed{
\operatorname{ind}_{-}(F^+_{0.10,e,\rm tail})
=
\operatorname{ind}_{-}(F^+_{0.10,o,\rm tail})
=
0,
}
\]

with zero kernel.

## 13. Sectorwise \(\rho=0.10\) resonance count

External Audit Round 105 confirmed

\[
\operatorname{ind}_{-}(F^-_{0.10,\rm tail})=4
\]

with zero kernel in each parity sector.

The present entry certifies

\[
\operatorname{ind}_{-}(F^+_{0.10,\rm tail})=0
\]

with zero kernel in each parity sector.

Therefore, sector by sector,

\[
\boxed{
N_{\rm tail}^{(e)}(0.10)
=
4,
}
\]

\[
\boxed{
N_{\rm tail}^{(o)}(0.10)
=
4.
}
\]

Equivalently, each compact relative parity-tail operator has exactly four generalized eigenvalues

\[
\delta=1+\mu(K)
\]

inside

\[
|\delta|<0.10,
\]

and hence exactly four resonances

\[
\mu(K)
\]

inside

\[
|1+\mu|<0.10.
\]

There is no fifth tail resonance in that window in either parity sector.

This statement is sectorwise; it is not a claim that the direct sum of both parity tails has total multiplicity four.

## 14. Remaining gates

The natural next endpoint pair is

\[
\rho=0.02.
\]

The same M3999 architecture can now be replayed with the exact generator shifts

\[
Z_n\mapsto Z_n\pm0.01\pi.
\]

To prove the tight cluster statement

\[
N_{\rm tail}^{(e)}(0.02)
=
N_{\rm tail}^{(o)}(0.02)
=
4,
\]

both the minus and plus \(\rho=0.02\) endpoints must be certified.

The separate two-mode low-core Feshbach problem remains outside the present tail theorem.

## Result

\[
\boxed{
\textbf{The }\rho=0.10\textbf{ plus tail endpoint is strictly positive in both parity sectors.}
}
\]

Together with the externally audited minus endpoint,

\[
\boxed{
N_{\rm tail}^{(e)}(0.10)
=
N_{\rm tail}^{(o)}(0.10)
=
4,
}
\]

with no endpoint zero mode.

Thus the fifth tail resonance near \(-1\) is rigorously excluded at radius \(0.10\) in each parity sector.
