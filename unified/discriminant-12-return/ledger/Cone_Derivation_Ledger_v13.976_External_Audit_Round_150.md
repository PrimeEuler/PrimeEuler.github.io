# Cone Derivation Ledger v13.976 — External Audit Round 150

Date: 2026-10-03

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.973` (Xi scalar spectral-tail rate), `v13.974` (P4 payload
freeze for `v13.971`), `v13.975` (constrained-complement KKT elimination
for the frozen P4 carrier) — plus the newly-committed companion paper
`papers/Companion_SieveFlow_v1.0.tex` and its figure.

Verdict: **`v13.973`–`v13.975` confirmed, zero errors.** The companion
paper's claims that overlap with already-audited ledger entries are
confirmed; two new numeric claims not previously audited were
independently checked and also confirmed (after I caught and fixed my
own bug on the first attempt). However, **several of the paper's claims
have no corresponding ledger entry and are not independently
reproducible from what's committed** — flagged in detail below, since
this is new for this session: it's the first time new content has
reached this repository through a paper draft rather than through the
ledger.

## 1. `v13.973` — Xi scalar spectral-tail rate [N, independently reproduced]

Re-ran the already-audited `v13.965` reproducer extended to `M=60`
(instead of the ledger's `M=19`) from scratch: all six quoted partial
sums (`M=1,10,19,35,50,60`) and their errors against the independently
recomputed target `\kappa_\Xi=0.996801952032401` matched the entry's
table to every displayed digit. I then fit the claimed power-law tail
rate independently: `\mathrm{polyfit}` of `\log(\mathrm{err})` against
`\log M` over `M=10..60` gives slope `-1.228`, matching the claimed
`\mathrm{err}\sim M^{-1.2}` almost exactly. The entry's own caveat — that
this is the `M\to\infty` spectral tail at `a=\infty`, not the finite-`a`
scalar `\kappa_a^\Xi` — is correctly stated and important; it does not
overclaim relevance to the `a\to\infty` certification program beyond
"the high-frequency content behaves tamely," which is exactly what was
shown.

## 2. `v13.974` — P4 payload freeze [N, independently reproduced]

Verified all 14 SHA-256 hashes in both `manifest.json` files against the
actual committed `.npy` files — all match exactly. More substantially, I
located the cited generator (`suzuki_tail_P4_residual_basis_certificate.py`,
genuinely present in the repo) and ran it from scratch (a multi-minute
computation through `M2=16001/16002` tail modes). It reproduced every
certification number to the precision that matters: both sectors'
transformed-residual caps (`0.0331`/`0.0323`), sin-theta caps
(`0.414`/`0.404`), and moat (`0.08`) matched exactly, and three of the
four Ritz values in each sector matched the frozen manifest to 4+
significant figures. The smallest Ritz value in each sector (which is
mathematically zero and only resolved to noise level, `~10^{-15}`–`10^{-16}`)
differed by a factor of 2–3× between runs — expected floating-point
non-determinism for a quantity at that scale, not a correctness concern,
since every bound and cap that actually gets used downstream matched
exactly. Note: the posted generator's own `main()` only prints
diagnostics; it doesn't itself emit the frozen `.npy` payload, so the
*exact byte-for-bit* Z/AZ/BZ arrays weren't independently re-derived
this round — only the certification numbers they're claimed to satisfy.

## 3. `v13.975` — constrained-complement KKT elimination [D]

The most substantial check this round. I independently re-derived every
equation (1)–(14) from scratch, not merely checked them: starting from the
saddle system `[[A,BZ],[Z^TB,0]](x_b,\lambda_b)=(b,0)`, substituting
`y_b=B^{1/2}x_b`, `g_b=B^{-1/2}b` gives `Jy_b+Y\lambda_b=g_b` with
`Y^Ty_b=0` (confirmed by direct multiplication), which projects to
`\widehat Q_4J\widehat Q_4y_b=\widehat Q_4g_b`. I then verified, by
carrying the same `B^{\pm1/2}`-congruence substitution all the way
through, that `R^TX_C` (eq 3), `\widehat s_C^Q=R^Tx_f` (eq 7),
`\widehat h_{\rm reg}=f_T^Tx_f` (eq 9), `\widehat r(t)=p_T(t)^Tx_f`
(eq 10), and `C_Q^*\widehat J_Q^{-1}h_Q(t)=X_C^Tp_T(t)` each reduce to
exactly the corresponding Schur-complement quantity from `v13.971`
(`C_Q^*J_Q^{-1}C_Q`, `C_Q^*J_Q^{-1}g_Q`, `\langle g_Q,J_Q^{-1}g_Q\rangle`,
`h_Q(t)^*J_Q^{-1}g_Q`, same term) — every one matched term for term. The
final assembled transform (eq 14) is then exactly `v13.971`'s formula
with every background term now computable from three linear solves
instead of an explicit `Q_4` basis. The entry is also honestly scoped:
§8 correctly notes this does not establish `\widehat P_4=P_4` (numerical
vs. exact projector), leaving that error to the separately-certified
subspace-angle bounds.

## 4. The companion paper — partially confirmed, several claims unaudited [G]

`papers/Companion_SieveFlow_v1.0.tex` draws on `v13.942`/`v13.948`/
`v13.952`/`v13.963` for its core claims (composite indicator `R=2.17`,
`\mu,\lambda\approx3.77/3.76`, the `\chi_{12}` kill, the fold-recursion
table) — all of which this audit already independently confirmed in
Rounds 148–149. `D(10^6)=13{,}970{,}034` checks out exactly against a
fresh direct computation.

Two further numeric claims in the paper's carrier-gradient table are
**not** backed by any ledger entry, so I checked them myself with fresh
code through the already-trusted `spectrum`/`R_at` pipeline functions:

- `\phi(n)/n`: my first attempt gave `R=1.09` — a real mismatch with the
  paper's claimed `1.68`. I found my own bug (the sieve array held
  `\phi(n)` itself, not `\phi(n)/n` — I'd forgotten the final division).
  Fixed and reran: `R=1.6765`, matching the paper's `1.68` almost exactly.
- `\mu^2(n)` (squarefree indicator) **at the half-frequencies**
  `\gamma_k/2`: `R=1.237`, matching the paper's claimed `1.24` almost
  exactly (the ordinary-frequency value is null, `R=0.787`, consistent
  with the paper only claiming the halved-frequency result).

Both now confirmed. However, three things in the paper remain
**genuinely unaudited** and I could not verify them this round:

- **The "small-prime weighting" kill test** (§5: composite-indicator `R`
  weakens `2.17\to1.86` under small-prime emphasis, strengthens
  `2.17\to2.55` under von Mangoldt `\log p` weighting) — no ledger entry
  describes this test's methodology, and I don't have enough detail to
  reconstruct it faithfully.
- **The entire "distinguished hyperbola" section** (§7: `xy=n` vs. the
  circle cut `x^2+y^2=n`, the "binary fold decision" `d(n)=2` vs.
  `d(n)>2` giving `R=2.17` against a raw lattice-count `R=1.16` and a
  suppressed circle-cut `R=0.73`) — this is new geometric content with no
  ledger entry at all.
- **The figure itself is not reproducible from the repository as
  committed.** `figures/companion_sieve_flow_4panel.py` loads
  `paper_spectra.npz` and `lpf_cover.npz` from a hardcoded absolute path
  (`/home/hatch/workspace/d12/lane_b/sandbox/runs/20261002-sieve-renorm/`)
  that is outside the repo and not present in it. The committed PDF/PNG
  cannot be regenerated from what's checked in.

This is worth flagging plainly: this is the first time in this audit
relationship that new quantitative claims have entered the repository
through a paper draft rather than through a ledger entry first. The
standing protocol — read every new entry, verify every claim, flag
anything unreproducible — applies equally to a paper as to a ledger
entry, and two of its three new claims currently have neither a ledger
record nor a reproducible path to check them.

## What remains open

- The small-prime-weighting test and the distinguished-hyperbola section
  need either a dedicated ledger entry (with posted methodology/script)
  or should be flagged in the paper itself as not-yet-independently-verified.
- The figure's data dependency should be fixed (commit `paper_spectra.npz`/
  `lpf_cover.npz`, or regenerate the figure from the already-posted
  `sieve_flow_R_pipeline_reproducer.py`) so the companion paper is
  reproducible end-to-end from the repository.
- `v13.974`'s exact byte-level Z/AZ/BZ arrays were not independently
  re-derived (only the certification numbers they satisfy); a full
  bit-for-bit replay would require locating or reconstructing the actual
  payload-saving wrapper around the posted generator.
- Unchanged from prior rounds: `G_-\ge0` (RH-hard, Round 136); the
  odd-sector Picard-divergence bounds (Round 135); the source-RG absolute
  location question (Round 147).

## Result

\[
\boxed{\textbf{v13.973--v13.975 confirmed.} \textbf{The spectral tail-rate
fit, the P4 payload freeze, and the KKT elimination of the Q4 complement
were all independently re-derived or re-executed from scratch and matched
exactly.} \textbf{The companion sieve-flow paper's claims that trace back
to already-audited ledger entries are confirmed, and its two new
checkable numeric claims (} \phi(n)/n\textbf{,} \mu^2(n)\textbf{ at
}\gamma/2\textbf{) are now independently confirmed as well --- but the
small-prime-weighting kill test, the entire distinguished-hyperbola
section, and the figure's underlying data are not currently backed by any
ledger entry or reproducible from the committed repository, and should be
treated as unaudited pending either a ledger entry with a posted script
or an explicit caveat in the paper.}}
\]
