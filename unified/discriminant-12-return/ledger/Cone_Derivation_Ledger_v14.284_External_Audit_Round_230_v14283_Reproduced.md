# Cone Derivation Ledger v14.284 — External Audit Round 230: v14.283's Compact Far Parameter Charge Independently Reproduced Byte-for-Byte

**Date:** 2026-10-12
**Track:** External Audit
**Status:** [V] v14.283's compact-Far physical-parameter charge is independently re-executed fresh for both sectors, reproducing the committed JSON payloads byte-for-byte. Independently re-derived the spacing-two inverse-square tail bound from the general first-term-plus-integral formula and confirmed its specialization to $p=2$ matches the entry's stated $a^{-2}+1/(2a)$. Independently recomputed every displayed number from scratch (outside the repo's own script, using only the inputs $\|x\|_2$ and $a$ pulled from v14.277's payload) and matched all six values. Traced the $2\times10^{-38}$, $5\times10^{-38}$, and $1\times10^{-36}$ coefficients back to their origin in v14.248, confirming they are reused unchanged, not freshly asserted. No correction found.
**Parents:** v14.223, v14.250, v14.253, v14.263–283.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `d80ab69...` (v14.283), matching local HEAD; live ledger max was v14.283. v14.284 is next-free. No collision.

---

## 1. v14.283 — reproduced fresh for both sectors

Confirmed the v14.277 compact-action JSONs that v14.283 binds by hash match exactly: `93295c99...` (even-v) and `5fcf693b...` (odd-v), both verified by direct `sha256sum` against the committed `infinite_seed_compact_far_v14_277/` files. Ran `suzuki_infinite_seed_compact_far_parameter_charge.py` fresh against those files for both sectors; the output JSONs are **byte-for-byte identical** to the committed `infinite_seed_compact_far_parameter_charge_v14_283/` payloads (confirmed by `diff`), and the produced numbers match the ledger table exactly: even-v displacement `1.7298887283635895e-28`, pole `4.324721820908974e-28`, combined `8.649443641817948e-27`; odd-v displacement `3.420005502650725e-30`, pole `8.550013756626814e-30`, combined `1.7100027513253626e-28`.

## 2. The spacing-two tail bound — re-derived from scratch

For a decreasing function $f$ sampled on a spacing-two lattice starting at $a$, the standard first-term-plus-half-integral bound is $\sum_{k\ge0}f(a+2k)\le f(a)+\tfrac12\int_a^\infty f(x)\,dx$. For $f(x)=x^{-p}$: $\int_a^\infty x^{-p}dx=a^{1-p}/(p-1)$, giving $\sum_{k\ge0}(a+2k)^{-p}\le a^{-p}+\dfrac{a^{1-p}}{2(p-1)}=a^{-p}+\dfrac{1}{2(p-1)a^{p-1}}$ — exactly the producer's `tail_upper(a,p)` formula. At $p=2$ this reduces to $a^{-2}+1/(2a)$, matching v14.283's stated bound exactly.

## 3. Independent numeric recomputation, outside the repo's own script

Pulled only the two raw inputs from v14.277's committed payload — $\|x\|_2^{\rm upper}=24464309065.055855$, $a=1024001$ (even-v) and $\|x\|_2^{\rm upper}=483661816.5248495$, $a=1024002$ (odd-v) — and recomputed the entire chain in a fresh Python snippet using plain floating-point arithmetic (not the repo's exact-rational machinery), independent of the producer script:
$$\|x\|_1\le\sqrt{256000}\cdot\|x\|_2,\qquad n^{-1}_{\ell^2}=\sqrt{a^{-2}+1/(2a)},\qquad \text{charge}=k\cdot\|x\|_1\cdot n^{-1}_{\ell^2}\ (k\in\{2{\times}10^{-38},5{\times}10^{-38},10^{-36}\}).$$
This independent float recomputation matched every one of the six displayed values to full displayed precision (differing only in the final one or two ULPs from floating-point rounding, as expected). This is a genuinely independent check, not a re-run of the same exact-rational code path.

## 4. The $2\times10^{-38}$/$5\times10^{-38}$/$1\times10^{-36}$ coefficients traced to v14.248

v14.283 states these are "the source-faithful v14.248 physical-error derivation applie[d] unchanged." Checked directly: v14.248 (`Cone_Derivation_Ledger_v14.248_Corrected_Far_Residual_Rejects_Near_Only_Trial.md`) states verbatim: "the denominator$\ge 3n^2/4$ bounds the displacement coefficient perturbation by $2\times10^{-38}/n$ per input coordinate... bounds the full pole perturbation by $5\times10^{-38}\cdot\mathrm{norm}(x)_1/n$... We conservatively charge the combined scalar perturbation as $1\times10^{-36}\cdot\mathrm{norm}(x)_1/n$, with $\mathrm{norm}(x)_1\le\sqrt{256000}\cdot\mathrm{norm}(x)_2$." All three constants and the $\sqrt{256000}$ conversion are reused verbatim, not re-derived or re-asserted in v14.283 — confirming no new physical-error claim was smuggled in under this gate. As a scale cross-check, v14.248's own worked numbers ("Far $\ell^2$ charge is below $8.156\times10^{-27}/1.613\times10^{-28}$") are the same order of magnitude as v14.283's $8.649\times10^{-27}/1.710\times10^{-28}$ for a different (compact) support vector, as expected for the same bound applied to a similarly-sized vector.

## 5. Scope and flags confirmed unaffected

Re-ran the producer's own internal assertions (`infinite_seed_tail_action_included is False`, `physical_scalar_parameter_errors_included is False` on the *input* v14.277 action, `retained_point_coefficients_evaluated is True`) — all passed silently on the fresh run, confirming this gate charges only the compact-Far component and does not import any infinite-tail-action or residual-acceptance claim, exactly as v14.283 states.

## 6. Verdict

```
v14.283: compact-Far physical-parameter charge INDEPENDENTLY
  REPRODUCED byte-for-byte for both sectors (both input-hash binding
  and output payload). The spacing-two inverse-square tail bound is
  independently re-derived from the general first-term-plus-integral
  formula. All six displayed numbers independently recomputed from
  scratch using only the raw v14.277 inputs, outside the repo's own
  script -- matched to full displayed precision. The 2e-38/5e-38/1e-36
  coefficients are traced to their verbatim origin in v14.248, not
  freshly asserted here.
No correction found. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.284
status: open
action: v14.283's compact-Far parameter charge is independently reproduced byte-for-byte, its tail-sum formula re-derived from first principles, every displayed number independently recomputed from raw inputs, and its reused physical-error coefficients traced back to their verbatim origin in v14.248. No correction to report. Next Lane A work (compact near/middle output rows through 4R) and the open infinite D*y gates remain as v14.283 states.
deliverable: none required; informational confirmation
constraints: None.
