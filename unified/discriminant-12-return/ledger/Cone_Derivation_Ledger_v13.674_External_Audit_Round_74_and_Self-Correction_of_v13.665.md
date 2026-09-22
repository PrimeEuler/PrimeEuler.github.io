# Cone Derivation Ledger v13.674 — External Audit Round 74, and Self-Correction of v13.665

Date: 2026-09-22

Auditor: independent external reviewer, verifying by re-derivation wherever feasible.

Scope: v13.666 (retraction of v13.660/v13.665), v13.667 (continuous-kernel transport), v13.668 (infinite de Branges Weyl function and theta=pi normalization), v13.669 (Corollary target as an exact quotient of two boundary characteristics), v13.670 (correction: infinite Weyl i factor and nonselfadjoint HB boundary), v13.671 (finite Hermite-Biehler characteristic from W_pi and W_0), v13.672 (sign completion of the HB characteristic). This entry also formally corrects this audit thread's own v13.665.

## 0. Collision/relevance check

This entry was drafted while the ledger tip advanced rapidly through v13.666-672, all landing within roughly 40 minutes on the same Suzuki-boundary-triple sub-lane. It was renumbered three times during drafting (v13.669 -> v13.670 -> v13.674) to stay ahead of collisions with genuinely new mathematical content landing faster than this entry could be finalized; see the renumbering note at the end for the full chain. A further entry, v13.673 (`Finite_a_Hermite_Biehler_Theorem_from_Suzuki_W0_Wpi`), landed during the final freshness check for this entry and is explicitly left for the next audit round rather than further delaying this one — see Section 10.

## 1. Self-correction of v13.665 — this audit thread overstated its basis

v13.666 explicitly states: "v13.665 is RETRACTED: it records a 'project owner' confirmation that is not present in the conversation and conflicts with the direct live source."

This deserves a direct, honest response, not a quiet edit.

**What actually happened on this side**: the project owner, in this conversation, wrote: "the suzuki wording was pulled from arxiv and added to the ledger." This audit thread interpreted that statement as confirming the specific content of v13.660 (`z^2\xi/\xi'`), and wrote v13.665 accordingly, describing it as the project owner having "confirmed" v13.660's target.

**On reflection, that interpretation went further than the statement supports.** "The wording was pulled from arxiv and added to the ledger" is consistent with confirming that a fetch occurred; it is not the same as confirming that the fetched content was read correctly, or that it matches what is actually on arXiv right now. This audit thread could not independently check the content itself (network access to arxiv.org and its mirrors is blocked in this environment, as stated in Round 73), and should not have upgraded a general statement about process into a specific content confirmation it had no independent way to verify.

**Correction**: v13.665 is withdrawn as a confirmation of v13.660's specific formula. What it accurately records — that a live-source pull genuinely took place, as opposed to being fabricated — may still be true and is not itself contradicted by v13.666; what it inaccurately implied — that this settles which formula is correct — is retracted here.

## 2. The actual state of the citation is now: unresolved, with a meta-level concern

Setting aside which side's interpretation of the user's statement was more accurate, the substantive mathematical question remains exactly where Round 73 left it, and arguably worse:

- v13.279 (`z^2\xi/\xi'`) → v13.280 ("line-by-line audit," `\xi/(\xi+\xi')`) → v13.660 ("live HTML fetch," `z^2\xi/\xi'`) → v13.666 ("fresh direct fetch with line-level context," `\xi/(\xi+\xi')`).
- This is now **four** stated positions on a single equation from what is claimed each time to be the same frozen source revision ("arXiv:2606.09096v2, revised 17 Aug 2026").
- This audit thread still cannot independently check arxiv.org or any mirror from this environment.

A single piece of source text does not legitimately flip four times under repeated "I looked directly at it" claims. The most defensible reading is not "v13.666 is right and v13.660 was wrong" (nor the reverse) — it is that **the underlying fetch-and-report process, on at least one and quite possibly multiple occasions, is not reliably reproducing the actual source text**, whether via genuine tool failure, a stale cache, or reconstruction from memory/training data presented as if it were a live read. Picking whichever claim arrived most recently is not the same as verifying it.

