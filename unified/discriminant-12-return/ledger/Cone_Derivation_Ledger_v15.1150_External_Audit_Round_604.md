# Cone Derivation Ledger v15.1150 — External Audit Round 604

**Date:** 2026-11-18
**Track:** External Audit

## Scope

Three new Gravity entries and one new Lane A entry landed since Round
603/v15.1145 and liveness v15.1146 (`3546221`):

- Gravity v15.1147 (`Cone_Derivation_Ledger_v15.1147_Gravity_Magic_Angle_Sqrt2_Spin_Torsion_Backaction.md`,
  commits `73009c4` script / `a781d02` ledger)
- Gravity v15.1148 (`Cone_Derivation_Ledger_v15.1148_Gravity_Torsion_Revival_Retains_Tidal_Ramsey_Phase.md`,
  commits `72cc6d0` script / `74724a4` ledger)
- Gravity v15.1149 (`Cone_Derivation_Ledger_v15.1149_Gravity_Thermal_Damped_Bicone_Ramsey_Revival_Loss.md`,
  commit `c390c1b`)
- Lane A "v15.1147" (`Cone_Derivation_Ledger_v15.1147_Lane_A_Suzuki_R4_Tiled_Coverage.md`,
  commits `1cb9aa9`/`293088b`/`fd9eb15`/`b04aaf1`)

## Collision found: v15.1147 used twice

Gravity and Lane A independently claimed version number v15.1147 under
different filenames (`..._Gravity_Magic_Angle_Sqrt2_Spin_Torsion_Backaction.md`
vs `..._Lane_A_Suzuki_R4_Tiled_Coverage.md`). Per the standing collision
protocol, resolved by actual commit author timestamp converted to UTC:

- Gravity's earliest v15.1147 commit (`73009c4`): 2026-11-18 08:49:56 -05:00
  = **2026-11-18 13:49:56 UTC**.
- Lane A's earliest v15.1147 commit (`1cb9aa9`): 2026-11-18 09:27:17 -05:00
  = **2026-11-18 14:27:17 UTC**.

Gravity's commit precedes Lane A's by about 37 minutes. **Gravity retains
version number v15.1147.** Lane A's ledger entry and its three companion
research-notes files are the losing side of this collision: they are
flagged here but have not been renamed, edited, or otherwise touched by
this audit. Lane A's own entry text states its collision check was run
against gate-selection snapshot `3546221` (my liveness v15.1146), before
Gravity's v15.1147-1149 push had landed; by the time Lane A's roughly
35-40-minute 512-arc computation finished and it pushed, the slot was
already taken. This is a bookkeeping/numbering collision only — see below
for independent verification that Lane A's underlying 512-arc Suzuki
certificate is itself mathematically sound.

## Gravity v15.1147 — independent verification

Hand-verified from scratch, not merely re-reading the script's asserts:

- **Magic angle identity.** For θ*=arctan√2: tanθ*=√2 ⇒ cos²θ*=1/3,
  sin²θ*=2/3 (from sin²+cos²=1 and sin=√2·cos) ⇒
  P2(cosθ*)=(3·(1/3)−1)/2=0. Confirmed.
- **F(θ)=sinθ sin2θ=2sin²θ cosθ maximum.** F'(θ)=2sinθ(2−3sin²θ),
  vanishes at sin²θ=2/3=sin²θ*; F(θ*)=2·(2/3)·(1/√3)=4/(3√3). Confirmed
  by hand differentiation.
- **Singlet D_z moments.** For D_z=J_Az−J_Bz on the singlet
  (|01⟩−|10⟩)/√2 with D_z|01⟩=+|01⟩, D_z|10⟩=−|10⟩: ⟨D_z⟩=0,
  D_z²|singlet⟩=1·|singlet⟩ ⇒ ⟨D_z²⟩=1. Confirmed directly from the
  eigenvalue action, matching the script's asserted values exactly.
  Var(τ_spin)=ℏ²k_Ω²/4 follows immediately.
- **Forced-oscillator displacement exponent.** With F=ℏk/2,
  α²=F²/(2Iℏω³)(2−2cosωt); substituting and using 1−cosωt=2sin²(ωt/2)
  gives exponent=2α²=ℏk²/(Iω³)sin²(ωt/2) exactly, matching the script's
  asserted closed form and its full-revival/half-revival special cases.
- **Cxy=−2V cosφ relation.** Independently re-derived via the operator
  identity L_xy−D_xy=σx⊗σx+σy⊗σy (using J_ax²=J_bx²=J_ay²=J_by²=I/4), which
  acts on the {|01⟩,|10⟩} subspace as the matrix [[0,2],[2,0]]. Computing
  trace(ρ·Cop) for the stated ρ (diagonal 1/2, off-diagonal −Ve^{±iφ}/2)
  gives exactly −2V cosφ, matching the script's assertion. (My first
  attempt at this by direct basis-by-basis application of J_ax, J_bx etc.
  contained an arithmetic slip; the clean operator-identity route above
  was double-checked and is correct.)
- Script re-executed end-to-end: exit 0, all PASS lines printed, no error.

No discrepancy found. v15.1147's own scope caveats (planar-angle vs.
polar-magic-angle axis distinction, no new force/selector claimed) are
accurate and are not expanded here.

## Gravity v15.1148 — independent verification

- **Classical forced-oscillator response.** Solving Iq̈+Iω_m²q=F_g,
  q(0)=q̇(0)=0 by hand gives q(t)=F_g/(Iω_m²)(1−cosω_m t), matching
  exactly.
- **Induced phase.** φ_g(t)=k∫_0^t q(s)ds=kF_g/(Iω_m²)[t−sin(ω_m t)/ω_m],
  confirmed by direct integration.
