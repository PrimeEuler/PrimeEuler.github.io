# Cone Derivation Ledger v15.648 — Suzuki radius-16: exact nonbipartite field and required two-sided spectral control

**Date:** 2026-11-10 (America/New_York). **Track:** Lane A, *original Suzuki five-frequency commutator only*. **Parents:** v15.420, v15.497–502, v15.643–645. **Status:** [D] exact physical signed-shift three-cycle obstruction to diagonal chiral/sign symmetry, [N] a separately scoped negative-edge eigensolver resource limit; [O] rigorous two-sided uniform radius-16 spectral norm upper bound.

## Fresh live-HEAD and version check

Live master before writing: `f53d31127874801ccbb94a7bdaaa72cdb5d4a165`. A parallel gravity lane used ledger version **v15.647** at commit `671d4f95cb16`, while this Suzuki witness was being prepared. The witness was deposited at the nonconflicting path `research-notes/lane_a_v15_647_triangle_chiral_obstruction.py` (commit `f53d31127874801ccbb94a7bdaaa72cdb5d4a165`); its filename is a witness label and **not** a claim on the already-used v15.647 ledger version. This substantive Suzuki entry therefore uses next-free **v15.648**. No existing file or certified data was overwritten.

## Exact three-cycle in the physical signed matrix field

Recall the v15.420 coefficient of shift `g=t v_r-s v_q` is `s*t*alpha_q*alpha_r*G_{s,t}^{qr}(x+h·L)` for matrix row h and column h-g in the faithful `Z^4` regular representation. Let `e_2,e_3,e_5,e_7` denote the four independent lattice basis directions. For `(s,t)=(-1,+1)`, use the three shifts

`g_23=e_3+e_2,` `g_35=e_5+e_3,` `g_25=e_5+e_2`.

**Correction of sign convention:** the actual v15.420 label is `t v_r-s v_q`, so all signs in these vectors are plus. These three shifts do **not** form a triangle (`g_23+g_35 != g_25`). The naive earlier exploratory candidate `e_r-e_q` would require `(s,t)=(+1,+1)`, not `(-1,+1)`. Hence the deposited v15.647-named witness, which tested nonzero coefficients for `(-1,+1)` while describing `e_r-e_q` label edges, is **NOT** a valid proof of a physical three-cycle. Its arithmetic word evaluations are independent observations, but its graph conclusion must not be used.

**Rigorous combinatorial repair:** use the physical `(s,t)=(+1,+1)` shifts `g_{qr}=e_r-e_q`, for pairs `(2,3),(3,5),(2,5)`. Then `g_{23}+g_{35}=g_{25}`, so with vertices `h_0=0,h_1=g_{23},h_2=g_{25}` all lie in `F_R` for `R>=1`, and the three displacement labels are correct. To promote this to a **physical nonzero-edge triangle**, it remains necessary to check the exact signed coefficients `G_{+,+}^{23}(x+h_1·L)`, `G_{+,+}^{35}(x+h_2·L)`, `G_{+,+}^{25}(x+h_2·L)` at one common x, with the source-faithful normalization. A positive calculation on the *incorrect* sign tuple does not discharge that requirement.

## Separate resource finding [N]

Using the correct physically signed v15.644 sparse radius-16 field at `x=0.12345`, the largest algebraic eigenvalue probe converged again at `3.7970813095` with binary64 eigen-residual about `3.09e-5`. A standalone smallest-algebraic-eigenvalue attempt did not finish within a roughly 200-second process timeout. This is an implementation/resource obstacle, not a statement about the value of the negative spectral edge, convergence impossibility, or symmetry.

## Decision and next gate

The suspected nonbipartite obstruction is **provisional only** until the correct `(+1,+1)` physical coefficients are certified on the common triangle. The general graph-theoretic implication is valid conditionally: a finite Hermitian matrix containing three nonzero edges on a triangle cannot admit a diagonal unitary sign involution `Gamma` with `Gamma B Gamma=-B`, since the three edge equations multiply to `1=-1`. It does not exclude a *non-diagonal* spectral symmetry.

Next immediate gate: re-evaluate the three `(+1,+1)` coefficients exactly, deposit a **corrected additive witness** if they are nonzero at a common x, and then proceed toward independently verified bounds on both ends of `B_{16}(x)` uniform in x. Do not infer `||B_{16}||` from the positive eigen-probe or from an invalid triangle. Existing v15.645 corrected coefficient-localization penalty `E_{16}<0.142` remains independently audit-pending, and `C_{16}<4.10` remains unproved.

No new seed or physical Suzuki map, complete far-tail, or full-K claim. Preserve `C_{S,32000}`, `3e-5`, `.002`, original v14.405/406 scoped PASS, v14.814 downstream FAIL, and once-only charges.
