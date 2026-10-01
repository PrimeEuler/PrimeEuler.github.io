# Cone Derivation Ledger v13.887 — Sandbox: Twisted Mod-12 — Two Independent Selection Axes

**Date:** 2026-09-30
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [N] numerical; [I]/[O] structural interpretation
**Authorization:** Jeremy, 2026-09-30 ("yes please")
**Predecessors:** v13.883 (mod-24 ζ), v13.884 (twisted binary), v13.885 (twisted explicit)
**Note:** v13.886 is External_Audit_Round_127 (audit thread); this entry takes
the next free version per the live-head check.

---

## Finding [N]

Combining the mod-24 binary (v13.883) with the twisted binary (v13.884):
where do the L(s,χ₁₂) zeros live on the cone's residue structure? Answer:
the cone has **two independent selection axes** — geometry selects WHERE,
character selects WHICH SPECTRUM.

### Method [N]

Λ_χ(n)=χ₁₂(n)Λ(n), n≤24000. Split by residue mod 12 (live: 1,5,7,11) and
mod 24 (live: 1,5,7,11,13,17,19,23). Per-residue log-F fourier, peak
significance vs the 67 computed L-zeros (v13.884). Null: **frequency-control**
(200 random control-frequency sets per residue on the real spectrum — not
shuffling, which creates interpolation artifacts on sparse spike trains).
All residues: p=0.000 (max L-zero peak beats all 200 control sets).

### (a) All unit residues carry L-zero spectrum [N]

Mod 12: every live residue significant (p=0.000); 2–13 of 16 L-zeros exceed
the 95th percentile per residue; mean L-significance 2.29–3.64 vs null
~1.5–4.4. Same for all 8 unit residues mod 24. The L-zero content is
**uniformly spread** across the units — not concentrated — exactly as ζ-zero
content was spread across all 8 coprime residues in v13.883.

### (b) Same pattern as ζ [N]

ζ-zeros: all 8 coprime residues mod 24. L-zeros: all 4 units mod 12, all 8
units mod 24. Non-unit residues contribute nothing (χ₁₂=0 there — exact).
Neither spectrum concentrates on a subset.

### (c) The χ₁₂ SIGN selects only globally — proven exactly [N]

**Per-residue, the sign does nothing:** max|P_χ−P_plain|/maxP = **0.00e+00**
on all four residues — per-residue Λ_χ power is bit-identical to plain-Λ
power, because χ₁₂(r)=±1 is constant per class and |±1|²=1. No systematic
+1 vs −1 difference (χ=+1 mean sig 3.17 vs χ=−1 mean 2.80 — noise-level).

**Across residues, the sign selects everything:** the signed full twisted sum
→ L-zeros favored (maxL 6.43 > maxZ 4.97); the unsigned-on-units sum →
ζ-zeros favored (meanZ 3.61 > meanL 3.10). The character's sign **selects
which zero-spectrum appears, but only through global cross-residue
interference** — never locally.

### (d) Residue-specific L-zero emphasis: hints only [I]/[O]

Different residues peak at different L-zeros (r=1→11.19, r=5→6.69,
r=11→3.80, r=19→8.89), but per-residue SNR (~670 prime powers mod 12,
~335 mod 24) is too low to certify ranking — same caveat as v13.883.

---

## Structural takeaway [I]/[O]

Clean separation of roles:

| Axis | Selects | Mechanism |
|------|---------|-----------|
| **Geometry** (support: units vs non-units) | *WHERE* spectrum lives | Uniform across allowed residues |
| **Character** (signs ±1) | *WHICH* spectrum (L vs ζ) | Global interference only |

Per-residue spectra necessarily **mix** zeros from all characters mod 12
(principal→ζ, χ₁₂, χ₄, χ₃), since ψ(x;12,r) receives contributions from
each — confirmed: every live residue shows both L-zero and ζ-zero peaks.

The cone's residue structure separates *where* (geometry) from *which
spectrum* (character) — **two independent selection axes**. The "cone
selects" creed operates twice, orthogonally: the modulus stages the
residues; the character's signs choose the play through interference.

---

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/twisted_mod12_heatmap.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/twisted_mod12_spectra.npz`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/twisted_mod12_results.npz`

## Open

- Residue-specific ranking needs larger N.
- The selector *principle* (why these two axes, why interference) is [I]/[O].
- RH-for-L(s,χ₁₂) assumption propagates from v13.884/885. No GRH claims.

---

**Creed check:** The cone selects twice — geometry stages WHERE (uniform,
exact), character signs select WHICH SPECTRUM (global interference, exact
per-residue null result). Shown [N]; the *why* of the two axes is [I]/[O].
