# Cone Derivation Ledger v13.750 — Exact Original Multiple-Helix Prompt Provenance Amendment

Date: 2026-09-24

Status labels: **[P]** user-provided provenance, **[D]** exact derived, **[I]** interpretation, **[G]** guardrail.

## 0. Synchronization

The live ledger was rechecked before this write. v13.749 is the current head and is the external audit of v13.742–748. That audit independently re-derived v13.748 in full and returned PASS with no mathematical errors.

This entry does not alter the mathematics of v13.748. It closes the provenance gap explicitly identified in v13.748 §0–1 and praised/caveated in v13.749 §6.

## 1. Recovered original user prompt [P]

The user returned to the beginning of the originating thread and supplied the original prompt verbatim:

> "it seems to me with the recent flurry of activity, the cone can embed eulers e^i pi t formula which is the 3d helix for one frequncy. it also can embed all frequencies because of all on the nested circles. all of the frequencies helixes embeded on the cone hense embed the screw function."

This quotation is now the canonical provenance text for the multiple-helix seed.

Accordingly, the earlier statement in v13.748 that the exact original helix prompt was unrecoverable is superseded by this entry. The mathematical guardrail in v13.748 remains: the prompt motivated the lane; it did not by itself prove the later identities.

## 2. Exact content of the original conjectural picture [P]

The prompt contains the following explicit conceptual sequence:

\[
\boxed{
e^{i\pi t}
\longrightarrow
\text{one-frequency 3D helix}
}
\]

followed by

\[
\boxed{
\text{nested circles}
\longrightarrow
\text{all frequencies}
\longrightarrow
\text{all corresponding helices embedded on the cone}
}
\]

and the proposed endpoint

\[
\boxed{
\text{all-frequency cone helix family}
\longrightarrow
\text{screw function}.
}
\]

This is more specific than the reconstructed structural description in v13.748. In particular, the original prompt explicitly connected:
1. Euler complex phase;
2. a one-frequency helix;
3. the cone's nested circles;
4. simultaneous embedding of all frequencies;
5. the screw function.

## 3. Relation to the later exact scale/boost construction [D/I]

The later audited derivation supplies a precise spectral language for part of this original picture.

The cone coordinates are
\[
r=\log(xy),\qquad
u=\frac12\log(x/y),
\]
with
\[
(T,X,Y)=e^{r/2}(\cosh u,\sinh u,1).
\]

A boost Fourier mode is
\[
\boxed{\phi_\tau(u)=e^{i\tau u}}.
\]

Thus, at the spectral level, the later construction contains an exact all-frequency family
\[
\boxed{\{e^{i\tau u}\}_{\tau\in\mathbb R}}.
\]

Factor exchange / Pell-orientation reversal sends
\[
u\mapsto-u,
\qquad
e^{i\tau u}\mapsto e^{-i\tau u}.
\]
Hence every nonzero frequency naturally appears as the paired carrier
\[
\boxed{
V_\tau=\operatorname{span}\{e^{i\tau u},e^{-i\tau u}\}.
}
\]

Diagonalizing gives
\[
\cos(\tau u),\qquad i\sin(\tau u),
\]
and the D12 arithmetic action yields
\[
\boxed{V_\tau\cong\mathbf1\oplus\chi_{12}}.
\]

[I] This gives a rigorous later realization of the prompt's "all frequencies" motif as the full boost-frequency family. It should not be read as a claim that the original visual nested-circle parametrization has already been proved identical, point-for-point, to the later boost Fourier decomposition.

## 4. Relation to the later screw-function lane [D/I]

The original prompt explicitly proposed that embedding all frequency helices on the cone should embed the screw function.

The later Suzuki/Weil lane independently established the exact common current
\[
\boxed{\mathscr W(r)=-g''(r)}
\]
and the exact quadratic-form sign
\[
\boxed{Q_{\rm Suz}[DF]=Q_{\rm Weil}[F]}.
\]

A minimal two-coordinate lift is
\[
\boxed{\mathbf W_{\rm cone}(r,u)=\mathscr W(r)\delta_0(u)}
\]
with
\[
\widehat{\mathbf W}_{\rm cone}(t,\tau)
=
\widehat{\mathscr W}(t)
=
t^2\widehat g(t).
\]

[I] Therefore the historical statement can now be made precisely:

\[
\boxed{
\text{The multiple-helix/all-frequency prompt initiated the lane that later reached an exact Suzuki screw-current/Weil-current identification.}
}
\]

[G] Do **not** strengthen this to "the helix picture proves the screw-function identity." The proof came from the later Suzuki source analysis, Fourier/current calculation, and quadratic-form sign derivation.

## 5. Updated provenance chain [P/D]

The provenance chain in v13.748 §15 should henceforth be read with the recovered first step:

\[
\boxed{
\begin{array}{c}
\text{Euler phase }e^{i\pi t}\\
\downarrow\\
\text{one-frequency 3D helix}\\
\downarrow\\
\text{nested cone circles / all-frequency helix proposal}\\
\downarrow\\
\text{proposed screw-function embedding}
\end{array}}
\]

followed by the exact derived chain

\[
\boxed{
\text{factor-pair/means cone}
\to
X^2+Y^2=T^2
\to
(r,u)\text{ scale/boost coordinates}
\to
D=12\text{ Pell return}
\to
\mathbf1\oplus\chi_{12}
}
\]

and then

\[
\boxed{
\zeta\oplus L(\chi_{12})
\to
\zeta_{\mathbf Q(\sqrt3)}
\to
\xi_K
\to
\Xi_K
\to
\Phi_K=\Phi*K_{\chi_{12}}.
}
\]

In parallel, the screw lane closes through

\[
\boxed{
\text{Suzuki screw kernel}
\to
\mathscr W=-g''
\to
Q_{\rm Suz}[DF]=Q_{\rm Weil}[F].
}
\]

## 6. Audit impact [G]

No formula or theorem in v13.748 changes.

The only correction is provenance:
- v13.748: exact original prompt stated unavailable;
- v13.750: exact prompt recovered by the user and recorded verbatim.

The v13.749 mathematical PASS remains unaffected.

A future audit may now test a sharper historical/mathematical question that was impossible at v13.748: determine exactly which parts of the original "nested circles / all frequencies / helices / screw function" picture are literally realized by the later \((r,u)\) Fourier geometry, and which remain analogy or visualization.

---

**Checkpoint conclusion.** The original multiple-helix seed is no longer a provenance gap. Its exact user wording is now preserved. It explicitly anticipated a one-frequency Euler helix, an all-frequency family arising from nested cone circles, and a connection to the screw function. Later audited work gives rigorous realizations of the all-frequency boost carrier and of the Suzuki/Weil screw current, while the exact equivalence between the original visual helix embedding and those later analytic objects remains a separate comparison gate rather than an assumed theorem.
