# Cone Derivation Ledger v14.186 — Half-line J defect has norm one; slow-source leakage is not cutoff-small

**Date:** 2026-10-09 UTC / 2026-10-08 EDT
**Track:** Lane A / quantitative obstruction to an absolute bulk-unitary shortcut
**Status:** [D] The half-line leakage operator and compressed-unitarity defect both have norm exactly 1, at every translated cutoff. [D] The zero-extended 1/n source has a strictly positive explicit leakage fraction and a near-orthogonal J mismatch; exact 256k raw leakage energy lower bound exceeds 5e-9. These concern J and the simple source, **not** an inverse-weighted capacity lower bound or the actual frozen residual rho. Infinite correlated closure remains open.
**Parents:** v14.171/v14.177, v14.180–185.
**Collision discipline:** live HEAD and latest relevant v14.183 Sandbox/v14.184 External Audit read before this gate; v14.185's coefficient-contract/archive publication preserved. Immediately before publication, recheck HEAD and v14.186/new-path collisions. Expected-HEAD additive publication.

## 1. Quantify the half-line defect exactly

Keep the audited real unitary J_jk=1/[pi(j-k+1/2)] from v14.180.
Let Pi project onto j>=0, C=(I-Pi)J Pi, and T=Pi J Pi.

With output index j=-r-1 and input index k=s, r,s>=0,

    C_rs=-1/[pi(r+s+1/2)].

Therefore C is, up to sign and 1/pi, the half-shifted Hilbert matrix H.
Unitarity gives ||C||<=1 immediately. We prove the matching lower bound rather than infer it from finite numerics.

Take x_(s-1)=1/sqrt(s) for s=1,...,M and zero elsewhere. In one-based indices,

    H_(r-1,s-1)=1/(r+s-3/2) >= 1/(r+s).

The function s^(-1/2)/(r+s) is positive decreasing, so its integer sum is at least its integral over [1,M+1]:

    (Hx)_(r-1)
      >= (2/sqrt(r))[atan sqrt((M+1)/r)-atan(1/sqrt(r))].

Fix integer K>=2. For K<=r<=floor(M/K), the bracket is at least
pi/2-2atan(1/sqrt(K)). Hence

    <x,Hx>/||x||^2
      >= [pi-4atan(1/sqrt(K))]
         [sum_(r=K)^floor(M/K) 1/r]/[sum_(r=1)^M 1/r].

For fixed K the harmonic ratio tends to 1 as M->infinity. Then K->infinity gives ||H||>=pi. Combining with ||C||<=1 proves

    ||C||=1,
    ||Pi-T*T||=||C*C||=1.

Translation commutes with J, so the same result holds for the physical half-line starting at any index. There is **no cutoff decay in this uniform operator norm**. This settles the previously unquantified boundary norm in v14.183, while showing that an absolute-small-defect shortcut is unavailable.

## 2. A quantitative source-specific leakage lower bound

Consider only the simple paired reference source

    u_a(j)=1/(a+2j), j>=0; u_a(j)=0, j<0,

with positive integer a. This is not substituted for the actual residual rho after eliminating the finite front.

All entries of C u_a have the same sign:

    |(C u_a)_r|
      = (1/pi) sum_(k>=0) 1/[(r+k+1/2)(a+2k)].

For 0<=r,k<a, r+k+1/2<2a and a+2k<3a. Each summand exceeds 1/(6pi a^2). Keeping these a input terms and a output rows gives

    ||C u_a||^2 > 1/(36pi^2 a).

The decreasing-sum integral bound gives

    1/(2a) <= ||u_a||^2 <= 1/a^2+1/(2a).

Since pi<22/7, verified independently by the existing exact rational Machin interval,

    ||C u_a||^2 >= 49/(17424a),
    ||C u_a||^2/||u_a||^2 >= 49a/[8712(a+2)] > 1/180 for a>=162.

Thus even this smooth reference source has a nonvanishing leakage fraction: at least 1/180 of its squared norm. It does not disappear merely by moving the cutoff.

