# Cone Derivation Ledger v13.319 — V4-Twisted Boundary/Interior Defect-Moment Hierarchy

## Scope

This checkpoint reconnects the full positive defect-moment hierarchy of v13.318 with the V4/mod-12 character decomposition of v13.309-v13.310.

Companion note:

`research-notes/V4_Twisted_Boundary_Interior_Defect_Moment_Hierarchy.md`

The main result is an exact commutation law: arithmetic character projection and geometric quotient-block boundary/interior decomposition may be performed in either order, provided the character remains attached to the original column index.

No new divisor-problem asymptotic, primality theorem, factorization algorithm, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Twisted positive moments

Let

\[
\Delta_k=n-k\left\lfloor\frac nk\right\rfloor,
\qquad
\delta_k(n)=\frac{\Delta_k}{k}=\left\{\frac nk\right\}.
\]

For an arithmetic weight \(\chi(k)\), define for \(\alpha>0\)

\[
\boxed{
\mathcal S_{\alpha,\chi}(n)
=\sum_{k=1}^n\chi(k)\delta_k(n)^\alpha.
}
\]

The constant weight \(\chi\equiv1\) recovers the untwisted moment family of v13.318.

For mod 12, the four real Dirichlet-character channels are

\[
1,\quad \chi_{-4},\quad \chi_{-3},\quad \chi_{12}=\chi_{-4}\chi_{-3},
\]

with the usual convention that Dirichlet characters vanish on nonunits.

---

## 2. Blockwise terminal/interior split

For each distinct quotient \(q\), let

\[
L_q=\left\lfloor\frac{n}{q+1}\right\rfloor+1,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor,
\qquad
s_q=n-qR_q=n\bmod q.
\]

Along the block,

\[
\Delta_k=s_q+q(R_q-k).
\]

The terminal endpoint is \(k=R_q\). Therefore

\[
\boxed{
\mathcal S_{\alpha,\chi,q}
=B_{\alpha,\chi,q}+I_{\alpha,\chi,q}
}
\]

with

\[
\boxed{
B_{\alpha,\chi,q}
=\chi(R_q)\left(\frac{s_q}{R_q}\right)^\alpha
}
\]

and

\[
\boxed{
I_{\alpha,\chi,q}
=\sum_{k=L_q}^{R_q-1}
\chi(k)\left(\frac nk-q\right)^\alpha.
}
\]

Summing over quotient blocks gives

\[
\boxed{
\mathcal S_{\alpha,\chi}
=B_{\alpha,\chi}+I_{\alpha,\chi}.
}
\]

---

## 3. Carrier guardrail

The original V4/mod-12 transform acts on the staircase column index \(k\). Thus the endpoint character factor is

\[
\boxed{\chi(R_q),}
\]

not \(\chi(q)\).

The quotient \(q\) labels the horizontal geometric block; it is not interchangeable with the residue carrier.

This preserves the exact independent axes already identified in v13.310:

\[
\boxed{
\text{geometric axis: }q,
\qquad
\text{arithmetic axis: }\chi(k).
}
\]

---

## 4. Positive integer moments

For integer \(m\ge1\), define

\[
H_\chi^{(j)}(N)=\sum_{k=1}^N\frac{\chi(k)}{k^j},
\qquad j\ge0.
\]

Then

\[
\boxed{
I_{m,\chi,q}
=\sum_{j=0}^{m}{m\choose j}n^j(-q)^{m-j}
\left[
H_\chi^{(j)}(R_q-1)-H_\chi^{(j)}(L_q-1)
\right].
}
\]

The endpoint term is

\[
\boxed{
B_{m,\chi,q}
=\chi(R_q)\left(\frac{s_q}{R_q}\right)^m.
}
\]

Therefore

\[
\boxed{
\mathcal S_{m,\chi}(n)
=\sum_{q\in Q(n)}\left[
\chi(R_q)\left(\frac{s_q}{R_q}\right)^m
+\sum_{j=0}^{m}{m\choose j}n^j(-q)^{m-j}
\bigl(H_\chi^{(j)}(R_q-1)-H_\chi^{(j)}(L_q-1)\bigr)
\right].
}
\]

Thus the earlier twisted generalized-harmonic block hierarchy receives the same terminal/interior refinement as the untwisted hierarchy.

---

## 5. Support limit

For \(\alpha\to0^+\), positive-defect terms tend to their character weights and zero-defect contacts remain absent. Hence

