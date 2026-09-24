# Cone Derivation Ledger v13.767 — Lane B Full Relative Trace Carrier and Canonical-Quotient Intertwiner Obstruction

Date: 2026-09-24

Lane: B — Norm-Quotient / Idele-Class Representation, with cross-lane relevance to Lane A.

Status: [D] full centered prime–archimedean/origin relative trace carrier; [D] exact trivial-(C_{\mathbb Q}^1) sector; [N] no unitary intertwiner from the atomic prime-power carrier to the canonical norm-line generator; [X] common Lane-A Suzuki–Weil current realized exactly as the mixed trace functional.

Parents: v13.731, v13.736, v13.739, v13.744, v13.746, v13.760, v13.763–766.

## 0. Synchronization

The live ledger was checked immediately before this write. Current ledger head is v13.766 (Lane A); recent repository head is commit `2171c548e3a2bbdfe2190a4016ba65f530c73d0f`. No v13.767 exists and there is no numbering collision.

Round 94 independently PASSed v13.763 and explicitly endorsed adjoining the archimedean/origin carrier before returning to the original v13.760 B.2 canonical-sector gate. Lane A v13.765–766 preserves the same cross-lane guardrail: the Lane-B bulk trace does not solve the finite-(A) Schur boundary problem.

## 1. Imported finite-place carrier [D]

On
[
\mathcal H_{\rm fin}=\bigoplus_p\ell^2(\mathbb N_{\ge1}),
]
let
[
H_{\rm fin}e_{p,k}=k\log p\,e_{p,k},
\qquad
A_{\rm fin}e_{p,k}=\log p\,e_{p,k}.
]
For \(\phi\in C_c^\infty(\mathbb R)\), v13.763 gives
[
\boxed{
\langle\mu_{\rm Weil}^{\rm fin},\phi\rangle
=
\operatorname{Tr}\left[
A_{\rm fin}e^{-H_{\rm fin}/2}
(\phi(H_{\rm fin})+\phi(-H_{\rm fin}))
\right].
}
]

## 2. Archimedean/origin carrier [D]

From v13.746,
[
\mathscr W_{\infty/0}
=
-\frac12\operatorname{Pf}\frac1{|r|}
-(2A+1)\delta_0-r_1''(r),
\qquad
2A+1=\log(2\pi)+\gamma.
]

Define the archimedean/origin relative trace functional directly by
[
\boxed{
\tau_{\infty/0}(\phi)
:=
\left\langle
-\frac12\operatorname{Pf}|r|^{-1}-r_1'',\phi
\right\rangle
-(\log(2\pi)+\gamma)\phi(0).
}
]
Then
[
\boxed{
\tau_{\infty/0}(\phi)
=
\langle\mathscr W_{\infty/0},\phi\rangle.
}
]

The contact term may be represented by the one-dimensional bookkeeping channel
[
\mathcal H_0=\mathbb C,\qquad H_0=0,
]
with signed weight
[
c_0=-(\log(2\pi)+\gamma).
]
This does not assert a new spectral zero; it is only the operator realization of the contact distribution \(c_0\delta_0\).

Away from the origin, the real-place contribution can be placed in a commutative semifinite multiplication algebra, while the \(\operatorname{Pf}|r|^{-1}\) singularity requires finite-part/relative normalization. Thus the correct global object is a mixed ordinary/semifinite-relative trace, not a single ordinary trace-class operator.

## 3. Common full centered trace [D/X]

Define
[
\boxed{
\mathfrak T_{\rm common}(\phi)
:=
\tau_{\infty/0}(\phi)
-
\operatorname{Tr}_{\mathcal H_{\rm fin}}
\left[
A_{\rm fin}e^{-H_{\rm fin}/2}
(\phi(H_{\rm fin})+\phi(-H_{\rm fin}))
\right].
}
]

Using v13.763,
[
\mathfrak T_{\rm common}(\phi)
=
\langle\mathscr W_{\infty/0}-\mu_{\rm Weil}^{\rm fin},\phi\rangle.
]
Using v13.746,
[
\boxed{
\mathfrak T_{\rm common}(\phi)
=
\langle\mathscr W_S,\phi\rangle.
}
]

Explicitly,
[
\boxed{
\begin{aligned}
\mathfrak T_{\rm common}(\phi)
={}&
-\frac12\left\langle\operatorname{Pf}|r|^{-1},\phi\right\rangle
-(\log(2\pi)+\gamma)\phi(0)
-\langle r_1'',\phi\rangle\\
&-
\sum_{p,k\ge1}(\log p)p^{-k/2}
[\phi(k\log p)+\phi(-k\log p)].
\end{aligned}
}
]

