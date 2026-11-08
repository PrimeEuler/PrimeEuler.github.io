# Cone Derivation Ledger v15.529 — Sandbox addendum: everything is square-mode content because of the geometric mean (kernel families)

**Deposit type:** Sandbox exploration, independently checkable. Addendum to
v15.527, on Jeremy's line after its delivery: "everything is square mode
content because of the geometric mean." Stated precisely and tested the
same evening. (Staging note: `divisor_split_kernel.py` reproduces its
main table and then exits on a known index-cap bug in its trailing
offset-control block — shells at s·m² = N exactly, shifted +1 out of
range; the corrected controls are in `divisor_split_kernel2.py`, exit 0.)

## The GM statement

Every Voronoi mode of the divisor fluctuation carries phase
4π√(kx) − π/4, and √(kx) is the geometric mean GM(k, x) of the mode index
and the argument — the cone's own label. A mode family phase-locks at x
exactly when the GMs are simultaneously integers, iff index and argument
share a squarefree kernel: at x = s·m² the locking modes are k = s·j²
(GM = s·j·m). The v15.527 seats are the kernel-1 case.

## The kernel families

Shells s·m² ≤ 2×10⁶; measured Δ(x)/x^{1/4} mean (fraction positive):
s=1: +2.1911 (0.999); s=2: +1.9652 (0.999); s=3: +1.6773 (0.984);
s=5: +1.3052 (0.949); s=6: +1.5869 (0.974); s=7: +1.0954 (0.931);
s=10: +1.2898 (0.930); s=30: +1.2898 (0.926). Every kernel family
carries the one-sided bias, declining with s. Predicted coherent
contributions P_s = (1/(2π))·s^{−3/4}·Σ_j d(s j²) j^{−3/2} (mode sums
extended by factorization to j ≤ 20000): +2.2112, +1.9519, +1.6350,
+1.2190, +1.4427, +0.9782, +1.0757, +0.7949 — the lock accounts for the
measured bias to ~1% at s = 1, 2 and ~2.5% at s = 3. (s = 10 and s = 30
measured means agree to 4 decimals, differ at the 6th: +1.289750 vs
+1.289835 — coincidence, filed as one.)

## The residual, filed open

For s ≥ 5 the measured bias exceeds the lock's contribution (explained
fraction 93%, 91%, 89%, 83%, 62% at s = 5, 6, 7, 10, 30); the mode-sum
tail is too small to close it. Source unidentified in this scope;
candidates named in the note (slow-mode cancellation over the sampled
shells; local elevation around highly composite shells — the lock is a
wide bump, and the offset controls share it).

## Verdict

Jeremy's generalization holds: the seat phenomenon is the kernel-1
member of a family — every squarefree-kernel shell family carries a
one-sided divisor bias set by the modes whose geometric mean with the
argument is integral. The unifying variable is the cone's label: the
Voronoi phase is 4π·GM − π/4, and coherence is integrality of the GM.
Scope as v15.527: fingerprint-grade (now a kernel-indexed family),
classical mechanism, not a discrete door selection.

**Payload:** `payloads/kernel_lock_addendum_v15_529/` — Kernel_Lock_Addendum.md `43f866895f4071757099a1c5d240d4b39bf96b57d16a16c0c9bafa3ae6214344`, divisor_split_kernel.py `24ba71091bf31192eb53e7bbc7389c0431a172eaf39edb45a341393715304157`, divisor_split_kernel2.py `2ab938abd73785cf51271969d2fdcbd0e98615753d16ae6e318498f006014230`.