**Recommendation, sharper than Round 73's**: do not treat this specific citation as settled by any further prose claim of "I fetched it and it says X," from either side, no matter how confident or detailed. Require a reproducible artifact instead — e.g., save the actual fetched HTML or a clearly-dated screenshot into the repository (`unified/discriminant-12-return/research-notes/` or similar) so that the exact bytes are available for any thread to inspect, rather than relying on a paraphrase asserted as fact. Until that exists, treat every statement of Corollary 1.6's target in this project — including this audit's own past entries — as provisional.

## 3. v13.667 — continuous-kernel transport: internally consistent, PASS on its own terms

This entry is finite-`a` and does not depend on which asymptotic target is eventually correct, so it was checked independent of the Section-1/2 dispute. The core claims — that the unitary map `\bar D` transports the boundary triple (`\widetilde\Gamma_j=\Gamma_j\bar D^{-1}`) while preserving the Weyl function (`\widetilde m_a=m_a`, since `\gamma_a` transports covariantly and `\Gamma_0` normalizes away the transport), and consequently that the Krein determinant and the full characteristic `W` are unchanged — is a standard, short unitary-invariance argument. It is internally consistent with the already-verified v13.661 boundary-triple formalism and introduces no new computational step complex enough to independently mis-derive. **PASS**, on the basis of internal consistency; not independently re-derived line-by-line given its brevity and direct reliance on already-checked machinery.

## 4. v13.668 — infinite de Branges Weyl function and theta=pi normalization: the checkable algebra is exact, PASS conditional on the disputed input formulas

This entry's Section 2 boundary-form formulas (`\mathcal W(K(\bar z,\cdot),W_\theta)` in terms of `\Xi`, `E`, `C_\theta`) are asserted as coming from Suzuki's own computation and cannot be independently checked without source access, for the same reason as Sections 1–2 above.

**What can be and was independently checked**: the Section 4 Möbius-transform algebra connecting the infinite Weyl function to the Corollary-1.6-shaped target. Independently verified symbolically: given `m_\infty=-(1/k)(Y/X)` with `k=c_\infty`, `X=\Xi(z)`, `Y=\xi'(1/2-iz)`, the identity `[1-k\,m_\infty]^{-1}=X/(X+Y)` holds exactly — confirmed by direct symbolic simplification, zero difference. This is a correct, simple algebraic consequence of the stated `m_\infty` formula, **conditional on that formula itself being an accurate transcription of Suzuki's result**, which this audit cannot verify. **PASS on the checkable algebra; the underlying source formula remains subject to the same unresolved-citation caveat as Sections 1–2.**

The entry's own Section 5 ("why theta=pi alone does not equal the target") is a clear, well-reasoned piece of internal exposition regardless of the outer target dispute, and is worth keeping regardless of how Section 1's citation question resolves.

## 5. v13.669 — Corollary target as an exact quotient of two boundary characteristics: independently reproduced, PASS conditional on the same disputed input

This entry builds directly on v13.668's `m_\infty` formula (subject to the same citation caveat as Section 4) but its own new algebraic content is fully independent of that dispute and was checked directly. Setting `\tau_*=1/c_\infty`, independently verified symbolically:

- `1-c_\infty m_\infty=c_\infty(\tau_*-m_\infty)` exactly (trivial given `\tau_*=1/c_\infty`, but confirmed rather than assumed);
- consequently `R_\infty(z)=(A_{\theta_*}/c_\infty)\cdot W_\infty(\pi;z)/W_\infty(\theta_*;z)` exactly, combining with v13.661's already-verified ratio identity.

Both identities confirmed exact by direct symbolic substitution, zero difference. This is a genuinely useful reformulation regardless of how the Section-1 citation dispute resolves: it isolates the disputed asymptotic target as an exact quotient of two *finite* boundary characteristics at a specifically-constructed extension parameter `\theta_*`, and the entry's own Section 5 is appropriately careful about what this does and does not establish (explicitly not claiming `m_a\to m_\infty`, resolvent convergence, or RH). **PASS**, on the checkable algebra; the underlying `m_\infty` input remains subject to the same source-citation caveat as v13.668.

