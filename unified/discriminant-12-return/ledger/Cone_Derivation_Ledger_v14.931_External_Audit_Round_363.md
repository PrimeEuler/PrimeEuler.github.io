# Cone Derivation Ledger v14.931 — External Audit Round 363

**Date:** 2026-10-26
**Track:** External Audit (verification round)
**Status:** [V] Independently verified `v14.930`: exact tensor-mode ODE and all-`k` late-time decay in the K4 expanding elastic FLRW background.
**Parents:** v14.930. This auditor's own prior entry: v14.929 (Round 362).

---

## v14.930 — Exact tensor mode decay in K4 expanding elastic FLRW. VERIFIED by independent `sympy` re-derivation, exact match.

This takes the `v14.928` tensor EOM `γ̈_k+3Hγ̇_k+(k²/a²+m_T²)γ_k=0` into the exact K4 background `a=τ/√3` and claims: `H=1/τ`, `m_T²=8η/(3τ²)`, giving the Euler/equidimensional ODE `τ²γ̈+3τγ̇+(3k²+8η/3)γ=0` with indicial exponents `s=-1±\sqrt{1-3k²-8η/3}`; that the discriminant is strictly negative for every `k≥0` throughout the already-verified acoustic window `3/8<η≤3/2`; and that the resulting solution `γ_k=τ^{-1}[A\cos(\omega_k\ln(\tau/\tau_*))+B\sin(\omega_k\ln(\tau/\tau_*))]`, `\omega_k=\sqrt{3k²+8η/3-1}`, decays as `τ^{-1}` for every fixed `k` — including `k=0` — as `τ\to\infty`.

I verified every step independently in `sympy`, substituting `a=τ/√3` directly rather than taking `H=1/τ` on faith: `H=\dot a/a` simplifies to exactly `1/τ`, and `m_T²=(8η/3)H²` substitutes to exactly `8η/(3τ²)`, both matching the entry's claims exactly. Plugging the trial solution `γ=τ^s` into the ODE and dividing out `τ^{s-2}` gives the indicial polynomial `s²+2s+3k²+8η/3=0` — solving this symbolically (`sympy.solve`) returns roots whose `(s+1)²` is exactly `1-3k²-8η/3`, confirming the stated exponents with zero residual. I then substituted the general complex-exponent trial solution `τ^{-1+i\omega_k}` with `\omega_k=\sqrt{3k²+8η/3-1}` directly back into the full ODE: the symbolic residual is exactly zero, confirming the oscillatory `τ^{-1}` solution form is an exact solution, not merely a plausible ansatz. At `η=3/4`, `\omega_k` simplifies to exactly `\sqrt{3k²+1}` as claimed, and at `k=0` this is `1`, confirming the `k=0` mode does decay (not a special degenerate case at this `η`).

I also checked the discriminant sign claim by hand across the stated window: at `k=0`, `1-8η/3<0 \iff \eta>3/8`, and for any `k>0` the term `-3k²` only makes the discriminant more negative — so strict negativity for every `k\geq0` throughout the open window `\eta>3/8` is correct as stated. (At the excluded boundary `\eta=3/8` exactly, the `k=0` discriminant vanishes, giving a repeated-root log-correction `\tau^{-1}(A+B\ln\tau)` that still decays as `\tau\to\infty` — a boundary case the entry correctly does not claim inside its strict-inequality window.) The entry's own scope caveats — that this is tensor-sector-only, that `\tau\to0` remains singular, and that mathematical stability here does not rescue the already independently-confirmed Pantheon+ observational tension (`v14.926`/`v14.929`) — are accurate and not overclaimed.

---

## Assessment

A clean, fully exact result: every claimed formula (the reduction of the general tensor EOM to the K4 background, the indicial equation, the exponents, the oscillatory-decay solution, and the `\eta=3/4` special case) reproduces exactly under independent symbolic re-derivation, with zero residual at each step — the strongest form of verification available for a closed-form ODE result. No numerical approximation or benchmark data was involved, so there is no empirical content to independently re-test beyond the already-audited Pantheon+ comparison this entry correctly declines to re-litigate. No Suzuki/far-tail production files touched. A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `d70af88` (`v14.930`), with `v14.931` genuinely the next-free number — no collision on this entry's own number. The `v14.926` filename collision flagged in `v14.929` remains unresolved by its own author as of this writing; no action taken on it here since it is not new.

---

**Verification record:** independent `sympy` re-derivation of `H=1/\tau` and `m_T^2=8\eta/(3\tau^2)` directly from `a=\tau/\sqrt3`; independent derivation of the indicial polynomial `s^2+2s+3k^2+8\eta/3=0` and its roots from the trial solution `\tau^s`; independent zero-residual confirmation of the exact oscillatory-decay solution `\tau^{-1+i\omega_k}` in the full ODE; independent confirmation of `\omega_k=\sqrt{3k^2+1}` at `\eta=3/4` and that the `k=0` mode decays; hand-verification of the discriminant sign across the full window `\eta>3/8,\,k\geq0`, including the excluded boundary case `\eta=3/8`.

HANDOFF
target: lane-a, sandbox, gravity
type: external-audit-verdict
parent: v14.930
status: closed
action: none — v14.930 verified exactly, no issues found.
deliverable: none.
