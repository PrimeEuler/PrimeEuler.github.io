# Cone Derivation Ledger v13.820 — Adversarial \(\rho=0.02\) Cap Audit on Frozen Endpoint Payloads

Date: 2026-09-26.

Lane: A.

Status: [A] full source-thread adversarial audit completed on the unchanged v13.818 frozen payloads; [P] every finite-buffer, coupling, solve-residual, reference-defect, tail-floor, remote-Gram, far-tail, and terminal-margin cap passes; [H] audit caps deliberately widened to remove brittle sub-percent headroom; [G] no \(\rho=0.02\) endpoint theorem promoted in this entry.

Parents: v13.818–819.

Research artifact:

- research-notes/suzuki_endpoint_M3999_rho002_adversarial_audit.py
  - initial commit 0e616400544e11c6ed77a1f1b8a1f73472ab94b2
  - hardening commit 78281caa929b2bc75d374c1978e4245c897f4e60

No GitHub workflow/status run is attached.

## 0. Audit discipline and scope

External Audit Round 106, v13.819, directly executed and confirmed v13.816–818 and explicitly cautioned that the \(\rho=0.02\) scale has materially tighter reference gaps than \(\rho=0.10\).

The present source-thread audit therefore treats every frozen object and every numerical cap as untrusted until independently replayed.

The v13.818 frozen payloads are consumed unchanged. No eigenspace or Cholesky factor is regenerated.

The audit covers, in both parity sectors:

1. minus-endpoint four-negative finite graph space;
2. minus-endpoint six-positive finite/remote-corrected space;
3. plus-endpoint standard ten-coordinate finite/remote-corrected core;
4. all four structured high buffers;
5. corrected odd-v negative-pole conditioning;
6. all frozen couplings;
7. long-double solve residual envelopes;
8. frozen reference defects;
9. graph-form versus Schur-form consistency;
10. interval remote-tail floors;
11. explicit normalized remote Grams through two million;
12. analytic far-tail envelopes;
13. the \(|Z_n|<8\) far-generator cap;
14. the crude common remote-cross cap \(20\);
15. residual-operator perturbation caps;
16. final terminal positivity margins.

## 1. Frozen payload immutability [PASS]

The audit invokes the v13.818 fail-closed hash/rank verifiers before any matrix calculation.

The hashes reproduce exactly:

minus even-v:
\[
\texttt{f42f62b50fbd8ebd8e40a692450915ed4f6b4bcb9b5a2822f55f103c6f4bb5b3},
\]

minus odd-v:
\[
\texttt{550fc794249e79ebb943ac1771542f7c2940827bfe8dfe71c84acc9d477fed9f},
\]

plus even-v:
\[
\texttt{d2bb5e790023af852e349e001876369e5d9fd43a56a85f7fb3edc687d7d3ef5c},
\]

plus odd-v:
\[
\texttt{7eb101a7138b27a92412c9f381a12d53aacd70af437d86ed478f4dc44a86f8df}.
\]

The exact rational first minors remain nonzero:

\[
\det Q_{{\rm neg},e}[1:4]
\approx4.229675411445356\times10^{-4},
\]

\[
\det Q_{{\rm pos},e}[1:6]
\approx8.54925792559225\times10^{-10},
\]

\[
\det Q_{{\rm neg},o}[1:4]
\approx9.18745847606495\times10^{-2},
\]

\[
\det Q_{{\rm pos},o}[1:6]
\approx-3.807883816357752\times10^{-8}.
\]

The plus Cholesky factors retain exact nonzero triangular determinants.

## 2. Structured buffer audit [PASS]

The outward pole-free factorization residuals are

\[
5.9329795122\times10^{-11}
\quad\text{minus even-v},
\]

\[
5.9341713356\times10^{-11}
\quad\text{minus odd-v},
\]

\[
6.1670137696\times10^{-11}
\quad\text{plus even-v},
\]

\[
6.1679186418\times10^{-11}
\quad\text{plus odd-v}.
\]

The hardened caps are

\[
6.5\times10^{-11}
\]
for both minus buffers and
\[
6.8\times10^{-11}
\]
for both plus buffers.

Thus factorization-residual headroom is approximately \(9.5\%\)–\(10.3\%\).

