# Cone Derivation Ledger v14.865 — Spin-zero focus and first ladder-edge test

Date 2026-10-25. Parents v13.595, v14.620, v14.767, v14.864. Research note research-notes/Spin_Zero_Focus_First_Ladder_Edge_Test.md commit 9a912ff672fceb833ad264a0fac8ceea40fdf8d2. Live prewrite HEAD 9a912ff672fceb833ad264a0fac8ceea40fdf8d2. Additive only; Suzuki/far-tail untouched.

[D] The outer SU(2) edges m=-j and m=j-1 have equal squared J+ amplitude 2j and centered positions X=1/2-j and X=j-1/2. Eliminating j yields the unit parabolas Y²=1−2X and Y²=1+2X, with vertices ±1/2, common focus (0,0), and intersection (0,1). The j=1/2 representation contains one edge X=0,Y=1, exactly this intersection.

[D] At j=0 all Jx,Jy,Jz,J± vanish on a one-dimensional representation. No ladder transition exists. Formal extension of either outer-edge formula to j=0 gives distinct VERTICES (±1/2,0), not the common focus. Accordingly calling (0,0) a spin-zero focus is geometric terminology and does not prove that the SU(2) j=0 representation sits there as a physical ladder edge. The edge operators preserve fixed j and cannot couple V0 to V1/2.

[D] Under dilation u, the curves become Y²=u²±2uX, with vertices ±u/2 and common focus zero; the first j=1/2 edge occurs at (0,u). The geometric height u does not change the dimensionless spin-j transition amplitude; the u factor is coordinate choice.

[O] Study an explicitly defined pair-creation/number-changing operator between the two-oscillator bicone vacuum and its first nontrivial pair sector. Distinguish bicone total-spin L=0 inside j=1/2⊗j=1/2 from j=0 oscillator vacuum. No scalar particle, Higgs identification, Newton G, or EM/G hierarchy derived.

Flags: first_last_edge_parabolas=EXACT; common_focus_zero=EXACT; jzero_SU2_edge=ABSENT; first_edge_intersection=EXACT; focus_equals_jzero_operator_state=NOT_DERIVED; quarter_grid_operator_selection=NOT_DERIVED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: magnetic-first-last-ladder-and-spin-zero-focus
parent: v14.865
status: open
action: Check first/last J+ edge derivation, focus versus intersection, j=0 vanishing-generator caveat, and u scaling; assess number-changing bicone maps separately. Do not modify Suzuki/far-tail.
deliverable: scoped verdict.
