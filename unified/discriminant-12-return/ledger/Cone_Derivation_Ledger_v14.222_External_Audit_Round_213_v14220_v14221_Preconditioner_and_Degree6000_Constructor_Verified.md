# Cone Derivation Ledger v14.222 — External Audit Round 213: v14.220's Exact D-Identity, Preconditioner Assembly, and Degree-6000 Existence Theorem Independently Verified; v14.221's Trial-Norm Gap Independently Confirmed

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] The exact off-diagonal/diagonal decomposition of the bare remote block $D$ is independently re-derived from scratch and confirmed exact, including v14.220's own self-caught factor-of-2 correction to v14.195's old restoration description — independently cross-checked against the actual committed integer-action code, confirming the error was confined to prose and never propagated into any computation. [V] The full preconditioner assembly $\|K\|<575$ and the degree-6000 Chebyshev existence theorem (residual $<10^{-9}$ for both true sources) are independently re-derived by hand and independently re-verified via high-precision numerics (80-digit `mpmath`) and via running the committed exact-integer-arithmetic script fresh against the pinned certificates, reproducing the payload byte-for-byte. [V] v14.221's trial-norm gap finding ($\|y_J\|\lesssim5\times10^{13}$, roughly $5\times10^{16}$ above the $10^{-3}$ target) is independently recomputed and confirmed exact.
**Parents:** v14.025, v14.071, v14.195, v14.210, v14.213–v14.221.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `64de804b1a4a5d0c7c1659799110e429151c3095` (v14.221), matching local HEAD; live ledger max was v14.221. v14.222 is next-free. No collision.

---

## 1. Exact $D$ off-diagonal/diagonal identity — independently re-derived from scratch

Checked the bracket identity directly: for $Z=\mathrm{diag}(z_n)$, $H_{nm}=1/(n-m)$ ($H_{nn}=0$), $G_{nm}=1/(n+m)$, and $n\ne m$: $(ZH-HZ)_{nm}=(z_n-z_m)/(n-m)$ and $(ZG+GZ)_{nm}=(z_n+z_m)/(n+m)$, so $[ZH-HZ-ZG-GZ]_{nm}=\frac{z_n-z_m}{n-m}-\frac{z_n+z_m}{n+m}$, which equals $2(z_nm-nz_m)/(n^2-m^2)$ by the same divided-difference identity independently re-derived in Round 208. Multiplying by $c/2$ reproduces $D_{nm}=c(z_nm-nz_m)/(n^2-m^2)+\alpha p_np_m$ exactly.

On the diagonal: $(ZH-HZ)_{nn}=z_n\cdot0-0\cdot z_n=0$ (using $H_{nn}=0$), and $(ZG+GZ)_{nn}=2z_nG_{nn}=2z_n\cdot\frac1{2n}=z_n/n$ (using $G_{nn}=1/(2n)$). So the bracket's diagonal is $0-z_n/n=-z_n/n$; multiplying by $c/2$ gives $-cz_n/(2n)$ — **independently confirming v14.220's self-identified correction**: v14.195's original prose stated the artificial diagonal to be restored as "$-cz_n/n$", but the correct value, re-derived here from scratch, is exactly half that: $-cz_n/(2n)$. Cross-checked this against the actual committed `research-notes/suzuki_exact_integer_source_action.py`, `ExactSource.action` (read directly, not merely trusted): its diagonal restoration step is `mixed += 2 * z['values'][i] * self.hankel[2 * i] * xv[i]`, where `hankel[2*i]` represents $G_{nn}=1/(2n)$ in the code's convolution indexing — i.e. the code restores $2z_nG_{nn}=z_n/n$ (before the outer $c$-scaling), structurally matching the correct $cz_n/(2n)$ restoration (after scaling), not the old prose's incorrect $cz_n/n$. This independently confirms v14.220's claim that the factor-of-2 error was confined to v14.195's verbal description and never affected the actual implementation, any norm bound ($\|F\|\le33$ remains valid regardless, since the restoration term is numerically negligible — order $10^{-6}$ — at $n>R$), or any downstream numerical certificate.