The resulting nominal full-buffer floors are

\[
\boxed{
\mu^-_e>0.00657076091723,
}
\]

\[
\boxed{
\mu^-_o>0.00514554131059,
}
\]

\[
\boxed{
\mu^+_e>0.00988743246265,
}
\]

\[
\boxed{
\mu^+_o>0.00769536069944.
}
\]

After the common
\[
\epsilon_F=2.1\times10^{-13}
\]
exact-vs-nominal charge, all remain positive with essentially unchanged displayed values.

For corrected odd-v the independently recomputed negative-pole denominators are

\[
\boxed{
0.989143722012074
}
\]
at the minus endpoint and

\[
\boxed{
0.989893805932662
}
\]
at the plus endpoint.

## 3. Finite coupling / residual / reference cap audit [PASS]

The hardened cap table is:

| frozen restriction | actual \(\|F_{FC}Q\|_F\) | cap | actual solve residual | cap | actual reference defect | cap |
|---|---:|---:|---:|---:|---:|---:|
| minus-neg even | 0.195317135 | 0.21 | \(8.565\times10^{-17}\) | \(1.00\times10^{-16}\) | \(9.993\times10^{-17}\) | \(1.20\times10^{-16}\) |
| minus-neg odd | 0.250024705 | 0.27 | \(1.807\times10^{-16}\) | \(2.10\times10^{-16}\) | \(2.373\times10^{-16}\) | \(2.80\times10^{-16}\) |
| minus-pos even | 1.032139616 | 1.08 | \(1.308\times10^{-15}\) | \(1.45\times10^{-15}\) | \(1.055\times10^{-15}\) | \(1.20\times10^{-15}\) |
| minus-pos odd | 0.766704953 | 0.81 | \(1.115\times10^{-15}\) | \(1.25\times10^{-15}\) | \(9.007\times10^{-16}\) | \(1.05\times10^{-15}\) |
| plus even | 1.059241577 | 1.11 | \(1.709\times10^{-15}\) | \(1.90\times10^{-15}\) | \(9.794\times10^{-16}\) | \(1.15\times10^{-15}\) |
| plus odd | 0.805671599 | 0.85 | \(1.285\times10^{-15}\) | \(1.45\times10^{-15}\) | \(6.749\times10^{-16}\) | \(8.00\times10^{-16}\) |

The cap headrooms are therefore:

- coupling: \(4.64\%\)–\(7.99\%\);
- solve residual: \(10.83\%\)–\(16.76\%\);
- reference defect: \(13.80\%\)–\(20.08\%\).

No sub-percent finite cap remains.

## 4. Finite restricted-form margins [PASS]

Using the widened audit caps in the fixed-\(Q\) resolvent perturbation formulas gives:

### minus four-negative spaces

Even-v:
\[
\boxed{
-Q_{{\rm neg},e}^{T}S^-_{\rm exact}Q_{{\rm neg},e}
>
0.00266179948027\,I.
}
\]

Normalized:
\[
>0.99999991429\,I.
\]

Odd-v:
\[
\boxed{
-Q_{{\rm neg},o}^{T}S^-_{\rm exact}Q_{{\rm neg},o}
>
0.00398570593918\,I,
}
\]

normalized:
\[
>0.99999984934\,I.
\]

### minus six-positive spaces

Even-v finite normalized lower bound:
\[
\boxed{
C^-_{e,6}>0.99999997665\,I.
}
\]

Odd-v:
\[
\boxed{
C^-_{o,6}>0.99999999354\,I.
}
\]

### plus ten-coordinate cores

Even-v:
\[
\boxed{
C^+_{e,10}>0.99999888825\,I.
}
\]

Odd-v:
\[
\boxed{
C^+_{o,10}>0.99999961814\,I.
}
\]

The worst normalized finite loss is therefore only approximately

\[
1.12\times10^{-6}
\]

on the even-v plus endpoint.

## 5. Independent graph-versus-Schur checks [PASS]

The full finite graph form was independently compared with the one-sided Schur expression for every frozen restriction.

Operator-norm discrepancies are:

\[
7.02\times10^{-17}
\quad\text{minus-neg even},
\]

\[
6.60\times10^{-17}
\quad\text{minus-neg odd},
\]

