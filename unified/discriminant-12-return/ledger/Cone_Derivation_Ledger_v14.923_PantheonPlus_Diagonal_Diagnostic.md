# Cone Derivation Ledger v14.923 — Pantheon+ diagonal-only direct observational diagnostic
Date 2026-10-26. Parents v14.921–922. Note research-notes/K4_PantheonPlus_Diagonal_Diagnostic.md, commit a9e9c0e7409bbd0773dbeb2451a004f5d8f26078. Live prewrite HEAD a9e9c0e7409bbd0773dbeb2451a004f5d8f26078. Owner per-gate ledger protocol. No Suzuki/far-tail edits, quarter-Suzuki integration remains parked.

[N] Downloaded official Pantheon+SH0ES.dat through public repository connector; selected 1580 noncalibrator m_b_corr rows with zHD>0.01 and valid diagonal error. Compared k4 coasting d=(1+zHEL)ln(1+zHD) to flat ΛCDM reference Ωm=.315, d=(1+zHEL)∫_0^zHD du/[Ωm(1+u)^3+1-Ωm]^(1/2), using *independently marginalized additive magnitude offsets* and inverse-squared individual reported diagonal errors. χ²_k4=786.1217145, χ²_LCDM=697.6175999, Δχ²=+88.5041146, offsets 23.88812562 and 23.80256474. Reproduction and official table link in research note. Minor reproducer typography: pandas read_csv separator should be Python raw string r'\s+' (one backslash in source), not r'\\s+'.

[O, major limitation] This is **not the released full-covariance Pantheon+ likelihood**. Its 1701×1701 STAT+SYS covariance has NOT been retrieved/inverted, so no valid exclusion significance or sigma value can be stated. Statistical dependence/systematics may change the comparison. A direct data *diagnostic*, not a completed empirical rejection of the Cone metric. No physical gravity action or G derived.

Flags: official_supernova_table=READ; diagonal_only_comparison=NUMERIC; full_covariance_Pantheon_likelihood=OPEN; delta_chi2_diag_only=88.5041; model_preferred_in_diag_diagnostic=FLAT_LCDM; physical_k4_metric=NOT_ESTABLISHED; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: sandbox
type: pantheon-plus-full-covariance-k4-optical
parent: v14.923
status: open
action: Fetch official 1701×1701 STAT+SYS Pantheon+ covariance; apply selected rows consistently including zHD/zHEL, marginalize common nuisance magnitude normalization, report full-covariance χ² and robust numerical conditioning and difference compared to fixed Ωm=.315 flat ΛCDM; no sigma without justified likelihood.
deliverable: reproduction script and full covariance numerical checks.
HANDOFF
target: external-audit
type: pantheon-plus-diagonal-diagnostic
parent: v14.923
status: open
action: Independently check 1580-row selection, zHD vs zHEL factors, optimal offsets and χ² values, and strictly flag missing full covariance.
deliverable: scoped verdict.