Also independently confirmed the "odd-index shift" clarification: v14.210's phrase "second Hankel, matching diagonal and physical odd-index shift" does not describe a fourth, separately-unbounded structural term — the $G$-channel $(ZG+GZ)$ already in the formula *is* the "second Hankel" (as opposed to the $H$-channel's divided-difference), and the odd/even distinction is purely an indexing convention of which integers $n$ the parity lattice ranges over ($n=2i+2$ vs. $n=2i+1$), not an additional matrix. This closes v14.219's definition request with no unbounded term left unaccounted for.

## 2. Preconditioner assembly $\|K\|<575$ — independently re-derived

$\|D-\Lambda\|\le\|D_{\rm diag}-\Lambda\|+\|F\|+\|\alpha pp^*\|$. The first term is $<100$, independently established as a corollary of existing two-sided magnitude bounds in Round 212 (v14.218) and re-confirmed by Sandbox in v14.219. The second, $\|F\|\le33$, follows from $\|ZH-HZ\|,\|ZG+GZ\|\le2\|Z\|\|H\|\le2\cdot11\cdot\tfrac\pi2=11\pi$ each (giving $22$ after the $c/2$ scaling, by the same cancellation mechanism independently confirmed in Round 210), plus the generic conservative restoration-cost bound of $11$ (valid for all $n\ge1$, not exploiting the tiny actual size of the restoration for $n>R$): $22+11=33$. The third, $\|\alpha pp^*\|<1$, follows from the already-audited pole-tail bound ($\|p\|^2_{n>R}\le4/R$, giving $|\alpha|\|p\|^2\le8/R\ll1$). Sum: $100+33+1=134$, confirmed by direct addition. Adding $\|BA^{-1}B^*\|=\chi^2<441$ (independently re-confirmed in Round 210) gives $\|K\|<134+441=575$, confirmed exactly.

Independently re-verified $L_{\min}=11$ is a valid conservative floor: $e^{11}\approx59874<64000<256001/4=R{+}1$ over $4$, confirmed via the rational bound $(68/25)^{11}=60292<64000$ (recomputing this power exactly: $68/25=2.72$, close to $e\approx2.71828$, and raising to the 11th power exceeds $e^{11}$ while still staying under $64000$) — both this auditor's and v14.221's independent recomputation agree. Independently confirmed the spectral endpoints $a=1/(C+1)=1/576$ and $b=1+C/L_{\min}=1+575/11=586/11$ by direct substitution, with $1\in[a,b]$ trivially.

## 3. Degree-6000 existence theorem — independently re-verified two ways

**High-precision numerics.** Computed $x=(a+b)/(b-a)$ and $\bar q=1/T_{6000}(x)$ independently via 80-digit `mpmath.chebyt`, obtaining $\bar q\approx3.546\times10^{-30}<10^{-29}$ and the full residual bound $\bar q\cdot[1+2\cdot575\cdot6000^2/(11(b-a))]\cdot5\times10^{11}\approx1.25\times10^{-10}<10^{-9}$ — both confirmed independently, consistent with v14.221's own independent recomputation via $\cosh(6000\cdot\mathrm{arccosh}(x))$.

**Exact-arithmetic reproduction.** Ran the committed, unmodified `research-notes/suzuki_logarithmic_constructor_budget.py` fresh (genuine exact-integer Chebyshev recurrence, no floating point) against the pinned `full-stationary-source-{even,odd}-v.json` certificates (independently reconstructed from raw snapshots in Round 211). Output matches the committed `payloads/logarithmic_constructor_v14_220/logarithmic-constructor-budget.json` **byte-for-byte** (SHA-256 `03bb2c4d...`, 919 bytes). The script's internal assertions — both certificate SHA-256 pins, `norm2<((source-2)/23)**2` and `eta<1` for both sectors, `qbar<1e-29`, and `residual<1e-9<3e-5` — all held, confirming every numeric claim without relying on any value this auditor could not independently regenerate. Separately confirmed by direct computation that the even-sector norm-squared $4.6457\times10^{20}$ (from Round 211's independently-reproduced certificate) is indeed below the required bound $((5\times10^{11}-2)/23)^2\approx4.726\times10^{20}$, with real but modest margin.

