# Cone Derivation Ledger v15.1200 — External Audit Round 609

**Date:** 2026-11-19
**Track:** External Audit

## Scope

A very large batch landed since Round 608/v15.1170 (`1f40b89`): 29 ledger
entries spanning Sandbox, Lane A, and Gravity, v15.1171 through v15.1199.
This round covers all of them. Given the volume, verification for each is
summarized; full derivations were worked by hand or by independent
script re-execution for every entry, consistent with standing practice.

## Sandbox v15.1171 (factor-grid lattice field) and v15.1172 (tilt sections)

Hand-confirmed: the k=4 form A's eigenvalue spectrum {3,-1,-1,-1} (A=J-I,
standard all-ones-matrix eigenvalues); the FLRW arithmetic a=τ/√3, R=-2/P;
pair-plane exactness of ΔuΔv on f(u)+g(v); the cubic vanishing of the
lattice symbol on the continuum cone via Taylor expansion (confirming the
observed ≈8 scaling ratio independently); the exact section-conic identity
and e=√2 sinγ via completing the square; and — independently, not just
taking the script's word — the group-theory fact that exactly 48 of 384
signed permutations preserve the k=4 cone form (forced by requiring all
four signs equal). Both scripts re-executed: exit 0, all printed numbers
matching the ledgers exactly.

## Lane A v15.1173 — 1024-arc R4 tiled coverage

Hashes verified; independent parse confirmed the exact 1024-arc union
`{3497..4008}∪{4010..4521}`, 254 rebase flags at the expected positions,
all extrema, and zero mismatches against the audited 512-arc parent
(v15.1147/Round 604). **Independently re-executed the full script myself**
(after one background timeout, restarted and completed): the regenerated
certificate is **bit-for-bit identical** to the committed one
(`08740b55...`).

## Gravity v15.1174–1177 (quarter-interlayer virtual transitions, K4 gap
selector, Jxy/Casimir distinction, holonomy obstruction)

All hand-verified exactly: the Schur-elimination effective hop
`-(g²/Δ)a_kb_k` and the D=3 counterexample (a_1²=5/4, a_2²=9/4, ratio
3/√5); the K4 SVT squared-frequency gap ratio 3 and its vanishing at p=0
and η_s=3/2; the exact midpoint identity f_D(k+1/2)=[f_D(k)+f_D(k+1)]/2+1/4
and all three Casimir differences `(4D+1)/16`, `L(3L+4)/16` (cross-checked
against D=5: C_EM=6, C_quarter=117/16, C_closed=99/4, all confirmed by
hand); and the holonomy no-go `(i-1)A=0⇒A=0` for a parallel intertwiner
between flat sectors differing by β=1/4. All four scripts re-executed:
exit 0.

## Gravity v15.1178–1179 (Casimir-free tidal alternative, Jxy vertex/focus)

Hand-confirmed the general h²/4 midpoint-completion identity, the
rotation-invariance of trE/trE²/trE³ under conjugation, and the explicit
τ=-(3/2)ΔQsin2θ torque computed directly from the rotated matrix. For
v15.1179, hand-derived the full parabola algebra from scratch — crossing
X_c=(n-k)/2, vertex (n-k)/4, curvature sum 1/k-1/n, the shifted-parabola
equation Y²_Jxy=(2k+1)X+k(k+1), vertex X_v=-k(k+1)/(2k+1), focus
1/[4(2k+1)], the harmonic-mean identity, and all four worked examples
(k=0..3) — every one matched exactly. Scripts re-executed: exit 0.

## Lane A v15.1180 — 256-state R4 outer extension

Hashes verified; independent parse confirmed the exact 256-state union
`{3369..3496}∪{4522..4649}` (disjoint from, and adjoining, v15.1173's
tile), 64 rebase flags including the step-513 restart, and all extrema.
**Independently re-executed the full script**: certificate reproduced
**bit-for-bit identical** (`7e21780d...`).

## Gravity v15.1181–1185 (same-cut quadratic level, observability
hyperboloid, boost-vs-ladder, boost generator obstruction)

All hand-confirmed: the null-plane intersection Y²=K²+2KX-μ and its
focus μ/(2K); the Q=1/4 SU(2) completion identity (j+1/2)²-j(j+1)=1/4;
the light-cone-coordinate null shift ΔT=ΔX=μ/(2K) from Q=UV-Y²; the
boost/Schwinger conserved-quantity mismatch (product nk vs. sum D) with
the worked (2,1)→(4,½) vs. (2,1)→(3,0) example; and the A_i,B_i quarter
factor formulas with the full L=3 worked example (1/4,7/4,3/8),
(3/4,5/4,7/8),(5/4,3/4,7/8),(7/4,1/4,3/8), confirmed exactly by hand from
the general Q_h=h²/4 identity.

