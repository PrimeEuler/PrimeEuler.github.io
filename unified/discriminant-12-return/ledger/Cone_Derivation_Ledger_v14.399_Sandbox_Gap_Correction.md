# Cone Derivation Ledger v14.399 — Sandbox Track (Little Euler)

## Sandbox HANDOFF-ACK v14.398: Finite Gap Correction Constructed and Norm-Certified — 520,191 Rows per Sector, Correction Norm ≤ 4.85e-6 (Cap 0.002), Whole-Trial Triangle Upper ≤ 1.683e-4

**Track:** Sandbox (our Lane B). **Closes:** the v14.398 sandbox HANDOFF (construct, norm-certify and freeze the specified finite gap correction from the independently replayed v14.396 residual buffers, without recomputing the original-seed action). **Status:** [D] for every number below (exact integer/Fraction arithmetic). **Scope:** candidate construction only, in the v14.339/v14.341 experiment pattern. No new residual is evaluated, and no contraction, acceptance, stationary or capacity claim is made. Using the v14.396 point residual to choose a represented correction does not assert that the point equals the exact physical Schur residual.

---

## 1. Definition and support

$$
\delta_{\mathrm{gap}}(n) \;=\; \Big\lfloor r_{\mathrm{gap,point}}(n) \,\big/\, \mathrm{midpoint}\big(\log_{\mathrm{normalized}}(n, 128)\big) \Big\rfloor_{160},
$$

- even-$v$: $n = 1040385, \dots, 2080765$ (step 2), odd-$v$: $n = 1040386, \dots, 2080766$ (step 2); 520,191 values per sector; zero elsewhere.
- $r_{\mathrm{gap,point}}$ is the exact dyadic point residual of v14.396, reconstructed from the frozen parents (v14.373 compact chunks + v14.393 seed buffers, all hash-verified) by the v14.396 convention — **not** recomputed from any operator action — and pinned to the v14.396 manifest: reconstructed residual SHA-256 `52211d2328ed390dc9874b1534784c709fe9412244f552194f4dd558b9e830fe` (even), `350e020a7bc9f30aa66dae7b1b7966e112b81c56141c7bd73ae64eaeefdcb5fd` (odd), matching exactly.
- $\log_{\mathrm{normalized}}$ is the pinned module `suzuki_certified_remote_diagonal.py`, verified byte-identical to the repository copy (SHA-256 `08226538dffb5db42d85db5edb0f1c043a56df326ed1f51dc7391ca7cf8a2788`); midpoint $= (\mathrm{lo}+\mathrm{hi})/2$ at 128-bit enclosure, as in v14.341. Observed midpoints on the support: $[12.4688, 13.1620]$ in both sectors (all $> 11$, as in v14.341).
- The correction is **added to the preserved v14.345 trial** (refined Near + v14.341 Middle/window patch + unchanged original infinite seed). The gap support is disjoint from the finite trial support; nothing outside the gap support changes.

## 2. Norm certificates (exact)

| quantity | even-$v$ | odd-$v$ |
|---|---|---|
| correction norm² (exact Fraction in cert) | $2.3445343902891275\times10^{-11}$ | $2.3359448724928147\times10^{-11}$ |
| correction norm upper (outward, 192-bit) | $4.842039229796809\times10^{-6}$ | $4.833161359289399\times10^{-6}$ |
| correction $\ell^1$ | $2.853264033897469\times10^{-3}$ | $2.847623000164413\times10^{-3}$ |
| base trial norm upper (v14.345 RHS cert) | $1.6343873796462063\times10^{-4}$ | $1.63414040717791\times10^{-4}$ |
| **whole-trial norm upper (triangle)** | $\mathbf{1.6828077719441745\times10^{-4}}$ | $\mathbf{1.682472020770804\times10^{-4}}$ |
| buffer | 8,843,247 B = 520,191 × 17 B, $\lfloor\cdot\,2^{160}\rfloor$ signed LE | same |
| buffer SHA-256 | `171883d6c8e41e9a92f88bea4fa96b70f538ada49ea296876e1f06aebe1f9da6` | `f3a9b9a06efb728ee8ed51b4294fbd406d0b9bad8248831d03b3c4586f846a66` |

The unchanged **0.002 norm cap** (v14.339) is satisfied in both sectors by a factor of ~400. The base-trial uppers are taken from Lane A's own v14.345 RHS certificates (`wider_correction_rhs_and_lift_v14_345/wider-correction-RHS-{sector}.json`, field `new_whole_trial_norm_upper`), hash-bound in the sandbox certificates.

## 3. Verification

- 64 sample rows per sector (fixed boundary rows + seeded randoms) checked by an independent integer-only path: $\lfloor r_{\mathrm{int}} \cdot \mathrm{den} / (\mathrm{num} \cdot 2^{96}) \rfloor$ equals the producer's delta at every sample.
- One-quantum bound at every sample: $0 \le r_{\mathrm{gap,point}} - \delta_{\mathrm{gap}} \cdot \mathrm{logpoint} < \mathrm{logpoint} \cdot 2^{-160}$.
- Buffer round-trip: decoded buffers reproduce the delta lists and the exact norm² sums.
- Residual provenance: the reconstruction asserted the pinned v14.396 residual hashes before any delta was computed (§1), so the correction is bound to the same point both replays (v14.397, Audit R259 and sandbox) verified.

## 4. Domain justification

$\delta_{\mathrm{gap}}$ is finitely supported (520,191 modes) with dyadic-rational values; finitely supported sequences lie in the operator domain and in every weighted $\ell^2$ space of the framework, and the domain is a vector space containing them, so adding $\delta_{\mathrm{gap}}$ to the existing domain-admissible v14.345 trial keeps the sum domain-admissible. $(D\delta_{\mathrm{gap}})_n$ is a finite sum at every row.

## 5. Payload

Frozen at `research-notes/payloads/sandbox_gap_correction_v14_398/` (34 files): both correction buffers as base64 parts (15 parts per sector, 800,000 B parts; reassembly: concatenate `.b64.partNNN` in numeric order and base64-decode), both certificates (`gap-correction-even-v.json`, `gap-correction-odd-v.json`), the as-run producer (`build_gap_correction.py`), and `manifest.json` binding every buffer hash. Post-push, the payload was re-downloaded from the repository and reassembled fresh: both buffers reproduce the §2 SHA-256 values exactly.

## 6. Handoff status and limits

The v14.398 sandbox HANDOFF is **CLOSED** by this return. What this enables is Lane A's side of v14.398: binding a new complete RHS, a fresh lift, and support-aware action/residual consumers for the changed trial — including the fresh output split the changed compact support requires (v14.373's moment splits do not certify the changed vector). Whether this finite refinement improves the seed's gap behavior is an empirical question for that evaluation; per v14.398 itself, no assumption is made that repeated finite extensions close the beyond-support residual, and the sandbox makes no such claim here.
