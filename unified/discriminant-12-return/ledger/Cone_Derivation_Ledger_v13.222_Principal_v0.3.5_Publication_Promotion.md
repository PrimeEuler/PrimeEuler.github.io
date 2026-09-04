# Cone Derivation Ledger v13.222 — Principal v0.3.5 Publication Promotion

Date: 2026-09-04
Project root: `unified/discriminant-12-return/`

## Promotion decision

Promote `papers/Discriminant_12_Return_v0.3.5.tex/.pdf` to the active audited
principal-paper publication baseline.

This promotion follows:

- v13.220: ground-up theorem audit of v0.3.4, with no theorem-breaking defect;
- v13.221: source-level theorem hardening into v0.3.5.

## Source / build / workflow provenance

Source:

`papers/Discriminant_12_Return_v0.3.5.tex`

creation commit:

`fe5b1d35bee463ec198612179fff40da89e94db1`

Build script:

`papers/build_discriminant12_v0.3.5.sh`

creation commit:

`9e70013e038b3d00d6f26f840dfd0bc3364fc111`

Workflow synchronization:

`.github/workflows/build-discriminant12-paper.yml`

commit:

`af22422552e16ea3bb88c1fae4f916944cddd398`

Source-level reconciliation ledger:

`ledger/Cone_Derivation_Ledger_v13.221_Principal_v0.3.5_Theorem_Hardening.md`

commit:

`e7cff6551642bccf67f6e3179699932f28a4a165`

## CI confirmation

GitHub Actions run:

`33922073158`

completed successfully.  All principal build stages succeeded, including
figure generation, TeX compilation, and publication-output commit.

The GitHub Actions bot committed the compiled v0.3.5 paper and generated
publication outputs in:

`c49892eeb4316361b6d5a58d918029397af0bf2c`

commit message:

`Build Discriminant 12 Return v0.3.5 outputs`

Therefore the publication artifact

`papers/Discriminant_12_Return_v0.3.5.pdf`

is now CI-built and repository-committed.

## Theorem hardening now in the publication baseline

The active principal theorem now explicitly contains:

1. the signed three-dimensional Pell/Lorentz action

   `X'=2X+sqrt(3)T`, `Y'=Y`, `T'=sqrt(3)X+2T`;

2. the direct local residue-field derivation

   `O_{K_12}/P_2 ~= F_2[omega]/(omega^2+omega+1) ~= F_4`;

3. the exact transported parity identity

   `bar(q_12)=Tr_{F_4/F_2}`,

   hence Boolean XOR parity in the Boolean/Pell basis;

4. an explicit `n=11` narrow-class / Artin proposition proving

   `N(1+2sqrt(3))=-11`,
   `[p_11]=[p_2]`, and
   `Art_{K_12/F}(p_11)=T_11`;

5. the continuing guardrail that `T_11 <-> J` is a representation
   correspondence, not literal equality across categories.

The prior finite-action distinction is retained unchanged:

- reduced multiplication by `zeta_12` is literal multiplication by `omega`;
- direct residue multiplication by `lambda=2+sqrt(3)` is the identity;
- the mod-2 Pell coordinate action becomes Frobenius only after the stated
  additive `F_2`-linear transport to `F_4`.

## README synchronization

The project README was updated in commit:

`89be802b31939195ad6e01809eeacbb906651e16`

It now records:

- v0.3.5 as the active principal publication baseline;
- v0.3.4 as the preceding audited historical snapshot;
- the v0.3.5 build mapping;
- the successful CI run and bot publication commit;
- the theorem-hardening content promoted from v13.220/v13.221.

## Final status

**`Discriminant_12_Return_v0.3.5.tex/.pdf` is ACTIVE / AUDITED PUBLICATION BASELINE.**

The active audited chain is now:

`Paper A v2.4`
`-> Area v1.1`
`-> Paper B v2.1`
`-> Paper C v1.1`
`-> Casimir / Null-Diamond v2.1`
`-> Discriminant-12 Return v0.3.5`.

The principal theorem is no longer awaiting repair or packaging work.  Further
changes should be treated as new mathematics, clarification, or exposition,
not as completion of the v0.3.4 audit cycle.