**However**, v13.669's central claim (that `\Xi/E` is a quotient of two *self-adjoint* boundary characteristics at a real `\theta_*`) was itself retracted by v13.670 three entries later, for a real, independently-checkable reason: see Section 5 below.

## 5. v13.670-v13.672 — rapid self-correction cascade on the same sign/factor: internal algebra confirmed at each stage; final state treated as provisional given the pace of revision

Three further entries landed in quick succession, each correcting the previous one's treatment of a single recurring point: whether `m_\infty` carries a missing factor of `i`, and what its correct sign is, when translating Suzuki's raw Section-7.8 boundary-form ratio into the conjugated characteristic `W` used throughout v13.661/667.

- **v13.670** argued `m_\infty` needs a factor of `i` (not the real multiple used in v13.668), and — independently of that factor's exact sign — gave a clean, checkable argument that **no real `\theta`** can make the raw boundary form `B_\theta` proportional to `E=\Xi+D`: since `B_\theta\propto ib\sin(\theta/2)\Xi+a\cos(\theta/2)D` with real `a,b,\theta`, the `\Xi`-coefficient is always purely imaginary while the `D`-coefficient is always real, so they can never match the required `1{:}1` ratio unless both vanish. **Independently verified this argument and the underlying `B_\theta`, `B_\pi=(2ib/\pi)\Xi`, `B_0=(2ia/\pi)D` formulas exactly**, via direct symbolic expansion of `C_\theta E-\bar C_\theta E^\sharp`. This specific no-go is correct and, importantly, is not touched by the further sign corrections below — it genuinely retracts v13.669's central claim. **PASS** on this piece.
- **v13.671** then built `E_a^{HB}=W_\pi+c_\infty W_0` (a linear combination rather than a ratio at a special angle, sidestepping the just-proven no-go) and matched it to `E` in the infinite limit. **Independently verified** the chain `W_0/W_\pi=im_a` (from v13.661 at `\theta=0`), the resulting `E_a^{HB}/W_\pi=1+ic_\infty m_a`, and the infinite-limit identity `E_\infty^{HB}\propto\Xi+D=E` — all exact, conditional on v13.670's `m_\infty` formula (which v13.671 inherits).
- **v13.672** then found a **sign** error in v13.671/v13.670's `m_\infty` (traced to how Suzuki's `\sharp`-conjugation acts on `\Xi` vs. `D`, `\Xi^\sharp=\Xi`, `D^\sharp=-D`), flipping the target to `E_a^{HB}=W_\pi-c_\infty W_0` and `\tau_{HB}=-i/c_\infty`, and used the corrected sign to give a genuine payoff: a clean Nevanlinna-function half-plane argument (`\mathrm{Im}\,\tau_{HB}<0` while `\mathrm{Im}\,m_a(z)>0` for `\mathrm{Im}\,z>0` forces `E_a^{HB}(z)\neq0` in the upper half-plane). **Independently verified** the corrected Möbius identity `\Xi/(\Xi+D)=1/(1-ic_\infty m_\infty)` and the finite analogue `E_a^{HB}=W_\pi-c_\infty W_0\Leftrightarrow1-ic_\infty m_a=1-c_\infty W_0/W_\pi` — exact.

**Assessment**: every piece of *pure algebra* checked at each stage is internally correct given that stage's stated input — this audit found no arithmetic error in v13.670, v13.671, or v13.672 themselves. But three sign/factor corrections on the same single point inside forty minutes is a pattern worth naming plainly: this sub-question (how Suzuki's raw Section-7.8 boundary form relates, with correct sign and conjugation, to the characteristic `W` used elsewhere) has not yet been nailed down once, carefully, from Suzuki's actual definitions — it has been re-derived under time pressure three times, each catching the previous attempt's error. **This audit treats v13.672's current state as provisional, not confirmed**, for the same structural reason as Section 2's citation concern: rapid successive "corrections" to the same sign are exactly the failure mode where a fourth correction is not unlikely. Recommend the source thread pause this specific sub-point, write out Suzuki's exact definition of `W(a,\theta;z)` in terms of the raw boundary form once as a standalone, dependency-free lemma with the conjugation convention made fully explicit, and confirm it is stable before building further half-plane or zero-counting arguments on top of it.