\[
1.29\times10^{-15}
\quad\text{minus-pos even},
\]

\[
3.73\times10^{-16}
\quad\text{minus-pos odd},
\]

\[
1.08\times10^{-15}
\quad\text{plus even},
\]

\[
6.95\times10^{-16}
\quad\text{plus odd}.
\]

All are below conservative residual-based envelopes exceeding \(5\times10^{-15}\).

No sign/transposition inconsistency is detected.

## 6. Outward interval remote-tail floors [PASS]

Using 80-digit interval arithmetic, the exact remote starts \(4001/4002\), the full \(\|B_{\rm prime}\|<2.05\) certificate, and the corrected odd-v pole allowance:

### minus endpoint

\[
\gamma^-_e(4001)
\in
[
3.18003114023348665367\ldots,
3.18003114023348668774\ldots
],
\]

so safely

\[
\boxed{
\gamma^-_e(4001)>3.18003114023348.
}
\]

\[
\gamma^-_o(4002)
\in
[
3.18016610573875293915\ldots,
3.18016610573875297320\ldots
],
\]

so

\[
\boxed{
\gamma^-_o(4002)>3.18016610573875.
}
\]

### plus endpoint

\[
\boxed{
\gamma^+_e(4001)>3.39351949707118,
}
\]

\[
\boxed{
\gamma^+_o(4002)>3.39366445882790.
}
\]

The corrected odd pole cost is included at both signs.

## 7. Far-generator and remote-cross caps [PASS]

For \(n\ge2,000,001\), the endpoint-shifted generator obeys an 80-digit interval upper bound

\[
|Z_n^{(\pm,0.02)}|
<
7.454682
<
8.
\]

Thus the common far-generator cap

\[
\boxed{|Z_n|<8}
\]

has substantial room.

The crude common remote-cross cap is re-derived inside the hardened audit script rather than merely assumed.

Using the worst \(1.02\) Hilbert coefficient, full prime bound, global cusp/arch majorants, and rank-one pole bounds gives component totals

\[
16.11436
\quad\text{even-v},
\]

\[
10.78103
\quad\text{odd-v}.
\]

Therefore

\[
\boxed{\|F_{RF}\|<20}
\]

is independently revalidated.

## 8. Explicit remote-Gram audit [PASS]

Using the frozen preconditioners unchanged, direct residual accumulation through \(16001/16000\), then the eight-level inverse-power expansion through \(2,000,000\), gives:

| endpoint/subspace | actual \(\lambda_{\max}(H_{2M})\) | hardened cap | headroom |
|---|---:|---:|---:|
| minus-pos even | 0.0459979411 | 0.0480 | \(4.35\%\) |
| minus-pos odd | 0.0083016321 | 0.0088 | \(6.00\%\) |
| plus even | 0.0414692774 | 0.0435 | \(4.90\%\) |
| plus odd | 0.0329410692 | 0.0345 | \(4.73\%\) |

The corresponding analytic far envelopes are

\[
9.85529\times10^{-5},
\quad
1.77110\times10^{-5},
\quad
8.88290\times10^{-5},
\quad
7.03573\times10^{-5},
\]

against widened caps

\[
1.20\times10^{-4},
\quad
2.20\times10^{-5},
\quad
1.10\times10^{-4},
\quad
8.50\times10^{-5}.
\]

Far-envelope headroom is approximately \(20.8\%\)–\(24.2\%\).

## 9. Frozen-coordinate conditioning caps [PASS]

Observed normalized preconditioner/dressed-plane norms are:

minus-pos even:
\[
\|L^{-1}\|_2=2.01629,\qquad \|W L^{-T}\|_2=2.71788;
\]

minus-pos odd:
\[
1.10676,\qquad1.18509;
\]

plus even:
\[
20.31346,\qquad20.31618;
\]

plus odd:
\[
12.09829,\qquad12.10233.
\]

The widened caps are respectively

\[
(2.05,2.80),\quad
(1.13,1.23),\quad
(20.8,20.8),\quad
(12.4,12.4).
\]

All pass with explicit runtime checks.

## 10. Replay-arithmetic reserve [PASS]

As an independent audit-only diagnostic, the normalized Gram was accumulated twice from the same residual rows:

