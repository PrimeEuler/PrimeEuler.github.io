# Cone Derivation Ledger v13.748 — From the Original Multiple-Helix Seed to the Two-Channel Dedekind Theta Current

Date: 2026-09-24

Status labels: **[P]** user-provided provenance, **[D]** exact derived, **[I]** interpretation, **[O]** open, **[G]** guardrail.

## 0. Synchronization and purpose [G]

The live ledger was rechecked immediately before this write and remained through v13.747. No v13.748 collision was present.

This checkpoint is intentionally broader than a normal incremental entry. It records the full conceptual chain now visible across the project so the external audit and parallel threads can see how the current Dedekind construction grew out of the original cone program.

**Provenance guardrail.** The project began from the user's original multiple-helix representation. The exact original helix prompt/wording is not preserved in the currently retrievable repository/history. Therefore this entry records that multiple-helix representation as the user-provided seed, but does **not** fabricate a verbatim reconstruction or promote details not recoverable from the audited papers/ledger. The earliest exact recoverable formulas begin with the factor-pair/means cone below.

## 1. Original multiple-helix seed [P/G]

[P] The user's starting geometric representation was a multiple-helix picture that motivated looking for a lower-dimensional common carrier and projections of the intertwined strands.

[G] The exact original prompt, strand count, phase conventions, and literal helix parametrization are not recoverable from the present repository/history. They must be restored from the original conversation if a future archival pass finds it. Everything below is the exact recoverable mathematical development that followed that seed.

The durable structural idea inherited from the helix picture is the coexistence of a longitudinal/scale direction, a transverse/orientation or phase direction, projections that can merge distinct strands, and discrete returns of a continuous motion. Those features later reappear exactly as the logarithmic cone coordinates \((r,u)\), the norm projection \((r,u)\mapsto r\), the Pell boost \(u\mapsto u+R_{12}\), and paired boost modes \(\{\tau,-\tau\}\).

## 2. Factor pairs and the AM–GM cone [D]

For positive factors \(x,y\), define
\[
X=\frac{x-y}{2},\qquad Y=\sqrt{xy},\qquad T=\frac{x+y}{2}.
\]
Then
\[
\boxed{X^2+Y^2=T^2}.
\]

Thus the arithmetic mean \(T\) and geometric mean \(Y\) place every factor pair on the null cone. The signed-\(Y\) algebraic cone gives the full two-sided Lorentz carrier; the positive-factor table gives its \(Y\ge0\) trace.

The companion all-four-means note later identified
\[
HM=\frac{Y^2}{T},\qquad RMS=\sqrt{T^2+X^2}.
\]

For fixed product \(xy=n\),
\[
T^2-X^2=n,\qquad Y^2=n,
\]
and divisor pairs lie on the fixed-\(Y\) hyperbola. The early row/column parabolas include
\[
x=1:\ Y^2=1-2X,\qquad y=1:\ Y^2=1+2X.
\]

## 3. Rapidity and two logarithmic cone directions [D]

On a fixed product shell define
\[
u=\frac12\log\frac{x}{y}.
\]
Then
\[
x=\sqrt n\,e^u,\qquad y=\sqrt n\,e^{-u},
\qquad
(T,X,Y)=\sqrt n(\cosh u,\sinh u,1).
\]

Define the geometric scale coordinate
\[
a=\frac12\log(xy)
\]
and the arithmetic/Tate norm coordinate
\[
\boxed{r=\log(xy)=2a}.
\]
Then
\[
x=e^{r/2+u},\qquad y=e^{r/2-u},
\qquad
\boxed{(T,X,Y)=e^{r/2}(\cosh u,\sinh u,1)}.
\]

The two commuting directions are scale \(r\mapsto r+c\) and boost \(u\mapsto u+b\). Factor exchange is \(u\mapsto-u\).

[G] Prime-power support is at
\[
\boxed{r=k\log N\mathfrak p},
\]
or \(a=(k/2)\log N\mathfrak p\). This factor of two is mandatory.

## 4. Lorentz/Pell discretization and discriminant 12 [D]

The audited Paper A to Paper B to Paper C to discriminant-12 chain yields
\[
\boxed{g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix}},
\]
with characteristic polynomial \(t^2-4t+1\) and expanding unit
\[
\boxed{\varepsilon=2+\sqrt3}.
\]