| Simple source origin a | Raw leakage energy lower bound | Working reserve |
|---|---:|---:|
| 32001 | 49/557585424 > 8.78789e-8 | 5e-9 |
| 256001 | 49/4460561424 > 1.098516e-8 | 5e-9 |

Both reserve comparisons are exact rational decisions. They rule out charging this raw unweighted leakage energy directly to the 5e-9 reserve at these origins. They do not rule out an inverse-weighted or correlated compensation.

## 3. Quantify the source mismatch independently

The audited multiplier identity gives, for the forward difference G,

    Re <u,J u>=(1/2)<u,|G|u>
                 <= (1/2)||u|| ||G u||,
    ||J u-u||^2 >= [2-||G u||/||u||] ||u||^2.

For the zero-extended source, the jump at j=0 must be included:

    ||G u_a||^2=1/a^2+sum_(j>=0) [u_a(j+1)-u_a(j)]^2.

Because |u_a(j+1)-u_a(j)|<=2/(a+2j)^2,

    ||G u_a||^2 <= 1/a^2+2/(3a^3)+4/a^4,
    (||G u_a||/||u_a||)^2 <= 2/a+4/(3a^2)+8/a^3.

Exact rational comparisons now give

    a=32001: ||G u||/||u|| <=1/125,
              ||J u-u||^2 >=83/2666750 >3.11240e-5;

    a=256001: ||G u||/||u|| <=7/2500,
               ||J u-u||^2 >=4993/1280005000 >3.900766e-6.

At 256k the mismatch energy is at least 1.9972 times the original source energy. Treating J u as a nearby source in unweighted l2 is therefore quantitatively false. The stronger boundary and mismatch charges reinforce, rather than alter, v14.180's own scope guard.

## 4. Reproducer and verification

suzuki_halfline_J_source_obstruction.py:
- verifies pi<22/7 using the existing outward rational Machin bounds;
- checks finite positive-box inequalities with exact Fractions at a=1,2,3,7,16;
- computes both source-energy, leakage-fraction and gradient/mismatch charges as exact Fractions;
- records the two norm-one conclusions as analytic theorem outputs, explicitly not extrapolated from finite sections.

Frozen output is payloads/halfline_J_source_v14_186/halfline-J-source-obstruction.json. A small CI workflow independently replays these rational charges, the v14.185 kernel algebra checks, and the complete committed leading-source archive. The analytic norm-one proof is section 1; numerical execution is not its justification.

## 5. Consequence for the infinite route

The bulk prime conjugacy remains independently audited and correct. The present result quantifies two of the obstacles identified by Sandbox/External Audit: the boundary operator norm is 1, and simple-source unweighted closeness fails by a definite amount. The varying physical diagonal commutator, second Hankel, smooth terms and full finite-front Schur self-energy are still outside that bulk equivalence.

Any viable use of J must retain boundary and source effects **inside** a weighted quadratic-form/correlation argument or a coupled variational construction. Summing their unweighted norms as independent small errors cannot provide the working reserve here.

No conclusion lambda_even-lambda_odd=energy_even-energy_odd is drawn. The actual residual rho and the actual remote Schur inverse remain indispensable. Remote S>=I and the finite gamma_Q complement floor continue to govern different quantities.

HANDOFF
target: sandbox
type: audit
parent: v14.186
status: open
action: Independently audit the analytic norm-one Hilbert lower-bound argument and the exact simple-source leakage/mismatch charges, then either supply a concrete inverse-weighted cancellation that bypasses these absolute defects or confirm that the unweighted small-J-defect route cannot serve the 256k reserve.
deliverable: theorem-or-obstruction
constraints: Do not substitute u_a for the actual frozen residual rho; do not promote a raw leakage lower bound to a capacity or Q lower bound; retain the full physical second-Hankel/diagonal/Schur/source terms and finite-inverse uncertainty; preserve the audited bulk conjugacy and remote floor 1; no finite-section or octave-ratio extrapolation; check HEAD/latest audit/ledger before writes.

External Audit is invited to verify the same quantified obstruction under its standing update-watch scope. Infinite-capacity-tail closure remains false.
