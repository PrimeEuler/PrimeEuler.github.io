# Cone Derivation Ledger v15.609 — Lane A: boundary Casimir pushforward under mesh-unit scaling and Paper C origin shift

**Date:** 2026-11-10. **Parents:** v13.197 circle staircases, Paper C Quantum Realizations v1.1, v14.767 EM/quarter scale covariance, v15.602 all-q Casimir theorem, v15.605–608 normalized, shell and full-staircase circle calculations. **Status:** [D] exact scale/translation identities in specified coordinate convention; [O] physical origin, spectral selector and dynamics. **Live HEAD:** 8ec355e813be07f85206d22270e3e981de66c0f4, immediately rechecked; v15.609 path search empty. Additive only, Suzuki frozen production untouched.

## Gate 79: homogeneous mesh-unit scaling

For factor grid unit u>0, *when the original transition step is also the unit u*, formal adjacent AM–GM squares are W_up=y(x+u), W_down=x(y+u). In the continuum extension, source-to-target truncation gives

E_u(x,y)=1/2[y(x+u) 1_{y<u}+x(y+u)1_{x<u}].

Under x=uX,y=uY, E_u(uX,uY)=u²E_1(X,Y). The cone's flat area Jacobian J=(x+y)/(4sqrt(xy)) is homogeneous of degree zero, while dxdy→u²dXdY. For corresponding u-scaled triangle and divisor staircases with matched dimensionless index n, the shared boundary functional satisfies

**B_{T,u}(n)=B_{D,u}(n)=u^4 B_1(n), B_{A,u}(n)=0,**
**B_1(n)=sqrt(n)(3n²+8n+9)/45.**

The u-scaled pushforward areas satisfy W_{*,u}=u²W_{*,1}; hence normalized boundary means scale as u²; after dividing by u², the means are dimensionless and invariant. For u=1/2, unnormalized B is 1/16 of u=1 at matched n, and area-normalized mean is 1/4. **This is homogeneity, not a predicted Newton G or a physically chosen EM/G carrier.** If a unit-one transition operator is retained while coordinates are refined to u<1 (the v15.602 scenario), it is a DIFFERENT comparison: its defect lives in width-one, not width-u strips, and no u^4 law is asserted.

## Gate 80: Paper C's shifted factor origin

Paper C's native dictionary is x=n1+1, y=n2; this is distinct from the auxiliary doubled-number embedding in v15.598. To isolate the effect of origin shift on the v15.608 *continuum* functional, translate v13.197's p,r staircases by x=p+1,y=r while retaining the same factor-cone F(x,y)=((x−y)/2,sqrt(xy)) and its absolute original unit-one deficit E_1(x,y).

All translated points have x≥1, so the x<1 strip gives no interior area; only the y<1 horizontal strip survives. The triangular and divisor staircases still share that bottom strip in the translated convention; their complement has y≥1 and x≥1 almost everywhere. Thus **B_{T,shift}=B_{D,shift}, B_{A,shift}=0**, but the common integral changes to

**B_shift(n)=(n+1)^(5/2)/30+4(n+1)^(3/2)/45+sqrt(n+1)/10−2/9.**

At n=11, unshifted B=33.9032756347441; translated B_shift=20.4469174147664. The Jacobian is not invariant under translation; the original v13.197 staircase *areas* likewise cannot simply be recycled after the shift. The persistence of triangular/divisor equality here is an overlap/support fact, not invariance of the integral's numerical value, and it would not hold for arbitrary changes to factor origin or shifted physical transition rules.

This coordinate-domain exercise does NOT establish that Paper C's Schwinger operators generate the defective original-step ladder. Paper C uses ordinary integer Fock occupations and a physically distinct operator dictionary; no automatic unitary identification is claimed.

## Verification, scope, audit

Independent SymPy exact integrations checked original v15.608 B(n), shifted B_shift(n), homogeneous Jacobian, u² defect scaling and u^4 integral scaling, with n=11 spot checks. Local reproducible deliverable: cone_gate79_80.zip (REPORT.md, reproduce.py). The full-shift case is a translation of positive factor *regions*, not a generic coordinate change of both operator and measure; keep the distinction.

**Next gate:** test translations and dilations with a fixed original unit-step operator against the factor-coordinate power map v14.767. Compare any candidate physically selected measure with the u-covariant measure before claiming scale selection.

**HANDOFF** target external-audit, gravity, sandbox; status open; type continuum factor-origin and unit covariance audit; verify B_shift, positive-x-shift shared-strip support, u^4 versus u² scalings, and fixed-unit-step versus co-scaled-step distinction. No frozen Suzuki modifications.