**v15.1185 note:** this entry ships two scripts — a flagged-buggy
exploratory one (reversed factor-ratio check) and a validated replacement.
**Independently confirmed both claims**: ran the exploratory script
myself and it genuinely crashes with `AssertionError` at exactly the
line the ledger identifies as having the reversed ratio; ran the
validated script and it passes cleanly with the corrected mirror-boost
check. All other scripts in this sub-batch: exit 0.

## Gravity v15.1186–1191 (boost finite-carrier no-go, K4 oscillator
squeeze, vector/scalar canonical reduction, provenance clarification)

Hand-confirmed the trace-cyclicity no-go (tr(U†AU)=trA forces η=0 since
trA>0) and its infinitesimal form (tr[G,A]=0≠trA); independently
re-derived the general friction-removal substitution Ω²=ω²-(F/2)Ḣ-(F²/4)H²
for arbitrary exponent F=3+r, confirming the vector/scalar case F=3
exactly and the general formula Ω²=ω²-(3+r)(1+r)/(4τ²); derived the full
complex-mode equation α̇=-iΩα+(Ω̇/2Ω)α* by direct differentiation from
scratch.

For v15.1188 (vector canonical reduction), **independently ran the
archived, pre-session, single-commit `vector_sector.py`** (never modified
since v14.935) and confirmed its raw output exactly reproduces the
claimed K_f, V_f, and B⋆ formulas after substituting the background
identity ȧ²=κC/3 and accounting for the second-derivative factor of 2 —
a stronger check than the new script's own internal consistency, since it
verifies against genuinely unmodified prior source.

For v15.1190 (scalar canonical reduction), **ran the committed reproducer
itself**, which copies and executes the three archived
`matter_sector.py`/`eh_scalar.py`/`assemble.py` files into a temp
directory and extracts exact coefficients: reproduced K_PP, M, V_PP, ω²,
and ν_S²=(8η_s-3)(1+k²)/3 exactly. v15.1191 is itself a provenance
clarification flagging that the *original* Gravity run used a
hand-reconstructed copy of the archive rather than a byte-verified one,
and explicitly asks the Audit to run the committed reproducer against
this repository's real checked-in files. **That is exactly what this
Round did**: confirmed via `git log` that `matter_sector.py`,
`eh_scalar.py`, and `assemble.py` each have exactly one commit (v14.935)
and have never been modified since, then ran the reproducer against them
directly with a clean PASS. This resolves v15.1191's flagged open item.

## Gravity v15.1192–1195 (Maxwell null-stress scalar phase match, Ward
closure, Weyl/full-Riemann transfer, initial-value Green response)

Extensive algebra, all hand-confirmed: the SVT projector identities for a
null stream (trivial once Pn=0 is noted), both phase-match quadratics
q²=(8η_s-3)/[16(3-2η_s)] and the vector/tensor comparisons; the Ward
compatibility identity τJ̇_Φ+√3J_B+J_ψ=0; the forcing-term algebra
(re-derived independently and caught my own arithmetic slip on first
pass, corrected on redo) confirming F_J=2k²J_Φ/[3(1+k²)] and the final
forcing -3√3J0τ^(-4-iw)/k²; the particular-solution and denominator
D=1+2iw at phase match, with Im(D)=2w>0 proving D≠0 for any k>0; the
R_S=W_S-Ricci_S/2 consistency identity; and the initial-value Green's
function construction via standard variation of parameters, confirmed
to reduce to exactly the ledger's P_IV(τ) formula. All five scripts
re-executed: exit 0, every printed numeric coefficient (including the
complex transfer coefficients C_W, C_R at η_s=3/4, k²=1/2, and the
initial-value R_S at τ=1,2) matching the ledgers exactly.

## Gravity v15.1196 (compact-Maxwell finite-arm scalar STF, isotropic
leakage)

Hand-confirmed the binomial-expansion formula for G(r) and its exact
value G(1)=1024/3003; confirmed the general differential-proxy formula
D=(2G+1)S0/3+(Ābar-Acenter) and its reduction under the (flagged,
unproved) ansatz Abar=Acenter·G. Both the "exploratory" (narrower
ansatz) and "validated" (general) scripts run cleanly — this is a
disclosed scope limitation, not a crashing defect. Exit 0 for both.

## Gravity v15.1197→v15.1198 (full-Riemann arm-trace basis error and its
correction)

