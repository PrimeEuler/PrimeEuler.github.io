# Cone Derivation Ledger v13.219 — Principal v0.3.4 Publication Promotion

**Date:** 2026-09-04  
**Status:** CLOSED publication-promotion checkpoint for the principal Discriminant-12 paper after the v13.218 downstream foundation audit.  
**Authoritative source:** `papers/Discriminant_12_Return_v0.3.4.tex`  
**Authoritative compiled output:** `papers/Discriminant_12_Return_v0.3.4.pdf`

Status labels: [S] source-established, [D] exact derived, [Audit] correction/reconciliation, [Pub] publication/build status.

---

## 1. Why this checkpoint exists

Ledger v13.218 audited `papers/Discriminant_12_Return_v0.3.3.tex` against the now-stabilized foundation chain:

1. Paper A v2.4;
2. Area note v1.1;
3. Paper B v2.1;
4. Paper C v1.1;
5. Casimir / Null-Diamond v2.1.

That audit found that the principal algebraic spine remained valid, but v0.3.3 required a narrow foundation-synchronization revision. The most important repair was categorical: the project had to distinguish literal residue-field multiplication by the Pell unit from the mod-2 Pell coordinate action transported to the additive carrier of `F_4`.

This checkpoint records the corrected source, the publication-pipeline changes, both failed CI attempts and their causes, the final successful build, and the promotion of v0.3.4 to the active principal baseline.

---

## 2. [D / Audit] Mathematical repairs carried into v0.3.4

### 2.1 Ramified-ideal coordinates are separated from factor coordinates

The ramified ideal basis is

\[
f_1=2,\qquad f_2=\sqrt3-1.
\]

v0.3.4 writes an ideal element as

\[
\alpha=m f_1+n f_2=(2m-n)+n\sqrt3,
\]

so

\[
N_{F/\Q}(\alpha)
=(2m-n)^2-3n^2
=2q_{12}(m,n),
\]

with

\[
q_{12}(m,n)=2m^2-2mn-n^2.
\]

The symbols `(x,y)` are reserved for the separate Paper-A factor-cone carrier. This prevents the earlier notation from suggesting a literal identification of two different coordinate systems.

### 2.2 Paper-A two-sided Cone convention is restored

The factor-cone section now uses

\[
X=\frac{x-y}{2},\qquad
T=\frac{x+y}{2},\qquad
Y^2=xy,
\]

with both lifts

\[
Y=\pm\sqrt{xy}.
\]

Thus

\[
T^2-X^2-Y^2=0.
\]

The two involutions remain distinct:

- factor exchange `(x,y)->(y,x)` is `X->-X` and sends rapidity `s->-s`;
- cone-side reflection is `Y->-Y` and leaves `X,T` fixed.

No cyclotomic identification is inferred from the geometric `Y` reflection.

### 2.3 Paper-A row/column convention is synchronized

For fixed factor level `u>0`, v0.3.4 uses

\[
x=u\quad\Longrightarrow\quad Y^2=u^2-2uX,
\]

with vertex `(u/2,0)`, and

\[
y=u\quad\Longrightarrow\quad Y^2=u^2+2uX,
\]

with vertex `(-u/2,0)`.

The fixed-`T` circle tangent condition remains

\[
T=u/2,
\]

and the side-view tangent endpoints

\[
(T,X)=\left(\frac u2,\pm\frac u2\right)
\]

remain the two null eigenrays of the discriminant-12 boost.

### 2.4 The `n=11` shell is explicitly two-sided

The distinguished factor pairs `(11,1)` and `(1,11)` satisfy

\[
X=\pm5,\qquad T=6.
\]

On the full Cone the shell has the four lifts

\[
\boxed{X=\pm5,\qquad Y=\pm\sqrt{11},\qquad T=6.}
\]

The arithmetic Artin specialization remains independent of this visualization.

---

## 3. [D / Audit] Finite-reduction correction

This is the principal mathematical publication repair in v0.3.4.

### 3.1 Mod-2 Pell coordinate action

On the ramified-ideal quotient, in the basis `(f_1,f_2)`,