1. ordinary binary64 Gram accumulation;
2. 64-bit-significand long-double Gram accumulation.

The operator-norm differences are below

\[
1.42\times10^{-17},
\quad
1.92\times10^{-18},
\quad
4.30\times10^{-17},
\quad
7.45\times10^{-17}
\]

for minus-even, minus-odd, plus-even, plus-odd respectively.

Thus the standing replay-arithmetic reserve

\[
10^{-8}
\]

is extremely conservative relative to observed accumulation drift.

The exact-vs-nominal source/operator budget
\[
\epsilon_F=2.1\times10^{-13}
\]
remains the inherited validated v13.357 budget plus the already-audited endpoint reserve; it is not re-proved from first principles here.

## 11. Residual-operator perturbation caps [PASS]

Using the widened finite caps and frozen-coordinate conditioning gives derived normalized residual-operator uncertainties

\[
2.27\times10^{-7}
\quad\text{minus-pos even},
\]

\[
1.56\times10^{-7}
\quad\text{minus-pos odd},
\]

\[
1.01\times10^{-6}
\quad\text{plus even},
\]

\[
7.64\times10^{-7}
\quad\text{plus odd}.
\]

The fail-closed caps are

\[
5\times10^{-7},
\quad
4\times10^{-7},
\quad
2\times10^{-6},
\quad
1.5\times10^{-6}.
\]

All have approximately factor-two or better slack.

## 12. Final audited terminal budgets [PASS]

After combining:

- hardened finite normalized lower bounds;
- outward interval tail floors;
- widened explicit Gram caps;
- widened far envelopes;
- residual-operator perturbation caps;

the final audit ceilings/margins are:

### minus six-positive even-v

\[
H^-_e<0.048120225001,
\]

\[
\boxed{
\gamma^-_e C^-_{e,6}-H^-_e
>
3.13191084098.
}
\]

Normalized post-tail lower bound:
\[
\boxed{
>0.9848679786.
}
\]

### minus six-positive odd-v

\[
H^-_o<0.008822080001,
\]

\[
\boxed{
\gamma^-_o C^-_{o,6}-H^-_o
>
3.17134400520.
}
\]

Normalized:
\[
\boxed{
>0.9972258994.
}
\]

### plus even-v

\[
H^+_e<0.043610860004,
\]

\[
\boxed{
\gamma^+_e C^+_{e,10}-H^+_e
>
3.34990486435.
}
\]

Normalized:
\[
\boxed{
>0.9871476699.
}
\]

### plus odd-v

\[
H^+_o<0.034585585003,
\]

\[
\boxed{
\gamma^+_o C^+_{o,10}-H^+_o
>
3.35907757792.
}
\]

Normalized:
\[
\boxed{
>0.9898083969.
}
\]

These are audit targets with deliberately widened caps, not midpoint best values.

## 13. Audit verdict

No frozen hash, exact rank, buffer-conditioning, corrected-pole, coupling, solve-residual, reference-defect, graph-form, tail-floor, explicit-Gram, far-tail, conditioning, or residual-operator cap fails.

Crucially, the cap program no longer relies on sub-percent headroom.

The smallest theorem-scale reference remains the even-v plus core,

\[
\lambda_{\min}(L_0L_0^T)
=
0.002423439244832\ldots,
\]

but its hardened finite loss is only approximately

\[
2.69\times10^{-9},
\]

and its remote-corrected normalized audit lower bound remains above

\[
0.9871.
\]

Therefore the frozen v13.818 data are suitable for a subsequent \(\rho=0.02\) endpoint certificate.

## Guardrail

This entry is deliberately an audit/hardening checkpoint.

It does not itself promote

\[
\operatorname{ind}_{-}(F^-_{0.02,\rm tail})=4
\]

or

\[
\operatorname{ind}_{-}(F^+_{0.02,\rm tail})=0.
\]

A subsequent certificate entry should consume these exact frozen payloads and the audited widened caps without regeneration.

## Result

\[
\boxed{
\textbf{PASS: every adversarial }\rho=0.02\textbf{ finite-side, tail-floor, and remote-Gram cap closes on the unchanged frozen payloads with non-brittle headroom.}
}
