# Cone Derivation Ledger — v14.442

## Lane A: recovered residual return, scoped finite-plus-gap PASS, External Audit HANDOFF

**Parent inspected:** `defc1f389be4fc998dca0f8c1431f7bab994d45e` (v14.441).  
**Residual workflow:** run `38737467408`, head `6a548517124ff52da5548c8fff81135454b7d1fb`; both matrix jobs completed successfully.  
**Threshold:** unchanged `3e-5`. **Original `C_S_32000` and every inherited acceptance threshold remain unchanged.**

## Frozen return

Exact certificates and a hash manifest are deposited additively at
`payloads/gap_extended_residual_return_v14_442/`.

| sector | artifact / ZIP SHA-256 | certificate SHA-256 | residual buffer SHA-256 |
|---|---|---|---|
| even-v | `11974737629` / `678802eb98f56b9473e97d94de2a5bf80a6e4470e16380e5582d745f4f9d3c23` | `17da7371cf3c73b417397332b8e40aea1143f8b6785b5383ce8183b4c5d5390b` | `31bec0540ff2682ff0a4cbec39a326682a207ae6b7c3b90b42833b5d07eb4684` |
| odd-v | `11973393563` / `93690f44660b0351892460075556ae02319a5907b2a42e4c5c363c8af16a41e7` | `29162aa8ec5d443b25e309c757bb467ea9fd3f2ab234d70ce12df66afbb82a07` | `bd5b71cf8e45df07297067328516c95bbe4ef6376b808aea14fc075a3ee8b6a3` |

Each residual buffer is 27,371,490 bytes, 912,383 rows, width 30 at 256-bit scale. The ZIP digests match GitHub artifact metadata; the extracted certificate and buffer digests match the frozen manifest.

## Evaluated scoped gate

| sector | finite-plus-gap Schur residual interval | physical residual interval | finite-plus-gap upper < 3e-5 |
|---|---:|---:|---|
| even-v | [`2.0119108512272408e-5`, `2.0120943872605e-5`] | [`2.011994544023358e-5`, `2.012010694464383e-5`] | **PASS** |
| odd-v | [`2.0081249564761065e-5`, `2.008143141954647e-5`] | [`2.0081259817936012e-5`, `2.0081421166371523e-5`] | **PASS** |

The exact rational bounds are preserved in the deposited certificates. The consumer records and this deposit preserves:

- the original v14.294/v14.327/v14.393 seed provenance;
- v14.354 self terms charged exactly once to the inherited finite-seed error;
- source plus v14.403 fresh-lift transport added exactly once;
- compact certificate/buffer hashes exactly equal to the v14.437 return;
- gap-seed self rows already excluded.

## Scope fence

This is a certified pass of the 912,383-row finite-plus-gap gate only. Both certificates explicitly state:

- `beyond_gap_residual_evaluated = false`;
- `stationary_acceptance_met = false`;
- `whole_residual_acceptance_certified = false`;
- `infinite_capacity_tail_closed = false`.

Therefore this entry does **not** claim whole-residual, stationary, or infinite-capacity closure. The pass unlocks the already-authorized next gate: fresh far moments/splits and evaluated beyond-support residual certification.

## HANDOFF — External Audit

Please independently verify run `38737467408`, the two artifact ZIP digests, the frozen certificate/buffer hashes, the exact rational interval comparisons against `3e-5`, and the once-only accounting flags. Please return any correction before Lane A treats the beyond-support result as accepted. Lane A may prepare and execute the unlocked beyond-support gate additively, but will preserve this scope fence until an evaluated certificate exists.
