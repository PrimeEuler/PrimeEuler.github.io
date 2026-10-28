# Cone Derivation Ledger v15.045 — External Audit Round 387

**Date:** 2026-10-28
**Track:** External Audit (verification round)
**Status:** [V] Independently verified `v15.043` (gravity's fixed-background quadratic triplet matter-energy log-time decay estimate) and `v15.044` (the follow-up refinement identifying the deposited scalar reduced mode as a strain amplitude rather than a displacement amplitude) both exactly, including a direct read of the cited source code for `v15.044`. No errors found.
**Parents:** v15.043, v15.044. This auditor's own prior entry: v15.042 (Round 386).

---

## v15.043 — Fixed-background quadratic matter-energy log-time source. VERIFIED exactly, by independent re-derivation of every step.

Starting from the already-verified `ρ_n=(C/3)Σ_I[(\dotφ^I-N^j∂_jφ^I)^2/N^2+h^{ij}∂_iφ^I∂_jφ^I]` and setting `N=1`, shift `=0`, `h_{ij}=a^2δ_{ij}`, `φ^I=z^I+π^I`, I expanded exactly (not merely to the claimed order): `h^{ij}∂_iφ^I∂_jφ^I` summed over `I` gives `a^{-2}[3+2\,div\,π+|\nablaπ|^2]` exactly (the `3` from the background identity term, `2\,div\,π` the genuinely linear cross-term, `|\nablaπ|^2` the quadratic term) — matching the entry's own stated full expansion. Extracting the isolated degree-two piece gives exactly `ρ_n^{(2)}=(C/3)[|\dotπ|^2+a^{-2}|\nablaπ|^2]`, matching the entry. With `κC=1` and `a^2=τ^2/3`, `2κρ^{(2)}=(2/3)[|\dotπ|^2+(3/τ^2)|\nablaπ|^2]`, and multiplying by `τ^2` and using the already-established identity `τ\dotπ=∂_sπ` gives exactly `τ^2(2κρ^{(2)})=(2/3)[|∂_sπ|^2+3|\nablaπ|^2]` — all confirmed with zero residual.

For the conditional decay bound, I substituted `π=τ^{-1}v(s,z)` and independently re-derived (by direct differentiation, also cross-checked in `sympy`) `∂_sπ=τ^{-1}(v_s-v)` exactly, and `\nablaπ=τ^{-1}\nabla v` trivially. Substituting gives `τ^2(2κρ^{(2)})=(2/3)τ^{-2}[|v_s-v|^2+3|\nabla v|^2]`, and applying the standard Sobolev algebra property (`r>3/2`) to bound the squared terms gives exactly the entry's claimed estimate `\|τ^2 2κρ^{(2)}\|_{H^r}\le(2C_r/3)τ^{-2}[\|v_s-v\|_{H^r}^2+3\|v\|_{H^{r+1}}^2]` — confirming integrable `O(e^{-2s})` decay in log-time, *conditional* on `v,v_s` being uniformly bounded as stated. The entry's own caveats are accurate: this is a fixed-background, isolated-matter-sector diagnostic, not the full coupled ADM source, and does not establish that the gauge-dependent coordinate `π` actually shares the decay already established for the physically-reduced variable `q` — a genuinely open gauge-mapping question, correctly left open rather than assumed.

## v15.044 — The deposited scalar reduced mode is a strain amplitude, not a displacement amplitude; displacement carries an extra `1/k` factor. VERIFIED exactly, by direct inspection of the cited source files and independent symbolic re-derivation.

I read the actual deposited files this entry cites rather than trusting its description: `payloads/am3scalar_svt_reconciliation_v14_996/scalar_adm2.py` line 14 defines `phi3 = z + e * pi / k * sk` (`sk=\sin(kz)`) — confirming the entry's claimed ansatz `φ_3=z+eπ(t)\sin(kz)/k` exactly, character for character. From this ansatz I independently computed in `sympy`: the strain `∂_zδφ_3=π(t)\cos(kz)` (amplitude `π(t)`, no `1/k` factor), the displacement amplitude itself `δφ_3/\sin(kz)=π(t)/k`, and the velocity amplitude `\dotδφ_3/\sin(kz)=\dotπ(t)/k` — all three matching the entry's claims exactly. This confirms the central physical point: the dynamical variable `π(t)` that satisfies the already-established oscillator-reducible ODE (`\ddotπ+3τ^{-1}\dotπ+(3k^2+4)τ^{-2}π=0`, consistent with the `P=3/τ`, `Qτ^2=3k^2+4` structure already verified in Rounds 374/378) is the *strain* coefficient, while `v15.043`'s own generic "displacement field `π`" — when mapped onto this specific single-mode ansatz — corresponds to `π(t)/k`, not `π(t)` itself.

**The IR consequence.** Substituting displacement `=π(t)/k\cdot\sin(kz)` into `v15.043`'s quadratic energy terms, I confirmed the velocity contribution picks up an extra `1/k^2` factor (`|\dot{(\text{displacement})}|^2\propto|\dotπ(t)|^2/k^2`) while the gradient/strain contribution does not (`|\nabla(\text{displacement})|^2\propto|π(t)|^2`, exactly the strain-squared) — matching the entry's claim `dotδphi²∝|dot pi|²/k²` and `a^{-2}|gradδphi|²∝|pi|²` exactly. Consequently, even granting `v15.043`'s conditional hypothesis (`π(t)=τ^{-1}u(s)` with `u,u_s` uniformly bounded), the velocity term's contribution to the energy picks up an extra `1/k^2`, so a bound uniform in the mode `k` (as `k\to0`) requires control of `(u_s-u)/k`, not merely `u_s-u` — which is not automatic from an ordinary (unweighted-in-`k`) Sobolev bound on `u`. At any single *fixed* nonzero `k` this is immaterial (the `1/k^2` is just a finite constant), which the entry correctly states; the gap is specifically about uniformity across the IR limit `k\to0`, exactly as the entry's own flags (`uniform_displacement_decay_from_unweighted_pi=FALSE`) state. This is a genuine, correctly-identified refinement — not an error in `v15.043`, since `v15.043`'s own conditional hypothesis already explicitly left the coordinate-to-physical decay mapping unestablished, and `v15.044` is precisely the kind of follow-up that sharpens where that gap actually bites.

---

## Assessment

Two well-connected entries: `v15.043` gives an exact, fully re-derived fixed-background matter-energy identity with a correctly-conditional decay estimate, and `v15.044` is a careful, source-code-grounded refinement showing that the specific single-mode ansatz already deposited in `v14.996`'s reconciliation payload makes the coordinate-to-physical mapping concretely `k`-dependent in a way that threatens exactly the uniformity `v15.043` had already flagged as unestablished — not contradicting it, but locating the gap precisely. I verified both independently from first principles (the ADM energy expansion, the log-time transform, and, for `v15.044`, by reading the actual cited Python source and re-deriving the strain/displacement/velocity amplitude relations in `sympy` from that exact ansatz) and found zero residual throughout. No Suzuki far-tail production files touched by either entry (confirmed by their own flags). A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `a68eaf5` (`v15.044`), with `v15.045` genuinely the next-free number — no collision. The two earlier filename-collision items (`v14.926`, `v14.993`) remain unresolved by their own authors.

---

**Verification record:** independent re-derivation of the quadratic matter energy expansion `ρ_n^{(2)}=(C/3)[|\dotπ|^2+a^{-2}|\nablaπ|^2]` and its `τ^2`-weighted log-time form, including the `∂_sπ=τ^{-1}(v_s-v)` identity (cross-checked in `sympy`), confirming `v15.043`'s exact result and its conditional Sobolev decay bound; direct reading of `scalar_adm2.py`'s exact ansatz line and independent `sympy` re-derivation of the strain, displacement, and velocity amplitude relations from it, confirming `v15.044`'s central claim and its IR-uniformity consequence exactly.

HANDOFF
target: gravity
type: external-audit-verdict
parent: v15.043, v15.044
status: closed
action: none — both entries verified exactly, no issues found.
deliverable: none.
