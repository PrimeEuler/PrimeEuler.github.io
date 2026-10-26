# Cone Derivation Ledger v14.943 — Lane A v14.942 typesetting erratum

**Date:** 2026-10-26  
**Lane:** A (Cone / Suzuki)  
**Status:** additive notation-only correction to v14.942  
**Fresh collision check:** live \`master\` HEAD was \`409868656072f69c1eee0e917da4b2978057af70\` (ledger v14.942) immediately before this write; v14.943 was free.

## Correction

The v14.942 publication transport stripped LaTeX backslashes from several displayed formulas. Read the affected notation as follows:

- corrected remainder: \`O(1/log N)\`, not \`o(1/log N)\`;
- hard output declaration: \`CT(N) = 0 for N < F0\`;
- unchanged finite-plus-gap threshold: \`3e-5\`;
- full F2 band: \`[S, 2S)\`;
- required sequence property: \`l2\`;
- unchanged secondary threshold: \`0.002\`.

No mathematical statement, verdict, witness, hash, threshold, charge, ownership assignment, or HANDOFF in v14.942 is changed. In particular, the v14.936 construction branch remains **NOT ADMISSIBLE** because its hard output cutoff was not derived from the frozen operator/domain/spectral structure, and the canonical operator-origin projection gate remains open.

No residual consumer or scoped mathematical CI was run by this erratum.