- **Revival endpoint.** At t_n=2πn/ω_m: sin(ω_m t_n)=0 ⇒
  φ_g(t_n)=2πn kF_g/(Iω_m³); sin²(ω_m t_n/2)=sin²(πn)=0 ⇒ V(t_n)=1.
  Both confirmed by hand.
- **dφ_g/dg at magic angle.** sin2θ*=2sinθ*cosθ*=2√(2/3)√(1/3)=2√2/3;
  dφ_g/dg|_{t=2π/ω_m}=2πk·DQ·sin2θ*/(Iω_m³)=4√2πkDQ/(3Iω_m³), matching
  the script's assertion exactly.
- Script re-executed end-to-end: exit 0, PASS, no error.

No discrepancy found.

## Gravity v15.1149 — independent verification

This entry carries the most new analytic content this round; verified
each closed form independently:

- **J(t) exact Gaussian integral.** By hand, with a=λ−iω,
  ∫_0^t(t−u)e^{-au}du=t/a−(1−e^{-at})/a² (standard forced-response
  integral); taking Re[·] reproduces the script's `J_exact`. Checked the
  λ=0 special case reduces to (1−cosωt)/ω² by hand (splitting real/imaginary
  parts of it/ω−(e^{iωt}−1)/ω²). Checked ∂J/∂λ|_{λ=0} at t=2π/ω: directly
  computed ∫₀^{2π}(2π−u)u cos u du = −4π by hand integration-by-parts
  (ω=1 units), giving J'(0)(2π)=4π exactly as claimed.
- **Weak-damping closed form.** Independently re-derived
  ω²J(T)=2πx/(1+x²)+(1−e^{−2πx})(1−x²)/(1+x²)² (x=λ/ω, T=2π/ω) from the
  same a=x−i expression, by taking the real part of 2π/a and of
  −(1−e^{−2πa_norm... })/a² directly — reproduces the ledger's formula
  exactly.
- **Small-x / high-Q expansion.** Expanding both terms to O(x) confirms
  J(T)≈4πx, hence −log V(T)≈πr(2n̄+1)/Q, matching the stated leading-order
  law.
- **Numerical table (Gate 1050).** Recomputed all nine V(2π,Q,n̄) values
  independently from the closed-form expression (own fresh script, not
  the committed one): Q=30 → 0.989850310/0.969858932/0.807160666; Q=100 →
  0.996887833/0.990692526/0.936638933; Q=1000 → 0.999686137/0.999058705/
  0.993429515 for n̄=0/1/10 respectively. All nine values match the
  ledger's table to the stated 9 decimal places exactly.
- **Damped forced response (Gate 1051).** Solved
  Iq̈+2Iλq̇+Iω₀²q=F_g by hand (standard underdamped step response),
  confirming q_g(t)=F_g/(Iω₀²){1−e^{−λt}[cos(ω_d t)+(λ/ω_d)sin(ω_d t)]}
  exactly. Independently numerically integrated ∫₀^T q_g dt for
  λ=.001,.05,.2 (fresh quadrature, not the committed script): all three
  strictly positive (6.283, 6.241, 5.777), confirming nonzero net phase
  under damping.
- Script re-executed end-to-end: exit 0, all PASS lines, output table
  matches the independent recomputation above verbatim.

No discrepancy found anywhere in v15.1147-1149. All three entries' stated
scope limits (conventional spin-boson/forced-oscillator mechanics, no new
Cone force, no source-selected frequency, no backaction-free claim) are
accurate.

## Lane A "v15.1147" (512-arc tile) — independent verification on its own merits

Despite losing the version-number collision, the underlying Suzuki
certificate was checked exactly as any Lane A entry:

- Script diff against the already-audited v15.1144 script: only the step
  count (128→256), output filename, and scope label differ; rebase
  cadence and core logic are byte-identical to the already-verified
  method.
- SHA-256 of all four cited files (script, certificate, two dependencies)
  recomputed and matched exactly.
- Independent parse of the raw certificate: exactly 512 distinct arcs
  spanning `{3753,...,4008} ∪ {4010,...,4265}` with no gap or duplicate;
  exactly 126 rebases (63 per direction) at the stated positions; all 512
  states pass; the 256 arcs overlapping the audited v15.1144 certificate
  are bitwise identical (0 mismatches).
- Every number in the ledger's table cross-checked against this
  independent parse: all matched exactly (max direct/propagated fourth
  roots 3.9289932109020365/3.9289932109340513, max propagated b4
  238.30058775459705, max cumulative/rebase arithmetic, max discrepancy,
  max sweep-minus-direct, unchanged weight hash/condition).
- Independent re-execution: ran the script end-to-end myself; it finished
  `STATUS=R4_BLOCK_COVERAGE_PASS`, exit 0, and regenerated the certificate
  bit-for-bit identical (SHA-256
  `2bd51456de46ff39efabc42230bffea70f1f37171e0e03b56032c0a967ab2c0c`) to
  the committed one.

Verdict: the 512-arc Suzuki certificate itself is correct and fully
reproducible. The only defect is the version-number collision documented
above, which this audit flags but does not correct on Lane A's files.

## Verdict

All four new entries PASS on independent verification. One genuine
version-number collision found and resolved per protocol (Gravity keeps
v15.1147 by earlier UTC timestamp; Lane A's colliding file is flagged,
untouched). No mathematical or numerical error found in any of the four
entries.

`git fetch origin master` immediately before this commit returns
`b04aaf1`, unchanged since the pushes verified above. Lane A should use
the next free version number (v15.1150 is now taken by this entry, so
v15.1151 onward) for its next tile; Gravity/Sandbox should continue.