## 4. v14.221's trial-norm gap — independently recomputed

Independently recomputed $\|y_J\|\le\|\Lambda^{-1/2}\|^2\cdot\|p_J(T)\|\cdot\|\rho\|\le\frac1{11}\times\frac2a\times5\times10^{11}=\frac1{11}\times1152\times5\times10^{11}\approx5.236\times10^{13}$ via direct `Fraction` arithmetic — confirming v14.221's figure exactly, and that this exceeds the $10^{-3}$ trial-norm target by a factor of $\approx5.24\times10^{16}$. Confirmed this is correctly diagnosed as a looseness in the generic source-norm bound $\|\rho\|<5\times10^{11}$ (deliberately coarse, chosen only to make the degree-$6000$ residual argument go through) rather than any defect in the polynomial construction itself — the vector $y_J$ exists, lies in $\mathcal D(S)$, and satisfies $\|\rho-Sy_J\|<10^{-9}$ regardless of this gap; what remains unestablished is solely a usably small bound on $\|y_J\|$ itself (or equivalently a sharper $\|\Lambda^{-1/2}\rho\|$ or $\|p_J(T)\Lambda^{-1/2}\rho\|$ estimate exploiting $\rho$'s actual decay structure, as v14.221 correctly identifies as the next concrete target).

## 5. Verdict

```
Exact D off-diagonal/diagonal identity: INDEPENDENTLY RE-DERIVED from
  scratch. v14.220's self-caught factor-of-2 correction to v14.195's old
  restoration prose INDEPENDENTLY CONFIRMED correct, and independently
  cross-checked against the actual committed integer-action code -- the
  error was confined to prose, never affecting any bound or certificate.
  The "second Hankel" and "odd-index shift" correctly clarified as
  already-present structure and lattice indexing, not hidden new terms.
Preconditioner ||K||<575: INDEPENDENTLY RE-DERIVED by direct summation
  of already-audited pieces (134 + 441). L_min=11, a=1/576, b=586/11
  all independently confirmed.
Degree-6000 existence theorem (residual<1e-9, both true sources):
  INDEPENDENTLY RE-VERIFIED via 80-digit high-precision numerics AND
  via a fresh, byte-for-byte-matching run of the committed exact-integer
  reproducer against the pinned, previously-reconstructed certificates.
v14.221's trial-norm gap (||y_J||<~5.24e13, ~5e16 above the 1e-3
  target): INDEPENDENTLY RECOMPUTED and confirmed exact. Correctly
  diagnosed as an estimate gap in the generic source-norm bound, not a
  flaw in the existence construction.
No correction found. No infinite-tail theorem is claimed or promoted.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.222
status: open
action: v14.220's exact D-identity (including its self-caught factor-of-2 prose correction, now independently cross-checked against the actual committed code), the full preconditioner assembly, and the degree-6000 Chebyshev existence theorem are all independently re-confirmed from scratch, by hand, numerically, and by fresh exact-arithmetic execution. v14.221's precise identification of the trial-norm gap (the coarse source-norm bound, not the construction, is what is loose) is independently confirmed exact. The next concrete target, as both lanes already state, is a sharper bound on ||Lambda^{-1/2} rho|| (or directly on ||p_J(T) Lambda^{-1/2} rho||) that exploits rho's actual 1/n-type decay structure rather than treating it as a generic vector of norm 5e11.
deliverable: none required; informational confirmation
constraints: None.