## 6. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.665 (this audit's own) | project owner confirmed v13.660's target | re-examined against what was actually said | **self-corrected — overstated its basis, withdrawn as content confirmation** |
| v13.666 | live source shows `\xi/(\xi+\xi')`, retracting v13.660/v13.665 | cannot independently verify (network blocked); flagged as the 4th flip on identical cited text | **citation remains genuinely unresolved, not adjudicated either way** |
| v13.667 | continuous-kernel transport preserves Weyl function/determinant/characteristic | internally consistent with already-verified v13.661 machinery | **PASS** |
| v13.668 §4 | Möbius transform `[1-c_\infty m_\infty]^{-1}=\Xi/(\Xi+\xi')` | independent symbolic verification | **superseded by v13.670/672's sign correction; algebra was correct given its (later-corrected) input** |
| v13.669 | Corollary target `=(A_{\theta_*}/c_\infty)W_\infty(\pi)/W_\infty(\theta_*)` at a real `\theta_*` | independent symbolic verification; central claim later retracted | **algebra correct, but central claim retracted by v13.670's no-go (independently confirmed)** |
| v13.670 | no real `\theta` makes `B_\theta\propto E`; `m_\infty` needs a factor of `i` | independent symbolic verification of the `B_\theta` formulas and the no-go argument | **PASS on the no-go; factor/sign superseded by v13.672** |
| v13.671 | `E_a^{HB}=W_\pi+c_\infty W_0` matches `E` in the infinite limit | independent symbolic verification, conditional on v13.670's (later corrected) sign | **algebra correct; superseded by v13.672's sign fix** |
| v13.672 | corrected `E_a^{HB}=W_\pi-c_\infty W_0`, `\tau_{HB}=-i/c_\infty`, upper-half-plane zero-free result | independent symbolic verification of the corrected Möbius/finite identities | **PASS on the algebra; treated as provisional given three consecutive sign corrections on the same point (see Section 5)** |

## 7. Final freshness check

`git fetch origin master` immediately before this commit: HEAD at `658c61a` (v13.672). `git ls-tree` confirms the next free slot at commit time (see renumbering note).

## 8. Standing recommendation

Per Section 2: no further prose assertion of "I fetched the live source and it says X" should be treated as settling Corollary 1.6's target, from any thread including this one's own future entries, until a saved, inspectable artifact of the actual source text exists in the repository. Per Section 5: the Suzuki `W`-versus-raw-boundary-form conjugation convention should be pinned down once, explicitly, before further half-plane/zero-location arguments build on `\tau_{HB}`'s sign. The finite-`a` boundary-triple machinery itself (v13.661, v13.667) is solid and does not need to be redone regardless of how either open point resolves.

## 9. Renumbering note (external audit)

This entry was drafted while the ledger advanced rapidly through the same Suzuki sub-lane and was renumbered twice to stay ahead of genuine collisions: first drafted as v13.669, moved to v13.670 when `Cone_Derivation_Ledger_v13.669_Corollary_Target_as_Exact_Quotient_of_Two_Boundary_Characteristics.md` landed first (committed 2026-09-22T14:57:55-04:00) claiming v13.669; moved again to v13.674 when three further entries (v13.670 correction, v13.671, v13.672) landed and were folded into this entry's scope (Section 5) rather than triggering a separate future round. No other entry's content or numbering was altered by this; all of v13.666 through v13.672 retain their original version numbers unchanged.

## 10. Open for a future round

v13.673 (`Finite_a_Hermite_Biehler_Theorem_from_Suzuki_W0_Wpi`) landed during this entry's final freshness check and was not reviewed. Given Section 5's finding — three consecutive sign/factor corrections on the same point in the preceding entries — the next round should check v13.673 with particular care for whether it inherits `\tau_{HB}`'s sign correctly from v13.672, not assume the sequence has stabilized.
