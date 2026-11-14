# Cone Derivation Ledger v15.947 — Restore original Cone T(n)=D(n)+A(n) upper half-disk, using half-grid remainder of fixed-product parabola intersections

**Date:** 2026-11-13 Eastern. **Track:** Gravity/AM–GM parabola and original Paper A divisor-count geometry. **User insight:** The fixed-factor hyperbola parabola offsets `v_k=(n-k²)/(2k)`, measured modulo 1/2, underlie D(n), and T(n) stations lie in a circle geometry with outer diameter n+1. **Parents/redundancy:** Original exact formulas **already recorded** in v13.690 §7, v14.368, `papers/Companion_SieveFlow_v1.0.tex`, `payloads/divisor_split_sign_v15_527/divisor_split_sign.py`; v15.932 fixed-diameter quarter-row curvature, v15.943 fixed-product half-interleaved curvature, v15.944 *divisor-contact* restricted sums. This note **recovers the original exact identity** and sharpens its proper interpretation on the upper half-DISK versus the outer single circle. No claim that old formulas are new. Latest external Audit Round 576 **v15.945** independently confirmed v15.940–944 but found the v15.940 liveness-note numbering collision. The *additive* v15.946 restores that Gravity content at a free version; original files left untouched. **Immediately prewrite HEAD:** c181015bf80b1538cd31a10241141c0357e2c89e (v15.947 reproducer). Target absence checked. No Suzuki, Audit, Sandbox or historical artifact overwritten.

**Status:** [D] old exact divisor and harmonic identities reconstructed; [D] exact half-disk nonlinear coordinate mapping and triangular station count; [D] boundary-vs-interior correction and direct 1..300 enumerative verification; [N] no new physical gravitational Casimir equality or source selector.

## Gate 722 — return to original parabolic signed offsets, not the v15.944 restricted divisor weighting

At fixed factor hyperbola **ab=n**, row `k` has projection **v_k=X_n(k)=(n-k²)/(2k)=(n/k-k)/2**. Let `{x}=x−floor(x)` denote fractional part, including negative x, so **2(v_k mod 1/2)={n/k}** exactly. Summing over **ALL integer rows 1≤k≤n** (not merely k|n, as in a different v15.944 comparator), and setting **H_n=Σ_(k≤n)1/k**, gives

**2Σ_(k≤n)v_k=n H_n−T(n)**, **T(n)=n(n+1)/2**,
**B(n):=2Σ_(k≤n)(v_k mod 1/2)=Σ_(k≤n){n/k}**,
**D(n)=nH_n−B(n)=Σ_(k≤n)floor(n/k)**,
**A(n)=T(n)−D(n)=B(n)−2Σ v_k**.

This recovers exactly the established v13.690 formulas, rather than replacing D(n) by an unnormalized raw offset sum. The fine distinction is important: **the offset-remainder sum B alone is not D**; adding the continuous nH_n term and subtracting B produces the integer contact count. Equivalently, **k+floor(2v_k)=floor(n/k)**, and summing the left side immediately yields D(n). Every offset supplies the arithmetic floor correction where the continuous parabola meets the discrete half-grid.

## Gate 723 — nonlinear factor-pair circle map and correct meaning of T(n) upper half

Every positive integer pair (a,b) maps under the established original Cone map to

**X=(a−b)/2, Y=√(ab)≥0, R=(a+b)/2**,

obeying the exact circle equation **X²+Y²=R²**. The selected complete triangle of positive factor-pair *stations* is

**U_n={(a,b)∈Z_{≥1}²: a+b≤n+1}**.

It contains **Σ_(s=2)^(n+1)(s−1)=n(n+1)/2=T(n)** stations. Their cone images lie **inside or on the upper half-DISK** of radius (n+1)/2, including the concentric integer-diameter levels 2,3,…,n+1. These station images are generally **not ordinary integer Cartesian lattice points** in (X,Y): X is integer/half-integer and Y=√(ab). Thus one must not claim T(n) ordinary Euclidean integer points lie *on the single outer circumference*.

