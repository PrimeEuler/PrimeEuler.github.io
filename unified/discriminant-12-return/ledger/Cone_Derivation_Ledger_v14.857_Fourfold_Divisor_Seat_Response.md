# Cone Derivation Ledger v14.857 — Fourfold divisor anomaly and central-seat response

Date 2026-10-25. Gravity arithmetic lane. Parents v13.177, v14.767 and v14.856. Research note research-notes/Divisor_Fourfold_Anomaly_Central_Seat_Response.md commit bd14557b39fafb4b26bf18700f4e021e9ebc7c8f. Live prewrite HEAD bd14557b39fafb4b26bf18700f4e021e9ebc7c8f. Additive only, Suzuki/far-tail untouched.

## Finite-cutoff anomaly [D]
The Paper A identity \(A(n)=T(n)-D(n)\) implies \(T-A+D=2D\). For common unscaled product cutoff n, EM unit-grid contacts number D(n); proposed half-grid gravitational contacts number D(4n). Define
\[
\Delta_4(n)=D(4n)-4D(n)=4n\log4+O(\sqrt n).
\]
The ratio of total count to naïve fourfold count is
\[
\mathcal A(n)=\frac{D(4n)}{4D(n)}-1
=\frac{\Delta_4(n)}{4D(n)}
\sim\frac{\log4}{\log n}\to0.
\]
Exact examples (n,D(n),D(4n),delta): (12,35,198,58); (25,87,482,134); (100,482,2468,540); (1000,7069,33805,5529). Thus the absolute divisor contact excess grows O(n), while its *relative* proportion vanishes slowly. The arithmetic difference is not merely the leading dilation factor, but has no automatically physical significance.

## Conditional contact-weighted potential [I/D]
Take central-seat normalized displacement ξ=δ/u and AM–GM shape \(f(ξ)=1-\sqrt{1-ξ²}\), f''(0)=1. A separately POSTULATED equal-contact energy \(E_{u,n}(δ)=ε D(\lfloor n/u²\rfloor)f(δ/u)\) yields \(k_{u,n}=εD(\lfloor n/u²\rfloor)/u²\) and k_{1/2,n}/k_{1,n}=4D(4n)/D(n) in the same δ coordinate. In ξ coordinates the ratio is D(4n)/D(n). This toy model assumes identical energy ε per contact and a shared physical product cutoff; neither assumption comes from the divisor count or geometric parabola alone. A per-contact normalized total energy \(E_*=const\) removes the contact-count effect entirely.

## Critical physical boundary [O]
A causal contact-weighted action, source normalization, and physical calibration must determine ε, cutoff, and displacement ruler before claiming energy/stiffness or G. Suzuki/Weil trace carrier is not the divisor staircase by v13.770. No physical EM/G hierarchy derived.

Flags: fourfold_divisor_anomaly=EXACT; delta4_leading=4n_log4; relative_anomaly_vanishes=TRUE; contact_stiffness=CONDITIONAL; Newton_G_derived=FALSE; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: gravity-arithmetic-contact-response-audit
parent: v14.857
status: open
action: Independently verify D(4n)-4D(n) asymptotic and all numeric examples, scale factors in fixed-delta versus fixed-xi seat stiffness, and action-dependence of equal-contact weights. Do not modify Suzuki/far-tail.
deliverable: scoped audit verdict.
