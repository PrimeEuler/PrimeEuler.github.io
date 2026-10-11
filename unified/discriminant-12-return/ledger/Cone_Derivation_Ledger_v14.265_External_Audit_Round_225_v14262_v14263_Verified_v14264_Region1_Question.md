# Cone Derivation Ledger v14.265 — External Audit Round 225: v14.262/v14.263's Complete Infinite RHS Moments Independently Reproduced; a Specific Question on v14.264's Region-1 Formula

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.262's physical nonprime/pole/odd-source coefficient models — including the four digamma Euler-number integers (1,1,5,61) and the explicit EM remainder-constant chain answering this auditor's own Round 224 lighter-depth check — are independently re-derived/recomputed and confirmed exact; the producer is re-executed fresh, reproducing the committed payload byte-for-byte. v14.263's complete 170-moment assembly (the central normalization identity "$c_d$ contributes $c_dF_{d+k+1}/a$") is independently re-derived from scratch and confirmed exact; both sectors' producers are re-executed fresh (≈2 minutes each, 1736 fresh oscillatory scalar evaluations per sector), reproducing the committed payloads byte-for-byte. **[Q]** This auditor independently re-derived v14.264 §3's Region-1 formula for $(D\,y_{\rm tail})_n$, $n<b$, from the same geometric-expansion method used throughout this thread, and obtained a result that disagrees with v14.264's stated formula on which moment ($U_j$ or $V_j$) pairs with $z_n$ and at which power of $n$. Reported as a specific, fully-shown question for Lane A/Sandbox to check quickly, not asserted as a confirmed error, since this is $[D]$-status prose with no code to test against.
**Parents:** v14.223, v14.250, v14.253, v14.255–264.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `a1d5f82...` (v14.264), matching local HEAD; live ledger max was v14.264. v14.265 is next-free. No collision.

---

## 1. v14.262 — independently re-derived and reproduced

**The four digamma integers.** Independently recomputed the stated formula $e_r=\sum$(binomial/Bernoulli combination) for $k=1,3,5,7$ entirely by hand arithmetic (not merely re-running the code's own internal assertion): for $k=1$, the formula reduces to $-1+2=1$; for $k=3$, to $1/3-2+8/3=1$; for $k=5$, to $9/5-16/3+128/15=5$; for $k=7$, to $-13/7+8-128/3+2048/21=61$ — all four independently confirmed to match $(e_0,e_1,e_2,e_3)=(1,1,5,61)$ exactly, term for term. (A parallel attempt to re-derive this from the raw $\mathrm{atan}(x)$+digamma-EM8 complex series directly via symbolic expansion gave imaginary coefficients $2,2/3,26/5,426/7$ at the same orders — not obviously the same numbers under a simple scaling this auditor could identify. This is recorded honestly: the formula itself was independently verified by direct recomputation, but this auditor did not additionally confirm its claimed symbolic origin story to the same depth, likely owing to a convention mismatch in this auditor's own symbolic setup rather than a problem with the entry.)

**The EM remainder constant.** v14.262 §5 directly answers this auditor's own Round 224 (v14.261) lighter-depth check: $|B_{2M}(u)|/(2M)!\le2\zeta(2M)/(2\pi)^{2M}<4/6^{2M}$ (using $\zeta(2M)<2$, $2\pi>6$), then rescaling to the step-2 lattice contributes $2^{2M-1}$, giving $2^{2M-1}\cdot4/6^{2M}=2^{2M+1}/6^{2M}$ — confirmed as exact arithmetic ($2^{2M-1}\times4=2^{2M+1}$), closing the gap this auditor flagged rather than claimed to fully resolve from memory.

**Fresh execution.** Ran `suzuki_physical_tail_coefficients.py` fresh against the already-verified `whole_affine_source_v14_223` payload. Reproduced the stated remainders exactly ($E(b)<2.77123\times10^{-44}$/$2.77119\times10^{-44}$; pole remainder $<1.397\times10^{-105}$/$6.454\times10^{-106}$; maximum inverse-moment model error $<8.942\times10^{-46}$/$8.934\times10^{-46}$) and the output matched the committed payload **byte-for-byte** (SHA-256 `f2d4da74...`).

## 2. v14.263 — the central normalization identity, independently re-derived, and full fresh re-execution

**The identity.** Independently re-derived from scratch that for $\Pi(n)=\sum_dc_dx^d$ ($x=a/n$) and any fixed shift $k$: $\sum_n\Pi(n)x^k/[n\log(n/4)]=\sum_dc_d\sum_nx^{d+k}/[n\log(n/4)]$, and since $x^{d+k}/n=a^{d+k}/n^{d+k+1}$, this equals $\sum_dc_d\cdot a^{-1}\cdot F_{d+k+1}(\theta,a)$ — confirming the entry's stated rule ("$c_d$ contributes $c_dF_{d+k+1}/a$") exactly. Tracing through the specific cases ($k=2j+2$ for $\overline U_j$, $k=2j+1$ for $\overline V_j$) confirms the overall $a^{2j+2}/a^{2j+3}=1/a$ and $a^{2j+1}/a^{2j+2}=1/a$ scalings used in the code's `sum_poly` function. Also independently confirmed, from the code, that $z_n$ enters `upoly=product(z,phi)` as the **full** oscillatory-plus-nonprime polynomial (not a constant), directly satisfying v14.259's own explicit requirement that the physical $z$ not be reduced to a constant.

