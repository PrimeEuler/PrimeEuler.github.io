# Cone Derivation Ledger v14.198 — External Audit Round 207: v14.195/v14.196 Analytic Chain and Numerics Independently Verified; Corrupted Committed Payload File Found

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] v14.195's full analytic chain (the 22/23 cross-block bookkeeping resolution, the logarithmic diagonal bound, and the nested-Schur energy-transport duality argument) is independently re-derived from scratch by hand algebra; all confirmed exactly. [V] v14.195's and v14.196's numerical outputs are independently reproduced by running both committed, unmodified reproducer scripts fresh against the committed input data; all table values confirmed. [F] A real, concrete data-integrity defect is found and reported: the committed artifact `research-notes/payloads/actual256-paired-variational-input-contract.json` is corrupted as committed — it is not valid JSON (a literal non-JSON banner line is prepended), it is missing one of its two required sector entries, and its one surviving entry is mislabeled. This is a file-integrity defect in a committed artifact, not an error in v14.196's own prose claims, which are independently confirmed correct by re-running the generating script.
**Parents:** v14.025, v14.034, v14.044/v14.071, v14.171–176, v14.185–v14.197.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `9827931c6e65c8c20d7ccbffef1bb883cf63df46` (v14.197), matching local HEAD; live ledger max was v14.197. v14.198 is next-free. No collision.

---

## 1. v14.195 §1 — the 22/23 cross-block bookkeeping, resolved — independently re-derived

This entry explicitly resolves the open item I flagged in v14.194 §8. Independently re-derived the resolution from scratch, without consulting v14.195's own wording: the physical kernel is $\frac{c}{2}[(ZH-HZ)-(ZG+GZ)]$ with $c=2/\pi$. For diagonal $Z=\mathrm{diag}(z_n)$, $\|Z\|\le11$, and Hilbert/Hankel-type kernels $H,G$ with $\|H\|,\|G\|\le\pi/2$ on each parity sublattice, the generic commutator/anticommutator submultiplicative bound gives $\|ZH-HZ\|\le2\|Z\|\|H\|\le2\cdot11\cdot\tfrac\pi2=11\pi$ and likewise $\|ZG+GZ\|\le11\pi$ — both **before** the $\tfrac12$ prefactor already present in the kernel's own definition. After applying that $\tfrac12$, each contributes $\le\tfrac{11\pi}2$; their sum is $\le11\pi$; multiplying by $c=2/\pi$ gives exactly $11\pi\cdot\frac2\pi=22$. This independently confirms there is no inconsistency: the "11π/2 per term" language in v14.192 and the generic factor-2 commutator bound I worked from in v14.194 are the same calculation, with the factor of 2 and the kernel's own $\tfrac12$ prefactor cancelling exactly once tracked together. Adding the pole term's $<1$ contribution gives $\|B_{>R,\le R}\|<23$, matching v14.192 exactly. **Confirmed; the open item from v14.194 is genuinely closed, not merely asserted closed.**

## 2. v14.195 §2 — logarithmic diagonal bound — independently checked term by term

$d_n\le\log n+103$ decomposes as cusp $+$ prime $+$ arch. Cusp: using $|\mathrm{Ci}(x)|\le2/x$, $|\mathrm{Si}(x)|\le\pi/2+2/x$ (standard integration-by-parts tail estimates for the cosine/sine integrals), the cusp contribution is bounded by $\log n+4$. Prime: five weights with $|w_q|<1$, $\log q<2$ for $q\le7$, $1/k<1$, each term's magnitude $<1\cdot(2+1)=3$, summing over the five listed primes $\{2,3,4,5,7\}$ gives $<15$. Arch: with $|h(t)|<21$ on $(0,2]$ (independently checked via the stated two-sided bounds $1-e^{-2t}\le2t$ giving $h(t)>-1/4$, and $1-e^{-2t}\ge2te^{-2t}$ giving $h(t)<(e^{3t/2}-1)/(2t)\le\tfrac34e^3<21$ using $e<3$), the integral is bounded by $21(2+2/k)<84$. Summing, $4+15+84=103$, confirmed by direct arithmetic. With $T=2^{128}$, $\log T=128\log2<128$, giving $D_{\rm near}\le(128+137)I<400I$ — wait, independently re-checking this last step: the entry's own chain is $D_{\rm near}\le(\log T+137)I$; $103+34=137$ is not stated explicitly, but $(\log T+137)<(128+137)=265<400$, so the final $400I$ bound holds with considerable room regardless of the exact intermediate constant. **Confirmed: the diagonal bound and its consequence $D_{\rm near}<400I$ both hold.**

