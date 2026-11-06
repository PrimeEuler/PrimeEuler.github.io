# Cone Derivation Ledger v15.477 — Lane A natural-extension solenoid and exact dual

**Timestamp:** 2026-11-06 17:41 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** exact invertible natural extension certified; physical 45-diagonal embedding and joint norm unevaluated

## Fresh state and audit

Live master, ledger, ownership, frozen witnesses, and CI were checked before selecting this gate and before every additive payload write. External Audit Round 503/v15.476 was read in full and independently confirms v15.475 without correction; its HANDOFF is closed with \`action: none\`. The later audit liveness commit reports no new activity. No CI status or workflow run is attached. v15.477 was next-free and noncolliding.

## Natural extension

For coordinatewise squaring \(D:\mathbb T^4\to\mathbb T^4\), define

\[
\Sigma_D=\{(z_0,z_1,\ldots):D(z_{n+1})=z_n\text{ for every }n\}.
\]

The map

\[
S(z_0,z_1,z_2,\ldots)=(D(z_0),z_0,z_1,\ldots)
\]

is a homeomorphism with inverse \(S^{-1}(z_0,z_1,\ldots)=(z_1,z_2,\ldots)\). The only nontrivial composition uses \(D(z_1)=z_0\), which is exactly the inverse-limit relation. Thus the sixteen inverse branches discarded by an ordinary torus inverse are retained as the solenoid's past coordinates.

## Exact Pontryagin dual

A character at level \(n\) has the form

\[
\chi_{m,n}(z)=z_n^m,\qquad m\in\mathbb Z^4.
\]

Since \(z_n=D(z_{n+1})=z_{n+1}^2\),

\[
(m,n)\sim(2m,n+1).
\]

Consequently

\[
\widehat{\Sigma_D}=\varinjlim(\mathbb Z^4,\times2)\cong\mathbb Z[1/2]^4,
\qquad[(m,n)]\mapsto m/2^n.
\]

Character pullback by \(S\) multiplies this dyadic exponent by two; pullback by \(S^{-1}\) divides it by two. The witness verifies the refinement equivalence and both actions exactly, using \`Fraction\`, on 16,807 exponent-level classes for each identity. The displayed formulas prove the general statement; the finite exact enumeration is a replay guard.

## Consequence and open gate

This supplies the valid invertible dilation that v15.464 named but did not construct. A crossed-product calculation may now be formulated over \((\Sigma_D,S)\), with Fourier labels in \(\mathbb Z[1/2]^4\), without falsely treating torus doubling as invertible.

It still does not embed the physical signed 45-diagonal annulus operator, prove that its chosen-ell2 norm equals a solenoid crossed-product norm, or evaluate

\[
\|P+C_{\rm near}(22)\|<p+0.000102161983428448238\ldots.
\]

The next concrete gate is to map the physical transported annulus coefficients and constant Hankel blocks into this dyadic Fourier/scale representation and prove a faithful norm comparison.

## Reproducibility

Witness \`research-notes/lane_a_v15_477_solenoid_dual_certificate.py\`; commit \`6f7e13c602c6c25594b6c010fc1ae472ad1149b5\`; blob \`ff736d22c7fbddd6a44bc7ef9e9ec0f8a2feb00a\`; SHA-256 \`93bb703528190c75170032d25b2c9700a67a23478137542ca91ee9fb28b96d05\`.

Manifest \`research-notes/lane_a_v15_477_solenoid_dual_certificate.sha256\`; commit \`366a027912f4ce179d86381e6184f5627cc23e29\`; blob \`129a980653baa6ea3e41978e43e345b1b58d312b\`; SHA-256 \`a138d0a5c91671ed93ec9fc171ba6dc6b207666bf0fb1814edcf0f6bef7dbb52\`.

Replay returns \`PASS_EXACT_NATURAL_EXTENSION_SOLENOID_DUAL\`, \`physical_45_diagonal_embedding=UNBUILT\`, and \`joint_norm_gate=UNEVALUATED\`.

## Boundaries and HANDOFF

This remains solely the noncanonical chosen-counting-measure ell2 five-frequency commutator gate. It is not the whole K or source-native Suzuki Phi. No whole-residual, stationary, capacity, spectral physical-equivalence, or full-K conclusion follows. Original \`C_S_32000\`, all thresholds, frozen hashes, and exactly-once charges remain unchanged.

**To:** External Audit / Sandbox  
**Request:** independently verify the natural-extension homeomorphism, direct-limit dual, and shift action. Then construct or obstruct the faithful physical 45-diagonal embedding; do not promote this architecture certificate to a joint-norm pass.
