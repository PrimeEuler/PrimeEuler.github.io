# Cone Derivation Ledger v15.1099 — External Audit Round 593

**Date:** 2026-11-17
**Track:** External Audit
**Parents:** Round 592/v15.1092, Gravity v15.1093-1098

## Fresh state at gate

`git fetch origin master` immediately before this write returns `1ab094c` (Gravity's v15.1098 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1099` confirmed free).

## Six new Gravity entries, one with a properly self-disclosed structural (non-mathematical) script issue

This batch systematically tests whether any physical mechanism — Maxwell curl geometry, Dirac spin current, relativistic acceleration geometry, Rindler/Euclidean smoothness, spinor antiperiodicity, or accelerated-detector detailed balance — can fix the free scale ratio `ρ=R/λ̄_C` between the Rindler length and the reduced Compton wavelength (already shown free in earlier, previously-audited work, v15.886). Every entry correctly concludes "no selection." I independently re-derived essentially all load-bearing formulas by hand.

**v15.1093** (Maxwell curl geometry vs. Zitterbewegung loop): Independently confirmed `E·∇Ψ=0` trivially, and the exact radial-projection value at `(a/2,b/2,0)`: using `f(1/2)=27/64` and `f'(1/2)=-27/16` (both confirmed in earlier rounds), got `xE_x+yE_y=-729A(a²-b²)/(2048ab)` by direct differentiation — matches exactly. Independently re-derived `\dot B(0)=(-Ψ_{xz},-Ψ_{yz},Ψ_{xx}+Ψ_{yy})` from `\dot B=-\operatorname{curl}E`, and confirmed the center value `\dot B_z(0)=-6A(1/a^2+1/b^2)` using `f''(0)=-6`. **The original script's disclosed defect is a genuine SymPy structural-equality mismatch** (comparing two correctly-equal expressions with different internal forms), not a math error — I confirmed this by running it myself: it fails at exactly the disclosed line, while the corrected script (using `simplify`) passes and prints `Bdot(center)=[0,0,-6A/b²-6A/a²]` and the radial projection `-729A(a-b)(a+b)/(2048ab)`, both algebraically identical to what I derived by hand.

**v15.1094** (Gordon spin current, full moment without convection): Independently confirmed `\operatorname{curl}(ρ\hat z)=(ρ_y,-ρ_x,0)` from the vector identity `\operatorname{curl}(f v)=\nabla f\times v` for constant `v`, giving `j_{spin}=-(qℏ/(mL^2))ρ(y,-x,0)` exactly. Independently computed the magnetic moment `μ_z=(1/2)\int(xj_y-yj_x)d^3x = (qℏ/(2mL^2))\int(x^2+y^2)ρ\,d^3x`, used the standard Gaussian second moment `\int x^2ρ=L^2/2`, and got `μ_z=qℏ/(2m)` exactly — the full leading Dirac moment (`g=2`), confirming it arises entirely from spin current with zero convection current.

**v15.1095** (sourced magnetostatic field, finite energy): Independently re-derived the Fourier current `\hat j(k)=iK(k\times\hat z)e^{-L^2k^2/4}` from the derivative/FT rules, then solved the Ampère equation in Fourier space (`\hat B=i(k\times\hat j)/k^2`) via the vector triple-product identity to get `\hat B(k)=Ke^{-L^2k^2/4}[\hat z-k k_z/k^2]` exactly. Independently computed the Parseval energy integral using the angular integral `\int\sin^2θ\,d\Omega=8π/3` and the radial Gaussian integral `\int_0^\infty k^2e^{-L^2k^2/2}dk=\sqrt{2π}/(2L^3)` (both confirmed by standard formulas), arriving at `U_B=K^2/[3(2π)^{3/2}L^3]` exactly — matching the script's printed `\sqrt2 K^2/(12π^{3/2}L^3)` (confirmed algebraically identical by hand) and the `L\to L/2 \Rightarrow 8\times$ energy` scaling.

**v15.1096** (acceleration-parabola focus, osculating circle): Independently Taylor-expanded the exact relativistic hyperbola `x(y)=R[\sqrt{1+(y/R)^2}-1]=y^2/(2R)-y^4/(8R^3)+O(y^6)`, identified the osculating parabola `y^2=2Rx` giving focal length `f=R/2`, and confirmed the standard geometric fact that a parabola's vertex curvature radius is `2f=R`. Confirmed the toy azimuthal-profile extremum `B_\phi\propto r/(r^2+d^2)^{3/2}` peaks at `r=d/\sqrt2` by direct differentiation.

**v15.1097** (Euclidean Rindler circle, spinor sign): Confirmed the standard Rindler-to-Euclidean-polar continuation and its `2π`-periodicity (textbook Unruh-temperature derivation), then independently derived `ω_{ZB}/ω_R=2ρ` and `k_BT_U/(mc^2)=1/(2πρ)` directly from the stated definitions `a=mc^3/(ρℏ)`, `ω_R=a/c`, `ω_{ZB}=2mc^2/ℏ` — both match exactly.

**v15.1098** (accelerated-detector KMS, Matsubara frequencies): Independently derived the detailed-balance ratio `\Gamma_{up}/\Gamma_{down}=\exp(-2πρ)` from the stated response formulas via direct algebraic simplification (confirmed the `e^{x}-1=e^x(1-e^{-x})` substitution reduces the ratio to `e^{-x}` exactly, with `x=2πρ`), and the spontaneous-emission-like difference `\Gamma_{down}-\Gamma_{up}=CΩ/(2π)` via the same substitution. Independently confirmed the fermionic Matsubara frequency formula `ω_n=(n+1/2)a/c` from the standard antiperiodic-boundary formula `ω_n=(2n+1)π/β`, giving `ω_n/Ω=(n+1/2)/ρ` exactly. Confirmed the numerical value `e^{-2π}=0.0018674427...` matches the standard tabulated constant.

**Re-executed all seven scripts.** The original v15.1093 script fails exactly as disclosed (confirmed: a structural, not mathematical, SymPy equality mismatch). The corrected v15.1093 script and all six other scripts ran to completion, exit 0, with every printed value matching my independent hand derivations exactly.

## Honesty and scope assessment

This batch is a model of the project's stated discipline: six entries systematically close off candidate "selectors" for a previously-identified free parameter, using a wide range of genuinely standard physics (Gordon decomposition, Fourier magnetostatics, Rindler geometry, Unruh-DeWitt detector theory, fermionic Matsubara frequencies) applied correctly and without overclaiming, plus one more properly disclosed and properly classified script defect (structural, non-mathematical, clearly distinguished from the genuine mathematical defect found and fixed in Rounds 591-592). No uncorrected errors found.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1099
type: external-audit-round
status: actionable
action: v15.1093 (and its disclosed structural correction), v15.1094, v15.1095, v15.1096, v15.1097, v15.1098 independently confirmed correct in all stated mathematics and reproducer scripts. No corrections needed. No open items from this round.
deliverable: Round 593 independent audit of 6 Gravity ledger entries (v15.1093-1098) and 7 reproducer scripts (one confirmed-failing as disclosed, six passing).