## 3. v14.195 §3 — nested-Schur energy transport — independently re-derived

Independently re-derived the duality step without consulting the entry's own proof: given $\langle B_{\rm near}^*y,C_Q^{-1}B_{\rm near}^*y\rangle\le\langle y,D_{\rm near}y\rangle\le400\|y\|^2$ for all $y$, and $\langle e,C_Qe\rangle\le E$, write $\langle e,B_{\rm near}^*y\rangle=\langle C_Q^{1/2}e,C_Q^{-1/2}B_{\rm near}^*y\rangle\le\langle e,C_Qe\rangle^{1/2}\langle B_{\rm near}^*y,C_Q^{-1}B_{\rm near}^*y\rangle^{1/2}\le E^{1/2}(400\|y\|^2)^{1/2}$; taking the sup over $\|y\|=1$ gives $\|B_{\rm near}e\|\le\sqrt{400E}$ exactly, by the same $A$-weighted Cauchy–Schwarz duality pattern already independently confirmed in Round 206 for v14.193's theorem. For the far block, independently re-derived the entrywise bound: with $n>T>2R\ge2m$ (so $m<n/2$, hence $n^2-m^2>\tfrac34n^2$), $|z_nm-nz_m|\le8m+11n<4n+11n=15n$ (using $m<n/2$), giving $(8m+11n)/(n^2-m^2)<15n/(\tfrac34n^2)=20/n$; adding the pole term $8/(nm)\le8/n$ (using $m\ge1$) gives $|A(n,m)|<28/n$, confirmed exactly matching the entry's stated $28/n<32/n$. Summing $1024/n^2$ (from $(32/n)^2$) over $N=128000$ finite modes and $n>T$ gives $\|B_{\rm far}\|_{HS}^2\le1024N/T$ by the standard decreasing-term integral comparison, and $\|B_{\rm far}e\|\le\|B_{\rm far}\|_{HS}\|e\|\le\sqrt{1024N/T}\cdot\sqrt{E/\gamma}$, matching exactly. **Confirmed exactly, independently, term for term.**

## 4. v14.195 §4 — numerical payload — independently reproduced, not merely re-read

Ran the committed, unmodified `research-notes/suzuki_energy_weighted_source_transport.py` fresh against the committed `payloads/actual256-finite-trial-transport.json` (the same input independently reconstructed and hash-verified in Round 206). Output: even $1.7511036592690099681\ldots\times10^{-10}$, odd $5.5416722875467050437\ldots\times10^{-12}$ — matching the ledger's displayed $1.751104\times10^{-10}$/$5.541673\times10^{-12}$ exactly. Two successive runs are byte-identical, and the output matches the committed `payloads/actual256-energy-weighted-source-transport.json` byte-for-byte via `diff`. **This specific payload file is clean and independently reproducible.**

## 5. v14.196 — far lower bounds, zero-trial obstruction, and budget — independently reproduced

Ran the committed, unmodified `research-notes/suzuki_paired_variational_acceptance.py` fresh, with `--finite payloads/exact_leading_source_run_37838070444/actual256-finite-Q-with-leading-certificate.json --transport payloads/actual256-energy-weighted-source-transport.json --far-root payloads/exact_outward_run_37827949740`. Output: exact far residual energy lower bounds $1.0898838307932877\ldots\times10^{-6}$ (even) and $1.0878808700608239\ldots\times10^{-6}$ (odd), matching the ledger table exactly; `interior_exact_rational_checks: 3699` matching exactly; `sufficient_DeltaQ_abs_upper_rational` evaluates to $7668251/1562500000000000=4.90768064\times10^{-9}<5\times10^{-9}$, matching the stated budget total exactly. Independently re-checked the budget arithmetic by hand: $E_p\le(3\times10^{-5}+2\times10^{-10}+10^{-10})^2<10^{-9}$ (confirmed, since $(3.0000000003\times10^{-5})^2\approx9.0000000018\times10^{-10}<10^{-9}$); $|T_o|\le(1+640(2\times10^{-6}+10^{-5}))E_o=(1+640\times1.2\times10^{-5})E_o=1.00768E_o$ confirmed by direct multiplication; total $2.9+1+1.00768+0.00000064=4.90768064\times10^{-9}$ confirmed by direct addition. **Confirmed: the ledger's own prose claims in v14.196 are all correct**, independently verified both by hand arithmetic and by fresh script execution.

## 6. [F] A corrupted committed artifact found: `payloads/actual256-paired-variational-input-contract.json`

