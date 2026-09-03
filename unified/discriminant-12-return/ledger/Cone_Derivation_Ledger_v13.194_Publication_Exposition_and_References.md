# Cone Derivation Ledger v13.194 — Publication Exposition and References

**Status:** Publication-facing exposition pass after the second external audit and figure integration.  
**Date:** 2026-09-03  
**Paper baseline:** `Discriminant_12_Return_v0.3.3.tex`

Status labels follow the project convention: [S]/[D]/[I]/[O]/[Audit].

---

## 1. Purpose

This pass does not alter the audited mathematical spine. Its purpose is to make the principal discriminant-12 paper read as a self-contained mathematical paper rather than as a derivation log.

The stable dependency chain remains

\[
K=H^{-1}
\Longleftrightarrow \sigma=2
\Longrightarrow \tau=4
\Longrightarrow \Delta=12
\Longrightarrow \lambda=2+\sqrt3
\Longrightarrow g_{12}=\times\lambda\text{ on }\mathfrak p_2
\Longrightarrow H_{12}=\times\sqrt3
\Longrightarrow \mathcal Z=\times\zeta_{12}
\Longrightarrow \mathbb F_4.
\]

No algebraic claim in this chain was strengthened during the exposition pass.

---

## 2. v0.3.3 changes

### [D] Introduction reorganized around compatibility

The introduction now distinguishes the paper's actual contribution from the standard background ingredients. It states explicitly that the point is the compatibility of the same discriminant-12 return across several carriers:

- centered `SL_2` return;
- ramified ideal lattice;
- Pell/Lorentz realization;
- real factor Cone;
- cyclotomic ideal;
- finite `F_4` reduction.

This avoids presenting standard Pell, cyclotomic, class-field, or finite-field facts as new in themselves.

### [Audit] Scope moved forward

The paper now says early that the real Cone is a parallel carrier rather than a finite quotient and that the several four-state groups are distinct symmetry layers.

The final scope section also states explicitly that no analytic zero-location claim is inferred from:

- the finite reductions;
- the class-field description;
- the Cone geometry.

### [S] Standard references added

A compact `thebibliography` is included so the paper has no BibTeX dependency at this stage. Standard references were added for:

- continued fractions and Pell arithmetic: Hardy--Wright; Serre;
- quadratic forms and ideal/class groups: Cox; Neukirch;
- cyclotomic fields: Washington;
- finite fields, Frobenius, and trace: Lidl--Niederreiter.

The citations support standard background only. They are not used as substitutes for the paper's explicit matrix and basis computations.

### [D] Conclusion tightened

The conclusion now follows the actual dependency order and emphasizes that the same return is transported through compatible carriers. The exact identity

\[
\bar q_{12}=\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}
\]

is promoted as the finite endpoint of the integral basis-compatibility argument, while `n=11` remains a downstream specialization.

---

## 3. Figure order retained

The publication-facing figure progression remains:

1. exact tangent-circle / null-eigenray figure in the Pell--Lorentz/Cone section;
2. mod-12 unit-shell figure after the `U(12)` labeling is introduced;
3. `n=11` divisor-summatory figure only in the distinguished-specialization section.

Each caption keeps the proof/illustration distinction explicit.

---

## 4. Build script

`papers/build_principal_paper.sh` now targets

`Discriminant_12_Return_v0.3.3.tex`.

It regenerates the three figure families and runs `pdflatex` twice with `-halt-on-error`.

[Audit] The repository build command is reproducible, but an end-to-end GitHub-repository compile has not been represented as completed unless the script is actually executed in a checkout containing the generated figures.

---

## 5. Publication guardrails preserved

The exposition pass preserves all existing publication guardrails, especially:

- trace selection does not make an arbitrary trace-4 rational matrix literally equal to `g12`;
- the ramified dual-number quotient is not identified with `F4` as a ring;
- `C_basis` is not the arithmetic reversor;
- factor exchange `J` is not identified with the integral reversor without a representation map;
- `T_11 \leftrightarrow J` remains a representation correspondence;
- the `n=11` geometry does not cause the Artin/class-field behavior;
- no RH or zeta-zero conclusion is drawn from the discriminant-12 package.

---

## 6. Current status

`Discriminant_12_Return_v0.3.3.tex` is the preferred publication-working source after:

- internal derivation;
- internal dependency and line audits;
- external audit round 1;
- reconciliation;
- source repair to v0.3.1;
- external audit round 2;
- figure-path/build baseline;
- figure integration;
- publication exposition/reference pass.

The remaining work is primarily typesetting/build inspection and any final copy-editing prompted by the rendered PDF, not a known algebraic repair.

---

**End of v13.194.**
