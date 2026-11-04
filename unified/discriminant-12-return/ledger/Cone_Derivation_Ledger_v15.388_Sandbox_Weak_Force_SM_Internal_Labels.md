# Cone Derivation Ledger v15.388 — Sandbox return: weak force on the cone — the SM internal label system reproduced in one frame

Date: 2026-11-04 (America/New_York). Lane: sandbox (our Lane B), depositing the weak-force exploration run in the Cone dynamics side thread, 2026-11-03 → 2026-11-04, at Jeremy's direction ("Ledger it", 2026-11-04). Parents: live HEAD v15.387 at deposit. Status: [D] exact, script-verified reproduction of the Standard Model internal label system in one cone frame, with exactly three imports named at the steps that use them; scope limits and negatives stated in-line. This is a disclosure deposit under the ledger-everything policy: listing is disclosure, not endorsement by the other lanes.

## Claim

The Standard Model's internal label system — color (p,q) and triality, weak slot and parity, hypercharge fractions AND integers, matter and antimatter, and the composite singlet rules — is reproduced in one frame built from the cone's native k=2 structure (U(2) container; lepton and Higgs doublets as shells) and Jeremy's AM-GM family's k=3 member, with exactly three imports named at the steps that use them.

## Chain of results (each exact, script-verified)

1. Single-cone and linear bicone hypercharge routes CLOSED negatively: singlet hypercharge differences have gcd exactly 2/3 (difference lattice (2/3)Z), so no integer β works; the B2 fit family (β = −2/(3t)) fits the full table but selects nothing.
2. Nonlinear door CLOSED: a compact U(1)'s charge lattice is fixed by single-valuedness (representation theory), independent of dynamics; thirds require the triple cover — a group-structure move, not a coupling. In the SM, fractional hypercharge IS color triality read through the (SU(3)×SU(2)×U(1))/Z₆ quotient.
3. Parabola 2/3 (v14.592: segment area, Airy exponent, evolute) is native and exact but the WRONG TYPE: it fails additivity under composition ((N−¼)^{2/3}: Q(1)+Q(2)=2.2777 ≠ Q(3)=1.9629), so it cannot be a charge. The 2/3 lands on heights/energies; the phase lattice stays integral.
4. The k=3 AM-GM member supplies a genuine Z₃ grading ON STATES: the 2+1 split grading c mod 3 (third-mode occupation; NOTE: not the (N,0) shell irrep triality N mod 3 — erratum recorded in the report). (k=2 parity, k=3 split grading) forces Y mod 2 for all eight multiplets with zero free parameters; every multiplet occupies an occurring slot with pair-state counts exactly 2j+1. Triality cannot be derived from weak-side data alone (L_L/Q_L share every k=2 label) — the second sector's existence is the content.
5. Integer parts: the anomaly system on Y_i = r_i + 2n_i has the complete solution family Y = t·(Q:1, L:−3, u:4, d:−2, e:−6), t = 2a + 1/3, plus a u↔d mirror. The cone's own native lepton anchor (Y_L = −1, spectrum {0,−1}) selects a = 0 uniquely; the mirror dies by charge matching in Q_L; Yukawa ties fix Y_H = +1 from all three terms; Y_singlet = 0. Full SM hypercharge table recovered uniquely.
6. Antimatter embeds in the signed third-mode sector (c → −c, grading flips sign); all eight anti-multiplets reproduce.
7. (p,q) color completion: the identity c = p − q holds EXACTLY on all fifteen fields (generation + antimatter + H + W + gluon) — the split grading and color irrep triality are one grading seen from the two factors. Composite rules check by dimension and triality: q⊗q̄ = 1⊕8, q³ = 10⊕8⊕8⊕1, 8⊗8 contains its singlet; box counting alone forbids singlets for q, qq, qq̄. (Representation-level confinement pattern only; no mechanism claimed.)

## Imports (named, not hidden)

(i) anomaly cancellation as a consistency condition — a promissory note against a chiral gauging that does not yet exist on the cone; (ii) the anomaly color multiplicity κ = 3, imported from the SM — its only candidate native source is the list length k = 3 itself (identification, not derivation); (iii) NOT an import: the lepton anchor is the cone's own pass-1 shell.

## Negatives / scope limits, stated plainly

Ŷ is NOT a frame operator (e_R sits at the frame origin with Y = −2 — the exact linear system has no solution); chirality is located but not opened (its whole content is one correlation between the internal frame and the bicone's (½,0) Spin(4) factor); generation slots c = τ + 3g are unbounded — no generation count, masses, or mixing; no gauge dynamics, couplings, Weinberg angle, or confinement mechanism. c = p − q is a consistency of the completed assignments (both sides trace to τ_SM), not a derivation of one factor from the other.

## Verdict

Hypercharge problem (fractions and integers) CLOSED, conditional on the three imports above; SM internal label system reproduced in-frame. Doors left standing, each now separate: chiral correlation, generation count/mixing, gauge dynamics.

## Payload and snapshot note

Payload: `unified/discriminant-12-return/payloads/weak_force_cone_v15_388/` — REPORT.md (the full thread report) plus the nine exact-arithmetic scripts, with `MANIFEST.sha256`. All ten files are byte-identical to the versions verified in the sandbox on 2026-11-04 (every script re-executed, exit 0; the "False" lines in their output are the documented negative results). SHA-256:

- REPORT.md `6be251fbf78aa7cae8ed3e82b4924256a0d2ee70a2bfbbf358d2d14fd8a0dc67`
- weak_force_cone.py `99100d3cbec9ccf04aed752561566438a9823b6a04bebfdbe2de15d1fd418281`
- bicone_hypercharge.py `7f727b9b62eb97814ba97f3810edf68ca65678eff8a8f759606de14bc0806596`
- nonlinear_z3_door.py `5e75239297d97c0a17dd7cd3ea4499270e200d35fd465a29551c7820bf5ff6fa`
- type_conversion_check.py `6525b779d52e37a6bf6d825b938e16f65c3cd4a27e65765dab01ffb59d5edd88`
- amgm_k3_triality.py `e01c9fc3b7d2051443f5ab0994bf957acdf0128c4d86973ddd2ed73a5730ad06`
- close_the_gap.py `877a06a68dc24fd915b08c1aef5ab39ee7d1fee3d62d8fa5b92e46`
- anomaly_integer_parts.py `f1c0e9cdbef3ca28f028c40d718b1f65e80eae6afbedc9363cabc1ffd2cb7ef3`
- open_more_doors.py `823d4360e086c8f2dccad0d08681ef77cdfea514f5234d82b633819cd364cbad`
- pq_color_completion.py `f536042591184a445287361db9b049dabe6811c331cf186e690cd78ddf68510a`

Snapshot note: the deposited REPORT.md is the report exactly as verified — its first 536 lines, ending at the (p,q) color completion. The living sandbox report has since grown two further evening sections ("2 SU(3) glued together?" and the acceleration-parabola coupling anatomy, with their own scripts `doubled_k3.py` and `coupling_ratios.py`); those are NOT part of this deposit, are not covered by this entry's chain or verdict, and remain sandbox-only pending their own deposit.
