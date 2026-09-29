# Cone Derivation Ledger v13.860 — Strategic Note: `λ_a>0` as a Candidate Lane A Target

Date: 2026-09-29

Author: external audit thread (Claude, independent instance), by the project owner's request. This is a coordination/strategy note, not a derivation — it proposes a question for Lane A to evaluate and decide, following the same non-binding convention as v13.760 and v13.833. Nothing here is certified, nothing here directs Lane A's work; the point is to put an option in front of them with the reasoning shown, not to make the call for them.

Parents: v13.833 (the original Bucket 1/2/3 triage), v13.838–v13.859 (the sandbox's Bucket 2 chain, all independently audited in Rounds 114–120), v13.801–v13.837 (Lane A's Bucket 3 finite-tail program).

## 0. Why this note exists

Since v13.833's triage, the sandbox track has collapsed Bucket 2 from "genuinely open, untouched since v13.779" down to a single, precisely named, remaining condition. Meanwhile Lane A has spent the same stretch on a Bucket-3 target (the six-root Rouché/winding-number certificate for the M3999/4000 pencil) that has been repeatedly timing out. This note asks a narrow question: given where Bucket 2 now stands, is there a higher-leverage use of Lane A's specific toolkit than the target it's currently grinding on? The honest answer requires Lane A to check one thing this note cannot verify from the audit seat — see §3.

## 1. Where Bucket 2 actually stands now (all audited, Rounds 114–120)

The chain, compressed: v13.838 characterized the gap (Suzuki's text gives no two linear conditions fixing `(I_0,I_1)`) → v13.840/842 built a kink-faithful distributional `T_a` and, via a pre-registered falsification test, ruled out a boundary-artifact explanation for the observed `Θ(e^A)` growth → v13.844 reformulated the dead edge criteria into `R1` (finite normalized limits `L_0,L_1`) and `R2` (the cancellation identity `L_0+L_1=0`) → v13.846 found the exact discrete mechanism forcing that cancellation → v13.848 proved two new theorems: the continuum (8.5) problem is uniquely solvable with no selection ambiguity, and — the load-bearing one — **the `H^1_0` Galerkin computation provably converges to Suzuki's true deficiency vector, via the same Friedrichs-extension density argument Suzuki proves himself in his own §3.2**, conditional on nothing but `T_a`'s invertibility → v13.849 honestly found no structural proof of the deeper orthogonality lemma, correctly diagnosing the kernel as outside classical Wiener–Hopf theory → v13.851–858 (Round 120) closed the downstream absorption walls and the operator-vs-Suzuki identification gaps on the `T_a`-side, leaving one open equation (whether the surviving distortion identifies with Suzuki's infinite-volume target) plus the bulk lemma's remaining piece.

**Every one of these results — without exception — carries the same standing hypothesis: `λ_a>0`.** Lemma 6.2 (Suzuki, p.21) proves `T_a=A_a-λI` invertible only for `λ<λ_a`; the entire Bucket 2 chain runs at `λ=0`, so every theorem in it is conditional on `λ_a>0`. This is not a new gap the sandbox introduced — it was already implicit in Suzuki's own text — but the sandbox's work has now made it the *only* remaining gap between the numerics and a genuine theorem about Suzuki's actual operator.

## 2. What `λ_a>0` is, precisely, and why it is not Bucket 1

\[
\lambda_a := \inf_{0\ne v\in\mathfrak D(Q_a^W)}\frac{Q_a^W(v)}{\|v\|_{L^2}^2}
\]

— the bottom of the spectrum of Suzuki's self-adjoint operator `A_a` on the finite interval `(-a,a)` (Suzuki, eq. 1.7, p.4). Proving `λ_a>0` for a given finite `a` is a **local, finite-interval spectral-positivity statement** — it is not the same claim as Bucket 1's screw-kernel positivity, which is global (all of `\mathbb R`, or the full infinite-volume Weil quadratic form) and, via v13.753's exact identity, provably equivalent to RH. `λ_a>0` at one fixed finite `a` is a strictly weaker, strictly more local statement: a coercivity/spectral-gap fact about one specific compact-resolvent operator, of exactly the kind that has known, tractable techniques (variational bounds, discretized eigenvalue certification, interval arithmetic on a Rayleigh quotient) even when the corresponding infinite-volume statement would be as hard as RH. **This is not a backdoor into Bucket 1** — closing it says nothing about RH — but it is a real, well-posed, apparently tractable target that the whole Bucket 2 program is waiting on.

## 3. The one thing this note cannot verify, and Lane A must

Lane A's current toolkit (the M3999/4000 program, v13.801 onward) is built around a specific discrete operator, `B_sm=D_{\log}-H` (the "smooth bulk," a parity-mode Hilbert-matrix construction), certified via finite-section inertia counts, interval arithmetic, and exact-rational-rank checks — precisely the machinery a rigorous `λ_a>0` certification would need. **Whether `B_sm` (or a direct discretization of it) is the same operator as Suzuki's `A_a`, or is cleanly reducible to it, has not been checked by this audit thread and is not obviously true from the two constructions' surface descriptions** — one is a discrete parity-Fourier-mode construction tied to the D12 screw function, the other is `A_a`, the Friedrichs extension of `B_a=D^*G_aD` on `H^1_0(-a,a)`, described directly via Suzuki's continuous kernel. They may be the same object viewed two ways (both trace back to the same screw-Weil quadratic form, per v13.753), or they may be related-but-distinct realizations that would need an explicit translation lemma before Lane A's existing certificates say anything about `λ_a`. **This is the first thing to determine, and only Lane A — who built and understands `B_sm` in detail — is positioned to answer it quickly.**

## 4. The proposal, stated as a question, not a directive

If `B_sm` and `A_a` are the same operator (or reducible to each other with a short argument), then Lane A's existing certified-numerics discipline — the same discipline that produced the exact endpoint inertia theorems of v13.832 and the six-dimensional Feshbach reduction of v13.836 — is very plausibly better matched to certifying `λ_a>0` (a single bottom-of-spectrum bound at a fixed finite `a`, or a small family of `a`) than to the six-root winding-number certificate it has been timing out on. A rigorous `λ_a>0` certificate would close the single standing hypothesis under the sandbox's entire Bucket 2 chain — an outsized return relative to the current Bucket-3 target, which, per v13.833's original triage, was never on the critical path to either Bucket 1 or Bucket 2.

If `B_sm` and `A_a` are *not* cleanly identifiable, this proposal doesn't apply as stated, and Lane A's current target stands on its own merits exactly as before.

## 5. What this note does not claim

It does not claim `λ_a>0` is easy — only that it is a different, more tractable *kind* of hard than Bucket 1, and structurally suited to tools Lane A already has. It does not claim the `B_sm`/`A_a` identification holds — that is precisely the open question in §3. It does not diminish Lane A's Bucket 3 work, which remains correct and rigorous on its own terms. It makes no RH, GRH, or Hilbert–Pólya claim.

## Result

\[
\boxed{
\textbf{Bucket 2's entire audited chain (v13.838–859) now reduces to one hypothesis: } \lambda_a>0 \textbf{ — a finite-interval spectral-positivity statement, not RH-equivalent, and structurally the kind of problem Lane A's certified-numerics toolkit was built for. The open translation question (does } B_{\rm sm}\textbf{ identify with Suzuki's } A_a\textbf{?) is for Lane A to evaluate. This is an option on the table, not a directive.}
}
\]
