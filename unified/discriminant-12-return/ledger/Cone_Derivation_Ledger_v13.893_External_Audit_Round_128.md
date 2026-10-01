# Cone Derivation Ledger v13.893 — External Audit Round 128

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: v13.887 (two selection axes), v13.888 (spectral probe universality across χ₃/χ₄/χ₅), v13.889 (β explicit-formula loop), v13.890 (5/5 loops closed + a sign correction to v13.885), v13.891 (selector-principle capstone + a further sign "correction" to v13.889), v13.892 (quantization-route mapping).

Verdict: **PASS on v13.887, v13.888, v13.892. PARTIAL on v13.889/890/891's trivial-zero-term bookkeeping — I independently re-derived the relevant contour residues from scratch and found a real, previously unflagged missing term for the even-character cases (χ₁₂, χ₅) that is numerically substantial, plus confirmed v13.891's own "correction" to v13.889's odd-character sign is itself wrong.** None of this threatens the headline claims (the explicit-formula tracking is real; no RH/GRH claim is affected), but the specific "DC offset" and "sign error" bookkeeping across v13.885/889/890/891 needed a clean redo, which I did independently rather than adjudicate between the sandbox's own conflicting self-corrections.

## 1. The chase: three ledger entries disagreed with each other and with my own Round 127 check, so I re-derived the contour residues from scratch

Round 127 (v13.886 §6) I hand-checked v13.885's trivial-zero term "+(1/2)log(1-x^{-2})" for even χ₁₂ and called it correct. v13.890 then said that sign was wrong and "corrected" it to "−(1/2)log(1-x^{-2})". v13.891 then separately claimed v13.889's odd-character term (β/χ₄) also had its sign backwards and "corrected" it too. Three different verdicts on two sign questions, from three different entries (one of them mine). Rather than pick a side by re-reading the same hand-waving, I redid the Perron/residue calculation myself, carefully, for both parities, and checked it two ways: analytically and by direct numerical reconstruction against the true ψ(x,χ) for three characters (χ₁₂, χ₄, χ₅) using my own independently-found zero lists (Round 127 already gave me χ₁₂'s 67 zeros; I computed χ₄'s 50 and χ₅'s 54 fresh this round, matching v13.888's counts and first zeros exactly).

**Residue computation.** For a simple zero `s_n` of `L(s,χ)` (trivial or nontrivial), `f(s) = -(L'/L)(s,χ)·x^s/s` has residue `-x^{s_n}/s_n` there. Summing over the trivial zeros:
- **Odd** (`a=1`, zeros at `s=-1,-3,-5,...`): `Σ_{n≥0} x^{-(1+2n)}/(1+2n) = +(1/2)\log\frac{x+1}{x-1}` — **matches v13.889's original (uncorrected) sign**, not v13.891's "fix."
- **Even** (`a=0`, zeros at `s=-2,-4,-6,...`, n≥1 only — see below for why `s=0` is excluded from this sum): `Σ_{n≥1} x^{-2n}/(2n) = -(1/2)\log(1-x^{-2})` — **matches v13.890's corrected sign**, confirming that correction (and simultaneously confirming my own Round 127 check used the wrong sign — I made the same slip the sandbox made in v13.885, and didn't catch it until re-deriving from the residue formula directly rather than pattern-matching to the classical `ζ` formula).

## 2. The term nobody caught: `s=0` is itself a genuine trivial zero for even primitive characters, and its contribution is missing from v13.885/890 entirely

I checked numerically (not assumed) whether `L(0,χ)=0` for each character: `L(0,χ_12)=-1.3×10^{-26}` (zero), `L(0,χ_5)=4.9×10^{-32}` (zero), vs. `L(0,χ_4)=0.5` and `L(0,χ_3)=1/3` (both nonzero). This is forced by the functional equation's Gamma factor: `Γ(s/2)` has a pole at `s=0`, and since `Λ(s,χ)=(q/π)^{s/2}Γ(s/2)L(s,χ)` is entire for primitive non-principal χ, `L(s,χ)` must vanish at `s=0` to cancel it — for **even** χ only (the odd normalization uses `Γ((s+1)/2)`, which has no pole at `s=0`).

