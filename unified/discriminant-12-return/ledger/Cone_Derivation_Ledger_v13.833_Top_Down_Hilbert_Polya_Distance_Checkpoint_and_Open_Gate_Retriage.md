# Cone Derivation Ledger v13.833 — Top-Down Hilbert–Pólya-Distance Checkpoint and Open-Gate Retriage

Date: 2026-09-28

Author: external audit thread (Claude, independent instance), by request of the project owner. This is a coordination/strategy checkpoint, not a new derivation. Nothing below overrides a proven result; it re-sorts already-established facts by what they are actually load-bearing for. Every closed item cited here is cited to the entry that proved it and is not reopened.

Trigger: the project owner asked, from outside any specific audit round, "how far are we from the Hilbert–Pólya operator," followed by "work this top-down instead of inside-out and figure out what works." This entry is the resulting triage, written so Lane A (and any other contributor) can see it without reconstructing it from ~70 ledger entries.

Synchronization: live ledger head checked immediately before this write is v13.832 (`Full_Rho002_Endpoint_Inertia_Theorem`), commit `34de06e`, with two follow-on research commits (`c6d95c3`, `f0b39b5`, `8d89829`) not yet promoted to a ledger entry as of this write. No collision on the present version number. **This checkpoint does not audit v13.832** — that is separate, ordinary audit business and will be taken up as its own round.

## 0. Why this checkpoint exists

Lane A's naming has been reused across genuinely different programs at different times (see v13.760, which already did one round of this same registry service for the *previous* incarnation of "Lane A"). Read superficially, the ledger looks like a single monotone climb toward an operator. It is not: it is one continuous lineage that branched, partially retracted, and re-branched, and the branch that is structurally closest to an actual Hilbert–Pólya-style construction has been sitting untouched since **v13.779** (2026-09-25) while a separate, more numerically tractable branch — the finite-section screw/tail-resonance program — absorbed essentially all subsequent effort (v13.792 through the current v13.832). Nobody currently working the live branch was necessarily shown this framing, hence this entry.

## 1. The actual target object, restated

The one candidate in the entire ledger that is operator-theoretic rather than quadratic-form-theoretic is v13.754's boxed identity:
\[
\boxed{
E(z)=ic_\infty\,\Xi(z)\left[m_\infty(z)-\tau_{\rm HB}\right],
\qquad
\tau_{\rm HB}=i/c_\infty=i\,\xi(3/2)/\xi'(3/2),
}
\]
where \(m_\infty\) is the Weyl function of the (infinite-volume limit of the) Suzuki finite deficiency-index-\((1,1)\) self-adjoint extension. If \(m_A\to m_\infty\) could be established rigorously (not asymptotically/numerically) together with the correct boundary normalization, this is the one object in the project that would tie an actual operator's spectral data to \(\Xi(z)\) by an unconditional formula. Everything else described below is either upstream of this object, downstream of it, or orthogonal to it.

## 2. Retriage: four buckets, by what each open item can and cannot do

### Bucket 1 — Equivalent to RH itself. No finite computation closes these; only a counterexample would move them.

- **Suzuki/Weil screw-kernel positivity** (v13.753 §6, tagged `[C]`). Via the unconditional identity \(Q_{\rm Suz}[DF]=Q_{\rm Weil}[F]\) (v13.753 §3, hand-verified this session and in Round 91), positivity of the screw kernel on the relevant test class is exactly Weil's classical 1952 positivity criterion, which is exactly RH. This is not a technical lemma pending more work; it is the 160-year-old open problem wearing a different notation. No amount of finite-section certification anywhere in this ledger can prove it; a rigorous finite counterexample could disprove it.

- **Correction of a framing error made earlier in this same chat, recorded here for the record**: the Schur parameters \(\kappa_0,\kappa_1\) (v13.792–795) were informally described to the project owner as a live RH-positivity probe. On closer reading they are not: they are Schur parameters of a Weyl function \(m_A\), which is Herglotz/Nevanlinna by construction for *any* self-adjoint extension, RH or not. \(\kappa_0,\kappa_1\in[-1,1]\) is therefore automatic for the exact operator (v13.795 §2 says this explicitly) and a finite-section value outside that range is a truncation/conditioning diagnostic, not evidence about positivity. \(\kappa_0/\kappa_1\) convergence work belongs in Bucket 3 below (numerical-quality plumbing for the Weyl-function branch), not Bucket 1.

### Bucket 2 — Genuinely open, *not* equivalent to RH, and is the actual bottleneck on the one operator-flavored branch (§1)

