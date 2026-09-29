# Cone Derivation Ledger v13.863 — External Audit Round 121

Date: 2026-09-29

Auditor: External audit thread (Claude, independent instance).

Scope: v13.861 (H1 closed via dual-slot canonization) and v13.862 (PAIR-H located — found to be analytically equivalent to the standing "0.48 value" problem). Two entries, unlike Round 120's batch of eight, so full-depth verification is proportionate here.

Verdict: **PASS on both.**

## 1. v13.861 — H1 closed

**The load-bearing citation, checked directly against the PDF (pp.21–22), not taken on the entry's word.** The entry's central move is bypassing the hard version of H1 (direct membership `e_z\in\mathcal H(T_A)`) in favor of a "dual-slot" construction needing only `T_A^{-1}e_z\in\mathfrak D(T_A)`. I pulled §6.3 directly: "Let `e_z(x):=\exp(-izx)`. Since `e_z\in L^2(-a,a)` and `T_a` is invertible, the equation `T_aw_z=e_z` has a unique solution `w_z\in\mathfrak D(T_a)`... we conclude that `w_z=v_z`. Hence `v_z\in\mathfrak D(T_a)`." This is exactly the fact v13.861 §1 cites ("§6.3 proves `v_z=T_a^{-1}e_z\in\mathfrak D(T_a)`"), reproduced essentially word for word — not a paraphrase drifting from the source. Since `e^{zx}\in L^2` for *every* complex `z` trivially (bounded on a finite interval regardless of `\mathrm{Re}(z)`), and `T_a` invertibility is the standing `λ<λ_a` hypothesis already tracked throughout this chain, the dual-slot construction `u_{A,z}:=\bar DT_A^{-1}e_z` is well-founded on ingredients already established, not new assumptions.

**The β/α reading distinction is the entry's real content, and it's correctly reasoned.** Reading (β) — literally `\overline{\langle e_{\bar z},e_{\pm i}\rangle_{L^2}}` — would make the pairing `T_A`-independent, since the single `T_A^{-1}` is undone by taking the energy inner product against a bare exponential; this is diagnosed as "structurally wrong for Weyl data" because the whole point of the Weyl-function construction is that it depends on the operator. That diagnosis is correct: a Weyl function that doesn't depend on the operator whose Weyl function it claims to be isn't the object anyone wants. Reading (α) — the `u_{A,\bar z}` reading — keeps the `T_A^{-1}` and is entire in `z`, matching Suzuki's own `\langle v_z,v_\pm\rangle` pairing. Correctly resolved.

**Appropriately scoped.** Prong (a) (direct membership) is explicitly left open as "a standalone analytic gap if anyone ever wants it," not silently dropped — the entry is honest that it sidesteps rather than solves the harder question, because the easier route suffices for the T-side program. The v13.725 hygiene flag (that `e^x\in\mathcal H(T_A)` was itself an unstated premise there) is a genuine, useful catch rather than padding.

## 2. v13.862 — PAIR-H located, and this is the round's important finding

**The central claim is simple arithmetic once the setup is granted, and I checked it holds.** Total `I_{0,A}/(Ae^A)\to L_0` (given R1, already established) and edge `\to E` (given COMB-H); since bulk is defined as total minus edge over the same split, bulk `\to L_0-E` automatically. "(PAIR-H₀)" is exactly the statement bulk`\to0`, so (PAIR-H₀) `\iff E=L_0` follows immediately — correct, and the entry doesn't oversell this as a deep result, just an honest bookkeeping consequence that happens to be strategically important.

**Why this matters for what Lane A proposed:** the project owner relayed that a fresh Lane A instance, reading this ledger, judged "the T-side fixed-`A` pairing completion/H1 gate, followed immediately by PAIR-H" as the best next target. Both halves of that plan have just moved under it. H1 is now closed (v13.861, confirmed above) — so that half is already done, by the sandbox, before Lane A could start on it. PAIR-H is *not* closed, but this entry shows it isn't the "immediately follows" quick second step it might have looked like either: v13.862 §4 shows proving the bulk pairing vanishes is the *same depth* of problem as deriving the analytic value of the `0.48` constant — the standing hardest-open-item across every Bucket 2 entry since v13.849. Concretely, closing PAIR-H needs either new resolvent-kernel/oscillatory-integral asymptotics for `T_A^{-1}` in the bulk (explicitly said not to exist yet anywhere in the ledger), or the same edge-integral identity `E=L_0` that nobody has derived. This is a real, substantive redirection of difficulty, not a rhetorical hedge — worth relaying plainly rather than letting "PAIR-H" sound like a follow-on item of the same size as H1.

**The three-route stall analysis (§3) is honest, not padded.** Duality, T-side machinery, and the selection principle are each tried and each explicitly shown insufficient, with the specific shortfall named in each case (e.g., the duality bound overshoots the target by a factor of `Ae^{-\delta}`, and that gap "is" the oscillatory cancellation nobody has controlled yet). This is the same honest-negative-result discipline this thread has shown consistently since v13.849.

## 3. What I did not re-verify

I did not independently reproduce v13.855's numerical figures cited again here (bulk `<0.005\cdot Ae^A` at `A=6`, etc.) — those were already independently reproduced in Round 120. I did not attempt to verify the un-derived `c_1=-L'/L(1/2,\chi_{12})` claim (flagged by the entry itself as "analytic value not derived here," i.e., not claimed as established).

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.861 and v13.862 confirmed.} \textbf{H1 is genuinely closed — the citation underpinning it reproduces Suzuki's §6.3 essentially verbatim, checked directly. PAIR-H is not closed, and — this round's operationally important finding — it is now shown analytically equivalent to the standing "0.48 value" problem, the hardest unresolved item in the whole Bucket 2 chain, not a quick follow-on to H1. Both facts are directly relevant to any fresh assessment of what Lane A's next gate should be.}}
\]