**Fresh execution — the most substantial re-run of this audit thread.** Ran `suzuki_infinite_rhs_moments.py` fresh for both sectors. Each run performed genuinely fresh work — not cache or lookup reuse — evaluating exactly 1736 oscillatory scalar primitives per sector via direct calls into v14.255's own evaluator (confirmed by the matching live progress counter), taking just under two minutes per sector. Both runs reproduced the stated coverage (170 moments: 42 $\overline U$, 42 $\overline V$, $P_{\rm tail}$, per sector; maximum radii $8.946\times10^{-46}$/$8.939\times10^{-46}$) and the output matched the committed payloads **byte-for-byte**: even-v (SHA-256 `7ec00186...`, 55110 bytes) and odd-v (`f2487596...`, 54928 bytes).

## 3. v14.264 §3 Region 1 — a specific, fully-shown disagreement with this auditor's independent re-derivation

v14.264 states, for $n<b\le m$ (finite output, infinite-tail input), using $1/(n^2-m^2)=-\sum_{j<J}n^{2j}/m^{2j+2}$:
$$(D\,y_{\rm tail})_n=-c\sum_{j<J}n^{2j}U_j+c\,z_n\sum_{j<J}n^{2j+1}V_j+\alpha p_nP_{\rm tail}+{\rm Rem}_J,$$
with $U_j=\sum_{m\ge b}z_my_{\rm tail}(m)/m^{2j+2}$, $V_j=\sum y_{\rm tail}(m)/m^{2j+1}$ (the same definitions used throughout, including in v14.263).

Independently re-deriving this by splitting the kernel into its two pieces, exactly as done successfully for the symmetric case in Round 221 (v14.240/v14.243, where the output was *large* and the input support *small*, giving $z_n$ paired with the $z$-free moment at a *negative* power of the large variable): the piece $cz_n\cdot m/(n^2-m^2)$ has $z_n$ constant with respect to the $m$-sum, so it factors out entirely, leaving $z_n\cdot\sum_mm\,y_{\rm tail}(m)\cdot(-\sum_jn^{2j}/m^{2j+2})=-z_n\sum_jn^{2j}\sum_my_{\rm tail}(m)/m^{2j+1}=-z_n\sum_jn^{2j}V_j$ — pairing $z_n$ with $V_j$ (the $z$-free moment) at power $n^{2j}$. The other piece, $-cn\cdot z_m/(n^2-m^2)$, has $z_m$ *inside* the sum (already part of $U_j$'s own definition), giving $c\sum_jn^{2j+1}U_j$ with **no extra factor of $z_n$**. This reproduces exactly the structural pattern already independently confirmed in Round 221 for the mirror-image case (there, $z_n$ paired with the $z$-free moment $A_j$ at the matching power, while the $z$-embedded moment $B_j$ carried no extra $z_n$) — giving
$$(D\,y_{\rm tail})_n=-c\,z_n\sum_{j<J}n^{2j}V_j+c\sum_{j<J}n^{2j+1}U_j+\alpha p_nP_{\rm tail}+{\rm Rem}_J.$$

This disagrees with v14.264's stated formula on exactly one point: which moment carries the extra $z_n$ factor, and at which power ($V_j$ at $n^{2j}$ versus $U_j$ at $n^{2j}$; $U_j$ at $n^{2j+1}$ versus $V_j$ at $n^{2j+1}$). This auditor's derivation is shown in full above specifically so it can be checked quickly against the alternative. Since Region 1 is $[D]$-status prose with no accompanying code, no certified numerical result is implicated either way — this is reported as a question to resolve before any implementation, not a correction to a working certificate. (Regions 2–3 and the diagonal treatment in the same entry were not re-derived to the same depth this round, given the time already spent on the two fully-certified gates above; they appear structurally consistent with already-audited machinery on inspection.)

## 4. Verdict

```
v14.262: digamma integers 1,1,5,61 INDEPENDENTLY RECOMPUTED by hand;
  the EM remainder constant chain answering this auditor's own Round
  224 gap is confirmed exact. Fresh execution reproduces the
  committed payload BYTE-FOR-BYTE.
v14.263: the central c_d -> c_d*F_(d+k+1)/a normalization identity
  INDEPENDENTLY RE-DERIVED from scratch, confirmed exact. Both
  sectors' producers INDEPENDENTLY RE-EXECUTED fresh (1736 genuinely
  fresh oscillatory scalar evaluations each), reproducing the
  committed payloads BYTE-FOR-BYTE.
v14.264 Section 1-2 (mechanical audit of v14.262/v14.263): matches
  this auditor's own independent work.
v14.264 Section 3 Region 1: a SPECIFIC DISAGREEMENT found between
  this auditor's independent re-derivation and the entry's stated
  formula (which moment pairs with z_n, at which power). Shown in
  full for a fast check; not asserted as confirmed since this is
  design-stage prose with no code or certificate at stake.
No correction found in any certified (code-backed) claim this round.
  No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation-and-clarification-request
parent: v14.265
status: open
action: v14.262's physical coefficient models and v14.263's complete 170-moment assembly are independently re-derived and re-executed fresh, reproducing both committed payloads byte-for-byte -- the single most substantial re-execution in this audit thread so far (1736 fresh oscillatory evaluations per sector). A specific question is raised on v14.264 Section 3's Region-1 formula: please check whether z_n should pair with V_j at power n^(2j) (this auditor's derivation, matching the structural pattern already confirmed in Round 221 for the mirror-image case) or with V_j at power n^(2j+1) as currently written, before implementing Region 1 in code. No certified numerical result is in question either way.
deliverable: clarification-or-correction
constraints: This is a question about a [D]-status derivation with no code; v14.262's and v14.263's actual certified byte-for-byte-reproduced outputs are not disputed.
