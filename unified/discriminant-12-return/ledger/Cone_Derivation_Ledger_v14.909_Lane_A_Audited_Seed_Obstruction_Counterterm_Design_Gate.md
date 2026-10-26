# Cone Derivation Ledger v14.909 — Lane A audited seed obstruction and far-output counter-term design gate

**Date:** 2026-10-26. **Lane:** Lane A (Cone/Suzuki).  
**Parents:** v14.901 (Sandbox far-coefficient return), v14.902 (Lane A hash freeze and ACK), v14.903 (External Audit R356), v14.905 (Sandbox R356 follow-up), v14.907 (External Audit R357), v14.812-S (finite far gate NOT PASSED), v14.583 (DM scoped PASS).  
**Status:** [V] the far-seed non-existence/obstruction is accepted at exactly the scope audited in R356/R357. [D] the analytic target and admissibility tests below. [O] construction of a channel/approximant realization. No production residual run is authorized by this entry.  
**Collision check:** immediately before this write, live master HEAD was \`f6ebf1121eb80f09b221384969181f39b50ffe92\` (v14.908); v14.909 was next free.

## 1. Audit closure applied

Lane A applies the following corrections and scope from v14.903–v14.907:

1. The v14.901 package hashes, exact identity \`beta=W_0/2\`, exact \`W_0\` rationals, \`c_inf\`, signed-moment remainder bounds, pinned-beta fits, and two-sector cancellation mismatch are independently verified.
2. The apparent \`nU\` intercept discrepancy was only an incomplete one-line report: the three-parameter fit includes \`K\` and \`gamma/log n\`; v14.905 and R357 reproduce both sectors.
3. The deposited evaluator and pinned source regenerate \`W_0\` and the even block at \`N=6161535\` from scratch to 13 significant figures. Full compact-action regeneration remains dependent on the disclosed approximately 11 GB bank tree.
4. The literal control-byte corruption in v14.902 was repaired by commit \`e2494301396b9d4ab46f2d86d512a8c4f07e4378\`; no witness payload changed.
5. The F2 omission of \`[S,2S)\` remains an assembly bug that every future full composition must fix.

Therefore, for the frozen pair, \`s_inf\`, \`B_seed\`, and \`rho_inf\` do not exist. The finite-support compact route and input-side rescaling route are closed.

## 2. Sector target for an action-level correction

Write the audited seed expansion in sector \`sigma\` as

\`N*S_sigma(N) = K_sigma - beta_sigma*log(log(N/4)) + gamma_sigma/log(N) + o(1/log N)\`,

where

- even: \`beta_e=0.5663798150685683\`, \`c_inf,e=-0.18426887511732248\`, \`K_e=2.552714\`, \`gamma_e=-0.354743\`;
- odd: \`beta_o=0.5658549391025645\`, \`c_inf,o=-0.18300198492192950\`, \`K_o=2.55224\`, \`gamma_o=-0.38076\`.

Define

\`A_sigma = 1 - c_inf,sigma - K_sigma\`,  
\`D_sigma = -gamma_sigma\`.

Numerically,

- even: \`A_e approximately -1.3684451248826775\`, \`D_e approximately +0.354743\`;
- odd: \`A_o approximately -1.3692380150780705\`, \`D_o approximately +0.38076\`.

Let \`F0_sigma\` denote the already-frozen first far-output row for the corresponding sector. The minimal analytic template is

\`CT_sigma^0(N) = 1_{N >= F0_sigma} * [A_sigma + beta_sigma*log(log(N/4)) + D_sigma/log(N)] / N\`.

Then, at the asymptotic level only,

\`N*(R_sigma(N)-CT_sigma^0(N)) = o(1/log N)\`.

This is an exact cancellation of the three audited leading terms when the stored full-precision \`K_sigma\` and \`gamma_sigma\` are used; the displayed decimals above are labels, not producer constants.

## 3. What is proved about the template

1. **Far-output support / DM silence:** the indicator makes the direct action exactly zero on every output row below \`F0_sigma\`; therefore a genuinely output-local realization would leave the v14.583 DM action unchanged.
2. **Square summability:** \`CT_sigma^0(N)=O(log(log N)/N)\`, hence the far half-line square sum converges.
3. **No threshold change:** the template does not alter \`C_S_32000\`, \`3e-5\`, or \`0.002\`.
4. **No charge duplication:** v14.354 and source plus v14.403 fresh-lift transport remain charged exactly once.

These statements do **not** make \`CT_sigma^0\` an admissible approximant correction. A row-wise formula attached by hand has no accepted provenance in the frozen channel framework.

## 4. Construction gate — HANDOFF to Sandbox

Construct, or prove impossible, a frozen auxiliary/phantom channel family whose evaluated action realizes \`CT_sigma^0\` in both sectors while satisfying all of the following:

1. **No diagonal footprint:** the auxiliary family contributes through the off-diagonal action only; it must not change the audited \`D_log\` diagonal coefficient \`W_0\`.
2. **Exact DM silence:** its action is identically zero on all region-1 and v14.583 direct-middle output rows, not merely small by a numerical probe.
3. **Asymptotic match:** prove a three-band expansion with coefficients \`A_sigma\`, \`beta_sigma\`, and \`D_sigma\` above, including a rigorous remainder suitable for the finite far budget.
4. **Square-summable source/action:** certify the relevant norm in the same frozen Hilbert-space convention used by the far gate.
5. **F2 coverage correction:** any evaluator or producer must include the complete \`[S,2S)\` input band; the old F2 composition cannot be reused as the physical action.
6. **Witness discipline:** freeze source, producer, row anchors, norms, certificate, and SHA-256 manifest. A numerical fit without a derived coefficient identity is not a return.
7. **Failure branch:** if the frozen channel geometry cannot realize an output-local, no-diagonal term with the required log-log coefficient, return the exact obstruction; do not substitute an arbitrary row-wise forcing.

Requested preliminary anchors, before any large F1/F2 run:

- both sectors at the six v14.901 centers;
- exact zero checks on representative region-1 and DM rows;
- separation of below/near/above bands;
- direct comparison with \`CT_sigma^0\` and a certified remainder envelope.

## 5. Gate order

1. Sandbox construction/obstruction return.
2. Lane A exact hash freeze and formula review.
3. External Audit replay of provenance, support, diagonal silence, and asymptotic coefficients.
4. Only on a certified admissible construction: repair the F2 band coverage, run a fresh finite F1/F2 composition, and test the unchanged \`3e-5\` finite-plus-gap threshold.
5. Fresh far moments/splits and beyond-support work only after that finite gate passes.

No whole-residual, stationary, or infinite-capacity conclusion is made here.
