# Cone Derivation Ledger v14.171 — Uniform Infinite Full-Q Coercivity and 256k Gate

**Date:** 2026-10-08 UTC / EDT  
**Track:** Lane A / infinite-tail closure  
**Status:** [D] a uniform cross-block bound extends the audited frozen-plane full-Q coercivity bridge to every R>=8000 and the infinite closed form; [D] public constants checked with exact rational arithmetic. Independent audit requested before theorem-grade reuse. Actual 64k→128k finite outward gate independently audited; 128k→256k outward jobs launched by this commit. **Infinite capacity remainder remains open.**  
**Parents:** v14.025, v14.034/v14.036, v14.044/v14.071, v14.155/v14.158/v14.161, v14.168–v14.170.  
**Collision check:** Live HEAD `0714df5acac548bea29942a2e44287d5164f18cd`; latest relevant Sandbox v14.169 and External Audit Round 200 v14.170 read; ledger max v14.170; v14.171 and its payload namespace free. Expected-HEAD non-forced publication.

## 1. Audited finite gate and scope

Sandbox v14.169 and External Audit v14.170 independently recovered all four full-vector integer snapshots from run 37791856005, reproduced the source certificates and paired interval byte for byte, and checked all twenty assembly/residual caps and four trace caps. The actual source-faithful 64k→128k finite increment gate is closed. The frozen historical `overall_certificate_ready:false` fields remain untouched; these audits do not assert an infinite-tail theorem.

The v14.155 full-Q bridge was limited to R<=256000 by its rectangular harmonic cross-bound. The following proof replaces that cutoff-dependent bound with a uniform Hilbert-matrix bound. It uses the same exact represented P, same Q8 base, and same protected-positive partial-Schur comparison already independently audited in v14.158/v14.161.

## 2. Hilbert cross-block bound, including the infinite shell

Let H(r,j)=1/(r+j+1), r,j>=0, and w_j=(j+1/2)^(-1/2). For a=r+1/2 set f_a(t)=t^(-1/2)/(a+t). Direct differentiation gives

\[
f_a''(t)=\frac{3a^2+10at+15t^2}{4t^{5/2}(a+t)^3}>0.
\]

Midpoint convexity on each interval [j,j+1] implies

\[
\sum_{j\ge0}\frac{w_j}{r+j+1}
\le\int_0^\infty\frac{dt}{\sqrt t(a+t)}
=\frac\pi{\sqrt a}=\pi w_r.
\]

The first interval has an integrable endpoint singularity; midpoint Jensen follows by truncation, or directly by symmetry around 1/2. The integral follows from t=a s^2. Symmetry supplies the same column inequality. For finite vectors, weighted Cauchy–Schwarz gives

\[
\sum_r|(Hx)_r|^2
\le\sum_r\left(\sum_jH_{rj}w_j\right)
                   \left(\sum_jH_{rj}|x_j|^2/w_j\right)
\le\pi^2\sum_j|x_j|^2.
\]

Monotone truncation extends this to a bounded operator on ell2; no assumption that the weights themselves are in ell2 is used. Thus ||H||<=pi, also for every rectangular compression.

The old 8k front has 4000 modes in each parity. Write its reversed index r=3999-i and the shell index j>=0. The same-parity gap is exactly |m-n|=2(r+j+1). The global source majorant |z_n|<=10 (finite front v14.034 plus all n>=8000 v14.025) bounds the physical displacement kernel by

\[
\left|\frac2\pi\frac{z_n m-nz_m}{n^2-m^2}\right|
\le\frac{20}{\pi|n-m|}
=\frac{10}{\pi(r+j+1)}.
\]

Entrywise domination followed by the Hilbert norm bound yields ||B_disp||<=10 for a finite or infinite shell. The established global pole-vector cap and |alpha|=2 give

\[
\|B_{pole}\|<4\cosh^2(1/2)<256/49,
\quad \cosh(1/2)<1+1/8+\frac{1/384}{1-1/120}<8/7.
\]

Orthogonal restriction of the finite front to Q8 cannot increase either norm. Consequently

\[
\boxed{\|B\|<10+256/49=746/49<16}
\]

uniformly over all R>=8000 and the infinite shell.

## 3. The same partial-Schur comparison works on the closed form

