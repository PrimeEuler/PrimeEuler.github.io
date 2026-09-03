# Cone Derivation Ledger v13.193 — Principal Paper Figure Integration

**Status:** [D]/[Audit] publication-layout integration after v13.192 build baseline.  
**Date:** 2026-09-03

## 1. Source updated

Updated:

`unified/discriminant-12-return/papers/Discriminant_12_Return_v0.3.2.tex`

The existing `\graphicspath{{../figures/}}` preamble remains in place.

## 2. Tangent/null-eigenray figure integrated

Inserted after the exact factor-parabola tangency derivation in the Pell--Lorentz / factor-cone section:

`fig_cutting_plane_tangent_circle_audit.pdf`

with label:

`fig:tangent-null-rays`

The caption states only what is proved in the text:

- fixed-$T$ family $T=K/2$ for $K=1,\ldots,12$;
- emphasized $u=5,6,7$ row/column tangencies;
- tangent side-view points $(T,X)=(u/2,\pm u/2)$;
- these are the two null eigendirections of the discriminant-$12$ Pell boost.

Guardrail: the figure is explicitly described as illustrative; the null-eigenray theorem does not depend on the plotted discretization.

## 3. Mod-12 figure retained and caption tightened

The existing

`mod12_v4_cone_triple.png`

remains in the mod-$12$ unit-shell section. Its caption now explicitly states that the geometric placement realizes the four labels but is not itself the multiplication law of $U(12)$.

This preserves the separation

\[
\text{geometric shell labels}\neq\text{cyclotomic group law}\neq\text{Boolean translations}.
\]

## 4. n=11 divisor-summatory figure integrated

Inserted near the beginning of the distinguished $n=11$ specialization:

`fig_divisor_summatory_11_3panel.png`

with label:

`fig:n11-divisor-summatory`

The placement is deliberate. It occurs only after the general discriminant-$12$, cyclotomic, and finite-reduction theory is complete. This preserves the logical role of $n=11$ as a specialization/example rather than a selection premise.

The surrounding text explicitly says that the arithmetic specialization is established independently of the visualization.

## 5. Publication visual sequence

The principal paper now has the intended visual progression:

\[
\boxed{
\text{Pell/Cone theorem}
\to
\text{tangent/null-eigenray figure}
\to
\text{mod-12 }V_4\text{ shell}
\to
\text{cyclotomic + }\mathbb F_4
\to
\text{$n=11$ divisor specialization figure}.
}
\]

This mirrors the proof dependency architecture rather than the historical discovery order.

## 6. Build dependency status

The source now references three publication figures:

1. `fig_cutting_plane_tangent_circle_audit.pdf`
2. `mod12_v4_cone_triple.png`
3. `fig_divisor_summatory_11_3panel.png`

The two generated figures are produced by the existing scripts in `../figures/`; the mod-12 PNG is already present in the repository.

The build helper created in v13.192 is intended to regenerate these assets before the two-pass `pdflatex` build.

## 7. Current status

[D] Mathematical statements in the inserted captions match already-audited derivations.  
[Audit] Figure placement now follows the final dependency structure.  
[Audit] No new mathematical claim was introduced by the layout integration.  
[Open-build] An executed end-to-end TeX build remains to be run in a checkout with LaTeX and the figure scripts available.

---

**End of v13.193.**