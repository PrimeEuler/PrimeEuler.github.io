# Cone Derivation Ledger v15.597 — External Audit Round 520: Lane A's parabolic discrete-slope/cross-shell boundary address (v15.595) and inter-shell energy-commutator obstruction (v15.596) independently verified in full

**Date:** 2026-11-10
**Track:** External Audit
**Status:** [B] Two tightly linked entries extending the odd-quarter boundary program (v15.572–581) with a native-coordinate reformulation of the already-audited source-acceleration identity, a concrete rank-2 cross-shell witness map, and its exact energy-commutator structure — while explicitly and repeatedly declining to promote any of it to a physical shell-changing operator, photon, or field coupling. Every symbolic and arithmetic claim in both entries is independently re-derived from scratch and confirmed exactly; no corrections needed.
**Parents:** v15.581 (Round 519), v15.595, v15.596.

---

## Fresh pre-write check

`git fetch origin master` returns `35a989c` (v15.596), identical to the head just read. `v15.597` is next free; no collisions (confirmed via `git log --all --diff-filter=A -- "*v15.595*" "*v15.596*"` — each version created exactly once).

## v15.595 — parabolic finite-difference source response and next-shell missing-target address

**Independent re-derivation of Section 1.** Built `J±`, `Jx`, `Jy`, `M=Jz`, `H0=-gJx`, `S=i[H0,M]` from scratch on refined odd-quarter shells `j=1/4,3/4,5/4,7/4,9/4,13/4` and confirmed symbolically that `S=-gJy` exactly at every `j`. Independently computed `Ṡ=i[H0,S]` and confirmed `Ṡ=-g²(M+D/2)` (D=`[J+,J-]-2M`) exactly — consistent with the already-audited v15.580 identity, as the entry itself notes. Confirmed the diagonal identity `⟨m|Ṡ|m⟩=g²/2(w_up-w_down)` entry-by-entry against the actual truncated matrix at every shell state, not just symbolically. Confirmed `W_up(m)=R²-(m+1/2)²=(j-m)(j+m+1)` and `W_down(m)=R²-(m-1/2)²=(j+m)(j-m+1)` by direct algebraic expansion, and confirmed the formal identity `W_up-W_down=-2m` symbolically (not a spot check). Confirmed the `j=5/4` witness numerically: `m=-1/4` gives `W_up=3`, `W_down=5/2`, `⟨Ṡ⟩=g²/4`; mirror `m=1/4` gives `W_up=5/2`, `W_down=3`, `⟨Ṡ⟩=-g²/4`; the upper-open source `m=3/4` gives formal `W_up=3/2=c`. All match the entry's cited values exactly.

**Independent re-derivation of Section 2.** Built the rank-2 witness map `T=√c(|j',j'⟩⟨j,j-1/2|+|j',-j'⟩⟨j,-j+1/2|)` from scratch at each tested `j`, together with an independently-built Casimir-deficit operator `E=j(j+1)I-Jx²-Jy²-Jz²` on the source shell (built fresh, not copied from the cited formula). Confirmed `T†T=c(P_++P_-)=2E` exactly as an explicit matrix identity at every tested `j`, and confirmed the claimed magnetic-coordinate shifts `(M_{j'}T-TM_j)=±T` on the two legs exactly.

## v15.596 — inter-shell energy-commutator gate and native factor-shift obstruction

**Independent re-derivation of Section 1.** Built the diagonal "geometric radius" operator `𝓡=(j+1/2)I` and Casimir-label operator `𝓒=j(j+1)I` on each shell from scratch, together with `T` as in v15.595, and confirmed both commutators `[𝓡,T]=T/2` and `[𝓒,T]=(j+3/4)T` exactly at every tested `j` (symbolic matrix identity, not numeric). Split `T=T_++T_-` and independently confirmed `[M,T_+]=+T_+`, `[M,T_-]=-T_-` exactly. For the conditional Hamiltonian `H=αR+βC+ωM`, confirmed `[H,T_±]=(α/2+β(j+3/4)±ω)T_±` exactly by direct symbolic substitution — a genuine algebraic consequence of the three already-confirmed commutators, not a new independent claim. For the transverse driver `Jx`, independently computed `J_{x,j'}T-TJ_{x,j}` explicitly and confirmed it has nonzero support **outside** `T`'s own two-entry support at every tested `j`, directly verifying the claim that this commutator is not proportional to `T` (i.e., `Jx` does not make `T` a fixed-frequency transition operator).

**Independent check of Section 2 (factor coordinates).** By hand: `u=j+m,v=j-m` at the upper-open state `m=j-1/2` gives `(u,v)=(2j-1/2,1/2)`; at the target `j'=j+1/2,m'=j'` gives `(u',v')=(2j+1,0)`; difference `(Δu,Δv)=(+3/2,-1/2)` exactly as claimed. The mirrored lower branch gives `(-1/2,+3/2)` exactly as claimed. Both confirm the stated obstruction to a pure monotone-raising coordinate semigroup reaching the target in a single step.

## Scope and honesty assessment

Both entries sustain the same careful separation maintained since v15.572: v15.595 states plainly that `T` is "a concrete geometric destination and rank-two witness map, not a canonical physical operator," and that "the existence of a finite map alone does not specify phase, normalization... or selection rules"; v15.596 is explicit that the conditional-Hamiltonian energy gaps assume a Hamiltonian form the cone "has not *selected*... as its physical shell energy," and that the factor-coordinate composite path "is not unique as an operator." Neither entry promotes `T` to a physical creation operator, photon, or field coupling, nor claims a resolved obstruction either way — both end with an explicitly open next gate.

## Summary

Confirmed. Every factor-pair/parabola identity, the diagonal source-response formula, the `j=5/4` numeric witness, the rank-2 witness map's exact norm identity `T†T=2E`, its magnetic-coordinate shifts, both inter-shell energy commutators `[𝓡,T]` and `[𝓒,T]`, the `±M` commutators on `T_±`, the derived conditional-Hamiltonian commutator formula, the non-proportionality of the transverse-driver commutator, and both factor-coordinate shift calculations in v15.595–596 are independently re-derived from scratch and match exactly. No corrections needed to either entry.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.597
type: external-audit-round-520
status: closed
action: none — all claims in v15.595 and v15.596 are correct and independently re-derived from scratch, including a from-scratch Casimir-deficit operator and all four inter-shell commutators. No correction needed.
deliverable: independent confirmation of the native parabolic-coordinate reformulation of the source-acceleration identity, the j=5/4 numeric witness, the rank-2 cross-shell witness map's exact norm and magnetic-shift identities, and the full energy-commutator/factor-coordinate obstruction structure of v15.596 — all correctly scoped as finite algebraic architecture, with no physical shell-changing operator, photon, or field coupling claimed or implied.
