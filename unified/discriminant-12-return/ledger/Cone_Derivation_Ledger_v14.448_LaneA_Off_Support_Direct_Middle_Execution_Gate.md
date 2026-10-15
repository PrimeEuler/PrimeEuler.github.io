# Cone Derivation Ledger v14.448 — Lane A off-support direct-middle action gate

**Date:** 2026-10-15
**Track:** Lane A Cone/Suzuki
**Status:** [NEXT PHYSICAL GATE SPECIFIED; NOT YET EVALUATED]
**Parents:** v14.442 PASS, v14.443 External Audit Round 275, v14.445 Round 276, v14.447 certified 85 moments and split.
**Collision check:** fetched current live master immediately before this additive entry, HEAD `82baffb3bbf16019a924e59dddea033dcd50196b`, ledger max v14.447; v14.448 next free.

## 1. Structural simplification worth exploiting

The changed compact trial's support ends at compact index `U-1 = 1040382`; the physical direct-middle output indices are `i=U,...,2U-1`, `U=1040383` (1,040,383 outputs/sector). Consequently **none of these output indices belongs to the compact trial's input support**. The Toeplitz/Hankel offdiagonal channels contain no `i=j` artificial self row in this block, and the raw physical diagonal acts on zero compact input here. The off-support compact action therefore needs **neither** the in-support artificial-self compensation loop **nor** the raw diagonal addition used by v14.405. Keep the actual pole/rank-one term and full physical output `z_i`; this simplification is only for the compact component, not a license to drop the original infinite seed action or its self/diagonal handling.

Using the unchanged `suzuki_compact_component_rectangle.channels` native-scale four-component representation, the compact off-support action has the same operator expression as v14.405 without the support-only diagonal corrections:
`A_i(compact) = (c/2) * [ z_i * ( T x - H x )_i - ( T(zx) + H(zx) )_i ] + alpha * pole_i * P`.
Here each component retains its original native dyadic scale, four independent convolutions per component, and its own input offset; `P` is the same once-only full trial pole pairing. For each of the first/middle/last direct-middle rows check the channel sums against `direct_channel_row` exactly, and verify the input support does not overlap the output index. **Output z_i must be evaluated/certified at these new physical output modes**, not reused from the old input-z cache; it is a distinct new source of directed error.

## 2. Numerical gate and composition requirements

A. Evaluate/freeze two off-support compact-action direct-middle point buffers, physical modes even `2080767..4161531`, odd `2080768..4161532`, each length `1040383`; carry `z_i` interval error and parameter/pole truncation errors explicitly in native-scale directed error. Reuse reconstructed v14.403 changed trial with exact frozen hash pins from v14.405; do not recompute already certified 912383 rows.

B. Evaluate original infinite-seed-only action on this direct-middle range with a rigorously valid bank/tail split. Because this block extends past the previously certified v14.393 seed-gap window, **do not extrapolate** v14.393 520191-row seed action or treat v14.447 inverse moments as if they were pointwise actions. First derive certified split at these output indices and handle any internal self rows as appropriate for the original seed. Use the v14.447 freshly frozen 85 moments when mathematically valid.

C. Combine physical bare source `1/n` even or `1/(n-1)` odd, compact action, original seed action, and new certified error charges into the direct-middle residual. Compute directed `ell^2` on all 1040383 rows.

D. Beyond the direct-middle end, use the v14.447 strict support/far ratio <1/2 and 42 moments with a rigorously summable infinite-output norm remainder. The geometric `2^-84` ratio controls a truncation contribution; it does **not** by itself bound the full residual or validate missing noncompact seed/bare cancellation. Include those terms explicitly.

E. Combine disjoint beyond-gap physical supports in `ell^2`; the v14.444 exact-rational budgets are EVEN `2.2251541105255456e-5`, ODD `2.228757296675468e-5` (display approximations only). Each must include every beyond-gap numerical and analytic error. Global v14.403 source+lift transport is already charged once in the v14.442 budget, and v14.354 finite self terms remain charged exactly once; do not add either again.

## 3. Scope and status

The mathematical off-support identity and absence of compact diagonal/self rows follow from the frozen support endpoints; the 1,040,383 actual direct-middle rows **have not been run** in this entry. No new residual bound or infinity-tail conclusion is asserted. This entry resolves an implementation ambiguity before expensive CI and makes a concrete two-sector direct-middle + seed + far-moment producer handoff. Original `C_S_32000` and original acceptance thresholds untouched.

---

HANDOFF
target: sandbox, lane-a, external-audit
type: urgent-direct-middle-execution
parent: v14.448
status: ready
action: implement and execute the two-sector off-support compact direct-middle producer using v14.405 exact four-component input and new certified output z; independently implement original-seed direct-middle split and whole far bound; return hash-frozen point buffers/certificates and exact physical L2 error. No extra self or diagonal for compact on output outside support.
deliverable: full 1040383-row/sector direct-middle physical residual and rigorously summable beyond-middle infinite residual in both sectors, with exact budget comparison and provenance
constraints: no reuse of input z for output z; no treating moments as pointwise action; no acceptance claim from finite rows alone; no duplicate transport; no threshold changes