This is the full centered Suzuki–Weil current as one common trace functional.

## 4. Relative subtraction removes the origin ambiguity [D]

If \(\phi,\phi_0\) are smooth tests with
[
\phi(0)=\phi_0(0),
]
then \(\psi=\phi-\phi_0\) vanishes at zero. Hence the finite-part/contact package is an ordinary relative pairing:
[
\left\langle\operatorname{Pf}|r|^{-1},\psi\right\rangle
=
\int_{\mathbb R}\frac{\psi(r)}{|r|}\,dr
]
whenever the chosen test class gives the required decay.

Therefore
[
\boxed{
\begin{aligned}
\mathfrak T_{\rm common}(\phi)-\mathfrak T_{\rm common}(\phi_0)
={}&
\left\langle
-\frac12\operatorname{Pf}|r|^{-1}-r_1'',\phi-\phi_0
\right\rangle\\
&-
\sum_{p,k\ge1}(\log p)p^{-k/2}
[(\phi-\phi_0)(k\log p)+(\phi-\phi_0)(-k\log p)].
\end{aligned}
}
]
The \(\delta_0\) contact contribution cancels identically.

This is the natural relative trace form; it avoids pretending that the origin singularity is an ordinary trace-class multiplication operator.

## 5. One-sided anchored thermal form [D]

The v13.731 carrier supplies the complementary Laplace-domain realization. For \(\Re s,\Re s_0>1\),
[
\boxed{
\begin{aligned}
\mathfrak T(s;s_0)
={}&
\tau_\infty\left[
J_\infty(e^{-sH_\infty}-e^{-s_0H_\infty})
\right]\\
&-
\operatorname{Tr}_{\mathcal H_{\rm fin}}
\left[
A_{\rm fin}(e^{-sH_{\rm fin}}-e^{-s_0H_{\rm fin}})
\right],
\end{aligned}
}
]
and
[
\boxed{
\mathfrak T(s;s_0)
=
\frac{\xi'}{\xi}(s)-\frac{\xi'}{\xi}(s_0).
}
]

Thus the centered \(r\)-space current and the one-sided anchored Tate current are two test-function presentations of the same prime-plus-real-place architecture, with the polynomial/pole completion tracked as in v13.746.

## 6. Original v13.760 B.2 gate: trivial-(C_{\mathbb Q}^1) sector [D]

Let
[
G=C_{\mathbb Q},\qquad K=C_{\mathbb Q}^1.
]
The norm map gives
[
G/K\simeq\mathbb R_{>0}^{\times},
\qquad
r(g)=\log|g|_{\mathbb A}.
]

Averaging the regular representation over \(K\) projects to the trivial-\(K\) sector. After logarithmic coordinates this sector is
[
\boxed{\mathcal H_{\rm norm}=L^2(\mathbb R,dr)}
]
with
[
\boxed{(U_\tau f)(r)=f(r-\tau).}
]
With
[
U_\tau=e^{-i\tau H_{\rm norm}},
]
[
\boxed{H_{\rm norm}=-i\,\frac d{dr}}
]
(up to the global Fourier/sign convention).

Fourier transform diagonalizes it:
[
\widehat{U_\tau f}(t)=e^{-it\tau}\widehat f(t),
]
so
[
\boxed{\sigma(H_{\rm norm})=\mathbb R}
]
with absolutely continuous spectral type and no canonical point spectrum at \(k\log p\).

Therefore the first of v13.760 B.2's two alternatives is the exact outcome:
[
\boxed{
\text{trivial-}C_{\mathbb Q}^1\text{ sector}
=
\text{continuous regular norm-line representation}.
}
]

## 7. No unitary intertwiner with the prime-power Hamiltonian [N]

Suppose a unitary
[
V:\mathcal H_{\rm fin}\to\mathcal H_{\rm norm}
]
intertwined the generators:
[
VH_{\rm fin}V^{-1}=H_{\rm norm}.
]

Unitary equivalence preserves spectral type and point spectrum. But
[
H_{\rm fin}e_{p,k}=k\log p\,e_{p,k}
]
is pure point on its prime-power basis, whereas \(H_{\rm norm}\) has purely absolutely continuous spectrum on \(\mathbb R\).

Hence:
[
\boxed{
\text{no unitary intertwiner can identify }
H_{\rm fin}
\text{ with }
H_{\rm norm}.
}
]

The obstruction is stronger than differing sets of eigenvalues: their spectral measures are mutually different in type (atomic versus absolutely continuous).