Writing \(\varepsilon^n=x_n+y_n\sqrt3\),
\[
g_{12}^n=
\begin{pmatrix}
x_n+y_n&y_n\\
2y_n&x_n-y_n
\end{pmatrix},
\qquad
x_n^2-3y_n^2=1.
\]

The regulator is
\[
\boxed{R_{12}=\log(2+\sqrt3)}.
\]
The Pell return is pure boost:
\[
\boxed{r\mapsto r,\qquad u\mapsto u+R_{12}}.
\]
Since \(N(\varepsilon)=1\), Pell returns remain on a fixed norm shell and do not generate prime scales.

## 5. Cyclotomic V4 and Pell orientation [D]

For \(U(12)=\{1,5,7,11\}\cong V_4\),
\[
\boxed{\sigma_q(\varepsilon)=\varepsilon^{\chi_{12}(q)}}.
\]
Thus \(\chi_{12}\) is exactly Pell-time orientation:
\[
u\mapsto\chi_{12}(q)u.
\]

The independent ramified analysis distinguishes
\[
\chi_{-4}:i\mapsto\pm i,\qquad
\chi_{-3}:\mathbf F_4\text{ identity/Frobenius},\qquad
\chi_{12}:\sqrt3\text{ sign/Pell orientation}.
\]

## 6. Boost spectral pair and the representation 1 + chi12 [D]

For \(\phi_\tau(u)=e^{i\tau u}\), orientation reversal exchanges \(\tau\leftrightarrow-\tau\). Therefore
\[
V_\tau=\operatorname{span}\{e^{i\tau u},e^{-i\tau u}\}.
\]
With
\[
\phi_\tau^+=\cos(\tau u),\qquad
\phi_\tau^-=i\sin(\tau u),
\]
one has
\[
\sigma_q\phi_\tau^+=\phi_\tau^+,\qquad
\sigma_q\phi_\tau^-=\chi_{12}(q)\phi_\tau^-.
\]
Hence
\[
\boxed{V_\tau\cong\mathbf1\oplus\chi_{12}}.
\]

[G] The finite Dirichlet character is not a special numerical boost frequency. It is the odd boost-orientation representation; Frobenius evaluates that representation prime by prime.

## 7. Scale current and Suzuki/Weil projection [D]

The established common current is
\[
\boxed{\mathscr W(r)=-g''(r)}.
\]
A minimal untwisted lift is
\[
\boxed{\mathbf W_{\rm cone}(r,u)=\mathscr W(r)\delta_0(u)}.
\]
Projection gives \((\pi_r)_*\mathbf W_{\rm cone}=\mathscr W\), and
\[
\widehat{\mathbf W}_{\rm cone}(t,\tau)=\widehat{\mathscr W}(t)=t^2\widehat g(t).
\]
The Pell translation has multiplier \(e^{-i\tau R_{12}}\), so scale current and boost commute.

The exact sign from v13.747 is
\[
\boxed{Q_{\rm Suz}[DF]=Q_{\rm Weil}[F]}.
\]

## 8. Trivial and chi12 finite currents and prime-ideal emergence [D]

For unramified \(p\),
\[
\mu_{1,p}=\sum_{k\ge1}(\log p)\delta_{k\log p},
\qquad
\mu_{\chi,p}=\sum_{k\ge1}\chi_{12}(p)^k(\log p)\delta_{k\log p}.
\]
Thus
\[
\boxed{\mu_{K,p}=\sum_{k\ge1}[1+\chi_{12}(p)^k](\log p)\delta_{k\log p}}.
\]

If \(\chi_{12}(p)=+1\): two primitive atoms at \(\log p\).

If \(\chi_{12}(p)=-1\): odd powers cancel and even powers double,
\[
2\sum_{m\ge1}(\log p)\delta_{2m\log p}
=
\sum_{m\ge1}(2\log p)\delta_{m\log p^2},
\]
so one primitive atom occurs at \(2\log p\).

At \(p=2,3\), the \(\chi_{12}\) local factor is \(1\), so its logarithmic-derivative current vanishes and the trivial channel leaves one primitive atom at \(\log p\).