v15.1197 **self-identifies** a basis-conflation error mid-derivation
(using v15.787's `A` from the `Aδ+Rnn` decomposition where the `AδI+RQ`
decomposition's `A_iso=A+R/3` was needed) and explicitly warns not to
trust its printed number. Hand-confirmed the conversion A_iso=A+R/3, the
corrected two-arm formula ΔE=[(2F+1)/3]R+(F-1)A_iso, and that the
magnitude of v15.1197's error is exactly R(F-1)/3 as claimed. Ran
v15.1197's script: it reproduces exactly the flagged-wrong number
(5.687...-0.8042...i), consistent with the self-disclosure.

v15.1198 corrects this and derives a striking additional claim: that the
isotropic trace A_iso collapses to exactly `-√3·J0τ^(-4-iw)`,
**independent of η_s and k**, for this particular traveling-harmonic
solution. **Independently verified this from scratch** — built A_raw,
R, and A_iso directly from the already-confirmed Φ_N/Ψ_N/P_part formulas
in a fresh SymPy session (not reusing or trusting v15.1198's own script),
and confirmed the ratio simplifies to exactly -√3 (both symbolically,
`simplify(ratio-(-√3))==0`, and numerically to 1e-15). The corrected
two-arm numeric values (R_STF, A_iso, STF part, leakage, full proxy) at
η_s=3/4, k²=1/2 all hand/formula-confirmed.

**Finding (this audit): the committed v15.1198 reproducer script does
not actually run clean.** `k4_null_maxwell_full_riemann_arm_proxy_v15_1198_corrected.py`
crashes with `AssertionError` at its final line,
`assert s.limit(geom,kr,0)==R`, contradicting the ledger's claim that
"Equivalent complete local SymPy tests PASS." Diagnosis: this is a
shallow bare-`==` structural-equality bug, not a mathematical error —
independently confirmed `simplify(s.limit(geom,kr,0) - R) == 0` (and a
numeric spot check) both show the two sides are exactly equal; SymPy's
`limit()` simply returns an unsimplified form that isn't syntactically
identical to `R`. This is the same shallow-comparison pattern disclosed
earlier this session at v15.1093. All five assertions *before* the
failing one — including the central `A_iso=-√3` identity, the two
independently-expressed arm formulas' equivalence, and all six numeric
spot checks — do pass. The underlying mathematics in v15.1198 is correct;
the committed script's self-test is incomplete.

## Lane A v15.1199 — 128-state R4 outer extension

Hashes verified; independent parse confirmed the exact 128-state union
`{3305..3368}∪{4650..4713}` (adjoining v15.1180 outward), 32 rebase
flags, and all extrema. **Independently re-executed the full script**
(after one timeout from CPU contention with the concurrent v15.1173
re-run; restarted alone and completed).

**Finding (this audit): the committed certificate is not exactly what
the committed script produces.** The regenerated certificate differed
from the committed one by exactly one JSON field: the committed file
carries an extra top-level key `"ledger_version": "v15.1199"` that does
not appear in the freshly regenerated file. Confirmed by `grep` that the
string `ledger_version` appears nowhere in
`lane_a_v15_1199_suzuki_r4_outer_extension.py`, nor in the structurally
identical v15.1180/v15.1173 scripts, and confirmed the earlier two
certificates (already independently bit-matched in Rounds 604/608 and
above) carry no such field either. This means the published v15.1199
certificate was lightly post-processed (a version tag added) after the
script's run, so it is not literally reproducible by re-running the
committed script alone, unlike v15.1173 and v15.1180's certificates.
**This is a provenance/bookkeeping discrepancy only, not a computational
error**: every mathematical field in the certificate — all extrema, the
full arc union, every rebase flag — matches the independent re-execution
exactly. The working tree was restored to the committed state
(`git checkout --`) after this comparison; no file was altered.

## Verdict

Every mathematical and numerical claim across all 29 entries in this
batch is confirmed correct by independent hand derivation and/or
independent re-execution, including two numerical certificates
reproduced bit-for-bit (v15.1173, v15.1180) and a third (v15.1199) whose
mathematics is fully confirmed despite a minor certificate
post-processing discrepancy. Two defects were found by this audit itself
and are reported above: (1) v15.1198's committed reproducer script fails
its own final assertion due to a shallow equality-comparison bug (the
underlying math is correct); (2) v15.1199's committed certificate carries
one JSON field not produced by its committed script. Two further defects
were already self-identified and disclosed by Gravity before this audit
ran (v15.1185's exploratory script, v15.1197's basis-conflation error)
and are confirmed accurate as described. No silent patch was made to any
file; all findings are reported here only.

`git fetch origin master` immediately before this commit returns
`30c84f0`, unchanged since the pushes verified above. Gravity/Sandbox/
Lane A should continue; Lane A should note the v15.1199 certificate
provenance finding above for future producer runs.