Likewise, no unitary can turn the atomic trace carrier \(A_{\rm fin}e^{-H_{\rm fin}/2}\) into the ordinary spectral measure of \(-i\partial_r\).

This closes the original representation-theoretic ambiguity left open in v13.736/v13.760.

## 8. What does survive: distributional group-algebra/orbital pushforward [D]

Although there is no state-space unitary equivalence, the arithmetic measure acts canonically through the norm-line regular representation as a distribution in the group algebra.

Let
[
\mu_{\rm pp}=\sum_{p,k\ge1}(\log p)\delta_{k\log p}.
]
For \(\Re s>1\), define the damped distribution
[
d\mu_s(r)=e^{-sr}\,d\mu_{\rm pp}(r).
]
Its represented convolution operator is
[
U(\mu_s)
=
\sum_{p,k\ge1}(\log p)p^{-ks}U_{k\log p}.
]

Since
[
U_\tau=e^{-i\tau H_{\rm norm}},
]
functional calculus gives
[
\boxed{
U(\mu_s)
=
-\frac{\zeta'}{\zeta}(s+iH_{\rm norm}),
\qquad \Re s>1,
}
]
with the sign of \(iH_{\rm norm}\) adjusted if the opposite Fourier convention is chosen.

Thus the exact bridge is not a unitary identification of spectra but
[
\boxed{
\text{local adelic orbit distribution}
\longrightarrow
\text{norm pushforward}
\longrightarrow
\text{distributional group-algebra action on }L^2(\mathbb R).
}
]

The prime-power lengths are translation/orbit insertion parameters for the continuous norm carrier, not eigenvalues of its generator.

## 9. Cross-lane consequence [X]

Combining §3 with v13.744/746 gives an exact carrier for Lane A's entire full-line Suzuki–Weil bulk current:
[
\boxed{
\langle\mathscr W_S,\phi\rangle
=
\mathfrak T_{\rm common}(\phi).
}
]

Combining §6–8 explains its representation-theoretic status:
- the bulk current is a canonical explicit-formula/orbital distribution after local arithmetic data are retained and pushed to the norm coordinate;
- its auxiliary atomic trace carrier is not the trivial-norm-sector Hilbert representation;
- Lane A's screw/Weil form may use this common current without identifying the prime-power basis with norm-line eigenstates.

This preserves the v13.765–766 guardrail:
[
\boxed{
\text{full-line bulk trace closure}
\not\Rightarrow
\text{finite-}A\text{ Schur nonresonance}.
}
]

## 10. Updated Lane-B status

Closed:
1. finite centered prime-place trace carrier (v13.763/764);
2. archimedean/origin relative carrier and common full trace (this entry);
3. original v13.760 B.2 trivial-(C_{\mathbb Q}^1) sector construction (this entry);
4. unitary-intertwiner question between the atomic prime-power Hamiltonian and canonical norm generator: negative by spectral type;
5. exact replacement bridge: arithmetic distribution/group-algebra action
[
-\zeta'/\zeta(s+iH_{\rm norm}).
]

Still open:
1. formulate the same common trace directly from a canonical action on the full adèle-class space, rather than the local-factor/direct-sum carrier;
2. identify precisely which fixed-point/orbital trace regularization on that canonical space pushes forward to \(\mathfrak T_{\rm common}\), including the real-place finite-part/contact normalization;
3. no RH/Hilbert–Pólya conclusion.

## Result

The Lane-B fork in v13.760 is now resolved.

[
\boxed{
\mathcal H_{\rm norm}=L^2(\mathbb R,dr),\qquad
H_{\rm norm}=-i\partial_r
}
]
is the exact trivial-(C_{\mathbb Q}^1) sector and remains continuous.

[
\boxed{
\mathcal H_{\rm fin},H_{\rm fin},A_{\rm fin}
}
]
is an exact auxiliary atomic trace carrier for the arithmetic orbit distribution, not a quotient-state spectrum.

The full centered common current has the exact mixed relative trace
[
\boxed{
\mathfrak T_{\rm common}
=
\tau_{\infty/0}
-
\operatorname{Tr}_{\rm fin}
\left[
A_{\rm fin}e^{-H_{\rm fin}/2}
(\phi(H_{\rm fin})+\phi(-H_{\rm fin}))
\right]
=
\mathscr W_S.
}
]

The correct canonical bridge to the norm-line representation is distributional:
[
\boxed{
U(e^{-s\cdot}\mu_{\rm pp})
=
-\frac{\zeta'}{\zeta}(s+iH_{\rm norm}),
\qquad\Re s>1,
}
]
not a unitary identification of \(H_{\rm fin}\) with \(H_{\rm norm}\).
