# The triplet-charge build: a rotating-label configuration, and why the quantization loophole cannot be instantiated with the triplet action as deposited

Origin: the Wald discussion (2026-10-28). Charges measure coefficient x state and never
derive a coefficient -- except under QUANTIZATION, the loophole the project used once:
the dyon quarter (v14.731) is a Misner periodicity imposed on a NUT charge. This build
constructs the configuration that loophole requires for the triplet -- a stationary
configuration carrying a triplet Wald/Noether charge -- and tests whether a quantization
condition on that charge can pin kappa*C.

## The configuration

Rotating labels on the coasting background: phi^I(t, z) = R^I_J(omega t) z^J, R a rotation
about the 3-axis. Building it forces a disambiguation the record never needed (all its
label fields were time-independent):
  (R1) B = spatial strain, a^-2 F F^T -- the reading of the deposited work
       (F = deformation gradient, v14.989; B's eigenvalues the strain, v14.941);
  (R2) B = full spacetime contraction g^mn d_m phi d_n phi.

## Exact results (sympy-verified, triplet_charge.py)

(R1): B = a^-2 I exactly (R orthogonal, singular values 1), so A_B = 1/a^2: the rotation is
INVISIBLE to W and to the background stress-energy -- a degenerate background class.
The internal-rotation Noether charge density is EXACTLY ZERO: W contains no phi-dot, so the
canonical momentum vanishes and J^t = pi_I delta phi^I = 0 identically. The rotation is a
flat direction carrying a spatial flux but no charge. Nothing exists to quantize.

(R2): matched to the static normalization, A_B = 1/a^2 - omega^2 ((z1)^2 + (z2)^2)/3: the
rotation costs O(omega^2), and the charge density is a MOMENT density,
q_3 = (2C/3) omega ((z1)^2 + (z2)^2) -- proportional to C, but weighted by the squared
distance to the rotation axis. Its total over any ball scales as C * omega * R^5: omega and
R are state data, and the homogeneous cosmology has no finite total at all. A quantization
condition would pin C x (state), not C.

Finite carriers: none exist in the action as deposited. Derrick scaling for a lump,
E(lam) = lam E(1), is monotone (spreading runaway); W has no potential term, so no Q-ball;
a cut-out lump is the medium, not a soliton. A self-gravitating elastic star would still
carry profile state data absent a regularity-fixed period.

## The checklist, against the one success

Charge quantization pinned the quarter because Taub-NUT supplies all three:
  (i) a finite total charge; (ii) a period fixed by REGULARITY (Misner 8 pi n), making the
  conjugate angle compact with fixed range; (iii) a charge proportional to the target
  coefficient with everything else collapsed to pure numbers at the self-dual point.
The triplet as deposited fails all three: (i) zero (R1) or extensive (R2); (ii) no periodic
direction on the cosmology; (iii) omega, R and the profile survive as state data.

## Verdict

ROUTE CLOSED NEGATIVE. The quantization loophole is real in general -- it is how the
project's one coefficient was derived -- but it cannot be instantiated with the triplet
action as deposited. Instantiating it requires ADDING structure (a potential, a compact
label direction, a solitonic carrier): new chosen constants, the species a derivation was
meant to avoid. With v15.048 (compositeness: category failure) and the background-charge
analysis (Komar/Wald: vanishing or measuring), all three mechanism species for deriving
kappa*C are now closed with exact obstructions. The park specification is complete: any
future mechanism must arrive carrying a finite system, a regularity-fixed period, and a
charge that isolates the coefficient. kappa*C = 1 remains a matching; G_derived = false;
the Suzuki quarter remains PARKED (v14.916).

## By-products

(1) The B fork (R1 vs R2) is invisible on every deposited background (static labels) but
decides time-dependent-label physics; R1 is the reading consistent with the deposited
F/strain usage. Flagged for the gravity lane; no deposited result is affected.
(2) Under R1 the rotating-label background is stress-energy-degenerate with the static one
but is a different background for PERTURBATIONS: the v14.996 SVT certificate covers static
labels only. Flagged, not computed here.

Reproducer: triplet_charge.py (sympy; rotation algebra, both charge computations, Derrick
scaling). Claims [D] throughout; the carrier checklist is [I] as a criterion abstracted
from the v14.731 derivation.
