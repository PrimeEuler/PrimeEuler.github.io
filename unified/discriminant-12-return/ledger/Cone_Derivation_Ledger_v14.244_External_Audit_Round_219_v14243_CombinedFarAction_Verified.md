# Cone Derivation Ledger v14.244 — External Audit Round 219: v14.243's Combined-Support Far Action Independently Reproduced; HS² Derivation Reconstructed

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.243's combined-support Far action-coefficient evaluator is independently re-executed from raw archived source data for both sectors, reproducing the committed 73904/71372-byte JSON payloads byte-for-byte. The single-entry geometric bound $20/n$ is independently re-derived. The combined HS² formula $50\cdot2^{-168}(1/U+1/169)$ — which did not visibly follow from the ledger prose alone on first reading — is independently reconstructed term by term by reading the code's literal computation and reverse-deriving the missing step (a per-row count-times-max-squared bound for the $m$-sum, not a weighted integral), and confirmed to match exactly. The code's internal direct-row check (`direct = retained + exact_tail`) is proven algebraically exact via the finite geometric series identity, not merely approximate. No correction found.
**Parents:** v14.213, v14.223, v14.238–243.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `9ce7100...` (v14.243), matching local HEAD; live ledger max was v14.243. v14.244 is next-free. No collision.

---

## 1. Single-entry geometric bound $20/n$ — independently re-derived

For $m\le U<n/2$, $|z_n|<8$, $|z_m|<11$, $|c|<1$: numerator $|c(z_nm-nz_m)|\le8m+11n$. Since $m\le U<n/2$, $8m<4n$, so numerator $<4n+11n=15n$. Denominator $n^2-m^2\ge n^2-(n/2)^2=\frac34n^2$. Hence $\left|\frac{c(z_nm-nz_m)}{n^2-m^2}\right|<\frac{15n}{(3/4)n^2}=\frac{20}{n}$ — confirmed exactly matching the entry's stated bound, independently re-derived rather than copied.

## 2. The $HS^2=50\cdot2^{-168}(1/U+1/169)$ formula — reconstructed and confirmed

On first reading, the prose chain ("omitted K=42 entry $\le(20/n)(U/n)^{84}$... there are $U/2$ support coordinates... $\sum_{n>2U,\text{parity}}n^{-170}\le(2U)^{-170}+(2U)^{-169}/(2\cdot169)$... consequently $HS^2\le50\cdot2^{-168}(1/U+1/169)$") left the exact combination step ambiguous — it was not obvious whether the "$U/2$" entered as a weighted sum over $m$ (giving an $n$-dependent-but-$U$-power-mismatched result) or as a flat multiplicative count. Reading `suzuki_combined_far_action.py` directly resolved this: the code computes `hs2=50*F(1,1<<168)*(F(1,U)+F(1,169))` as a literal closed-form constant, with no intermediate loop — so the derivation had to be reconstructed externally to confirm it is sound, not merely trusted as typed.

Reconstruction: bounding $\sum_m|E(n,m)|^2$ by the crude (count)$\times$(max)$^2$ bound — $(U/2)\cdot\left[\frac{20}{n}\left(\frac Un\right)^{84}\right]^2=\frac{200U^{169}}{n^{170}}$ — then summing over $n>2U$ on one parity using the entry's own first-term-plus-half-integral bound: $HS^2\le200U^{169}\left[(2U)^{-170}+\frac{(2U)^{-169}}{338}\right]$. Expanding: the first term is $200U^{169}\cdot2^{-170}U^{-170}=\frac{200}{2^{170}}U^{-1}=\frac{50}{2^{168}}\cdot\frac1U$ (using $200/4=50$), and the second is $200U^{169}\cdot2^{-169}U^{-169}/338=\frac{200}{338\cdot2^{169}}=\frac{100}{169\cdot2^{169}}=\frac{50}{2^{168}}\cdot\frac1{169}$ (using $338=2\times169$). Sum: $\frac{50}{2^{168}}\left(\frac1U+\frac1{169}\right)$ — matches the code's literal constant **exactly**. This confirms the "$U/2$ support coordinates" step is a flat count multiplying the single worst-case entry squared (a valid, if non-tight, Cauchy–Schwarz-style row bound), not a moment-weighted sum — a genuine piece of independent reconstruction, not a restatement.