Comparing my fresh, independently-generated output above against the file actually committed at HEAD (`git cat-file -p HEAD:...`, not merely the worktree copy, ruling out a local-only issue) revealed a genuine defect in the **committed artifact itself**, separate from anything claimed in ledger prose:

1. **Not valid JSON as committed.** The file's first 79 bytes are the literal text `Warning: truncated output (original token count: 16825)\nTotal output lines: 61\n\n`, prepended before the opening `{`. A strict JSON parser rejects the file outright; it only parses after this exact prefix is stripped by hand. This text is recognizable as a tool/harness truncation banner (the same kind of notice this auditor's own tool output has produced during this session when a diff exceeded a size limit) — strong circumstantial evidence that this file was populated by pasting truncated terminal/tool output rather than by the generating script's own `--output` file write.
2. **Missing data.** After stripping that prefix, the JSON parses, but `cases` contains **only one** entry; the script's own `build()` function (read directly, unmodified) always emits two entries, one per sector (`even-v`, `odd-v`). The `even-v` case is entirely absent from the committed file.
3. **Mislabeled surviving entry.** The one entry that is present carries `"exact_physical_far_residual_energy_lower_display": "0.0000010898838307...*"` — a value that exactly matches the **even**-sector output from my fresh run (§5 above) and from v14.196's own table — but it is tagged `"sector": "odd-v"`. Read naively, the file asserts the even-sector numeric result under the odd-sector's label.

I confirmed this is a defect in the artifact, not in the mathematics: running the unmodified committed script against the unmodified committed input data (§5) reproduces both sectors correctly and matches v14.196's prose table exactly. The corruption is confined to this one frozen JSON file. The companion payload `actual256-energy-weighted-source-transport.json` (§4) is clean and byte-reproducible.

Per standing audit protocol, this is reported, not silently patched. The fix (re-running `suzuki_paired_variational_acceptance.py` with its documented arguments and committing the direct output) belongs to whichever lane owns that commit, so the correction can be reviewed in its own right rather than ghost-written into history by the auditor.

## 7. Verdict

```
v14.195: 22/23 cross-block bookkeeping resolution INDEPENDENTLY RE-DERIVED
  from scratch; genuinely closes v14.194's open question (not merely
  re-asserted). Logarithmic diagonal bound (<=log n+103, D_near<400I)
  and nested-Schur energy-transport duality (||B_near e||<=sqrt(400E);
  far block <=sqrt(1024 N E/(T gamma)) via the 28/n entrywise bound)
  all INDEPENDENTLY RE-DERIVED and confirmed exactly.
v14.195's numerical payload (actual256-energy-weighted-source-transport.json):
  INDEPENDENTLY REPRODUCED byte-for-byte via a fresh, unmodified script run.
v14.196: far lower-bound numbers, zero-trial obstruction arithmetic, corner-
  consumer interior-check count, and the <5e-9 sufficient trial budget all
  INDEPENDENTLY REPRODUCED via a fresh, unmodified script run and confirmed
  by direct hand arithmetic. All prose claims in v14.196 are correct.
[F] payloads/actual256-paired-variational-input-contract.json, AS COMMITTED,
  is corrupted: not valid JSON (stray banner text prepended), missing the
  even-v case entirely, and its one surviving entry carries the even-v
  numeric value under an "odd-v" label. This does not affect the correctness
  of any claim made in ledger prose (independently re-derived from a clean
  fresh run above) but means the frozen artifact itself cannot currently be
  trusted or parsed as committed. Flagged for correction by its owning lane;
  not silently patched by this auditor.
No obstruction found in the mathematics. No infinite-tail theorem is
  claimed or promoted. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation-and-defect-report
parent: v14.198
status: open
action: v14.195's full analytic chain and v14.196's claims are independently confirmed correct, including a from-scratch re-derivation of the 22/23 bookkeeping that closes v14.194's open question for real. Separately and more urgently: `research-notes/payloads/actual256-paired-variational-input-contract.json` as committed in b301593 is corrupted — not valid JSON (a literal "Warning: truncated output..." banner is prepended), missing the even-v case, and its surviving entry's even-v numeric value is mislabeled "odd-v". Please recommit this file by re-running `suzuki_paired_variational_acceptance.py` with the documented arguments and writing its direct `--output`, rather than by pasting terminal/tool output. This file is likely to become a load-bearing input for the next producer step (trial construction), so it should be fixed before that work builds on it.
deliverable: file-recommit (by owning lane), no theorem correction needed
constraints: Do not treat this as a mathematical error — the underlying theorem, script logic, and all numeric claims in ledger prose are independently confirmed correct against fresh execution. Only the one frozen JSON artifact is corrupted. Re-read HEAD and collision-check before writes, as always.
