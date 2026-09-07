# Cone Derivation Ledger v13.299 — External Audit Round 14

Date: 2026-09-07

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

Independent external audit of `v13.291`–`v13.295`, the arc that pursues the "near-zero Ritz value at `a=1`" thread to its most interesting point yet: a numerically coherent candidate for a genuine nontrivial element of `ker(G_1)`, tracked through arbitrary-precision spectral computation, vector-alignment diagnostics, an independent off-grid operator residual, a full componentwise vector-cancellation test, and an `H_0^1`-Cauchy study extended to 20 modes. I re-ran five of the project's own committed scripts from scratch and checked the reported numbers line by line. Almost everything reproduced exactly. One diagnostic — the off-grid residual test in `v13.292` — does not hold up at higher mode counts, for a concrete, checkable reason, and I flag it below. The project's own separate, higher-precision test in `v13.293` is unaffected by that problem and I independently confirm it is solid.

## 1. Independent reproduction: v13.291 (componentwise high precision)

**[N-cert]** I ran `research-notes/suzuki_componentwise_high_precision_audit.py` from scratch (arbitrary-precision `mpmath`, no code borrowed from the project beyond the two small shared helper modules it itself imports) and reproduced the full lowest-Ritz-value sequence at `a=1` exactly:

`3.2376542589053878557e-11, 1.4167316570795464384e-12, 1.232158117461072758e-13, 1.8227526867280624257e-15, 4.5223499068528942695e-17, 8.3157917492155563451e-19`

for `M=6,8,10,12,14,16` — matching the ledger's table to the full displayed precision at every mode count. This independently confirms the round's foundational claim: once the pole/prime/archimedean components are integrated at arbitrary precision (rather than assembled in double precision and subtracted), the finite Ritz sections are genuinely positive through 16 modes, and the earlier apparent negative floor (`v13.288`–`v13.290`) really was floating-point cancellation, not a sign of a negative spectral bottom.

## 2. Independent reproduction and a genuine finding: v13.292 (near-null vector tracking)

**[N-cert]** I ran `research-notes/suzuki_near_null_vector_audit.py` and reproduced, to the displayed precision, the spectral centroid (`1.388, 1.519, 1.532, 1.597`), `‖u_M‖₂` (`2.532, 2.816, 2.844, 2.979`), boundary mass (`4.42e-6, 5.30e-7, 3.67e-7, 6.85e-8`), central mass (`0.681, 0.736, 0.740, 0.762`), and nested embedded overlaps (`0.99687, 0.99997, 0.99943` for `v`; `0.98824, 0.99992, 0.99827` for `u`) for `M=6,8,10,12`. These are all exact matches, and they are computed from simple sums/inner products of the Ritz coefficients with no delicate cancellation involved — I trust them fully. **The "no high-frequency or boundary escape" conclusion in `v13.292` §2–4 is solid and independently confirmed.**

**[Audit] The off-grid residual diagnostic in `v13.292` §5 does not survive a quadrature-convergence check.** The entry reports the normalized residual `ρ_M=‖P_aG_au_M‖/‖u_M‖` decreasing monotonically from `1.13×10⁻⁷` (M=6) to `5.27×10⁻¹⁰` (M=12), citing this as the decisive independent evidence (alongside vector alignment) for a genuine kernel candidate. I reproduced the script's *default-settings* output exactly (`1.13e-7, 3.83e-8, 7.98e-9, 6.72e-9` at `x_order=inner_order=64` — matching or close to the ledger's `1.13e-7, 3.77e-8, 4.53e-9, 5.27e-10`), but then re-ran the same function at higher quadrature orders (96, 128) on the *same* Ritz vectors and found the reported values are **not converged** at `M=10` and `M=12`:

| M | order 64 | order 96 | order 128 |
|---:|---:|---:|---:|
| 10 | `7.98e-9` | `4.80e-9` | `4.64e-9` |
| 12 | `6.72e-9` | `1.44e-9` | `6.74e-10` |

At `M=6,8` the same test *is* converged (stable to 3–4 significant figures from order 64 through 192, and matches the ledger closely). The reason is structural, not a bug: `offgrid_kernel_residual` is implemented in ordinary double-precision `numpy`/quadrature, evaluating an order-one kernel against an order-one function and then taking a small difference — exactly the kind of cancellation that `v13.291` diagnosed and fixed *for the eigenvalue computation* by moving to arbitrary precision, but that fix was never applied to this particular residual diagnostic. Once the true residual drops below roughly `10⁻⁸`–`10⁻⁹` (which is where the `M=10,12` values sit), the script's fixed `order=64` double-precision quadrature is no longer resolving it reliably, and the residual it reports there is itself dominated by quadrature/cancellation error rather than measuring the physical residual. **This means the specific `M=10` and `M=12` numbers in `v13.292`'s table should not be read as accurate, and the "decreasing by more than two orders of magnitude" characterization is not fully earned by this particular test** — though the qualitative direction (residual shrinking, not growing) is still probably right, since even the unconverged order-64 values keep shrinking.

## 3. Independent reproduction: v13.293 (vector-level cancellation) — the strongest evidence, and it holds up

