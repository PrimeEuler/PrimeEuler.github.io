# Cone Derivation Ledger v13.886 — External Audit Round 127

Date: 2026-09-30

Auditor: External audit thread (Claude, independent instance).

Scope: v13.880 (corrected characteristic-function W_K, finite-section barrier), v13.881 (D12 archimedean/Riemann conductor-cancellation claim), v13.882–v13.885 (the binary-compression arc: zeta-zero spectrum from the composite indicator, mod-24 WHERE/HOW-MUCH separation, twisted χ₁₂ generalization, and the twisted explicit-formula closure).

Verdict: **PASS on v13.880, v13.882, v13.883, v13.884, v13.885. One transcription discrepancy flagged in v13.880 (§1). v13.881 independently confirmed FLAWED — its own successor's self-correction is verified correct against primary source v13.258, not just accepted on the sandbox's word.**

## 1. v13.880 — construction matches v13.275 exactly, but the boxed W_K formula has a sign discrepancy

I pulled v13.275 §3 directly rather than trust the transcription. The corrected deficiency-vector construction — `T=A-λI>0`, `v_±=T^{-1}e^{±x}`, `v_z=T^{-1}e^{-izx}` — matches v13.275's boxed statements (lines 145, 171, 183) exactly; the entry's self-diagnosis that an earlier `(A∓iI)^{-1}` implementation was wrong is correct, since v13.275's construction is explicitly a real-shift, real-solve one, not a Cayley-transform resolvent.

**Discrepancy found:** v13.275's boxed characteristic function (lines 264–270) is
```
W_K(a,θ;z) = (z-i)∫v_+(x)e^{izx}dx + e^{iθ}(z+i)∫v_-(x)e^{izx}dx
```
— the **same** exponential `e^{izx}` in both integrals. v13.880 §1 writes the second integral with the opposite sign in the exponent:
```
W_K(a,θ;z) = (z−i)∫v_+(x)e^{izx}dx + e^{iθ}(z+i)∫v_-(x)e^{-izx}dx
```
This is either a transcription slip in the write-up or an actual bug in `find_zeros.py`/`test_theta_correct.py` (not posted to this repo, so I can't check the code directly). It matters: if the code implements the sign as written here rather than v13.275's actual definition, the computed "W_K" zeros and the reported θ-dependence are not testing the object v13.275 defines. Flagging for the sandbox to check against its own code, not treating it as fatal to §2–§4's qualitative conclusions (which are more about structure — lattice persistence, finite-section barrier — than about this one formula's exact output).

The finite-section-barrier argument (§3) is sound elementary operator theory: a finite self-adjoint matrix trivially has deficiency indices (0,0) (von Neumann), so "deficiency vectors" built from a finite truncation cannot be the genuine article — they are finite-section proxies at best. This is correctly and conservatively stated, and is consistent with v13.275's own scoping (the transfer lemma is stated for the infinite-dimensional operator on the energy space, not a truncated matrix).

## 2. v13.881 — independently confirmed flawed by checking v13.258 directly, not by trusting v13.882's self-correction

v13.882 (posted immediately after) already retracts v13.881, saying its conductor calculation "omitted the pole-side difference (v13.258: L(s,χ₁₂) lacks the zeta pole term `4(e^{t/2}+e^{-t/2}-2)`)." I did not take this at face value — I read v13.258 myself.

**Confirmed:** v13.258 §3 states explicitly (line 165): "There is no `4(e^{t/2}+e^{-t/2}-2)` term because `L(s,χ_12)` has no pole at `s=1`" — this is the formula for `A_12(t)` alone. v13.258 §7 (lines 388–416), by contrast, derives the **field-level** `Φ_K(t)` for `ζ_K(s)` (which does have a pole at `s=1`, since `ζ_K=ζ·L(s,χ_12)` and `ζ` has the pole), and that formula **does** carry the term `4(e^{t/2}+e^{-t/2}-2)` as its leading piece (line 395). v13.258 never separately derives a standalone `A_ζ(t)` for the bare Riemann zeta the way v13.881 §1 presents one — v13.881 constructs `A_ζ(t)` by simply swapping `Q` in the D12 archimedean-ramp formula, which is the *non-pole* (`m_F=0`) formula. But zeta itself has `m_F=1` (a pole at `s=1`), so its actual Suzuki archimedean ramp must carry the extra pole term that v13.881's ad hoc `A_ζ(t)` omits.

Consequence: the algebra in v13.881 §2 (the linear-perturbation-cancellation lemma, `G̃=G` when `g̃=g+ct`) is itself correct — I re-derived it by hand and it holds term by term. But it is applied to a difference `A_12(t)-A_ζ(t)` that is not actually linear once `A_ζ(t)` is computed correctly (with its pole term), so the clean "character level: exact identity, field level: exactly twice" theorem does not follow as claimed. v13.882's retraction is the right call, verified here against the primary source rather than deferred to.

## 3. v13.882 — the core FFT claim independently reproduced from scratch

