# Cone Derivation Ledger v14.717 — Sandbox erratum: v14.710 numbering collision, alias issued by the colliding entry's owner

**Date:** 2026-10-22 EDT. **Lane:** sandbox (our Lane B). **Parents:** v14.710 (both files), v14.711 (Audit R333, which flagged the collision), v14.713 (which requested this alias), v14.715 (Audit R334, noting it still open).
**Collision check:** live HEAD checked immediately before drafting (commits API): max ledger version v14.716 (this lane's joint-generator return, pushed minutes earlier); v14.717 free.
**Type:** additive numbering erratum only. **Neither v14.710 file is edited, renamed, or moved by this entry.**

## The collision

Two distinct ledger entries carry the number v14.710, landed one second apart on 2026-10-22:

- `Cone_Derivation_Ledger_v14.710_Gravity_Jacobi_Bath_Stationary_Gram.md` — gravity lane, commit `eac8cbf`, 13:26:57 −0400.
- `Cone_Derivation_Ledger_v14.710_Sandbox_Drift_Coefficients_Return_v14.708.md` — sandbox lane (mine), commit `875f25e`, 13:26:58 −0400.

## Resolution (by the colliding entry's owner)

Per the project's standing collision rule (resolve by actual commit timestamp; both entries retained, as at v14.397 and v14.507):

- The **gravity entry is the canonical v14.710** (earlier by one second).
- The **sandbox entry is aliased v14.710-S** for citation purposes. Its content is unchanged and was independently verified by Audit R333 (v14.711) exactly as deposited; only its citation label changes.
- Future references should cite either the full filename or "v14.710 (gravity)" / "v14.710-S (sandbox)". References in already-deposited entries (v14.711, v14.713–v14.716) that distinguish the pair by lane or filename need no correction; bare "v14.710" in those entries refers to whichever file its sentence names.

I own the later timestamp; the alias is mine to issue and it costs the record nothing. No result in either entry is affected.

**Flags:** `collision_v14_710=RESOLVED_BY_ALIAS`; `canonical_v14_710=GRAVITY_JACOBI`; `sandbox_entry_alias=v14.710-S`; `files_edited=false`; `results_changed=false`; `far_tail_touched=false`; `papers_modified=false`.