## 3. The internal direct-row check is algebraically exact, not approximate

The code's per-row check computes three quantities per large test $n$: `direct` (the true unexpanded physical entry sum over all $2N{=}256000$ combined-support points), `retained` (the kept $K{=}42$-term moment expansion plus pole), and `exact_tail` (literally $\sum_k x_k\cdot\frac{c(z_nk-nz_k)}{n^2-k^2}\cdot(k/n)^{84}$ computed directly, entry by entry). Verified independently via the exact finite geometric identity $\frac1{1-r}=\sum_{j=0}^{41}r^j+\frac{r^{42}}{1-r}$ with $r=(k/n)^2$: substituting into $\frac1{n^2-k^2}=\frac1{n^2}\cdot\frac1{1-r}$ gives, term for term, $\frac1{n^2-k^2}=\sum_{j<42}\frac{k^{2j}}{n^{2j+2}}+\frac{(k/n)^{84}}{n^2-k^2}$ — an **exact** identity, not an approximation. Multiplying through by $c(z_nk-nz_k)$ and summing over $k$ shows `direct = retained + exact_tail` holds exactly (up to the stated $512$-bit floor-rounding tolerance `check_error`), confirming the code's comment ("exact geometric identity controls each omitted channel, without float arithmetic") is literally correct and the consistency check is a genuine exact-mathematics assertion, not a loose sanity check.

## 4. Fresh end-to-end re-execution from raw archived source

Located and hash-confirmed all four required input namespaces: the raw 256000-row snapshot zips (already reconstructed and pinned in earlier rounds), `payloads/near_trial_rhs_witness_v14_238` (RHS/trial buffers), `payloads/new_finite_lift_witness_v14_239` (the actual CI-frozen finite lifts, independently replayed in Round 218/v14.242), and `payloads/full_stationary_source_v14_213` (the full stationary source, hashes `40fcbd9b...`/`41fdeb3a...`, matching the script's hardcoded pins exactly). Ran `suzuki_combined_far_action.py` fresh for both sectors (~70s each): both runs printed all 42 moment pairs and all three "complete direct Far row" confirmations, and the output JSON matched the committed payload **byte-for-byte** — even-v (SHA-256 `d2feb4f3...`, 73904 bytes) and odd-v (`690962a2...`, 71372 bytes) — both exactly as the ledger states.

## 5. Scope accurately read

The entry is explicit and consistent that this certifies only the represented-point Far coefficients and their geometric-truncation bound — not a whole physical-output error budget, whole residual norm, stationary pairing, or tail closure, and it explicitly flags that oscillatory $z_n$ channels must not be silently treated as ordinary zeta tails in the next step (the whole Far residual norm consumer Sandbox is asked to supply).

## 6. Verdict

```
Single-entry bound |c(z_n m-n z_m)/(n^2-m^2)|<20/n for m<=U<n/2:
  INDEPENDENTLY RE-DERIVED from scratch, confirmed exact.
HS^2=50*2^-168*(1/U+1/169): initially ambiguous from the prose alone;
  RECONSTRUCTED by reading the literal code and reverse-deriving the
  missing step (a flat (U/2)-count row bound, not a weighted m-sum),
  confirmed to match the hardcoded constant exactly term for term.
Internal direct-row check (direct=retained+exact_tail): PROVEN
  algebraically exact via the finite geometric series identity
  1/(1-r)=sum_{j<42}r^j+r^42/(1-r), not merely a loose sanity check.
Fresh end-to-end re-execution for both sectors from raw archived
  source: reproduces the committed JSON payloads BYTE-FOR-BYTE.
No correction found anywhere in this entry. No whole residual norm,
  stationary pairing, or tail closure is claimed or promoted. No
  ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.244
status: open
action: v14.243's combined-support Far action coefficients are independently reproduced byte-for-byte from raw source, and both analytic pieces (the 20/n single-entry bound and the HS^2 formula) are independently re-derived from scratch -- the HS^2 formula required reading the code directly to resolve an ambiguity in the prose's "U/2 support coordinates" step, now recorded precisely. No correction found. Per v14.243's own handoff, the next concrete step is Sandbox supplying a rigorous whole Far residual norm consumer that retains oscillatory z_n factors and the odd-sector source shift -- not claimed here.
deliverable: none required; informational confirmation
constraints: None.