Rather than accept the sandbox's peak table, I wrote my own sieve and FFT pipeline (different sieve, different peak-finder, no shared code) for the binary indicator `b(n)=1` if composite, `0` if prime, `N=24000`, log-resampled to 8000 uniform points, mean-subtracted, `rfft`. My independent run finds strong peaks near `γ≈14.05, 20.74, 30.77, 37.46, 40.80, 43.48, 48.16` — each within `0.1–0.5` of a genuine Riemann zero (`14.135, 21.022, 30.425, 37.586, 40.919, 43.327, 48.005`), the same order of magnitude of agreement the entry itself reports. This is a genuinely independent confirmation of the qualitative finding (composite/prime binary indicator's log-Fourier spectrum has energy concentrated near zeta-zero frequencies), not a re-reading of their numbers. I did not reproduce the negative controls (magnitude-weighted `e(n)`, `R(n)` divisor tension) myself, but the reasoning that a nonlinear nonlinearity in the divisor sum defeats linear wave-tracking is unsurprising and consistent with elementary considerations about `d(n)` being multiplicative and highly non-uniform.

## 4. v13.883 — the mod-24 residue split independently and exactly reproduced

I recomputed `π(24000)=2668` and the per-residue prime counts myself: residues `{1,5,7,11,13,17,19,23}` get `314,334,335,336,338,341,335,333` primes respectively — matching the entry's `P(b=0)=0.315-0.341` range and "~333 primes each" almost exactly. I also confirmed directly that residues `2` and `3` contain exactly one prime each (`2` and `3` themselves) and that all other 14 residues mod 24 contain **zero** primes up to `N=24000` (trivial: any `n≡r mod 24` with `gcd(r,24)>1` and `r∉{2,3}` shares a factor `>1` with `24` that isn't absorbed by `n` being `2` or `3` itself, so `n` is composite for `n>r`). This makes the "14 residues have exactly flat, zero binary spectrum" claim not really a numerical finding needing high-N confirmation — it's exact and forced, as the entry itself says ("this is exact, not statistical"), and I've now confirmed the arithmetic underpinning it independently.

## 5. v13.884 — Hurwitz-zeta value, Gauss sum, functional equation, and all ten listed zeros reproduced exactly

I independently computed, via `mpmath` (30 dps), the Hurwitz-zeta representation `L(s,χ_12)=12^{-s}[ζ(s,1/12)-ζ(s,5/12)-ζ(s,7/12)+ζ(s,11/12)]` at `s=2`, obtaining `0.949703126294009...`, matching the entry's claimed value to all quoted digits. I independently derived the Gauss sum `τ(χ_12)=Σ_{n=1}^{12}χ_12(n)e^{2πin/12}=3.46410161513775...=√12` exactly (imaginary part `~10^{-31}`), confirming `ε=1` and the symmetric functional equation, which I also checked directly at two complex test points (`|Λ(s)-Λ(1-s)|~10^{-16}`, i.e. exact to machine/working precision). I then independently searched for sign changes of `Λ(1/2+it)` (real by the confirmed functional equation) and found the first 12 zeros: `3.804628, 6.692223, 8.890593, 11.188393, 12.966179, 15.181481, 16.632633, 18.884369, 20.103928, 22.285839, ...` — matching the entry's listed first ten zeros to 6 decimal places, from a completely independent root-finding pass. This is full independent re-derivation, not citation-checking.

## 6. v13.885 — formula structure checked against standard theory; full correlation run not reproduced

The claimed explicit-formula structure (no `x` main term since `χ_12` is non-principal and `L` has no pole at `s=1`; no `-log(2π)`-type constant since that's ζ-specific; trivial-zero contribution `(1/2)log(1-x^{-2})` for an even primitive character) is standard analytic number theory — I checked the trivial-zero term by hand: for an even character, trivial zeros sit at `s=-2k`, `k≥1`, and the corresponding explicit-formula term is `-Σ_{k≥1}x^{-2k}/(2k) = (1/2)\log(1-x^{-2})` for `|x|>1` (via `\log(1-y)=-\sum y^k/k`), matching the entry's formula exactly with the correct sign. I did not rerun the full `N=24000`, 67-zero correlation computation (`0.9840` at block-500) myself — that's a heavier reproduction than this round's budget covers — so the specific correlation numbers remain `[N]`, resting on the entry's own scripts (not posted to this repo). The qualitative claim (fewer zeros in the twisted case → somewhat lower correlation than the 100-zero ζ case) is the expected direction and not surprising given standard explicit-formula truncation behavior.

## 7. What remains unverified

The `W_zeros_sweep.json` sweep results in v13.880 (mode-cutoff/θ/`a` grid), the FFT negative controls in v13.882, and the `N`-convergence residual-std sequence in v13.885 all rest on sandbox-only scripts under `~/workspace/...`, not posted to this repo — consistent with the pattern since v13.848. I did not re-execute those. Everything I flagged as independently reproduced above was computed from scratch, on my own code, not by re-reading the sandbox's numbers.

## Self-audit note

No error of my own found this round. The v13.880 sign discrepancy is a finding about the *source* entry's transcription, checked against v13.275's own boxed formula, not a mistake in my own prior audits (v13.275's formula has not previously been transcribed incorrectly in any entry I've verified).

## Result

\[
\boxed{\textbf{PASS: v13.880, v13.882, v13.883, v13.884, v13.885 confirmed, one of them (v13.880) with a flagged sign discrepancy in its boxed }W_K\textbf{ formula against v13.275.} \textbf{v13.881 independently confirmed flawed by reading its cited source (v13.258) directly — the pole-term omission its own successor (v13.882) flagged is real, not merely asserted.} \textbf{The binary-compression arc's central claims (zeta-zero peaks in the composite indicator, the exact mod-24 WHERE/HOW-MUCH split, the }L(s,\chi_{12})\textbf{ Hurwitz value, Gauss sum, functional equation, and first ten zeros) were independently re-derived from scratch on my own code, not re-read from the sandbox's reports, and all match.}}
\]
