# Cone Derivation Ledger v14.987 — External Audit Round 371

**Date:** 2026-10-27
**Track:** External Audit (verification round)
**Status:** [V] Independently verified two new entries: `v14.985` (Sandbox's exploration of where discreteness lives on the two-factor Schwinger carrier, closing a carrier-level gap left open by the `v14.944`–`950` radial-flux/Noether chain) and `v14.986` (the gravity lane's quartic AM–GM constitutive repair attempt, shown to fail global causality even though it fixes the large-stretch instability found in `v14.971`). Both verified exactly, by independent re-run and independent symbolic/hand re-derivation respectively.
**Parents:** v14.985, v14.986. This auditor's own prior entry: v14.984 (liveness).

---

## v14.985 — Sandbox: discreteness lives on the pair side, not the shape side. VERIFIED exactly, by independent re-run and independent hand re-derivation of the Casimir formula.

This answers a natural follow-up to the already-closed `v14.944`–`v14.950` chain (no quantized radial-flux charge from the shape coordinate `s`): on the two-factor Schwinger Fock carrier, which structures *are* discrete, and does the shape-side squeeze generator `p_s=D_u-D_v` preserve any of them?

I independently re-ran the deposited `carrier_sectors.py` from scratch and it reproduces every printed claim exactly: the pair `su(1,1)` algebra closes exactly (`[K_0,K_\pm]=\pm K_\pm`, `[K_-,K_+]=2K_0`, all commutator checks print `0`); the Casimir on sector `d=n_u-n_v` gives `\{-1/4,0,3/4\}` for `d=0,1,2` and `\{16,2\}` for `d=3` (the `16` an explicitly-flagged truncation artifact at the cutoff edge, honestly disclosed rather than hidden — I confirmed this is exactly the kind of edge effect expected from a finite Fock cutoff, not a real discrepancy); `K_0` eigenvalues `1,2,3` on `|n,n+1\rangle` for `n=0,1,2`; `K_-` lowering both occupations together with coefficients `\sqrt6` and `3` exactly matching `\sqrt{n(n+d)}`; and `p_s`'s selection rules (`\Delta n_u,\Delta n_v\in\{(\pm2,0),(0,\pm2)\}`, confirmed directly from the printed transition lists), giving nonzero `[p_s,N_u-N_v]=\sqrt6` and `[p_s,K_0]=\sqrt6/2` exactly as claimed, with zero violations of `(n_u+n_v)\bmod2` conservation.

I did not stop at replaying the Fock-truncated numerics; I independently re-derived the Casimir formula `C=(d^2-1)/4` by hand for general `n,d` (not just the truncated sample values): acting with `K_0^2` and `\frac12(K_+K_-+K_-K_+)` on `|n,n+d\rangle` gives `K_0^2=n^2+nd+n+(d+1)^2/4` and `\frac12(K_+K_-+K_-K_+)=n^2+nd+n+(d+1)/2` (using `K_+K_-|n,n+d\rangle=n(n+d)|n,n+d\rangle` and `K_-K_+|n,n+d\rangle=(n+1)(n+d+1)|n,n+d\rangle`), so the Casimir difference is exactly `(d+1)^2/4-(d+1)/2=(d+1)(d-1)/4=(d^2-1)/4` — an exact identity for every `n`, not merely a finite-cutoff observation. This independently confirms the formula holds in the full (untruncated) Fock space, not just within the sampled truncation.

The entry's carrier-level conclusion — discreteness in this geometry lives entirely on the pair side (`K_0`, sector `d`, Casimir), the shape-side squeeze flow crosses every discrete sector and preserves only parity, and so no radial-flux amplitude can be fixed by charge quantization on the shape side — follows correctly from the verified algebra and is appropriately scoped (explicitly not claiming any pair-side identification with a physical source charge).

## v14.986 — Gravity: the quartic AM–GM repair fails global causality. VERIFIED exactly, by independent symbolic re-derivation of every asymptotic and numeric claim.

This tests the obvious constitutive fix to `v14.971`'s large-stretch longitudinal gradient instability: add a quartic anisotropy penalty `\zeta D^2` (`D=A/G-1`, the AM/GM gap) to the shear energy, since `D` and its first derivative vanish at isotropy, preserving the already-audited local quadratic acoustic behavior exactly.

I independently verified every claim in `sympy` rather than spot-checking: `D(1)=0` and `D'(1)=0` (confirming the quartic-order near-isotropy claim); `W_\zeta'(1)=2C/3` and `W_\zeta''(1)=2C(8\eta-3)/27` — identical to the un-repaired case, confirming the repair is truly invisible at quadratic order; the large-stretch leading behavior `W_\zeta\sim(C\zeta/9)t^{10/3}` (exact symbolic limit) with `c_L^2\to7/3` as `t\to\infty` (confirmed both symbolically and by direct numerical evaluation converging to `7/3\approx2.3333` from above as `t` grows — `2.52,\,2.34,\,2.334,\,2.3334` at `t=10,100,1000,10000`) — an exact, superluminal (`>1`) asymptotic longitudinal sound speed; and the small-stretch leading behavior `W_\zeta\sim(4C\zeta/9)t^{-2/3}` with `W_\zeta'<0` as `t\to0^+` (confirmed symbolically via the sign of the limit and numerically, with `W_\zeta'` growing large and negative as `t\to0`: `-10.6,\,-632,\,-29615` at `t=0.1,0.01,0.001`) — a genuine kinetic-sign ghost under compression.

So the repair is a real, if partial, fix: it corrects the large-stretch *gradient*-sign problem from `v14.971` while introducing two new, independently-confirmed pathologies — superluminal propagation at large stretch and a kinetic ghost at small stretch (compression) — exactly as the entry reports. The entry's framing (a "whack-a-mole" result: fixing one finite-strain pathology with a free quartic coefficient `\zeta` reliably creates another, since `\zeta` is not Cone-selected and nothing here constrains it to be causality-preserving) is accurate and not overstated, and its explicit note that this is a separate question from `v14.985`'s carrier-discreteness finding (no cross-identification of the free `\zeta` with any quantized charge) is correctly drawn.

---

## Assessment

Two tightly-scoped, honestly-negative results, both independently confirmed exactly — one closing a carrier-theoretic question left dangling since the `v14.950` chain (and in the course of verifying it, I went further than the deposited numerics by proving the Casimir formula exactly for the full Fock space, not just the truncated sample), the other closing the most natural first attempt at repairing `v14.971`'s instability and showing, by direct computation, that it merely trades one pathology for two others. No errors found in either entry. No Suzuki/far-tail production files touched (confirmed by both entries' own flags). A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `c3a368c` (`v14.986`), with `v14.987` genuinely the next-free number — no collision. The `v14.926` filename collision flagged in `v14.929` remains unresolved by its own author; not re-flagged in detail here.

---

**Verification record:** full independent re-run of `carrier_sectors.py` (exact reproduction of every printed check, including the honestly-disclosed truncation artifact), plus an independent from-scratch hand proof of the `su(1,1)` Casimir formula `(d^2-1)/4` for general `n,d` in the full (untruncated) Fock space (`v14.985`); independent `sympy` re-derivation of the quartic near-isotropy vanishing, the unchanged quadratic isotropic coefficients, and both large- and small-stretch asymptotic exponents and sign behaviors, cross-checked against direct numerical evaluation at multiple sample points (`v14.986`).

HANDOFF
target: lane-a, sandbox, gravity
type: external-audit-verdict
parent: v14.986
status: closed
action: none — both entries verified exactly, no issues found.
deliverable: none.
