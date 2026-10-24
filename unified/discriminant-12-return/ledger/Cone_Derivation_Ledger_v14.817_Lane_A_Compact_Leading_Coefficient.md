# Cone Derivation Ledger v14.817 — Lane A: exact compact far 1/n coefficient and seed cancellation target

**Date:** 2026-10-24. **Lane:** A / Suzuki. **Parents:** v14.812-S, v14.814–816 and the unchanged compact kernels in `research-notes/suzuki_gap_extended_compact_action.py`, `suzuki_compact_component_rectangle.py`, `suzuki_direct_middle_compact_action.py`, `suzuki_certified_remote_z.py`. **Status:** [D] compact finite-support leading-term derivation; [O] noncompact seed coefficient and resulting exact cancellation. No physical residual gate promoted.

**Collision check:** immediately before this additive write, live master HEAD `d87057b0279d676d7b6827213b0a903d951fcf0a` (v14.816), and v14.817 was next free.

## Exact off-support compact kernel

For output physical mode `n=2i+start` and input physical mode `m_j=2j+start` in a *fixed finite* compact-support trial `x=(x_j)`, the original direct-row verification in the pinned compact producer gives the non-diagonal physical kernel

`C(n) = sum_j c * ( z(n)*m_j - n*z(m_j) ) * x_j / (n^2 - m_j^2) + alpha * p(n) * P,`

where `p(n)=L*n/(n^2+t)` and `P` is the already-defined **single full compact pole pairing**, including all current components. This is the exact real-coefficient formula whose dyadic approximation the producers compute. It applies for `n` beyond *all* finite input modes: in particular no diagonal/self compensation is needed in the asymptotic region. The five-component changed trial must be used rather than the old four-component v14.452 trial.

Define the compact z-moment `M_z=sum_j z(m_j)*x_j`. Each input support and coefficient is fixed for the current frozen trial. The certified physical remote-z representation is a finite sum of bounded sinusoidal terms plus bounded nonprime part, hence `z(n)=O(1)` as `n→∞` (its asymptotic expansion also has O(1/n) corrections); `p(n)=L/n+O(n^-3)`. Expanding each finite denominator gives

`C(n) = (-c*M_z + alpha*L*P)/n + O(n^-2)`.

Therefore **the compact leading coefficient is determined exactly by only two aggregate functionals**,

`c_inf = -c*M_z + alpha*L*P.`

This is a coefficient identity, **not a numerical evaluation** of `M_z` or `P` for the v14.543/v14.500 five-component frozen trial. In particular output-z oscillations do not prevent the compact leading limit from existing, because their kernel contribution is O(n^-2). The finite support is crucial: this argument cannot be extended termwise to the infinite seed without a summability or uniform-tail justification.

## Reduced exact cancellation constraint

With the original bare source `1/n` (odd sector `1/(m-1)` in the producer's physical-index convention) and the noncompact seed action `S(n)`, if its leading coefficient `s_inf=lim n*S(n)` exists in the correct parity variable, the leading far residual vanishes iff

`1 + c*M_z - alpha*L*P - s_inf = 0`.

Equivalently, `s_inf = 1 + c*M_z - alpha*L*P`. This is the **actual target for the noncompact seed analysis**. It refines v14.816's `c_inf+s_inf=1` by eliminating the compact unknown. It does *not* assert the frozen trial satisfies that target. The measured 0.16–0.18 block residual means are empirical evidence of a mismatch on F1/F2, not an asymptotic coefficient proof.

## Necessary remaining work

1. From the frozen noncompact far-seed producer and its affine `W_0` construction, identify exactly the seed-channel terms contributing to `lim n*S(n)`, proving convergence and the error remainder uniformly in both parity sectors. Never assume termwise limits of an infinite sum.
2. Evaluate/bound the two frozen compact functionals `M_z` and `P` from their **current five-component** hash-pinned inputs, with both front fresh lift and direct-middle delta. Check the pole normalization (`alpha`, `L`) against the original producer, not a guessed constant.
3. Compare the certified seed coefficient to the required `1+c*M_z-alpha*L*P`. If it differs, derive an admissible correction and analyze its impact on all already-certified finite/DM gates before any far rerun.
4. Prefer explicit remainder inequalities to extrapolation from F1/F2 means. The frozen candidate **already fails** the finite-far budget unconditionally (External Audit R345).

**Scope:** All thresholds, original `C_S_32000`, original certificates, charge-once rules, and support partitions remain untouched. No F3 or whole-residual/stationary/capacity certification.

HANDOFF
target: lane-a seed-asymptotics / external-audit
type: compact-leading-coefficient-derivation
parent: v14.817
status: compact algebra CLOSED; seed coefficient OPEN
action: independently check the finite-support kernel expansion and derive the actual noncompact seed 1/n coefficient from its frozen producer with rigorous interchange/remainder control; compare against s_inf=1+c*M_z-alpha*L*P.
