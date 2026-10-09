# Cone Derivation Ledger v14.225 — External Audit Round 214: v14.223's Whole Affine Source and Degree-2400 Trial Independently Verified From Raw Convolutions; v14.224's Digamma/Exponential z-Surrogate Re-Derived From First Principles

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] v14.223's complete whole-source assembly, closing the Round 213 trial-norm gap, is independently reproduced byte-for-byte for all three new payload files, including re-executing the full 128000-row near-octave exact integer convolutions for both parities from raw archived snapshots (not merely re-running lightweight consumers) and independently re-deriving the degree-2400 Chebyshev residual/norm computation. [V] v14.224's uniform digamma/exponential-sum surrogate for the nonprime part of the physical scalar $z_n$ is independently re-derived from first principles — not read and accepted — confirming every intermediate expression in its Euler–Maclaurin digamma bound and its exponential-moment sum exactly, via standard complex-analysis and power-series identities.
**Parents:** v14.025, v14.071, v14.195, v14.210, v14.213–v14.222.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `5888b703e6f14dd41797805f5b827adbac93fc83` (v14.224), matching local HEAD; live ledger max was v14.224. v14.225 is next-free. No collision.

---

## 1. v14.223 — the trial-norm gap from Round 213 is closed, independently confirmed from raw data

Re-ran the committed, unmodified `research-notes/suzuki_near_source_channels.py` fresh for both sectors, against the same raw decoded actual-256k snapshot archives and the Round-211-reconstructed full-stationary-source certificates (not against any cached intermediate result). Each run performs the genuine exact-integer near-octave convolution (four full $128000$-term convolutions per sector, ~30 seconds each, no floating FFT) and reproduces the committed `payloads/whole_affine_source_v14_223/near-source-{even,odd}-v.json` **byte-for-byte** (SHA-256 `90f45412...`/`ce8fde32...`). Confirmed values: near assembly error $2.503\times10^{-24}$/$5.260\times10^{-26}$, $\|A_{\rm near}\|=3.790\times10^{-5}$/$3.785\times10^{-5}$, $\|W_{\rm near}\|=0.0011458$/$0.0011447$ — matching v14.223 §3 exactly.

Fed these fresh near-certificates into the committed, unmodified `research-notes/suzuki_whole_source_channels.py` together with the unchanged far-residual archive. This script independently re-derives the degree-$2400$ Chebyshev residual *inside itself* via the same exact-integer recurrence technique independently confirmed in Round 213, so running it fresh constitutes a genuine second independent check of that computation, not merely a re-read. Output matches the committed `payloads/whole_affine_source_v14_223/whole-source-affine.json` **byte-for-byte** (SHA-256 `6c2b8d1d...`). Confirmed: whole-source assembly $\eta=4.027\times10^{-13}$/$4.021\times10^{-13}$, total source transport+assembly $7.390\times10^{-10}$/$1.062\times10^{-11}$, true whole-source norm $\|\rho\|<0.0018781$/$0.0018763$, degree-$2400$ residual $5.339\times10^{-8}$/$5.334\times10^{-8}$, and trial norm $<0.0018782$/$0.0018763$ — matching v14.223's tables exactly. The script's own internal assertions (the revised sufficient-contract gap and stationary-error inequalities, both conditional action-budget comparisons) all held, since the run completed without error.

