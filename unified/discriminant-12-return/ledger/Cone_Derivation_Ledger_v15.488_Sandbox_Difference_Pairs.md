# Cone Derivation Ledger v15.488 — Sandbox return: the difference of two point pairs is the transfer pair (product = (p₁−p₂)²; same-shell differences are crossed pairs); it sharpens, and does not reopen, the force-law negative

Date: 2026-11-06 (America/New_York). Lane: sandbox (our Lane B), depositing the computation run in the Cone dynamics side thread 2026-11-06 at Jeremy's direction ("what about the difference between 2 parabolic point pairs on a boost hyperbola?"), under his standing keep-the-ledger-updated instruction of the same day. Parents: v15.487 (the force-law scan; its Level-1 invariant list is what this entry refines); v15.483 (the bilinear level: the kernel's band as a function of the difference variable); the dynamics chain v15.270–v15.282 (pair addresses; position as the crossing of opposite-sign parabolas). Live HEAD v15.487 at deposit. Status: exact algebra, verified numerically at machine precision (and in sympy up to exp/cosh rewriting). Disclosure deposit under the ledger-everything policy: listing is disclosure, not endorsement by the other lanes.

## Claim

The difference of two point pairs on boost hyperbolas is a well-defined pair — the **transfer pair** — with exact product equal to the momentum-transfer invariant of the two states, and with a species change that is the cone-native content of the observation: on a single hyperbola, the difference of two momentum pairs is a *crossed* (opposite-sign) pair, the species the framework's own dynamics uses for position-type data. The difference pair contains no separation and does not disturb the force-law negative of v15.487; what it does is identify, in pair language, the object that momentum-space interactions are actually functions of — and show that this framework's one native interaction object (the kernel's difference band) was already built from it.

## Chain of results (`difference_pairs.py`)

1. **The difference pair and its product (exact).** For pairs (u_i, v_i) = (m_i e^{ψ_i}, m_i e^{−ψ_i}) on uv = m_i², the componentwise difference D = (u₂−u₁, v₂−v₁) is itself a pair, whose pair coordinates are the displacement: T_D = (Δu+Δv)/2 = ΔT, X_D = (Δu−Δv)/2 = ΔX. Its product is
   (u₂−u₁)(v₂−v₁) = m₁² + m₂² − 2m₁m₂ cosh Δψ,
   verified numerically on four instances (including unequal shells) to < 10⁻¹². The right-hand side is the invariant (p₁−p₂)² of the two states — the momentum transfer squared of scattering kinematics, in pair dress.
2. **Same hyperbola: species change.** For m₁ = m₂ = m the product reduces to −4m² sinh²(Δψ/2) ≤ 0, and the components have opposite signs (instance ψ: 0 → 0.6 at m = 1: D = (+0.822119, −0.451188), product −0.37093044): the difference of two same-shell pairs is a **crossed pair** — a pair of the opposite-sign species. In the dynamics chain's construction (v15.270s), position-type data is carried exactly by crossed pairs (a state's position as the crossing of two opposite-sign parabolas); momentum-type data by same-sign pairs on a shell. Differencing two momentum pairs therefore lands in the position-type sector of the pair taxonomy — stated as a taxonomy fact, not a dynamics claim: the difference pair is not a position (it does not locate either body), it is a transfer, which is spacelike on-shell as transfers are.
3. **The ratio pair.** R = (u₂/u₁, v₂/v₁) = ((m₂/m₁)e^{Δψ}, (m₂/m₁)e^{−Δψ}): a pair on the mass-ratio shell uv = (m₂/m₁)²; on one shell it is the pure relative boost (e^{Δψ}, e^{−Δψ}) on uv = 1 with T = cosh Δψ — the scan's two-body invariant (v15.487) as a pair in its own right.
4. **Scope against v15.487.** The difference pair's invariant content is (m₁, m₂, Δψ) — it is a function of the two addresses, so the Level-1 content argument is untouched: no separation appears, and no force law becomes derivable. The refinement the difference pair adds is *where interaction-talk legitimately lives* in this framework: momentum-space interactions are functions of the transfer, the transfer's pair form is the difference pair, and the operator's kernel — the framework's one native interaction object — has its band exactly on the difference variable X = (N−M)/2 (v15.483). Force, in the pair language, is a property of differences of pairs, not of pairs; the scan's negative and this entry's positive are the same statement read from the two sides.

## Negatives / scope limits, stated plainly

The identity of §1 is standard relativistic kinematics expressed in pair coordinates — (p₁−p₂)² is the Mandelstam transfer, and no new invariant is claimed. The species observation of §2 is a fact about the pair taxonomy (signs of components); it does not make the difference pair a position, a force, or an interaction strength, and no amplitude, coupling, or cross-section is computed or implied. The 1+1-dimensional (single-boost) setting is the pair geometry's own; transverse momentum transfer is outside it. Nothing here revises v15.487, the doors, or the dictionary findings.

## Verdict

Deposited: the difference of two point pairs is the transfer pair — product (p₁−p₂)² exactly; on one hyperbola a crossed, spacelike pair — locating the difference, not the pair, as the framework's interaction-shaped object, consistent with the kernel's difference band and with the force-law scan's negative.

## Payload and snapshot note

Payload: `unified/discriminant-12-return/payloads/difference_pairs_v15_488/` — the full living REPORT.md (1347 lines: the v15.487 snapshot's content plus the difference-pairs section) and the build script, with `MANIFEST.sha256`. The script was re-executed from the staged copy on 2026-11-06 (exit 0). SHA-256 (generated mechanically from the manifest):

- REPORT.md `becbbc11223b4186235c3c6b201d6a480e1cc521993dd9e029ceeaf823208829`
- difference_pairs.py `438554351e80dfcdda3166b3d1588ad4536d296105ced75b8cba5ce8c69de7d6`

Snapshot note: this REPORT.md supersedes the v15.487 snapshot for the report as a whole. Its newest section closes with an in-text status line reading "not ledgered" — that line describes the section's state when written and is superseded by this deposit; the living file's line is being updated to name v15.488 (only that line; earlier sections' status lines name their own deposits and are unchanged).