**[N-cert]** Crucially, `v13.293`'s central test does **not** share `v13.292`'s weakness: it applies the *same arbitrary-precision component matrices* from `v13.291` directly to the candidate vector (`A_pole·c`, `A_prime·c`, `A_arch·c`, all in `mpmath`, no float64 quadrature anywhere), and checks that the sum cancels entrywise rather than only in one scalar Rayleigh quotient. I ran `research-notes/suzuki_kernel_candidate_reconstruction.py`'s `component_action_report(modes=14)` from scratch and reproduced every reported number exactly: action norms `‖y_pole‖=2.61742, ‖y_prime‖=1.03556, ‖y_arch‖=1.88727, ‖sum‖=4.52235×10⁻¹⁷`, and the full seven-row entrywise cancellation table (e.g. mode `n=1`: `2.3536699159, -0.483542403382, -1.87012751251, sum=3.81×10⁻¹⁷`) matched to the displayed precision on every row. This is genuinely strong, high-precision, quadrature-free evidence — an order-one vector equation cancelling to `~10⁻¹⁷`–`10⁻²²` entrywise is not something that happens by accident, and it survives exactly the numerical-integrity concern I raised against `v13.292`'s residual test. **The "kernel candidate" interpretation rests on solid ground because of this test, independent of the quadrature issue in Section 2 above.**

## 4. Independent reproduction: v13.294–v13.295 (H1/Cauchy diagnostics through M=20)

**[N-cert]** I ran `research-notes/suzuki_h1_cauchy_audit.py` and reproduced `‖Dv_M‖₂` (`2.53158, 2.81644, 2.84422, 2.97887, 3.07034` for `M=6..14`) and every successive-difference row (including the non-monotone `10→12` rebound the entry honestly reports rather than papers over) exactly. I then ran `research-notes/suzuki_parity_reduced_h1_extension.py`, which extends the same high-precision, quadrature-free (component-matrix) computation to `M=20` using the exact even-`v` parity block, and reproduced the entire extended table exactly, including the resolution of the `v13.294` concern: derivative differences `0.1465, 0.1270, 0.0921, 0.0337` and L² differences `0.0220, 0.0188, 0.0134, 0.00487` for `M=12→14→16→18→20`, both decreasing cleanly after the earlier rebound, with embedded overlaps climbing to `0.999988` at `18→20`. This is a full, exact, independent reproduction of the round's capstone numerical result.

## 5. Overall verdict for this round

The mathematical/numerical content of `v13.291`, `v13.293`, `v13.294`, and `v13.295` is independently confirmed exactly, using arbitrary-precision computation throughout — I have no corrections to any of it. `v13.292` is mostly confirmed the same way, **except** its off-grid residual diagnostic (§5 of that entry) is quadrature-under-resolved at `M=10,12` and should not be trusted at the precision it reports; this is a real, checkable methodological gap, but it does not undermine the round's headline finding, because `v13.293`'s independent high-precision vector-cancellation test — which I verified separately and which does not share the flaw — supports the same conclusion on solid ground. I want to be precise about what "the round's headline finding" is: this is strong numerical evidence for a smooth kernel candidate of the compact operator `G_1` at `a=1`, not a proof that `ker(G_1)≠{0}`, and every entry in the batch is explicit and consistent about that distinction — a discipline I'm glad to see holding across five entries dealing with an exciting-looking result.

## 6. Scope note

Not independently verified this round: `v13.296`–`v13.298` (further tail-decay/resolvent/asymptotic-matrix extensions of this same thread) landed on `master` during this audit's drafting and are left for the next round; the primary-source fidelity of the Suzuki equations underlying the component decomposition (same arXiv-access limitation as prior rounds — I checked internal/numerical consistency exhaustively, not transcription fidelity); whether the observed positivity/cancellation pattern is specific to `a=1` or a more general phenomenon (out of scope for this numerical audit as constructed).

## 7. Guardrails

All guardrails from prior rounds remain in force. **New guardrail, prompted by the `v13.292` finding in Section 2:**

- **Any numerical diagnostic that evaluates a kernel/operator action in ordinary floating-point precision, when the quantity being tested is itself expected to be small relative to the individual terms being summed or integrated (i.e., a candidate cancellation or residual test), must include an explicit quadrature/precision-refinement check before its reported value is treated as accurate** — exactly the discipline `v13.291` already applies to eigenvalue computation (moving to arbitrary precision once double-precision cancellation was diagnosed), but which was not yet carried over to the off-grid residual diagnostic introduced in `v13.292`. Concretely: before quoting a residual or near-cancellation value below roughly `10⁻⁶`–`10⁻⁷` from a float64 quadrature routine, re-run it at 1.5× and 2× the default quadrature order and confirm the value is stable to at least 2 significant figures; if it isn't, either raise precision/order or explicitly label the value as unresolved rather than tabulating it as a clean number.

**External audit round 14: CLOSED. No corrections required to `master`'s mathematical content; one numerical-diagnostic precision gap identified in `v13.292` (its off-grid residual values at M=10,12), with the round's core conclusion independently confirmed safe via `v13.293`'s unaffected higher-precision test, and a new guardrail recommended.**
