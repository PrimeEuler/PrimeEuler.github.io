# Cone Derivation Ledger v15.896 — Two circles on one fixed-product shell: exact rapidity map and contact orders

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** v13.177 parabola/tangent-circle theorem; v14.367 diameter–secant dictionary; v15.605 sector scaling; v15.864 tangency chain; v15.895 two-circle clarification. **Live master HEAD checked before ledger write:** 45d41dfab400513e0ba20238617ba85f5d175ef9. Target path checked absent. Additive only; no writes to Suzuki/Audit/Sandbox or certified objects.

**Question:** What exact map connects the sqrt(n) rest-shell circle and the n+1 outer chord circle, what are their distinct contact orders, and does the result supply a restoring-force clock?

**Status:** [D] exact 3-coordinate shell map, distinct contact and crossing, sector covariance; [N] no acceleration/time or force selector; [O] field-derived restoring dynamics and canonical action map.

## Gate 562 — exact shared-shell map across different sections

At factor-grid unit u>0 and normalized pair (un,u), introduce the original Cone coordinates

**X=(x−y)/2, T=(x+y)/2, Y=sqrt(xy)**,

so X²+Y²=T², and fixed-product xy=u²n becomes T²−X²=u²n.

The same shell admits the EXACT dimensionless parameterization

**x=u sqrt(n) exp(s), y=u sqrt(n) exp(−s)**,
**X=u sqrt(n) sinh(s), T=u sqrt(n) cosh(s), Y=u sqrt(n)**.

Its rest vertex occurs at s=0, (X,T,Y)=(0,u sqrt(n),u sqrt(n)). The divisor-pair point (x,y)=(un,u) occurs at **s_n=(1/2)ln n**, hence

**X_n=u(n−1)/2, T_n=u(n+1)/2, Y_n=u sqrt(n)**.

At that same point, the level-u row parabola in flat (X,Y), **Y²=u²+2uX**, is satisfied exactly, and so is its fixed-T outer circle **X²+Y²=[u(n+1)/2]²**. The `Y=u sqrt(n)` secant is the common normalized bridge. Important: the rest (X,T) shell tangent and the (X,Y) outer-circle/parabola crossing are distinct points of the shell at different s, not a single intersection in a single plane. At n=1 the rapidity stations coincide as shell points, but the rest circle and outer circle radii coincide only for the special u-scaled n=1 case; the row parabola's slope and outer circle's slope remain distinct at their shared top point.

## Gate 563 — orders of contact, no merging of curves

Set r=u sqrt(n)>0 and local X=z. In the auxiliary Euclidean (X,T) shell diagram,

**T_shell=sqrt(r²+z²)**, **T_restcircle=sqrt(r²−z²)**.

Both have value r and zero first derivative at z=0; their exact local separation is

**T_shell−T_restcircle=z²/r+z⁶/(8r⁵)+O(z¹⁰)**.

Thus the hyperbola and rest circle have ordinary second-order tangency: same point and slope, different signed curvatures (+1/r versus −1/r). This alone does not give mechanical restoring stiffness.

For level-u row parabola in (X,Y), at its vertex X=−u/2,

**X_parabola(Y)=−u/2+Y²/(2u)**.

For the distinct, small radius-u/2 circle tangent there,

**X_smallcircle(Y)=−sqrt(u²/4−Y²)=−u/2+Y²/u+Y⁴/u³+...**.

The parabola and small circle also have second-order tangency (nonzero gap Y²/(2u)+...), with no implied equality of curvature.

At the outer circle crossing P_n=(u(n−1)/2,u sqrt(n)), the slopes are

**dY/dX|parabola = 1/sqrt(n)**,
**dY/dX|outercircle = −(n−1)/(2sqrt(n))**,

so their slope difference is **(n+1)/(2sqrt(n))>0** for n>0. This is a transverse intersection, not tangency. Do not insert the potential-derived oscillator turning point at this location absent a dynamical map.

## Gate 564 — EM/G scaling and physically missing clock

The u=1 sector has parabola vertex −1/2; the u=1/2 sector has vertex −1/4. Under fixed normalized n, u→u/2 scales X,T,Y and BOTH radii by one half, while s_n=(1/2)ln n and all radius/slope ratios stay unchanged. This is the exact similarity correspondence, NOT an independently selected physical gravitational frequency or force.

At fixed u and n, arbitrary monotone choices s(t)=lambda t, with lambda>0, traverse the two geometrically distinguished stations over time Δt=[ln n]/(2lambda) (for n>1) without changing any contact or intersection identity. Their accelerations and any oscillator frequency therefore remain underdetermined. The shell hyperbola is a state-space/coordinate identity until s(t), metric interpretation and dynamics are supplied; treating it as a unique physical trajectory would impose a time law.

Physical meters-per-second radii require an additional velocity calibration v_*. A geometric rest-circle radius u sqrt(n) becomes velocity R_v=v_*u sqrt(n) only by explicit dimensional map; action in J s requires a separate canonical symplectic/action integral. A velocity-circle radius is not itself an action quantum.

## Gate 565 — reproducibility and next test

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_two_circles_shell_contact_v15_896.py`, commit **45d41dfab400513e0ba20238617ba85f5d175ef9**. Local Python/SymPy PASS: exact hyperbolic parameterization and endpoint; outer-circle/parabola chord point; AM−GM radius gap; second-order rest circle/hyperbola and small circle/parabola contacts; transverse outer crossing; u=1 versus u=1/2 similarity; and arbitrary traversal-rate counterfamily. Independent Audit pending.

**Verdict:** There is an exact map between the TWO circles via distinct stations on the same fixed-product Cone shell and a dimensionless rapidity difference (1/2)ln n. The half-offset parabola uniquely meets the larger n+1 circle at the shell's divisor-pair station, while the sqrt(n) rest circle touches the shell in its different (X,T) section. These exact statements do not derive restoring stiffness, frequency, rho, G, or a physical action-clock relation.

**NEXT:** test a Hamiltonian on the shared shell coordinate s, with a kinetic metric and potential obtained from the frozen Cone+EM/gravity field model, not inferred from contact alone. Check whether stable equilibrium s=0 exists and whether any symmetry/curvature fixes Hessian V''(0)/M_eff or generates a dimensionless EM/G response ratio. Compare to unforced shell motion as a negative control.

**HANDOFF External Audit/Muse:** independently check shell-to-chord mapping, the contact expansion, orientation/convention (X,Y) vs (X,T), sector scaling and n=1, and report the no-time-selector counterfamily. Separate process issue: Audit Rounds 569/570 had flagged missing v15.888 and v15.890 standalone reproducers; still open.