The exact frozen complement splits as Q8 plus the coordinate shell since P vanishes above 4000. The audited base is C8>=delta_p I, with delta_e=7.79e-6 and delta_o=3.26e-5. In the finite-front elimination of the infinite closed quadratic form, the bounded cross block just proved makes all finite-dimensional inverse/shear maps bounded. The v14.034/v14.036 positive full front supplies the positive protected Schur block S8. The exact nested remote certificate v14.044/v14.071 gives S_8,infinity>=I. Hence, as a quadratic-form identity on the shell domain,

\[
H_Q=D-B^*C_8^{-1}B
=S_{8,\infty}+E^*S_8^{-1}E\succeq I.
\]

For finite R the same identity holds with the corresponding principal compressions. This explicitly uses protected positivity; it does not identify the full-Q operator with the remote operator.

Set L=C8^-1 B. Completing the square and bounding the inverse shear gives

\[
\langle C(x,y),(x,y)\rangle
\ge\delta_p(\|x+Ly\|^2+\|y\|^2)
\ge\frac{\delta_p}{(1+16/\delta_p)^2}(\|x\|^2+\|y\|^2).
\]

This holds on the infinite form domain and extends by closedness. The exact rational constants strictly exceed

\[
\boxed{\gamma_{Q,e}=1.84\times10^{-18},\qquad
       \gamma_{Q,o}=1.35\times10^{-16}}
\qquad (R\ge8000\text{ and }R=\infty).
\]

These improve the old coarse floors and extend their scope to infinity. They are deliberately smaller than one.

Reproducer: `research-notes/suzuki_infinite_fullq_coercivity_bridge.py`. Frozen output: `payloads/infinite_fullq_bridge_v14_171/infinite_fullq_bridge.json`. Integer/Fraction checks verify the positive derivative coefficients, pole/cross arithmetic, downward floor rounding, and three independent exact finite block examples. The infinite Hilbert/form proof is the analytic argument above, not a sampled numerical test. Re-running the producer against the frozen output gives byte-identical JSON.

## 4. Next actual finite gate and remaining infinite object

The new `suzuki-normalized-tail-256k.yml` computes both 256k endpoints using the unchanged corrected-64k normalizers, paired source frontier 32000, exact integer point action, and existing outward full-vector replay. Only the producer CLI ceiling is extended from 128000 to the already certified scalar/floor range 256000; no numerical algorithm, source cap, normalizer, or old witness is changed. Certificates still use the previously audited v14.155 floors, pending review of this new uniform proof. Each full snapshot is independently replayed with `--require-targets`, and the pair consumer compares against the independently audited frozen 128k endpoints. Its exact finite interval must meet the same 9e-10 budget; failure remains a reported obstruction. It is not a geometric tail extrapolation.

The remaining infinite quantity is the v14.114/v14.117 correlated physical correction

\[
Q_\infty-Q_R=(\lambda_e-\lambda_o)
-C_S(\lambda_o K_{e,R}+\lambda_e K_{o,R}+\lambda_e\lambda_o),
\quad\lambda_p=\langle\rho_p,S_{p,R}^{-1}\rho_p\rangle\ge0.
\]

The valid K10 far-residual expansion must use a frozen finite solution and start beyond twice its support; the intervening octave must retain its exact correlation. Raw parity residual-energy differences are not inverse-weighted capacity differences. Neither the improved full-Q floor nor a successful finite 256k interval alone closes this quantity. Historical fast-solver capacity midpoints are not substituted for the newly audited actual normalized endpoints.

HANDOFF-ACK
from: v14.168
target: lane-a
status: closed
result: v14.169 and v14.170 independently replayed all actual full-vector certificates and the exact finite paired interval; the requested actual 64k→128k audit gate is satisfied and preserved with its finite-only scope.

HANDOFF
target: sandbox
type: audit
parent: v14.171
status: open
action: Independently verify the uniform Hilbert cross-block proof, its exact physical-kernel indexing, the infinite closed-form partial-Schur comparison, and both public full-Q floors, returning any missing hypothesis before downstream infinite theorem use.
deliverable: theorem-or-obstruction
constraints: Use the already-audited exact represented P and Q8/protected-positive inputs; check the midpoint-convexity Schur proof rather than a finite numerical Hilbert norm; preserve the separation between uniform coercivity and the still-open correlated capacity remainder; do not rewrite old lane results; check live HEAD, latest audit, and numbering before writes.

External Audit is invited to verify this explicit bridge under its standing update-watch scope. Lane A retains the actual 256k finite-certificate and source-faithful infinite-remainder work.
