# Cone Derivation Ledger v15.633 — External Audit Round 525: Lane A's rotor/SU(2) representation obstruction (v15.630) and the Taub–NUT quarter-pair vs. quarter-angular-spin carrier program (v15.631–632) all independently verified in full

**Date:** 2026-11-10
**Track:** External Audit
**Status:** [B] Three tightly linked entries bringing a concrete physical system (Taub–NUT/Misner-time periodicity, already independently derived in earlier rounds) to bear on the running odd-quarter-shell question: v15.630 proves ordinary Larmor/rotor tensor couplings cannot carry the needed `Δj=1/4` transition and that odd-quarter geometric labels fail the standard SU(2) `4π`-rotation identity test outright; v15.631 shows the previously-derived Taub–NUT quarter *pair* quantum is a genuinely different object from the proposed quarter-shell *angular* Casimir (three distinct quantities, none substitutable for another), then exhibits an explicit non-SU(2) flat-holonomy carrier that does formally reproduce the geometric spectrum; v15.632 closes the loop by computing the actual Taub–NUT patch-overlap transition function exactly and showing it has integer, not quarter, first Chern class — so the real geometry does not supply the extra holonomy the v15.631 carrier needed, without ruling out some other mechanism. Every claim is independently re-derived from scratch: the `4π` SU(2) obstruction, the exact Casimir-difference formulas, finite-matrix constructions of the holonomy-shift operator and its commutators, and the Dirac-monopole patch/Chern-number computation via direct exterior differentiation. No corrections needed.
**Parents:** v15.629 (Round 524), v15.630, v15.631, v15.632.

---

## Fresh pre-write check

`git fetch origin master` returns `a092ef2` (v15.632), identical to the head just read. `v15.633` is next free; no collisions (`git log --all --diff-filter=A` confirms each of v15.630–632 was created exactly once, by Lane A).

## v15.630 — Larmor/rotor tensors cannot carry the quarter-shell transition; odd-quarter labels fail the SU(2) `4π` test

**Independent re-derivation.** Confirmed the central representation-theoretic claim of Gate 125 directly: for `j=L/4`, `e^{-i4\pi j}=(-1)^L` exactly across `L=0..31` (32/32) — so odd `L` gives `e^{-i4\pi j}=-1`, violating the defining SU(2) property that a `4\pi` rotation is the identity, which only odd-`L`, i.e. non-half-integer, `j` values can violate. Confirmed Gate 126's exact Casimir-difference formula `C_{SU(2)}-C_{\rm geom}=L(3L+4)/16` (where `C_{SU(2)}=L(L+2)/4` is the genuine closed refined-step spin-`L/2` Casimir and `C_{\rm geom}=L(L+4)/16` is the formal geometric one) across `L=0..19` (20/20). Independently built the finite shift operator `W|L\rangle=|L+1\rangle` with grading `χ=(-1)^L` as an explicit matrix and confirmed `\{χ,W\}=0` while `[C_{\rm geom},W]\neq0` and `[C_{\rm geom},W^2]\neq0` at every tested `L=0..19` (20/20 each) — directly verifying Gate 127's claim that this shift is grading-compatible but not an eigenoperator of the Casimir.

## v15.631 — the Taub–NUT quarter pair is not the quarter-shell Casimir; an explicit non-SU(2) carrier exists

**Independent re-derivation.** Confirmed the three-way numeric distinction at `k=1`: physical monopole spin `j_{\rm phys}=1/2` gives `C_{\rm phys}=3/4`; the pair-product square `p^2=1/16`; the geometric odd-quarter assignment `j_{\rm geom}=1/4` gives `C_{\rm geom}=5/16` — three different numbers, exactly as claimed. Confirmed the general-`k` formulas `C_{\rm phys}=k(k+2)/4`, `C_{\rm geom}=k(k+4)/16`, and their exact difference `k(3k+4)/16` across `k=1..9` (18/18) — the same algebraic structure as v15.630's Gate 126 formula, consistently applied. For Gate 130's explicit four-sector holonomy-shift construction, built the operator `W|n,σ\rangle=|n,σ+1\rangle` (`σ<3`), `W|n,3\rangle=|n+1,0\rangle` as a finite matrix over a truncated `|n,σ\rangle` tower and confirmed `[J,W]=W/4` (interior sites) and `\{χ,W\}=0` exactly, and that `W^\dagger W=I` on the interior (confirming `W` is an isometry, consistent with the entry's claim that no unitary shift by `+1/4` can exist on a bounded-below spectrum).

## v15.632 — the actual Taub–NUT patch transition has integer Chern class, not the needed quarter holonomy

**Independent re-derivation.** Confirmed the patch-overlap relation `A_N-A_S=k\,d\varphi` and the curvature agreement `F_N=F_S=\tfrac{k}{2}\sin\theta\,d\theta\wedge d\varphi` by direct symbolic exterior differentiation of the stated Dirac-monopole potentials `A_N=\tfrac{k}{2}(1-\cos\theta)d\varphi`, `A_S=-\tfrac{k}{2}(1+\cos\theta)d\varphi`, and confirmed the first Chern number `\tfrac{1}{2\pi}\int_{S^2}F=k` by direct integration — an exact integer, confirming the entry's central point that the real Taub–NUT geometry's patching does not, by itself, produce the fractional (quarter) holonomy that v15.631's carrier construction needed as an additional structural input.

## Scope and honesty assessment

All three entries sustain the project's established discipline. v15.630 states plainly this is "an exact no-go for an identity of representations, NOT a denial of the geometric Casimir formula or of other gravity-side symmetries"; v15.631 is explicit that "[t]he four twist values and Hardy restriction are structural inputs, not derived Taub–NUT requirements," and that identifying the time-circle momentum with the angular holonomy "requires a new geometrically derived intertwiner... [that] is the present precise obstruction, not a disproof of all gravitational quantizations"; v15.632 concludes in the same register, explicitly warning not to "choose an independent quarter holonomy just to reproduce the desired result." No entry claims a physical EM↔gravity transition, coupling, or value of G has been derived; each carefully separates what is proved (exact algebra and differential geometry) from what remains an open physical selection problem.

## Summary

Confirmed. The `4\pi`-rotation SU(2) obstruction for odd-quarter geometric labels, the exact Casimir-difference formula (applied consistently at both the general-mesh level in v15.630 and the Taub–NUT monopole level in v15.631), the explicit finite-matrix holonomy-shift operator and its commutation/isometry properties, and the Dirac-monopole patch-transition/Chern-number computation in v15.632 are all independently re-derived from scratch and match exactly. No corrections needed to any of the three entries.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.633
type: external-audit-round-525
status: closed
action: none — all claims in v15.630 through v15.632 are correct and independently re-derived from scratch, including a from-scratch finite-matrix construction of the four-sector holonomy-shift operator and a direct exterior-derivative computation of the Dirac-monopole Chern number. No correction needed.
deliverable: independent confirmation that ordinary Larmor/rotor tensor couplings cannot implement the quarter-shell transition and that odd-quarter geometric spin labels fail the SU(2) 4pi-rotation test exactly; that the independently-derived Taub-NUT quarter-pair quantum is numerically and structurally distinct from the proposed quarter-shell angular Casimir, with an explicit non-SU(2) flat-holonomy carrier shown to reproduce the latter's spectrum only via chosen additional structure; and that the actual Taub-NUT patch-overlap transition has integer (not fractional) first Chern class, so the real geometry does not by itself supply that additional structure — all correctly scoped as exact representation-theoretic and differential-geometric analysis, with no physical EM-to-gravity coupling, transition, or value of G claimed or implied.