\[
\bar g_{12}
=
\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

Define the additive `F_2`-linear identification

\[
\psi:\mathfrak p_2/2\mathfrak p_2\longrightarrow\F_4
\]

by

\[
\boxed{f_1\mapsto1,\qquad f_2\mapsto\omega^2.}
\]

Then the transported action is Frobenius:

\[
\boxed{\psi\,\bar g_{12}\,\psi^{-1}=\Fr.}
\]

This is an equality of `F_2`-linear actions after an explicit carrier identification.

### 3.2 Literal residue multiplication by the Pell unit is different

Let

\[
\mathfrak P_2=\mathfrak p_2\OO_{K_{12}},
\qquad
\OO_{K_{12}}/\mathfrak P_2\cong\F_4.
\]

In that residue field,

\[
2\equiv0,
\qquad
\sqrt3\equiv-1\equiv1,
\]

and therefore

\[
\boxed{\lambda=2+\sqrt3\equiv1\pmod{\mathfrak P_2}.}
\]

Hence literal residue-field multiplication by `lambda` is the identity, not Frobenius.

By contrast,

\[
\mathcal Z=\times\zeta_{12}
\]

reduces literally to multiplication by

\[
\omega=\bar\zeta_{12},
\qquad \omega^3=1.
\]

Thus the publication-safe finite statement is:

\[
\boxed{\text{reduced }\zeta_{12}\text{ acts by }\times\omega,}
\]

while

\[
\boxed{\text{the mod-2 Pell coordinate action becomes Frobenius only after }\psi.}
\]

The two `F_2`-linear actions then generate

\[
GL_2(\F_2)\cong S_3.
\]

### 3.3 Ring/carrier guardrail

The map `psi` is not a ring isomorphism. The ramified quotient

\[
\mathfrak p_2/2\mathfrak p_2
\]

is nonreduced, whereas

\[
\OO_{K_{12}}/\mathfrak P_2\cong\F_4
\]

is a field. The exact bridge is additive and action-compatible only.

The finite-field trace statement remains exact under this same identification:

\[
\boxed{\bar q_{12}=\Tr_{\F_4/\F_2},}
\]

and in the principal/Boolean basis

\[
\Tr(\epsilon_1\omega+\epsilon_2\omega^2)
=\epsilon_1\oplus\epsilon_2.
\]

---

## 4. [S / Pub] Source creation

The corrected source was created as

`papers/Discriminant_12_Return_v0.3.4.tex`.

Source-creation commit:

`8618b598676aa07dc66867e316091e266a8c84ca`

message:

`Create principal paper v0.3.4 with foundation reconciliation`

The v0.3.3 source/PDF were not mutated or deleted. They remain the preceding historical publication snapshot.

---

## 5. [Pub] Build-script and workflow migration

### 5.1 Initial v0.3.4 build script

Created:

`papers/build_discriminant12_v0.3.4.sh`

commit:

`c7fe12a247cef1c6b92859a8376abd429d7476ff`

The script preserves paper-specific figure ownership and generates:

- `discriminant12_tangent_null_rays_3panel.pdf/png`;
- `discriminant12_divisor_summatory_11_3panel.pdf/png`;
- `mod12_v4_cone_triple.png`.

It stages the historical figure-reference names to paper-specific publication names rather than modifying Paper-A outputs.

### 5.2 Workflow retargeted to v0.3.4

`.github/workflows/build-discriminant12-paper.yml` was retargeted to

`papers/build_discriminant12_v0.3.4.sh -> Discriminant_12_Return_v0.3.4.tex`

in commit

`c0da2c36893b007106439551aaa318ea06a37869`.

The workflow also stages the canonical compiled output

`papers/Discriminant_12_Return_v0.3.4.pdf`.

### 5.3 Handoff README initially synchronized

The README was switched to the v0.3.4 source/build/workflow mapping in commit

`bb52b7b4912dcc182b3bf198ef78ca63d8bdcc82`.

At that point its publication wording remained conditional on a successful CI build, as required.

---

## 6. [Pub / Audit] CI failure history and repairs

The failed attempts are part of the reproducibility record and must not be erased from the audit trail.

### 6.1 Run 39 — missing `dvipng`

Workflow run:

`33903375118`

Conclusion: **failure**.

The failure occurred while a Matplotlib generator with `text.usetex=True` attempted to save PNG output. The GitHub runner lacked `dvipng`.

This was a publication-environment dependency failure, not a mathematical or TeX-source failure.

The workflow dependency set was repaired in commit

`ee7996cb6acc0a87292d7950a2624da37ce57869`

message:

`Install dvipng for principal Matplotlib TeX figures`

The active workflow now installs `dvipng` in addition to `cm-super` and the TeX/Matplotlib packages.

### 6.2 Run 40 — staged figure-name copy was bypassed

Workflow run:

`33903585344`

Conclusion: **failure**.

All three publication generators completed successfully. `pdflatex` then failed because the original source still referenced

`fig_cutting_plane_tangent_circle_audit.pdf`.

An initial attempt to make the `sed` filename remapping less brittle was committed as

`2473e393818de67a31b749788b0fa85abd6098bb`

message:

`Fix v0.3.4 staged figure-name remapping`.

Run 41:

`33903888567`

still failed. Inspection of its TeX log established the deeper cause: the staged file itself existed, but

`TEXINPUTS="$HERE:$FIG:"`

placed the original paper directory before the current build directory, so TeX resolved and compiled the unstaged original source instead of the remapped staged copy.

### 6.3 Staged-source precedence repair

The build script was corrected to use

`TEXINPUTS=".:$FIG:$HERE:"`

so the staged current-directory source has precedence over the original paper path.

Repair commit:

`1a1857ef75ea0214ed0fc70c0c4cbd993e037ce5`

message:

`Compile staged v0.3.4 source before original path`

This is now part of the project build invariant for staged-source publication builds: if a staged copy is intentionally rewritten, the build environment must resolve that staged copy first.

---

## 7. [Pub] Successful v0.3.4 build

Workflow run:

`33904189663`

Run number: 42.  
Conclusion: **success**.

The job successfully completed:

1. checkout;
2. dependency installation;
3. all three publication figure generators;
4. the isolated two-pass v0.3.4 TeX build;
5. publication-output commit.

The GitHub Actions bot committed the compiled PDF and generated publication figures in

`92faf441e08e61fe8cd4359c7b6b0a63e7cdd22a`

message:

`Build Discriminant 12 Return v0.3.4 outputs`

The committed PDF exists at

`papers/Discriminant_12_Return_v0.3.4.pdf`

with Git blob SHA

`7124b79e02b506ebc29b9ce27f8fffe45a09d92e`.

Therefore v0.3.4 has direct CI evidence of successful compilation in the repository publication environment.

---

## 8. [Pub] README closure

After CI success, the README was changed from conditional wording to a definitive v0.3.4 publication baseline and now records:

- the v0.3.4 source/PDF as current principal baseline;
- successful workflow run `33904189663`;
- output commit `92faf441e08e61fe8cd4359c7b6b0a63e7cdd22a`;
- `dvipng` as a required principal Matplotlib/LaTeX runner dependency;
- staged-source-first `TEXINPUTS` as a build guardrail.

README closure commit:

`027c682bed4536ae569529f623693e70cc32b349`

---

## 9. Final publication status

The active principal publication baseline is now

\[
\boxed{\texttt{Discriminant\_12\_Return\_v0.3.4.tex/.pdf}.}
\]

v0.3.3 is retained as historical provenance and reproducible prior state.

The current audited/project publication chain is therefore:

\[
\boxed{
\text{Paper A v2.4}
\rightarrow
\text{Area v1.1}
\rightarrow
\text{Paper B v2.1}
\rightarrow
\text{Paper C v1.1}
\rightarrow
\text{Null-Diamond v2.1}
\rightarrow
\text{Principal v0.3.4}
}
\]

This arrow notation records the audit/publication dependency order. It does not assert that every theorem in each later paper logically depends on every theorem in every earlier paper.

---

## 10. Final classification

- [D] Centered-Cayley selection, discriminant 12, Pell ideal action, Lorentz norm, cyclotomic integral completion, and `n=11` Artin specialization remain intact.
- [Audit] Ramified ideal coefficients and factor-cone coordinates are now explicitly distinct.
- [Audit] Principal geometry is synchronized with Paper A v2.4's two-sided Cone and row/column convention.
- [Audit] Literal residue multiplication by `lambda` is separated from the transported mod-2 Pell/Frobenius action.
- [D] Reduced `zeta_12` multiplication remains the literal order-3 multiplication by `omega` on `F_4`.
- [D] XOR parity remains the finite-field trace under the explicit compatible additive identification.
- [Pub] v0.3.4 successfully compiled in CI and has a committed canonical PDF.
- [Pub] v0.3.3 remains historical rather than being silently overwritten.
- [Pub] README and workflow mappings now identify v0.3.4 as the active principal baseline.

**Principal v0.3.4 audit/promotion cycle: CLOSED.**
