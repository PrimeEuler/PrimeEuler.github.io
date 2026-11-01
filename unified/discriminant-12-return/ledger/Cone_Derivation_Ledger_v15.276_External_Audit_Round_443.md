# Cone Derivation Ledger v15.276 — External Audit Round 443: verified v15.274-v15.275

**Date:** 2026-11-01
**Track:** External Audit
**Status:** [B] two Sandbox entries verified: exact identities hand-derived from scratch, payload scripts re-executed byte-identical.
**Parents:** v15.273 (Round 442), v15.274, v15.275.

---

## Fresh pre-write check

Live `origin/master` was `16b5940` (v15.275) both at the start of this round and immediately before this write; no further commits landed in between. `v15.276` is the next free ledger number; no collisions (single lane, strictly sequential).

## v15.274 — Position on the mass hyperbola as opposite-sign parabola crossing

Re-executed `state_crossing.py` — byte-identical. Independently re-derived every claimed identity from scratch:
- `E=(n+k)/2, p=(n-k)/2, m=√(nk)`: `E²-p²=[(n+k)²-(n-k)²]/4=nk=m²` — confirmed, a direct difference-of-squares identity.
- Boost parameter: with `ψ=½ln(n/k)`, `m cosh ψ = ½(n+k)=E` and `m sinh ψ=½(n-k)=p` — confirmed by direct substitution (`m cosh ψ = √(nk)·½(√(n/k)+√(k/n))=½(n+k)`, etc.).
- Light-cone labels `u=E+p=n, v=E-p=k` — immediate from the above, confirmed.
- Electron worked examples, independently recomputed: rest `u=v=m_ec²=0.51100 MeV` ✓; at `E=1 MeV`, `pc=√(1-0.511²)=0.85958`, giving `(u,v)=(1.85958, 0.14042)` ✓ and `ψ=arccosh(1/0.511)=1.2917` ✓; at `E=5 MeV`, `pc=√(25-0.261121)=4.97382`, giving `(9.97382, 0.02618)` ✓ and `ψ=arccosh(5/0.511)=2.9714` ✓. All four numbers match exactly.
- Seam claim (seat crossing `n=k` exists only for perfect-square `N`): confirmed logically — `36=6×6` has a matched factor pair, `12` and `60` (neither a perfect square) do not.

## v15.275 — Drive × reaction, nature's pushback

Re-executed `pushback.py` — byte-identical (seeded RNG, `np.random.default_rng(7)`, fully reproducible). Marked `[I]` interpretation over two anchors, both checked:
- Radiation-reaction time `τ₀=6.266e-24 s`: independently recomputed via `τ₀=2r_e/(3c)` with `r_e=α·ƛ_e` (using the already-verified `ƛ_e=3.8616e-13 m` from Round 442 and `α=1/137.036`), giving `r_e≈2.818e-15 m` (matches the standard classical electron radius) and `τ₀≈6.266e-24 s` — confirmed independently, not from the script's own number alone.
- The `⟨F_react·v⟩=-⟨P_Larmor⟩` identity over one period of harmonic motion is the standard Abraham-Lorentz/Larmor exact-cancellation result (textbook identity, e.g. Griffiths); the script's symbolic check is a legitimate verification of a known exact theorem, not a novel claim.
- The Langevin ensemble check (`⟨v²⟩=0.9991±0.0032` vs `k_BT/m=1`) reproduces exactly from the seeded RNG — a reasonable finite-sample statistical result consistent with equipartition.

## Scope check

Both entries correctly distinguish exact standard-physics anchors (computed, confirmed) from the interpretive identification of the geometric mesh's two parabola families with "drive" and "reaction" (explicitly marked `[I]`, not claimed as derivation). No gate or classification change in either.

## Summary

Two Sandbox addenda, both independently confirmed: every closed-form identity in v15.274 re-derived from scratch by hand (not read and accepted), both payload scripts re-executed byte-identical including a seeded stochastic simulation. Nothing to correct. `K_full` remains blocked at the same transfer gate; open items unchanged.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-443
parent: v15.276
status: closed
action: none — both entries independently confirmed exactly as stated; no correction needed.
deliverable: independent hand-derivation and re-execution confirmation of v15.274 (mass-hyperbola crossing identities) and v15.275 (radiation-reaction/Langevin anchors).