- **The boundary/integration-constant problem**: determine \(I_{0,A}/C_A\), \(I_{1,A}/C_A\) "from Suzuki's actual admissible deficiency-domain normalization and global solution conditions" — v13.773 §5, restated as the correct next gate in v13.773 §7. This is a well-posed linear boundary-value problem for a specific finite operator, not an unsolved conjecture of mathematics at large. It is the thing standing between the current state of the art and \(m_A\to m_\infty\) convergence, which is the thing standing between that and §1's identity meaning anything concrete.

  History of this specific gate, so it isn't re-litigated from scratch: obstruction found (v13.761 §6, v13.765 §6–7: bulk coercivity controls response size but not boundary-feedback sign/matching) → partially diagnosed as self-inflicted, i.e. the "Schur nonresonance" framing was measuring an artifact of an inadmissible source-splitting, not a real obstruction (v13.773, which retracts v13.745/758/761/765–766/769 on exactly this point) → a "Wiener–Hopf completion" claimed (v13.774) → retracted/bypassed instead of repaired (v13.776) → **this audit thread placed that bypass on HOLD at Round 98** (v13.778) because it resurrected a construction v13.757 had already identified and avoided as "the retracted inverse-source ansatz" → HOLD resolved by retraction, not repair (v13.779): "\[N\] no source-faithful equation follows from those differentiated identities without the missing domain data." That is where it was left. **No entry since v13.779 has returned to it.**

- **The de Branges/boundary-triple intertwining question** (v13.753 §11, last of the entry's own "next nonredundant gate"): whether the screw–Weil unitary map intertwines Suzuki's paired deficiency characteristic \(T_{\rm pair}(z)=C_\xi\,\Xi(-iz)/E(z)\) itself, not merely its quadratic form. Same family as the item above, also untouched since it was named.

  **Recommendation, not a directive**: if the goal is genuinely to close distance to an operator (as opposed to producing more certified finite-window facts), this bucket — not Bucket 3 — is where new effort has the highest expected payoff, precisely because it is hard-for-this-project rather than hard-for-mathematics.

### Bucket 3 — Rigorous, well-executed, independently useful as verification discipline, but not on the critical path to Bucket 1 or Bucket 2

- The entire M=3999/4000 finite-tail resonance/inertia/Feshbach-residue/projector-certificate program, v13.801 through the current v13.832 (Full Rho-0.02 Endpoint Inertia Theorem, not yet audited as of this checkpoint) — i.e., everything covered by External Audit Rounds 99–111 plus whatever v13.832 turns out to contain. Every theorem in this bucket is a true statement about one specific truncated approximating pencil's resonance structure in a small window near the origin. None of it, however extended, establishes \(m_A\to m_\infty\), closes the Bucket 2 gate, or touches Bucket 1. It is good, disciplined engineering — several genuine bugs have been caught and fixed here (Rounds 102–104), and the caps/margins have visibly gotten more honest since — but it is scaffolding around a different, smaller target than §1's object.
- The \(\kappa_0,\kappa_1\) numerical-Galerkin estimation itself (v13.794–800), now correctly recategorized per Bucket 1's correction as quality-control plumbing for the Weyl-function branch rather than a positivity probe.
- Historical precedent, same shape and same distance from the actual target: the N=16001 finite-precision LDL-certificate saga, v13.351–380.

### Bucket 4 — Dormant, unclear present relevance

- Lane B (norm-quotient/idele-class representation), untouched since v13.736 per v13.760's own registry. No new status to report; flagged only so it isn't forgotten twice.

## 3. What this checkpoint does and does not claim

This entry does not:
- prove or disprove RH, GRH, or Weil/Suzuki positivity;
- claim Bucket 2's boundary-constant problem is easy, only that it is a different kind of hard than Bucket 1's;
- diminish Bucket 3's results, which remain exactly as true and as narrow as their own entries state;
- direct any contributor's time — the recommendation in Bucket 2 is offered, not imposed.

It does claim, and stands behind: the screw-kernel-positivity gate (Bucket 1) is RH-equivalent by direct composition of two already-proven facts in this ledger (v13.753 §3's identity and classical Weil positivity), and the boundary-constant gate (Bucket 2) has not been touched by any entry between v13.779 and the current head.

## Result

\[
\boxed{
\textbf{Four buckets, one honest map: (1) RH-equivalent — no finite computation closes it; (2) genuinely open and load-bearing for the one real operator candidate in the ledger (v13.754), untouched since v13.779; (3) rigorous but orthogonal finite-section scaffolding, all current live work; (4) dormant.}
}
\]

This checkpoint supersedes no proof and blocks no work; it exists so that whoever picks up Lane A's next gate can choose Bucket 2 knowingly rather than by default.