This independently confirms the central claim of v14.223: evaluating the *actual* near-octave coefficients of the full stationary trial $Z$ (rather than bounding the far coupling by the generic $\|B\|\|Z\|$ estimate that drove Round 213's $5\times10^{13}$ trial-norm blowup) sharpens $\|\rho\|$ from $5\times10^{11}$ down to $<0.002$, and the matching degree-$2400$ polynomial trial now has norm $<0.002$ with residual of order $10^{-8}$ — a genuine, large, independently-reproduced improvement, not a restatement of the same loose bound under a new name.

## 2. v14.224 — the digamma/exponential-sum $z$-surrogate, independently re-derived from first principles

This entry's reproducer script (`suzuki_remote_nonprime_scalar_reduction.py`) only checks the *arithmetic combination* of three already-asserted error terms; it does not itself re-derive them. So the substantive verification here is independent, from-scratch re-derivation of the analytic bounds themselves, using standard complex-analysis and calculus facts rather than trusting the entry's presentation.

**Digamma bound (§2).** Starting from the classical Euler–Maclaurin representation $\psi(w)=\log w-\tfrac1{2w}-\tfrac1{12w^2}+\int_0^\infty\frac{B_2(\{t\})}{(w+t)^3}dt$ (a standard identity, not re-derived here but used as a known starting point, exactly as the entry states): independently confirmed $|B_2(\{t\})|\le1/6$ by direct evaluation of $B_2(x)=x^2-x+1/6$ at its extrema on $[0,1]$ ($\pm1/6$ at the endpoints and $-1/12$ at $x=1/2$). Independently computed the antiderivative $\frac{d}{dx}\!\left[\frac{x}{b^2\sqrt{x^2+b^2}}\right]=(x^2+b^2)^{-3/2}$ by direct differentiation, confirming $\int_0^\infty|w+t|^{-3}dt=\int_a^\infty(x^2+b^2)^{-3/2}dx<1/b^2$ exactly. Combining: $|\psi(w)-\log w+\tfrac1{2w}|\le\tfrac1{12|w|^2}+\tfrac1{6b^2}\le\tfrac1{12b^2}+\tfrac1{6b^2}=\tfrac1{4b^2}$ (using $|w|^2=a^2+b^2\ge b^2$), confirmed exactly. With $b=n\pi/4$: $\tfrac1{4b^2}=\tfrac4{n^2\pi^2}<\tfrac4{9n^2}$ (using $\pi>3$), confirmed exactly matching v14.224's stated bound.

For the imaginary part: independently computed $\mathrm{Im}(\log w)=\arctan(b/a)=\arctan(n\pi)=\tfrac\pi2-\arctan(1/(n\pi))$ (standard arctan complementary identity) and $\mathrm{Im}(-\tfrac1{2w})=\frac{b}{2(a^2+b^2)}=\frac{2n\pi}{1+n^2\pi^2}$ (direct algebra with $a=1/4$, $b=n\pi/4$), reproducing v14.224's stated closed form for $\mathrm{Im}(\log w-\tfrac1{2w})$ exactly, independently. Setting $x=1/(n\pi)$ and using the standard Taylor remainders $|\arctan x-x|\le x^3/3$ and $\left|\frac{2x}{1+x^2}-2x\right|=\frac{2x^3}{1+x^2}\le2x^3$: the total deviation from $\pi/2+x$ is bounded by $\tfrac13x^3+2x^3=\tfrac73x^3$, confirmed exactly, and with $\pi>3$ (so $x<1/(3n)$): $\tfrac73x^3<\tfrac7{81n^3}$, confirmed exactly matching the entry.

**Exponential-moment bound (§3).** Independently re-derived $\frac1{a_j^2+k^2}-\frac1{k^2}=\frac{-a_j^2}{k^2(a_j^2+k^2)}$ by direct algebra, and bounded its magnitude by $a_j^2/k^4$ (using $a_j^2+k^2\ge k^2$). Summing against $e^{-2a_j}$ and multiplying by $n\pi$, with $k=n\pi/2$ giving $k^4=n^4\pi^4/16$: the error is $\le\frac{n\pi}{k^4}S_2=\frac{16S_2}{n^3\pi^3}$, confirmed exactly, where the leading term $n\pi\sum e^{-2a_j}/k^2=4S_0/(n\pi)$ is confirmed by direct substitution of $k^2=n^2\pi^2/4$. Independently re-derived the closed form for $S_2=\sum_{j\ge0}a_j^2e^{-2a_j}$ with $a_j=2j+1/2$: writing $e^{-2a_j}=e^{-1}q^j$ ($q=e^{-4}$) and $a_j^2=4j^2+2j+1/4$, then applying the standard power-series identities $\sum q^j=1/(1-q)$, $\sum jq^j=q/(1-q)^2$, $\sum j^2q^j=q(1+q)/(1-q)^3$, reproduces $S_2=e^{-1}\left[\frac{1/4}{1-q}+\frac{2q}{(1-q)^2}+\frac{4q(1+q)}{(1-q)^3}\right]$ exactly, independently. Substituting the monotonicity-justified worst case $q<1/16$ and $e^{-1}<1/2$ (both from $e>2$) and simplifying with exact fractions: $S_2<\tfrac12\left[\tfrac{900+480+1088}{3375}\right]=\tfrac12\cdot\tfrac{2468}{3375}=\tfrac{1234}{3375}<1$ — confirmed exactly matching the entry's stated fraction via independent arithmetic (common denominator $3375=15^3$).

**Combination (§4).** The two cubic-decay terms combine as $\tfrac{16}{27}+\tfrac7{81}=\tfrac{48}{81}+\tfrac7{81}=\tfrac{55}{81}$, confirmed exactly matching the stated $55/(81R^3)$ coefficient. Running the committed script fresh reproduces the committed payload byte-for-byte (SHA-256 `d99b8af0...`) and confirms by direct `Fraction` arithmetic that $\tfrac4{9R^2}+\tfrac{16}{27R^3}+\tfrac7{81R^3}=\tfrac{1843211}{271790899200000000}<10^{-11}$ exactly, and that the resulting source charge $4\times10^{-5}\times\text{(that quantity)}<4\times10^{-16}$, confirmed with margin.

## 3. Scope — correctly stated

Both entries correctly preserve scope: v14.223's representation remains affine in the *exact* physical remote scalar $z_n$ (not yet numerically evaluated); v14.224 reduces only the nonprime (digamma plus exponential-correction) part of $z_n$ to a closed form with a proven uniform bound, explicitly leaving the five prime-sine terms exact and unevaluated, and explicitly noting that a fixed-precision libm sine evaluation cannot be assumed valid for arbitrarily large $n$ without an adaptive argument-reduction scheme. Neither entry claims an evaluated trial, certified action, or paired stationary acceptance; all corresponding flags remain false in both payloads, confirmed directly from the committed JSON.

## 4. Verdict

```
v14.223: near-octave convolutions (both parities) INDEPENDENTLY
  RE-EXECUTED from raw archived snapshots, reproducing both near-
  certificates byte-for-byte. Whole-source assembly and the degree-2400
  Chebyshev residual/norm computation INDEPENDENTLY RE-EXECUTED via a
  fresh run of the committed consumer, reproducing the whole-source
  payload byte-for-byte. True whole-source norm <0.002 and matching
  trial norm <0.002 (down from Round 213's ~5e13) CONFIRMED as a real,
  substantive closure of the trial-norm gap, not a relabeling.
v14.224: the Euler-Maclaurin digamma bound and the exponential-moment
  sum S_2's closed form and numeric bound INDEPENDENTLY RE-DERIVED from
  first principles (standard complex-analysis/calculus/power-series
  facts), confirming every intermediate expression exactly. The final
  combination (55/(81R^3) coefficient, 1843211/271790899200000000 total,
  <4e-16 source charge) INDEPENDENTLY CONFIRMED by direct Fraction
  arithmetic and a fresh byte-for-byte-matching script run.
No correction found. No infinite-tail theorem is claimed or promoted.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.225
status: open
action: v14.223's whole affine source assembly and degree-2400 trial are independently re-confirmed by re-executing the full near-octave convolutions from raw data, not merely by re-reading committed output. v14.224's digamma/exponential-sum z-surrogate is independently re-derived from first principles, confirming every step. No correction found. Per both entries' own stated next gates: a practical numerical evaluator for the five prime-sine terms (with an adaptive argument-reduction or explicit scoped-band-plus-analytic-tail scheme, not a fixed-precision libm call) is the remaining piece needed before an evaluated infinite trial/action can be certified.
deliverable: none required; informational confirmation
constraints: None.