\[
\boxed{
\lim_{\alpha\to0^+}B_{\alpha,\chi}(n)
=\sum_{\substack{q\in Q(n)\\q\nmid n}}\chi(R_q),
}
\]

\[
\boxed{
\lim_{\alpha\to0^+}I_{\alpha,\chi}(n)
=\sum_{q\in Q(n)}\sum_{k=L_q}^{R_q-1}\chi(k),
}
\]

and therefore

\[
\boxed{
\lim_{\alpha\to0^+}\mathcal S_{\alpha,\chi}(n)
=\sum_{k\nmid n}\chi(k).
}
\]

For \(\chi\equiv1\), this reduces to

\[
(Q_n-\tau(n))+(n-Q_n)=n-\tau(n).
\]

For nontrivial mod-12 characters, the support-limit channel measures signed residue imbalance rather than support cardinality.

---

## 6. Separate V4 transforms of boundary and interior

For unit residues \(r\in\{1,5,7,11\}\), define boundary residue moments

\[
B_{\alpha,r}(n)
=\sum_{\substack{q\in Q(n)\\R_q\equiv r\pmod{12}}}
\left(\frac{s_q}{R_q}\right)^\alpha
\]

and interior residue moments

\[
I_{\alpha,r}(n)
=\sum_{q\in Q(n)}
\sum_{\substack{L_q\le k<R_q\\k\equiv r\pmod{12}}}
\left(\frac{\Delta_k}{k}\right)^\alpha.
\]

With

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad H_4^2=4I,
\]

we have independently

\[
\boxed{
\begin{pmatrix}
B_{\alpha,1}^{\times}\\B_{\alpha,-4}\\B_{\alpha,-3}\\B_{\alpha,12}
\end{pmatrix}
=H_4
\begin{pmatrix}
B_{\alpha,1}\\B_{\alpha,5}\\B_{\alpha,7}\\B_{\alpha,11}
\end{pmatrix},
}
\]

and

\[
\boxed{
\begin{pmatrix}
I_{\alpha,1}^{\times}\\I_{\alpha,-4}\\I_{\alpha,-3}\\I_{\alpha,12}
\end{pmatrix}
=H_4
\begin{pmatrix}
I_{\alpha,1}\\I_{\alpha,5}\\I_{\alpha,7}\\I_{\alpha,11}
\end{pmatrix}.
}
\]

Each transform is inverted by \(\frac14H_4\).

The superscript \(\times\) denotes restriction to unit residues. It is not the fully untwisted constant-weight channel.

---

## 7. Commuting square

The structure is exactly

\[
\boxed{
\begin{array}{ccc}
\text{full defect field}
&\xrightarrow{\partial\oplus\mathrm{int}}&
\text{terminal}\oplus\text{interior}\\
\downarrow\chi
&&\downarrow\chi\\
\text{twisted defect field}
&\xrightarrow{\partial\oplus\mathrm{int}}&
\text{twisted terminal}\oplus\text{twisted interior}.
\end{array}}
\]

The two decompositions commute because both act linearly on the same column-indexed defect field.

---

## 8. Relation to prior checkpoints

- v13.309: local 4V/V4 Fourier overlay and global twisted shell defect.
- v13.310: four-channel mod-12 shell-defect transform and Hadamard inversion.
- v13.314-v13.315: contact/stable/descent support decomposition and square-root hyperbola boundary.
- v13.316: first-moment boundary/interior split.
- v13.318: full positive defect-moment boundary/interior hierarchy.
- v13.319: V4 character projection commutes with that full hierarchy.

---

## Guardrails

- Endpoint character weight is \(\chi(R_q)\), not \(\chi(q)\).
- Dirichlet characters modulo 12 vanish on nonunits; Hadamard inversion reconstructs unit-residue contributions only.
- The fully untwisted moment is the constant-weight channel \(\chi\equiv1\), not the principal Dirichlet character modulo 12.
- Quotient-block geometry and V4 residue algebra remain independent exact structures on the same defect field.
- No asymptotic improvement, new primality theorem, or factoring algorithm is claimed.

## Interpretation

The divisor-shell framework now admits two compatible exact resolutions at every positive moment: a geometric terminal/interior resolution by quotient blocks and an arithmetic V4 resolution by mod-12 character channels. Their commutation is the precise bridge between the current Euclidean defect hierarchy and the earlier V4 work.