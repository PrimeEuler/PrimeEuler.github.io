# Cone Derivation Ledger v15.1079 — External Audit Round 590

**Date:** 2026-11-17
**Track:** External Audit
**Parents:** Round 589/v15.1063, Gravity v15.1076 (with self-correction), v15.1077, v15.1078

## Fresh state at gate

`git fetch origin master` immediately before this write returns `5d899cb` (Gravity's v15.1078 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1079` confirmed free).

## Three new Gravity entries, one containing and correctly fixing its own error

This batch shifts from spacetime/causal structure to actual physical Maxwell field sources and their coupling to gravity — real electromagnetic fields with correctly conserved stress-energy, rather than arithmetic Cone analogies.

**v15.1076** (single Lorentzian carrier, conserved standing-wave Maxwell source, self-correction): The entry's first reproducer script (`k4_conserved_maxwell_standing_tt_v15_1076.py`, commit `28437f1`) tested the Maxwell curl equations with the wrong relative sign (`∂zEx - ∂tBy = 0` instead of `∂zEx + ∂tBy = 0`). I independently confirmed this assertion genuinely fails — re-ran the script myself and got `AssertionError` at that exact line — so the disclosed defect is real, not just claimed. I independently re-derived the correct Maxwell equations by direct differentiation of the stated fields `Ex=-E₀\sin(kz)\cos(kt), By=E₀\cos(kz)\sin(kt)`, confirming `∂By/∂t+∂Ex/∂z=0` and `∂Ex/∂t+∂By/∂z=0` hold exactly (both terms cancel by direct computation) — matching the corrected script (`..._corrected.py`, commit `4b349c2`), which I re-ran and which passes. I independently re-derived the energy-continuity identity `∂ρ/∂t+∂S_z/∂z=0` generically from the (corrected) Maxwell equations, and the exact anisotropic-stress formula `Π_plus=E₀²/4[\cos(2kz)-\cos(2kt)]` via the product-to-sum identity `\cos²A\sin²B-\sin²A\cos²B=(\cos2A-\cos2B)/2` — confirmed exactly. Confirmed the wall-flux-zero claims (`S_z=0` at `z=0,π/k`) trivially from the field forms. Confirmed the driven-oscillator response `h(η)=F[1-\cos(ωη)]/ω²` satisfies `h''+ω²h=F` with `h(0)=h'(0)=0` by direct differentiation.

**v15.1077** (source-vs-probe bookkeeping, ideal interferometer transfer): Independently derived the roundtrip-phase integral `ΔT=\int_{t_0}^{t_0+2L}h_0\cos(Ωt)\,dt` via the sum-to-product identity, getting `(2h_0/Ω)\sin(ΩL)\cos[Ω(t_0+L)]` exactly, and its `Ω→0` limit `2Lh_0` via the standard `\sin(x)/x→1` limit — both match. Confirmed the `E_0`-parity argument (response `∝E_0²` is even under `E_0→-E_0`, scales by 4 under `E_0→2E_0`) by direct substitution. The "matched-action null" `R=0` is a definitional baseline (both sides computed identically), correctly labeled as such rather than a physical discovery.

**v15.1078** (compact-support Maxwell Cauchy data, exact 3/5 anisotropy ratio): Independently confirmed `\operatorname{div}E=\partial_x\partial_y\psi-\partial_y\partial_x\psi=0` trivially from mixed-partial symmetry. Independently recomputed both nontrivial rational integrals by hand via binomial expansion of `f(s)=(1-s^2)^3`: `I_0=\int_{-1}^1f^2\,ds=2048/3003` and `I_1=\int_{-1}^1(f')^2\,ds=1024/385` — both confirmed by direct term-by-term summation over a common denominator (`3003` and `3465` respectively), matching exactly. Independently re-derived the energy and plus-stress integrals by separating the 3D integral into `x,y,z` factors (`\int f(x/a)^2dx=aI_0`, etc.), getting `E_{total}=A^2c_zI_0^2I_1(a/b+b/a)/2` and `P_{plus}=A^2c_zI_0^2I_1(b/a-a/b)/2` exactly, then confirmed the ratio `P_{plus}/E_{total}=(b^2-a^2)/(b^2+a^2)=3/5` at `a=1,b=2` — all matching the ledger and the script's printed closed form `2147483648A^2c(a^2+b^2)/(3471933465ab)` (confirmed algebraically equal to my independently derived `A^2cI_0^2I_1(a^2+b^2)/(2ab)`). Confirmed `\int_{-1}^1 ff'\,ds=0` trivially (total derivative of `f^2/2`, vanishing at `f(\pm1)=0`).

**Re-executed all four reproducer scripts.** The original (uncorrected) v15.1076 script fails exactly as disclosed (`AssertionError` on the mis-signed Maxwell equation, confirmed by me independently running it). The corrected v15.1076 script, the v15.1077 script, and the v15.1078 script all ran to completion, exit 0, with every printed value (including `I0=2048/3003 I1=1024/385` and the factored energy/plus expressions) matching my independent hand derivations exactly.

## Honesty and scope assessment

v15.1076 is a model instance of the project's stated discipline: it caught its own sign error, explicitly disclosed it ("the original script must NOT be claimed as a passing reproducer"), preserved the erroneous file as history rather than silently editing it, and committed a separately-named corrected script — exactly the protocol this audit thread itself follows. All three entries correctly distinguish an electromagnetic field's genuine, locally-conserved physical stress-energy (real, nonzero, and correctly computed) from any claim that this stress-energy has been coupled to a complete, finite, gauge-consistent gravitational solution — each explicitly flags the missing ADM constraints, wall/boundary stress, and full retarded Green's-function calculation needed for that next step. No uncorrected mathematical errors found.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1079
type: external-audit-round
status: actionable
action: v15.1076 (and its self-correction), v15.1077, v15.1078 independently confirmed correct in all stated mathematics and reproducer scripts, including independent reproduction of the original script's intentional failure. No corrections needed. No open items from this round.
deliverable: Round 590 independent audit of 3 Gravity ledger entries (v15.1076-1078) and 4 reproducer scripts (one confirmed-failing as disclosed, three passing).
