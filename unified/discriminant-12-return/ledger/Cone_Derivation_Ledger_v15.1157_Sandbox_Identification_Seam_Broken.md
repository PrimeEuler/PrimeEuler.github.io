# Cone Derivation Ledger v15.1157 — Sandbox: the identification seam is broken at weld standard (pair-side hbar-Z charges are not the radial flux)

**Deposit type:** Sandbox exploration, independently checkable.
Item 2 of Jeremy's 2026-11-18 gravity-thread tasking. Standard
fixed in advance by the 2026-10-28 assessment: derived from the
structure at weld standard (v14.904/v14.914, no fitted joint),
not kappaC=1-style matching; weak form only (the strong form
was closed by v15.050). Producer re-executed at staging,
exit 0 (5 checks, all PASS).

The pair side holds not one charge but three, from three
actions: dressed L = cosh(s) p_s in hbar-Z (v14.988), the
Hessian s-shift charge Q_s with CONTINUOUS spectrum
(v14.946/v14.952), and the spinor Noether charge
q_chi = -rho sdot in hbar-Z (v14.990). The flux side
(v14.944) holds a conserved current with amplitude Phi NOT
fixed by conservation (flags: independent factor Noether
charge NOT_DERIVED; amplitude arbitrary). The identification
fails on three exact pieces: (1) the pair charges disagree
with each other by state-dependent factors — from the
Hessian kinetic term p_s = -2 rho^2 sdot against
q_chi = -rho sdot, ratio 1/(2 rho); and the two U(1) momenta
are related through the spinor square root by the flow
factor -2 cosh(s) (dth/ds = -1/(2 cosh s) from
tanh s = cos 2th, verified), constant only at the seat
s = 0 — so at most one candidate could equal the flux, with
a state-varying normalization, which is not a dictionary
constant. (2) A static counterexample: at sdot = 0 both
pair charges vanish while Phi != 0 remains admissible on
the K4 side (v14.944's null current carries arbitrary N) —
no functional identity charge = flux exists. (3) The
identification must cross actions: the action generating
the radial/K4 side is the Hessian action, whose charge is
the unquantized Q_s; the hbar-Z charges live on
pair-mechanical actions with no radial sector, no sphere,
no flux. Crossing needs the pair-metric selection v14.990
files as unforced, plus fixing the flux amplitude v14.944
files as free — two joints; weld standard allows zero.

Verdict: BROKEN at weld standard. The identification
survives only as a postulated dictionary line (Phi := q_chi
or Phi := L) of kappaC=1 type, the form the 2026-10-28
standard excluded in advance; any argument treating the
radial flux as quantized because a pair charge is hbar-Z is
using the postulated form. The charges themselves, the
flux construction, and the weld are untouched. Reopening
condition: a coupled action that dynamically selects the
pair kinetic metric, or a K4-side Noether charge derived
from the factor product with Phi fixed. No selector
claimed; G_derived = false. Lane A files untouched.

**Payload:** `payloads/identification_seam_v15_1157/` — Identification_Seam_Verdict.md `7dea2aabfb8b7f64a4da70ca09098f22d561dcba4c69c3e8017835d7f6632c30`, identification_seam.py `f74413c48c26a568b2929818d49348c1979f52054f7f79862a7a5d3ba27739a3`.
