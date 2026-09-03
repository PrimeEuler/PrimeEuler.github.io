# Cone Derivation Ledger v13.192 — Publication Build Baseline

**Status:** [Audit] / publication infrastructure
**Date:** 2026-09-03

## 1. Stable mathematical baseline

`Discriminant_12_Return_v0.3.1.tex` remains the independently audited mathematical checkpoint. External audit v13.190 found no new mathematical errors in that source.

## 2. Compile-path repair

A publication-working copy has been created as:

`unified/discriminant-12-return/papers/Discriminant_12_Return_v0.3.2.tex`

The only intentional source-level change from v0.3.1 is the addition

```tex
\graphicspath{{../figures/}}
```

so that the paper can resolve figure assets stored in the sibling `figures/` directory when compiled from `papers/`.

This repairs the concrete path failure identified in v13.191 for

```tex
\includegraphics{mod12_v4_cone_triple.png}
```

whose actual repository location is `unified/discriminant-12-return/figures/mod12_v4_cone_triple.png`.

## 3. Reproducible build script

Added:

`unified/discriminant-12-return/papers/build_principal_paper.sh`

The script regenerates the three publication figure families

- `make_mod12_v4_cone_triple.py`
- `fig_cutting_plane_tangent_circle_audit.py`
- `fig_divisor_summatory_11_3panel.py`

and then runs `pdflatex` twice with `-halt-on-error` on v0.3.2.

This makes the intended build order explicit and reproducible.

## 4. Compile-status guardrail

The repository-connected environment used for this audit can read and write GitHub files but does not mount the repository into the local TeX runtime. Therefore the current status is:

- [D] static TeX/source audit: clean except for the now-repaired figure path;
- [D] build command and figure-generation dependencies: explicitly encoded in `build_principal_paper.sh`;
- [O] executed end-to-end repository build: still requires running the build script in a checked-out repository (locally or in CI).

Do **not** describe v0.3.2 as empirically compile-certified until that command has actually completed with exit status 0.

## 5. Publication figure order

The mathematically natural sequence for the next publication pass is:

1. Pell--Lorentz / Cone section: `fig_cutting_plane_tangent_circle_audit` to show the exact tangent endpoints and null eigenrays.
2. Mod-12 shell section: `mod12_v4_cone_triple` to show the four unit labels and the `x+y=12` outer shell.
3. Distinguished `n=11` section: `fig_divisor_summatory_11_3panel` to show the concrete divisor-shell specialization after the theory has already been established.

This preserves the logical guardrail that `n=11` is an example/corollary, not part of the discriminant-12 selection mechanism.

## 6. Next source pass

Once the build script is executed successfully, the next paper revision should integrate the tangent-circle and `n=11` figures into the corresponding sections, then perform a visual page-layout audit (float positions, caption length, equation breaks, and table width) before adding bibliography/citation infrastructure.
