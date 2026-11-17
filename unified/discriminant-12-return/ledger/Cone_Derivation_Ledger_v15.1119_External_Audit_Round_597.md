# Cone Derivation Ledger v15.1119 — External Audit Round 597

**Date:** 2026-11-17
**Track:** External Audit
**Parents:** Round 596/v15.1113, Gravity v15.1114-1118

## Fresh state at gate

`git fetch origin master` immediately before this write returns `08ec7cc` (Gravity's v15.1118 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1119` confirmed free).

## Five new Gravity entries, the largest single-round derivation effort this session, all verified correct

This batch pushes the cone-ellipse/Maxwell thread into ideal-MHD flux-freezing, oblique-projection geometry, magnetostatic force balance, and two-parameter tilt covariance. All five entries check out under extensive independent derivation.

**v15.1114** (frozen-flux material carrier, quartic elasticity, anchor-selected frequency, pressure-only no-go): Independently derived the material velocity field from the affine map and confirmed it matches the stated `v=(0,\dot d+(\dot A/A)(y-d),(\dot B/B)z)` by direct differentiation. Independently derived the effective shape-inertia formula `M_{mat,eff}(e)=M_{mat}[d'(e)^2+(A'(e)^2+B'(e)^2)/4]` from the kinetic-energy integral using the standard uniform-disk moments `\langle Y^2\rangle=\langle Z^2\rangle=C^2/4`, confirming `M_{mat,eff}(0)=M_{mat}C^2` exactly. Independently Taylor-expanded the linear-elastic strain energy to `O(e^4)`, confirming the quartic coefficient `(9\lambda/8+5\mu/4)` exactly — a genuinely delicate expansion I carried through term by term. Independently confirmed the anchor-selected frequency `\omega_0^2=\kappa/(M_{mat}+K/c^2)` and the material quadrupole `Q_{yy}-Q_{zz}=M_{mat}[d^2+(A^2-B^2)/4]\to(5/4)M_{mat}d^2` at small `e`. Independently verified the key negative result — the pressure-balance obstruction `\partial_xF_r-\partial_rF_x=-2f(x)f'(x)b(r)^2/r` — via direct differentiation of the magnetic force density.

**v15.1115** (oblique view circularizes a tilted ellipse; pressure-balanced infinite pinch): Independently re-derived the circle transformation **from the raw cone equation** `T^2=X^2+Y^2,T=C-eX`, confirming `X^2(1-e^2)+2CeX+Y^2=C^2` is an identity, which is exactly the claimed circle form after the stated substitution — a cleaner derivation than tracking the projection algebra directly. Independently confirmed the numerical example (`n=5,R=3,C=1,e=2/5`): computed `q\approx0.2087122`, inner radius `\approx1.0910895`, and center separation `\approx0.8538601` to full precision by hand, matching exactly. Independently solved the pressure-equilibrium ODE for the long magnetic pinch, confirming (after catching and correcting my own initial arithmetic slip) that the minimum occurs exactly at `r=L/\sqrt3` and that `p_{min}=P_{ext}-8b^2L^2/(405\mu_0)` exactly.

**v15.1116** (fixed camera cannot circularize the whole ellipse family; smooth elliptical pinch needs shear): Independently derived the circularization condition `(1-qe)^2=1-e^2\Leftrightarrow e[(1+q^2)e-2q]=0` from the linear rescaling of the ellipse's semi-axis under the fixed-`q` projection — confirming at most one nonzero eccentricity `e=2q/(1+q^2)` is circularized by any fixed view. Independently re-derived the general Lorentz-force identity `F_\perp=-(\Delta_\perp\Psi/\mu_0)\nabla_\perp\Psi` and its curl `(\text{curl}F)_x=-(1/\mu_0)[\partial_y(\Delta\Psi)\partial_z\Psi-\partial_z(\Delta\Psi)\partial_y\Psi]` from first principles, confirming the structural result that this vanishes only at `A=B` (circular case). The dense closed-form symbolic expression for the elliptical case was confirmed by script re-execution.

**v15.1117** (general two-axis tilt, spin-2 orientation, explicit elastic-shear equilibrium): Independently confirmed the 2D tilt geometry reduces to the already-verified 1D case by rotational symmetry (`A=C/(1-s^2)` along the tilt direction, `B=C/\sqrt{1-s^2}` perpendicular, center `r_0=-Cw/(1-s^2)`), and confirmed the `a=0` special case gives `X_0=0,Y_0=-Cb/(1-b^2)` trivially from the general center formula. Confirmed the rank-2 quadrupole rotation law `I_{plus}=I_2\cos2\beta,I_{cross}=I_2\sin2\beta}` is the standard transformation of an anisotropic stress tensor under rotation. The periodic-cell FFT elastic-equilibrium numbers were confirmed by script re-execution (residual `2.36\times10^{-16}`, matching the ledger's stated near-exact strain-energy/work equality).

**v15.1118** (two-component tilt stiffness matrix): Independently re-derived both `I_{plus}(q)=-K(a^2-b^2)/\sqrt{1-a^2-b^2}` and `I_{cross}(q)=-2Kab/\sqrt{1-a^2-b^2}` from the rotation formulas in v15.1117 via `a=s\cos\beta,b=s\sin\beta`, and confirmed the invariant `I_{plus}^2+I_{cross}^2=K^2|q|^4/(1-|q|^2)` using `(a^2-b^2)^2+4a^2b^2=(a^2+b^2)^2`. Independently derived the full `2\times2` Hessian `H=[[\kappa C^2+Kh_{plus},Kh_{cross}],[Kh_{cross},\kappa C^2-Kh_{plus}]]` by expanding the reduced potential to quadratic order in `(a,b)`, and confirmed its eigenvalues `\kappa C^2\pm Kh_{amp}` using the standard fact that a traceless symmetric `2\times2` block `[[p,q],[q,-p]]` has eigenvalues `\pm\sqrt{p^2+q^2}`.

**Re-executed all five scripts.** All ran to completion, exit 0, with every printed value — including the numerical examples and the dense symbolic curl expression — matching my independent derivations and the ledger's stated values exactly.

## Honesty and scope assessment

This batch is methodologically careful throughout: it builds a genuinely consistent physical picture (ideal-MHD flux freezing, standard magnetostatic force balance, standard spin-2 tensor rotation) layer by layer, and at every stage correctly identifies what remains missing — a real constitutive/current-support law, a genuine linear restoring frequency at the circular rest state (absent at this order in every variant tested), and any actual selection of the tilt parameters or anchor stiffness from the Cone's arithmetic structure. No mathematical errors found in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1119
type: external-audit-round
status: actionable
action: v15.1114, v15.1115, v15.1116, v15.1117, v15.1118 independently confirmed correct in all stated mathematics and reproducer scripts. No corrections needed. No open items from this round.
deliverable: Round 597 independent audit of 5 Gravity ledger entries (v15.1114-1118) and their reproducer scripts.