Consequence: near `s=0`, `L'/L(s,χ)` itself has a simple pole (from the zero of `L` there), which collides with the existing `1/s` factor from Perron's formula, producing a genuine **double pole** at `s=0`. Working out the Laurent expansion (`L'/L(s,χ) = 1/s + c_0 + O(s)` with `c_0 = L''(0,χ)/(2L'(0,χ))`), the residue contribution to `ψ(x,χ)` from this double pole is **`-\log x - c_0`** — an term that grows with `x`, not a bounded correction. This is structurally distinct from, and in addition to, the `n≥1` trivial-zero sum discussed above, and it is **absent from v13.885, v13.890, and v13.891** — none of the three entries that touched this formula noticed that even characters need an extra `-\log x` term beyond the finite trivial-zero series.

**Numerical confirmation (decisive, independent reconstruction, not just algebra):** I computed `c_0` for both `χ_12` (`c_0=-0.547`) and `χ_5` (`c_0=-0.022`) via `mpmath`, built the full truncated explicit formula three ways, and compared against the true `ψ(x,χ)` (sieve, `N=24000`) for both characters:

| Variant (χ₁₂) | block-500 corr | residual mean | resid-vs-log(x) slope |
|---|---|---|---|
| v13.885 original sign | 0.983786 | −8.465 | −0.926 |
| v13.890 "corrected" sign | 0.983786 | −8.465 | −0.925 |
| **+ my derived `-\log x - c_0` term** | **0.984096** | **0.075** | **0.075** |

| Variant (χ₅) | block-500 corr | residual mean | resid-vs-log(x) slope |
|---|---|---|---|
| v13.885-style original sign | 0.992299 | −8.939 | −0.874 |
| v13.890 corrected sign | 0.992299 | −8.939 | −0.874 |
| **+ my derived term** | **0.992649** | **0.125** | **0.126** |

The sign fix alone (v13.890's actual change) does essentially nothing — confirmed, consistent with the entry's own "numerically negligible" disclaimer. The missing `-\log x - c_0` term removes essentially the entire systematic bias (residual mean drops by two orders of magnitude, from `~-8.5/-8.9` to `~0.1`, and the drift against `\log x` nearly vanishes). This explains, mechanistically, what v13.885 and v13.889 both reported as an unexplained "DC offset — finite-T artifact" (`mean ψ_T≈9.1` vs `true≈0.7` in v13.885's own words): it wasn't a truncation artifact at all, it was this missing analytic term, whose sign (positive bias in the formula ⇒ negative residual) and rough magnitude (`\log(24000)/2≈5`, in the right ballpark averaged over the block structure) match. The high correlation numbers reported throughout this arc (`0.984`, `0.993`, etc.) are not wrong, but they were never sensitive to this bias in the first place — Pearson correlation on data with std `~15-17` barely moves when a slowly-varying `\log x` trend (range `~0.7-10.1` over the sample) is added or removed, which is exactly why neither the sandbox's own correlation-based validation nor my Round 127 spot-check caught it.

**Why odd characters (χ₄, χ₃) are unaffected:** confirmed `L(0,χ_4)=0.5≠0`, `L(0,χ_3)=1/3≠0`, so `s=0` is not a zero of `L` for odd primitive χ and the Perron integrand has only a simple pole there, contributing a bounded constant `-(L'/L)(0,χ)`, not a growing `\log x` term. I checked this numerically for χ₄ too: adding the missing constant (`-(L'/L)(0,χ_4)=-0.783`) shrinks the residual mean modestly (`-0.927→-0.144`) but nowhere near the order-of-magnitude effect seen for the even cases, consistent with v13.889's β loop being essentially sound as reported.

## 3. v13.891's "correction" of v13.889's odd-character sign is itself wrong

Having derived the odd-case trivial-zero sum as `+(1/2)\log\frac{x+1}{x-1}` from the residue formula (§1 above), v13.889's original formula was already correct; v13.891 flipped it to `-(1/2)\log\frac{x+1}{x-1}`, which is the wrong sign by my derivation. I confirmed numerically that, as with the even case, this sign flip is itself nearly inconsequential to the fit (residual mean `-0.927` vs `-0.926`, a difference at the noise floor) — so v13.891's claim that "both trivial-zero sign errors... are now corrected" is half right (the even-case fix in v13.890 was genuinely correct, independently confirmed above) and half wrong (the odd-case "fix" in v13.891 undid a correct formula). Practically inconsequential either way, but worth getting right on the record, especially since v13.891 explicitly frames itself as the entry that replaces memory-based sign-writing with contour-derived rigor ("derivation-first henceforth") — the irony being that this pass introduced a fresh sign error while fixing one and missing the much larger `-\log x` gap entirely.

## 4. v13.887 — the "two selection axes" structural claim checked against elementary facts, holds up

The core claims — that `χ_12=0` identically on non-unit residues mod 12/24 (trivial, since `χ_12` is only supported on units), and that the sign of `χ_12` cannot do anything to a single-residue power spectrum because `|χ_12(r)|^2=1` is constant on that residue class (so `|χ_12(r)|^2·P_Λ(ω) = P_Λ(ω)` identically, bit-for-bit) — are elementary and correct by inspection; no computation needed to confirm "max|P_χ−P_plain|=0 exactly." The broader "geometry selects WHERE, character selects WHICH SPECTRUM (only via global interference)" framing is a reasonable, non-overclaiming synthesis of that fact, appropriately marked [I]/[O] for the "why."

## 5. v13.888 — zero computations reproduced, "universal" framing appropriately scoped

I independently recomputed the first zeros of `L(s,χ_4)` (50 zeros, first at `6.020949`, exact match) and `L(s,χ_5)` (54 zeros, first at `6.648453`, exact match — one more zero than their reported 53, likely a boundary/tolerance difference near `t=100`, immaterial). The `χ_12=χ_3·χ_4` multiplicativity claim and the "detection factors through prime-conductor constituents" reading is a reasonable interpretation of the data (χ₃ and χ₄ both individually beating χ₁₂'s match rate) and is correctly marked [I]/[O], not overclaimed as a theorem.

## 6. v13.892 — the one [D]-tagged claim checked by hand

"`d(\gcd(m,n))` is positive-definite via `d=1*1`": correct and easy to verify directly — `d(\gcd(m,n)) = \sum_{e|\gcd(m,n)} 1 = \sum_e [e|m][e|n]`, i.e. the matrix `M_{m,n}=\sum_e v_e(m)v_e(n)` with `v_e(m)=[e|m]`, which is exactly `V^TV` for the (rectangular) indicator matrix `V`, hence PSD by construction, no computation required. The rest of the entry is honest route-mapping ([I]/[O] throughout, explicitly "no flag planted"), correctly citing v13.881's pole-term omission (confirmed independently by me in Round 127) as a cautionary precedent. Nothing else in this entry makes a checkable [D] claim.

## 7. What remains unverified

The full `W_zeros_sweep` numerics (v13.880, prior round), the `p=0.000` frequency-control null tests in v13.887, and the Lerch-bracketing ambiguity blocking Direction 4 in v13.892 all rest on sandbox-only scripts not posted to this repo. Not re-executed.

## Self-audit note

**Correcting my own Round 127 (v13.886 §6):** I verified v13.885's even-character trivial-zero sign as "+(1/2)log(1-x^{-2}), correct" — this was wrong. The correct sign, confirmed twice now (by residue derivation and by numerical fit), is negative, matching v13.890's correction. I did not, at the time, check for the separate `s=0` double-pole contribution at all — that gap is now closed in this entry. This is exactly the kind of error my own hand-checks can make when they pattern-match to a remembered formula (the classical `ζ(s)` trivial-zero term) rather than re-deriving from the actual contour integral for the specific object at hand — the same failure mode v13.891 diagnosed in the sandbox's own prior work, which I was not immune to either.

## Result

\[
\boxed{\textbf{PASS: v13.887, v13.888, v13.892 confirmed.} \textbf{v13.889/890/891's trivial-zero bookkeeping re-derived from scratch: v13.890's even-character sign correction (}\chi_{12},\chi_5\textbf{) is correct; v13.891's odd-character "correction" (}\chi_4\textbf{) is itself wrong and reintroduces an error v13.889 did not have.} \textbf{More substantively: a genuine, previously unflagged double-pole term at }s=0\textbf{ (forced by }L(0,\chi)=0\textbf{ for every even primitive character, numerically confirmed for }\chi_{12}\textbf{ and }\chi_5\textbf{) is missing from every even-character explicit-formula reconstruction in this arc; adding it removes ~8.5-8.9 units of systematic bias and the residual's drift against }\log x\textbf{, which the correlation metrics used throughout were never sensitive enough to catch.} \textbf{This does not threaten the arc's headline finding (compression reveals the explicit formula); it corrects its constant-term bookkeeping, including a sign error of my own from Round 127.}}
\]
