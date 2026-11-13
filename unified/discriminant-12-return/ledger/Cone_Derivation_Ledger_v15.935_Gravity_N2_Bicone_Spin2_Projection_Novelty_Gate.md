# Cone Derivation Ledger v15.935 — Does n=2 rest/Casimir circle coincidence select the spin-2 bicone channel?

**Date:** 2026-11-13 US Eastern. **Track:** Gravity / bicone spin-two test. **Parents:** Gravity v15.905, v15.931–934, and already-staged `arxiv/note-bicone-dipole-alpha/Note_BiconeDipole_FineStructure_v1.0.tex`, v15.625/630 Casimir-vs-physical-spin distinctions. **Immediately prewrite live HEAD:** 81899af1df2f65cd418ea3c6891028149c8073ff, target path absent. Strictly additive; preexisting papers, Audit, Sandbox, Suzuki production/certifications untouched.

**Owner's hypothesis:** The exact coincidence at factor-pair n=2, `R_rest²=n=2=R_C²=n(n+2)/4`, might distinguish a spin-2 graviton.

**Status:** [D] exact coupled spin1×spin1 decomposition, total-spin projectors and operator eigenvalues; [N] crossing is a multiple of identity and cannot pick J_total=2; [C] adding inter-cone exchange splits channels but imports a coupling; [O] a derived spin-2 massless helicity field and stress-energy coupling.

## Gate 689 — indexing discipline and crossing in glued bicone

The **factor pair** `(x,y)=(n,1)` of Paper C uses Fock total occupation N=n, single Schwinger spin **j=n/2** and outer radius **R_o=(n+1)/2**. At **factor n=2**, each copy is spin j=1, the inner/rest radius squared is 2 and **each** single-cone angular Casimir is j(j+1)=2. The outer transition radius squared is 9/4, yielding the usual 1/4 EM completion.

The *hydrogen principal-shell* convention in the independently staged bicone note is **j=(n_H−1)/2**, hence the same double spin-one representation corresponds to **n_H=3**, NOT hydrogen n_H=2. Conflating n and n_H here would falsely attach the spin-2 component to the wrong physical atom shell.

## Gate 690 — exact spin projectors

Set two ordinary, genuine spin-one SU2 generators `J,K` on `C³⊗C³` (9 dimensions), total rotation `L=J+K`, and exchange invariant `X=J·K=(L²−J²−K²)/2`. Since each spin-one Casimir equals 2I, the eigenvalues of X are **−2,−1,+1** in total-spin **0,1,2** sectors, respectively. The corresponding exact orthogonal projectors are

**P_0=(X+I)(X−I)/3** (rank 1),
**P_1=−(X+2I)(X−I)/2** (rank 3),
**P_2=(X+2I)(X+I)/6** (rank 5).

They satisfy `P_aP_b=δ_ab P_a`, `sum P_a=I_9`, and `L² P_s=s(s+1)P_s`. Interchange of the cones is `Swap=P_0−P_1+P_2`: symmetric spin-0 and spin-2 sectors, antisymmetric spin-1. Therefore bicone exchange parity alone **cannot distinguish** spin-0 from spin-2.

## Gate 691 — explicit circle-selector negative

On this joint space, a faithful symmetrized **single-cone** Casimir circle has squared-radius operator `C_pair=(J²+K²)/2=2I_9`. Its proposed decelerated-rest circle at factor n=2 has squared-radius operator `R_rest²=2I_9`; and the outer transition circle `R_trans²=(9/4)I_9`.

Thus **C_pair−R_rest²=0 on ALL NINE states**, including spin 0 and 1; `R_trans²−C_pair=(1/4)I_9` also does not distinguish them. Equivalently `(C_pair−R_rest²)P_s=0` for s=0,1,2. The n=2 crossing is **not a spin-two selector** in this canonical bicone: it is common to the entire product representation. This exact negative does not disprove another *independently specified* acceleration/deceleration action that acts nontrivially on the tensor product.

A chosen rotationally invariant exchange term `H_ex=gJ·K` would give channel shifts `−2g,−g,+g`; a chosen polynomial f(L²) can project exactly onto spin 2. But **nothing in the common AM–GM circle coincidence fixes g, its sign, or a special f**, and importing one to select spin 2 is not an emergent graviton prediction.

The physical graviton is a massless helicity±2 excitation of a Lorentzian spin-two gauge field; a finite nine-state rotational SU2 multiplet includes five massive-spin-2 polarizations in the abstract rotation representation and does not furnish those gauge constraints or stress-energy dynamics.

## Gate 692 — reproducibility and next discriminating question

**Reproducer:** `research-notes/k4_bicone_n2_spin2_projectors_v15_935.py`, additive commit **81899af1df2f65cd418ea3c6891028149c8073ff**. Exact SymPy matrices were first independently constructed and executed locally: 1+3+5 projector ranks; total L² eigenvalues 0,2,6; X eigenvalues −2,−1,+1; exchange parity; all nine crossing conditions; free exchange splitting, all PASS. Independent Audit pending.

**Verdict:** **YES**, spin 2 is an allowed component of the double spin-one bicone; **NO**, the n=2 geometric crossing on each constituent singles it out. The ratio of geometrical radius squares 2:2:9/4 remains an ordinary fixed-shell identity with no spin-sector selectivity, dimensional frequency, physical gravitational action, or G-free new measurement.

**Next:** If pursuing a physical spin-2 lead, require an independently supplied **rank-two symmetric traceless field/strain/tidal tensor** coupling from gravitational action, and calculate its matrix elements across s=0,1,2 without adjustable channel projectors. Check angular selection rules against ordinary quadrupole coupling and whether any dimensionless ratio differs from standard rotational Clebsch–Gordan predictions. Do not equate quarter-grid geometric C=L(L+4)/16 or a numerical value 2 with graviton helicity.