In contrast, **the single OUTER upper semicircle** R=(n+1)/2 is reached at a+b=n+1 and has exactly **n factor-pair stations** (for n≥1). On that outer circle, **ab≤n** holds only for **the endpoint pairs (1,n),(n,1)** (one for n=1) because with a+b=n+1 one has ab−n=(a−1)(b−1)≥0, with equality only when either factor is 1.

## Gate 724 — hyperbolic hits live entirely within the complete triangle

For every positive integer a,b, **ab≥a+b−1**, since (a−1)(b−1)≥0. Consequently **ab≤n ⇒ a+b≤n+1**, proving that **every** integer contact beneath the hyperbola lies within the n+1 half-disk station set U_n. Therefore

**D(n)=#{(a,b)∈U_n:ab≤n}**,
**A(n)=#{(a,b)∈U_n:ab>n}**,
**T(n)=D(n)+A(n)**.

This is a clean geometrical proof of the original colored upper-cone triangular count. The prime-number “hollow outer row” property follows from the two endpoint contacts, but the full D(n) includes all smaller radius circles. This original count is not the new restricted sum from v15.944, which samples only row indices dividing n and therefore counts contacts on the **single fixed-product boundary** ab=n rather than all ab≤n.

Example n=12: T=78, D=35, A=43, n outer semicircle stations=12, outer hits=2. n=30: T=465, D=111, A=354, outer stations=30, outer hits=2. No independent physical force constant enters these elementary exact arithmetic facts.

## Gate 725 — relationship to the recent quarter-grid Casimir investigations, without overclaim

The **modulo 1/2** remainder of the original X_n(k) rows is an exact integer/half-grid arithmetic quantization map, while the **interleaved k+1/2** rows of v15.943 sample a different, refined factor-index coset; their nonlinear midpoint defect is `−n/[4k(k+1)(2k+1)]`. Both are valid constructions using the same parabola formula, but they are **not the same offset statistic**. In particular the original D(n) identity is stronger for recovering the full summatory count than imposing the v15.944 weighted `nd(n)` restricted divisor-contact sum, and was known years earlier.

Likewise neither the modulo-half correction nor triangle partition alone identifies a **physical gravity quarter-grid Casimir**, a physical U1/Spin4 intertwiner, or a G-free observable. The quarter Casimir interleave `ΔC=−1/16` is a genuine *formal geometric polynomial* midpoint identity, but it does not enter the above classical D(n) proof as a necessary operator ingredient. Its potential role in a physically selected interleaved carrier remains an open hypothesis.

## Reproducibility / next discriminating gate

**Reproducer:** `research-notes/k4_T_D_A_halfdisk_parabola_recovery_v15_947.py`, additive commit **c181015bf80b1538cd31a10241141c0357e2c89e**. Exact Python `fractions.Fraction` verification of old harmonic/mod-half identities, T/D/A triangle enumeration, circle coordinate equation, boundary contact count and half-disk inclusion for **n=1..300**. Direct spot checks n=1,2,3,4,6,12,30,100,300. **External Audit pending**.

**Scientific result:** User's **global T/D circle-cone encoding** is the original exact program: floor and fractional-part corrections of the `(n-k²)/(2k)` parabolic offsets are what distinguish D(n) hits from T(n) total lattice-factor stations inside the diameter-(n+1) halfdisk. The proper interpretation is a **triangular stack of semicircles**, not T(n) stations restricted to its outer boundary. Restoring this avoids misdirection from v15.944's optional, different divisor-only sum and keeps the original 1/2-offset selector fully visible.

**NEXT:** Develop a direct row-by-row bijection from the v13.690 half-grid remainder construction to an explicitly *refined quarter-grid* coset coloring on the same U_n set, test whether it furnishes a nontrivial signed count beyond re-indexing floor functions. Distinguish integer-factor hits from half-integer interpolated points. Any claimed EM/G physical transition then needs independent source/operator normalization and a genuine dynamical observable. Handoff Audit: independently confirm the station-vs-Euclidean-point caveat, halfdisk vs boundary difference, and correction B≠D.
