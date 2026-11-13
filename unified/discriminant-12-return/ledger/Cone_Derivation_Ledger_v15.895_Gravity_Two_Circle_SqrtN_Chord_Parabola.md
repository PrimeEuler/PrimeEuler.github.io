# Cone Derivation Ledger v15.895 — Gravity: two-circle sqrt(n) chord and unit-parabola intersection

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** v13.177 parabola/anti-diagonal tangency, v14.367 diameter–secant, v15.605 secant scaling, Sandbox tangency chain v15.864, and v15.890–892 phase-space experiments. **Master HEAD verified immediately before write:** 177903b1222a6b7c722f27b8dd32b5a29ee16b82. New target checked absent; additive-only, no changes to frozen/Suzuki/Audit/Sandbox content. v15.894 has corrected the earlier Gravity-v15.889 collision additively.

**User clarification:** There are *two distinct circles*: the sqrt(n) circle tangent to the sqrt(n) rest-shell hyperbola, and the n+1 diameter–secant circle whose 1/2-offset unit parabola meets it at the sqrt(n) chord. Do not replace these geometric objects with the separate toy oscillator energy circle.

## Gate 559 — exact larger-circle parabola intersection

For the divisor pair (n,1), n>0, the diameter–secant circle in the flat (X,Y) plane is

C_out: X²+Y²=[(n+1)/2]².

Its secant foot is X=(n−1)/2, chord half-height Y=sqrt(n), because [(n+1)/2]²−[(n−1)/2]²=n exactly. The unit-factor row parabola is

P_1: Y²=1+2X,

which has Euclidean vertex (−1/2,0), giving the relevant half-unit offset. At the secant foot, 1+2[(n−1)/2]=n, so the point

**P_n=((n−1)/2, sqrt(n))**

lies simultaneously on the larger circle and parabola (and so does its reflected negative-Y point). Exact substitution of P_1 into C_out gives (X+1)²=[(n+1)/2]². The second possible X=−(n+3)/2 yields negative Y² for n>0, hence no additional real point. Thus the two physically used upper branches intersect exactly at the sqrt(n) chord endpoint.

They do NOT generally touch tangentially: at P_n, parabola slope dY/dX=1/sqrt(n), circle slope dY/dX=−(n−1)/(2sqrt(n)); their difference is (n+1)/(2sqrt(n))>0. Their gradients have nonzero determinant −2(n+1)sqrt(n). The meeting is transverse for all n>0.

## Gate 560 — the distinct sqrt(n) circle and shell tangency

The fixed-product shell xy=n maps to T²−X²=n and its rest vertex (X,T)=(0,sqrt(n)). In the auxiliary Euclidean (X,T) shell-section, the radius-sqrt(n) circle

C_rest: X²+T²=n

is tangent to the shell at (0,sqrt(n)): the gradients (2X,2T) and (−2X,2T) coincide there. In flat Cone (X,Y), the fixed-T=sqrt(n) circle likewise is X²+Y²=n, with top point (0,sqrt(n)); the line Y=sqrt(n) is tangent to that fixed-T circle there (v13.177).

Crucial section/convention warning: the action-shell hyperbola and its tangent Euclidean circle are shown in the (X,T) section, whereas the n+1 outer circle and factor-1 parabola are in (X,Y). The two circle radii are R_rest=sqrt(n) and R_out=(n+1)/2, with difference

**R_out−R_rest=[(sqrt(n)−1)²]/2 >= 0**,

equal only at n=1. This is exact AM–GM, but the two circles generally do NOT meet as plane curves if simply drawn concentrically in the flat section, and the outer parabola–circle intersection is not the same as shell tangency. Shared sqrt(n) is a geometric invariant and the common bridge across sections, not a proved single spacetime contact event.

## Gate 561 — three contacts, not one inferred force

The level-1 parabola P_1 is tangent to the SMALL half-scale circle C_(1/2) at its vertex (−1/2,0) (the separate v13.177 theorem). Meanwhile P_1 crosses C_out at P_n, and C_rest touches its shell hyperbola in a different plane. Thus at least three relations are in play: (a) parabola–small-half-circle tangency, (b) parabola–outer-n+1-circle crossing at sqrt(n), (c) sqrt(n)-circle–shell tangency.

The preceding gravity-lane toy oscillator's encoded velocity-energy circle R_v(E)=sqrt(2E/m) is a fourth object, and it must NOT silently be identified with either geometric circle. Giving a sqrt(n) radius physical units m/s requires an independent velocity normalization v_*, and converting circle motion into acceleration requires physical time evolution. None of these three contact identities independently supplies a restoring stiffness, mass normalization, oscillation frequency, G or the rho selector.

**Reproducer:** elementary exact algebra rechecked locally in SymPy for n>0: the AM–GM radius identity, P_1 chord endpoint, and nonzero gradient determinant. No external solver or physical measurement is invoked. Independent Audit pending.

**NEXT:** construct an explicit coordinate-map diagram between the (X,Y) outer-circle/parabola crossing and (X,T) shell-circle tangency, identify which 1/2 and 1/4 parabola levels can be mapped by sector scaling, and compute contact orders *without* superimposing distinct coordinate sections. Only then test dynamics from the frozen action instead of inserting a potential.

**HANDOFF Audit/Muse:** independently verify all circle radii, parabola intersections and tangency-vs-crossing classification; check conventions for (X,Y) vs (X,T), plus n=1 degeneracy and dimensions. Preserve the existing negative physical-selector verdicts.