Therefore
\[
\boxed{
\mu_K=
\sum_{\mathfrak p}\sum_{m\ge1}
(\log N\mathfrak p)\delta_{m\log N\mathfrak p}
=
\mu_1+\mu_{\chi_{12}}.
}
\]
Its Laplace transform gives
\[
-\zeta_K'/\zeta_K,
\]
and hence
\[
\boxed{\zeta_K(s)=\zeta(s)L(s,\chi_{12})}.
\]

## 9. Ramified local consistency [D]

For the trivial channel,
\[
L_2(s,\mathbf1)=(1-2^{-s})^{-1},\qquad
L_3(s,\mathbf1)=(1-3^{-s})^{-1}.
\]
For the character channel,
\[
\boxed{L_2(s,\chi_{12})=L_3(s,\chi_{12})=1}.
\]

This agrees with the independent ramified geometry: at \(2\), \(\varepsilon\equiv1\) and the surviving residue-field quotient is \(\chi_{-3}\), not \(\chi_{12}\); at \(3\), the D12 form develops its radical line and ramified \(S_3\) phase rather than an unramified \(\pm1\) Frobenius sign.

## 10. Archimedean recombination [D]

Write
\[
\Gamma_{\mathbf R}(s)=\pi^{-s/2}\Gamma(s/2).
\]
Since \(\chi_{12}\) is primitive even of conductor \(12\),
\[
\Lambda_\chi(s)
=
12^{s/2}\Gamma_{\mathbf R}(s)L(s,\chi_{12}).
\]
Multiplying the two channels gives
\[
\boxed{
12^{s/2}\Gamma_{\mathbf R}(s)^2\zeta_K(s)
=
12^{s/2}\pi^{-s}\Gamma(s/2)^2\zeta_K(s).
}
\]

Define
\[
\boxed{
\xi_K(s)=\frac12s(s-1)
12^{s/2}\pi^{-s}\Gamma(s/2)^2\zeta_K(s).
}
\]

## 11. Centered Dedekind function and logarithmic current [D]

Set
\[
\boxed{\Xi_K(w)=\xi_K(1/2+w)}.
\]
Then
\[
\boxed{\Xi_K(-w)=\Xi_K(w)},\qquad
\Xi_K(\bar w)=\overline{\Xi_K(w)}.
\]
The centered logarithmic derivative
\[
\mathcal L_K(w)=\Xi_K'(w)/\Xi_K(w)
\]
is odd.

