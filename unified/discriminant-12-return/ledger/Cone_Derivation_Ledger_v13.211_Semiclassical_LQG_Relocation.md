# Cone Derivation Ledger v13.211 — Semiclassical/LQG Relocation and Foundation Reconciliation

Date: 2026-09-04

Status: **[Audit] source-architecture reconciliation completed**

## 1. Reason for this checkpoint

During the foundations-directory review, `Note_SemiclassicalArea.tex` had been classified in v13.208 as an exploratory downstream item still living in `foundations/`. A full ledger search showed that this classification did not preserve the stronger architectural decision already made by the area branch.

The earlier ledger record is explicit:

- v13.196: the old semiclassical note supplied the induced cone-area calculation, but **the LQG comparison is not needed for the geometry**; the geometry was to be rewritten as a dedicated foundation source.
- v13.200: the area branch was frozen with `Note_AreaDistortion_AMGM_Cone_v1.1.tex` as the geometry-only publication source; the LQG comparison was retained only as separate research material.
- v13.201: Paper A's citation was redirected from the semiclassical/LQG note to the geometry-only area companion, explicitly recording that **no LQG interpretation is required by Paper A**.

Therefore v13.208's placement of the semiclassical note inside the active foundation dependency list was too weak and is superseded by this reconciliation.

## 2. [S] Geometric content extracted from the old note

The semiclassical note had already established the exact induced cone-surface element

\[
dA_{\rm cone}=\frac{T}{\sqrt2\,Y}\,dx\,dy.
\]

That valid geometry was not discarded. It was independently reorganized, extended, and publication-separated into the active geometry-only companion

`foundations/Note_AreaDistortion_AMGM_Cone_v1.1.tex`.

The active companion includes the exact flat Jacobian

\[
dX\,dY=\frac{T}{2Y}\,dx\,dy,
\]

the induced cone area

\[
dA_{\rm cone}=\sqrt2\,dX\,dY,
\]

and the inverse transported factor-area measure

\[
dx\,dy=2\cos\theta\,dX\,dY
       =2\operatorname{sech}s\,dX\,dY.
\]

Thus removing the semiclassical note from `foundations/` removes no required geometric theorem from the foundation chain.

## 3. [Audit] LQG material deliberately separated

The old note compares cone-band scaling with the loop-quantum-gravity area spectrum and records the formal normalization

\[
\gamma_{\rm eff}=\frac{1}{4\sqrt2}.
\]

The note itself already guards this as a normalization/consistency comparison rather than a derivation of the Barbero--Immirzi parameter or a demonstrated physical relation between the multiplication-table cone and LQG.

That distinction is preserved. The LQG branch is potentially interesting for future research, but it is not presently part of the audited foundation theorem chain.

## 4. [S] Repository relocation performed

The source was moved unchanged from

`foundations/Note_SemiclassicalArea.tex`

to

`research-notes/Note_SemiclassicalArea.tex`.

The new research-note source was created first, then the old foundation-local source was deleted, avoiding a live duplicate.

The old compiled

`foundations/Note_SemiclassicalArea.pdf`

was also removed from the live foundation directory. The GitHub connector cannot create/move binary PDFs directly, so no duplicate research-notes PDF was manufactured. The historical compiled PDF remains recoverable from Git history, and a research-note PDF can be regenerated later if the LQG branch is reopened.

No mathematical content was intentionally edited during the source relocation.

## 5. [Audit] Foundations inventory corrected

`foundations/FOUNDATIONS_INVENTORY.md` was updated to record:

1. `Note_AreaDistortion_AMGM_Cone_v1.1.tex` is the active geometry-only area/Jacobian companion.
2. `Note_SemiclassicalArea.tex` is outside `foundations/` and lives in `research-notes/` for possible future LQG investigation.
3. The semiclassical/LQG note is excluded from the active foundation dependency chain.
4. v13.196, v13.200, and v13.201 are the provenance for this separation.
5. The former foundation-local semiclassical PDF is historical Git provenance rather than a live foundation artifact.

## 6. Corrected active foundation dependency chain

The working chain is now

1. **Paper A v2.4** — audited geometric/conic foundation.
2. **Area Distortion v1.1** — exact one-sided area/Jacobian companion to Paper A.
3. **Paper B v2** — Lorentz/eigen-coordinate extension, still under theorem audit.
4. **Paper C** — quantum realization downstream of Paper B, requiring reconciliation.
5. **Casimir / Null-Diamond bridge** — core mathematics audited; corrected v2.1 promotion to `foundations/` remains the next structural operation.

`Note_SemiclassicalArea` is **not item 6** and is not part of this dependency chain.

## 7. Relation to the v13.208 directory audit

v13.208 remains useful as the original structural inventory checkpoint, but its classification

> `Note_SemiclassicalArea.tex` — exploratory downstream physics material inside foundations

and its inclusion of that note in the foundation dependency order are superseded by v13.211.

The corrected interpretation is:

> **historical/exploratory LQG research branch whose required geometric content was rewritten into the Area Distortion companion; source retained in `research-notes/` for possible future investigation.**

## 8. Commits in this reconciliation

- `1f82325aafaf4debc53d0400f17140c0722abf80` — create the unchanged semiclassical source in `research-notes/`.
- `d80011e8e4bbf313706f1964213a1cb8f18f8f1e` — remove the old foundation-local TeX source.
- `392e584639e043f91aa3deed7cfffe0e4fb2826b` — remove the old foundation-local compiled PDF.
- `17edda554e118b785a31da2bae8250143b50fc7f` — reconcile `FOUNDATIONS_INVENTORY.md` and the active dependency chain.

This ledger entry records the complete rationale so future chats do not reintroduce the LQG note into the foundation chain merely because older checkpoints mention it there.

## 9. Next structural task

Proceed with the already approved Casimir/null-diamond promotion as an atomic operation:

- produce corrected `foundations/Casimir_Null_Diamond_Standalone_v2.1.tex`;
- add its foundation-local build script;
- remove the old live v2 TeX/PDF from `papers/` only after v2.1 is established;
- update inventory/README/workflow state as appropriate;
- record the relocation and corrections explicitly in the next ledger checkpoint.
