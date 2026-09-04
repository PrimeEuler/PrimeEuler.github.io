# Cone Derivation Ledger v13.212 — Casimir / Null-Diamond Foundation Promotion

Date: 2026-09-04

Status: **[Audit] structural promotion complete; corrected v2.1 is the sole live authoritative source**

## 1. Purpose

This checkpoint completes the promotion approved in v13.209 for the paper formerly stored as

`papers/Casimir_Null_Diamond_Standalone_v2_Audited.tex`.

The goal was explicitly to avoid a live duplicate. The corrected next version is therefore established directly in `foundations/`, and the former v2 TeX/PDF are removed from `papers/` after the new source exists. Git history preserves the v2 audited snapshot.

## 2. Source-preservation method

The exact historical v2 TeX was recovered from Git blob

`904031e4fa5f5ebfab8bf71f516e93722aea945a`

rather than re-authored from memory. The new source was created from that exact body with only the four corrections required by the v13.209 mathematical audit.

New authoritative source:

`foundations/Casimir_Null_Diamond_Standalone_v2.1.tex`

The authoritative filename intentionally drops the `_Audited` suffix. Audit status belongs in the ledger and inventory, not in the publication filename.

## 3. [Audit] Four corrections incorporated in v2.1

### 3.1 Farey projective-orientation qualification

The v2 sentence saying primitive integer spinors with `|Delta|=1` have Farey-adjacent projective ratios was correct only after the standard representative convention is made explicit.

v2.1 now states that the projective ratios are written in standard reduced representatives with a common denominator orientation before invoking Farey adjacency.

The determinant--Lorentz theorem itself is unchanged:

\[
\langle Q_1,Q_2\rangle_\eta=\frac12(ad-bc)^2.
\]

### 3.2 Paper-C source status corrected

The phrase `existing audited quantum-realization manuscript` was removed.

v2.1 now states that the current working quantum-realization manuscript remains under audit and is not used by the null-diamond paper as an independently audited theorem source.

This prevents the foundation paper from inheriting unresolved Paper-B/Paper-C power-map claims.

### 3.3 Positive-discrete-series convention corrected

For the two-mode realization, fixing

\[
d=n_1-n_2
\]

gives the standard positive-discrete-series Bargmann index

\[
\boxed{k=\frac{|d|+1}{2}}.
\]

Only after choosing the oriented sector `d>=0` does this reduce to

\[
\boxed{k=\frac{d+1}{2}=X}.
\]

This correction is now explicit in the v2.1 source note.

### 3.4 State point versus transition-cell center clarified

The Paper-C dictionary

\[
x=n_1+1,\qquad y=n_2
\]

is now explicitly described as selecting one transition vertex in the four-corner transition-cell construction, not the cell center.

This preserves the exact center formulas

\[
X_c=\frac{\delta(p-q)}2,
\qquad
T_c=\frac{\delta(p+q+1)}2
\]

and the four cardinal half-step transitions without conflating the state dictionary with the midpoint geometry.

## 4. [D] Core theorem retained unchanged

The v13.209 audit passed the mathematical core, and no theorem-level formula was weakened during promotion.

For primitive unimodular spinors,

\[
M_F^2=\frac14,
\]

or at spacing `delta`,

\[
\boxed{M_F^2=\frac{\delta^2}{4}}.
\]

The compact and noncompact Casimir completions remain

\[
R_+^2=C_++M_F^2,
\qquad
R_-^2=C_-+M_F^2,
\]

and the unified ladder formula remains

\[
\boxed{
A_\pm^2
=
\sigma\bigl(C+M_F^2-Z_\pm^2\bigr),
\qquad
Z_\pm=q\pm\frac\delta2.
}
\]

The cyclotomic normalization remains

\[
\mathcal Z=\frac{H+iI}{2},
\qquad
\mathcal Z\overline{\mathcal Z}=I,
\]

and the ramified mod-2 return remains factor exchange, not Boolean translation.

No identification is introduced between the Lorentz norm, Casimir quadratic form, and cyclotomic relative norm.

## 5. True relocation, not duplication

After the corrected v2.1 source was established, the following live files were removed from `papers/`:

- `Casimir_Null_Diamond_Standalone_v2_Audited.tex`
- `Casimir_Null_Diamond_Standalone_v2_Audited.pdf`

This is deliberate. There is now one live authoritative null-diamond source:

`foundations/Casimir_Null_Diamond_Standalone_v2.1.tex`.

The historical v2 source and PDF remain recoverable through Git history. No mathematical provenance was discarded.

## 6. Build and CI reconciliation

A new foundation-local build entry point was added:

`foundations/build_casimir_null_diamond.sh`

It runs two halted-on-error `pdflatex` passes on

`Casimir_Null_Diamond_Standalone_v2.1.tex`.

A matching GitHub Actions workflow was added in the same reconciliation:

`.github/workflows/build-casimir-null-diamond.yml`.

The workflow watches the v2.1 TeX, the build script, and itself; installs the same baseline TeX packages used by the other non-Matplotlib foundation build; runs the build script; and commits

`foundations/Casimir_Null_Diamond_Standalone_v2.1.pdf`

when the output changes.

This satisfies the project CI invariant: authoritative source/build-target changes and publication workflow mappings are reconciled together.

At the moment of this ledger entry, the source/build/workflow wiring is established. The new v2.1 PDF is a generated artifact and should be considered present/certified only after the workflow has successfully produced and committed it. Connector-side binary limitations are not treated as publication build failures.

## 7. Inventory and README reconciliation

`foundations/FOUNDATIONS_INVENTORY.md` is updated so the null-diamond paper is no longer listed as a candidate in `papers/`. It is now an **ACTIVE / AUDITED BASELINE** in `foundations/`.

The inventory also records:

- the four v2.1 audit corrections;
- the removal of the old live v2 TeX/PDF;
- the new build script;
- the corrected foundation dependency chain.

The project `README.md` is updated so future sessions see immediately that:

- `Casimir_Null_Diamond_Standalone_v2.1.tex` is the sole live authoritative null-diamond source;
- `build_casimir_null_diamond.sh` is its build entry point;
- `build-casimir-null-diamond.yml` is its CI mapping;
- the old v2 live copy in `papers/` has been removed;
- the semiclassical/LQG note remains in `research-notes/`, outside the foundation theorem chain.

## 8. Corrected foundation dependency status

The working foundation chain is now:

1. Paper A v2.4 — audited geometric/conic foundation.
2. Area note v1.1 — exact one-sided measure companion.
3. Paper B v2 — current Lorentz/eigen-coordinate extension, still under theorem audit.
4. Paper C — downstream quantum realization requiring reconciliation after Paper B.
5. Casimir / Null-Diamond v2.1 — active audited bridge whose core theorem is independent of unresolved Paper-C power-map claims.

The ordering above is an audit/dependency workflow, not a statement that the null-diamond theorem logically depends on Paper C. Its core determinant--Lorentz, Casimir-completion, cyclotomic, and Boolean-return results have already been independently audited.

The semiclassical/LQG note is excluded from the chain and retained only as future research material.

## 9. Next main-path task

With the directory-level foundations audit, semiclassical/LQG relocation, and null-diamond foundation promotion reconciled, the next substantive theorem task is the ground-up audit of

`foundations/PaperB_EigenCoordinates_v2.tex`.

The known audit targets remain projective normalization, the `Gm=0` derivation, parabolic power-map wording, elliptic/hyperbolic eigen-coordinates, normalized Lorentz generators, orbit components/transitivity, and separation of Euclidean from Lorentzian metric statements.