Explicitly,
\[
\boxed{
\mathcal L_K(w)
=
\frac{2w}{w^2-1/4}
+\frac12\log12-\log\pi
+\psi(1/4+w/2)
+\frac{\zeta_K'}{\zeta_K}(1/2+w).
}
\]

## 12. New gate: theta kernel for the chi12 channel [D]

Define
\[
\boxed{
\vartheta_\chi(x)=
\sum_{n\in\mathbf Z}
\chi_{12}(n)
\exp\!\left(-\frac{\pi n^2x}{12}\right).
}
\]
There is no constant term.

For \(\Re s>1\),
\[
\int_0^\infty
\vartheta_\chi(x)x^{s/2}\frac{dx}{x}
=
2(12/\pi)^{s/2}\Gamma(s/2)L(s,\chi_{12}),
\]
so
\[
\boxed{
\Lambda_\chi(s)
=
\frac12\int_0^\infty
\vartheta_\chi(x)x^{s/2}\frac{dx}{x}.
}
\]

The primitive real even character has root number \(+1\), giving
\[
\boxed{\vartheta_\chi(x)=x^{-1/2}\vartheta_\chi(1/x)}.
\]

Split at \(x=1\), center \(s=1/2+w\), and put \(x=e^{2r}\). Then
\[
\boxed{
\Lambda_\chi(1/2+w)
=
\int_{\mathbf R}K_\chi(r)e^{wr}\,dr,
}
\]
with
\[
\boxed{
K_\chi(r)=e^{|r|/2}\vartheta_\chi(e^{2|r|}).
}
\]
The kernel is real and even.

## 13. Dedekind theta kernel as convolution [D]

v13.722 proved
\[
\boxed{
\Xi(w)=\int_{\mathbf R}\Phi(r)e^{wr}\,dr,
\qquad
\Phi(r)>0,\quad\Phi(-r)=\Phi(r).
}
\]

With the present normalizations,
\[
\xi_K(s)=\xi(s)\Lambda_\chi(s),
\]
hence
\[
\boxed{\Xi_K(w)=\Xi(w)\Lambda_\chi(1/2+w)}.
\]

Therefore
\[
\boxed{
\Xi_K(w)=\int_{\mathbf R}\Phi_K(r)e^{wr}\,dr,
\qquad
\Phi_K=\Phi*K_\chi.
}
\]
Explicitly,
\[
\boxed{
\Phi_K(r)=\int_{\mathbf R}\Phi(r-v)K_\chi(v)\,dv.
}
\]

Because both factors are real and even,
\[
\boxed{\Phi_K(-r)=\Phi_K(r)}.
\]
Differentiating,
\[
\boxed{
\Xi_K'(w)=\int_{\mathbf R}r\Phi_K(r)e^{wr}\,dr,
}
\]
and away from zeros,
\[
\boxed{
\frac{\Xi_K'}{\Xi_K}(w)
=
\frac{\int r\Phi_K(r)e^{wr}\,dr}
{\int \Phi_K(r)e^{wr}\,dr}.
}
\]

## 14. Positivity status [O/G]

The Riemann factor \(\Phi\) is rigorously positive by v13.722.

The character theta kernel \(K_\chi\) is a signed character series term-by-term. Numerical sampling suggests \(\vartheta_{\chi_{12}}(x)>0\) for \(x>0\), but this checkpoint does **not** promote that observation.

Thus \(\Phi_K=\Phi*K_\chi\) is exact, real, even, and rapidly decaying. A proof that it is positive requires an exact product identity or another proof of
\[
\vartheta_{\chi_{12}}(x)>0\quad(x>0).
\]

[G] Do not claim a positive Dedekind Xi kernel until that gate is proved.

## 15. Structural synthesis [D/I]

The recoverable chain is
\[
\boxed{
\text{multiple-helix seed}
\to
\text{factor-pair/means projection}
\to
X^2+Y^2=T^2
\to
(r,u)\text{ scale/boost cone}
\to
D=12\text{ Pell return}
\to
\mathbf1\oplus\chi_{12}
}
\]
then
\[
\boxed{
\mathbf1\oplus\chi_{12}
\to
\zeta(s)\oplus L(s,\chi_{12})
\to
\text{split/inert/ramified prime-ideal current}
\to
\zeta_{\mathbf Q(\sqrt3)}(s)
}
\]
and finally
\[
\boxed{
\text{two real gamma channels}
\to
\xi_K(s)
\to
\Xi_K(w)
\to
\Phi_K=\Phi*K_\chi.
}
\]

[I] The original helix motif has reappeared in a sharper form: two commuting coordinates, scale and boost; a projection that forgets boost orientation; discrete Pell returns along the boost fiber; and a two-state orientation representation whose channels recombine into the degree-two Dedekind object.

[G] This is a provenance/structural synthesis, not a claim that the original visual helix by itself proved the later arithmetic results.

## 16. Immediate audit targets [O]

1. Prove or disprove \(\vartheta_{\chi_{12}}(x)>0\) for all \(x>0\) by an exact Jacobi/product identity.
2. If positive, conclude \(K_\chi>0\) and \(\Phi_K=\Phi*K_\chi>0\).
3. Derive the pure \(\Phi_K\) kernel independently from a Hilbert/Hecke theta construction for \(\mathbf Q(\sqrt3)\) and compare it with the convolution formula.
4. Compare the logarithmic derivative of the convolution transform with the established prime-ideal plus two-real-place explicit-formula current.
5. Restore the original multiple-helix prompt verbatim if an archival source becomes available; until then retain the provenance gap explicitly.

---

**Checkpoint conclusion.** The D12 cone now has an exact two-channel arithmetic realization. The trivial and Pell-orientation channels reconstruct the finite prime-ideal current and the two real archimedean factors of \(\mathbf Q(\sqrt3)\). Centering gives an even entire Dedekind function \(\Xi_K\), and the theta lane gives the exact convolution kernel
\[
\boxed{\Phi_K=\Phi*K_{\chi_{12}}}.
\]
The remaining positivity question has been isolated to the exact sign of the primitive \(\chi_{12}\) theta kernel; it is not assumed.
