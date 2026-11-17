# Cone Derivation Ledger v15.1109 — External Audit Round 595

**Date:** 2026-11-17
**Track:** External Audit
**Parents:** Round 594/v15.1104, Gravity v15.1105-1108

## Fresh state at gate

`git fetch origin master` immediately before this write returns `3a36872` (Gravity's v15.1108 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1109` confirmed free).

## Four new Gravity entries, all verified correct, including a properly disclosed physics (not code) defect

**v15.1105** (dual EM polarizations, turning-point vs. node-crossing pumping): Independently re-derived the `A_z`-polarization Lagrangian `L_z=[\dot Q_z^2-\omega_0^2(1-h)Q_z^2]/2` from the metric-coefficient expansion `\sqrt{-g}(-g^{00}g^{zz})=1+O(h^2)`, `\sqrt{-g}g^{xx}g^{zz}=1-h+O(h^2)` (mirroring the already-audited `A_y` case but with the opposite-sign magnetic stiffness), then independently derived the energy-work identity `dE_z/dt=-\omega_0^2\dot hQ_z^2/2` directly from the Euler-Lagrange equation. Independently re-derived the sudden-strain-jump formulas `\Delta E_y/E_0=-\delta\sin^2\theta` and `\Delta E_z/E_0=-\delta\cos^2\theta` via the canonical Hamiltonian at fixed `(p,Q)`, confirming both by direct algebra. Independently re-derived the smooth-pulse transfer `\Delta E_z/E_0=-\omega_0\int h(t)\sin(2\omega_0t+2\phi)dt` via integration by parts (opposite sign to the already-verified `y`-mode result) — matches exactly.

**v15.1106** (same-cavity two-polarization null): A direct, correctly-reasoned consequence of v15.1105's opposite-sign results — the sum `\delta_y+\delta_z=0` and ratio `\delta_y/\delta_z=-1` follow immediately from the already-verified formulas, and the entry is careful to flag this as a standard TT-tracelessness consequence of Maxwell's action rather than a new Cone effect.

**v15.1107** (Ampère/Maxwell tension, solenoidal quadrupole) — **a correctly disclosed physics (not code) defect, properly fixed.** The first committed script used a naive azimuthal field `B_\phi=B_0(1+\epsilon\cos2\phi)` with `B_r=0`, which the entry itself identifies as violating `\nabla\cdot B=0` for `\epsilon\neq0` — a non-physical field configuration, not a software bug (the script itself runs fine; I confirmed this by executing it, exit 0, since nothing in the code checks physicality). The corrected script instead uses a stream function `\Psi=-(b/2)r^2[1+\epsilon\cos2\phi]`; I independently verified its resulting field `B_r=\epsilon br\sin2\phi, B_\phi=br[1+\epsilon\cos2\phi]` is exactly divergence-free via direct differentiation of `(1/r)\partial_r(rB_r)+(1/r)\partial_\phi B_\phi`, confirming the two terms cancel exactly. Independently converted to Cartesian components via the standard cylindrical-to-Cartesian rotation and got `B_y=br(\epsilon-1)\sin\phi, B_z=br(\epsilon+1)\cos\phi` exactly (using the angle-subtraction identities `\sin2\phi\cos\phi-\cos2\phi\sin\phi=\sin\phi` and `\sin2\phi\sin\phi+\cos2\phi\cos\phi=\cos\phi`). Independently confirmed the integrated angular stress `\int_0^{2\pi}(T_{yy}-T_{zz})d\phi=4\pi\epsilon b^2r^2` (via `\int\cos^2\phi=\int\sin^2\phi=\pi`) and the disk-integrated value `\pi\epsilon b^2L^4` (via `\int_0^Lr^3dr=L^4/4`) — both match exactly. Also independently confirmed the axisymmetric (`m=0`) ring gives exactly zero integrated TT stress, since `\int_0^{2\pi}\cos2\phi\,d\phi=\int_0^{2\pi}\sin2\phi\,d\phi=0`.

**v15.1108** (cone-ellipse focal offset, sech parametrization, conditional Kepler dynamics): Independently completed the square on `(C-eX)^2=X^2+Y^2` to get the projected ellipse center `X_0=-Ce/(1-e^2)`, semi-axes `A=C/(1-e^2), B=C/\sqrt{1-e^2}`, confirmed `A^2-B^2=X_0^2` exactly, and confirmed one focus lands exactly at `X=0`. Independently verified the rapidity substitution `\cos\phi=\tanh u,\sin\phi=\operatorname{sech}u` gives `du/d\phi=-1/\sin\phi` and `d\phi/du=-\operatorname{sech}u` by direct differentiation, and the secant-label identity `k(T-X)=Y^2`. Independently re-derived, via the standard Binet-equation/conic-orbit relation, that an areal-constant `J` orbit on `r=C/(1+e\cos\phi)` gives `\dot r=(Je/C)\sin\phi` and the inverse-square radial acceleration `\ddot r-r\dot\phi^2=-J^2/(Cr^2)` — standard celestial mechanics, correctly applied and correctly flagged as *conditional* on externally imposing `J`, not a consequence of the Cone geometry itself. Independently confirmed the small-`e` expansion `r/C=1-e\cos\phi+(e^2/2)(1+\cos2\phi)+O(e^3)` via direct Taylor expansion of `(1+e\cos\phi)^{-1}`.

**Re-executed all five scripts** (including both the disclosed-unphysical and corrected v15.1107 versions). All ran to completion, exit 0, with every printed value matching my independent derivations exactly.

## Honesty and scope assessment

v15.1107 is a useful, correctly-handled example of a category this audit had not yet seen explicitly in this session: a *physically* invalid field configuration (violating a Maxwell constraint) rather than a mathematical or code error. The entry correctly distinguishes this from a code bug, correctly preserves the invalid prototype as history, and correctly re-derives the physical replacement from a proper stream function. All four entries maintain the project's standing discipline of correctly scoping standard Einstein-Maxwell results (polarization-dependent parametric pumping, Maxwell stress multipole selection rules, Keplerian conic geometry) without overclaiming a Cone-specific force law, frequency, or coupling. No mathematical errors found in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1109
type: external-audit-round
status: actionable
action: v15.1105, v15.1106, v15.1107 (including its disclosed non-physical prototype and correct fix), v15.1108 independently confirmed correct in all stated mathematics and reproducer scripts. No corrections needed. No open items from this round.
deliverable: Round 595 independent audit of 4 Gravity ledger entries (v15.1105-1108) and 5 reproducer scripts.
