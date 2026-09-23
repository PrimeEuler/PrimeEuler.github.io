# Cone Derivation Ledger v13.713 — Centered Xi/Zeta Cone and Complete V4 Character Correspondence

Date: 2026-09-23

Status: exact analytic-number-theory lane opening checkpoint. This entry starts a distinct Xi/Zeta cone lane under the Broader Cone Toolkit, cross-linked to the existing logarithmic-torus and Suzuki/operator lanes.

Status labels: **[D]** exact derived, **[O]** open, **[G]** guardrail.

## 0. Synchronization and collision check

Immediately before this write, the live repository head was v13.712 / External Audit Round 82 at commit \`a63c0a3dc0034425104f8262b957602d5fbc8f83\`. The target v13.713 filename was absent and the ledger directory ended at v13.712. No collision was present.

This entry cross-references:
- v13.700, Broader Cone Toolkit / Non-D12 Findings Checkpoint;
- v13.703, Logarithmic Torus Involutions and Semidirect Product;
- v13.705–711, Suzuki/operator realization of the four cone characters;
- v13.712, external audit of the Suzuki/Fredholm-Weyl character program.

## 1. Why this is a separate lane [D/G]

The constructions below depend only on the zeta/xi Dirichlet, Euler-product, functional-equation, and logarithmic structures. They do **not** use Suzuki's operator model.

Therefore the organizational split is

\[
\boxed{
\text{Broader Cone Toolkit}
\longrightarrow
\begin{cases}
\text{Suzuki/operator lane},\\
\text{Xi/Zeta analytic-number-theory lane},\\
\text{D12 arithmetic lane},\\
\text{other applications}.
\end{cases}}
\]

[G] The common four-character table shared by the Suzuki and Xi/Zeta lanes is a representation-theoretic correspondence. It is not yet an operator intertwiner, determinant identity, or Hilbert–Pólya construction.

## 2. Dirichlet atoms are exact logarithmic cone atoms [D]

For
\[
s=\sigma+it
\]
and
\[
r_n=\log n,
\]
the Dirichlet atom is
\[
n^{-s}=e^{-sr_n}.
\]

Pair
\[
x_n=n^{-s},\qquad y_n=n^{-\bar s}.
\]

Then the logarithmic cone coordinates are
\[
\tau_n=\frac12\log(x_ny_n)=-\sigma r_n,
\]
\[
\ell_n=\frac12\log(x_n/y_n)=-itr_n.
\]

Hence
\[
\boxed{
n^{-s}=e^{\tau_n+\ell_n},
\qquad
n^{-\bar s}=e^{\tau_n-\ell_n}.
}
\]

For fixed \(s\), the discrete set of Dirichlet atoms lies on the logarithmic ray
\[
\boxed{
(\tau_n,\ell_n)=-r_n(\sigma,it).
}
\]

## 3. Symmetric-square null lift [D]

Choose
\[
p_n=n^{-s/2},\qquad q_n=n^{-\bar s/2}.
\]

Then
\[
u_n=p_n^2=n^{-s},\qquad
v_n=q_n^2=n^{-\bar s},\qquad
Y_n=p_nq_n=n^{-\sigma}.
\]

With
\[
u=T+X,\qquad v=T-X,
\]
one obtains
\[
\boxed{
T_n=n^{-\sigma}\cos(t\log n),
}
\]
\[
\boxed{
X_n=-i\,n^{-\sigma}\sin(t\log n),
}
\]
\[
\boxed{
Y_n=n^{-\sigma}.
}
\]

Thus
\[
Q_n(s)=
n^{-\sigma}
\left(
\cos(t\log n),
-i\sin(t\log n),
1
\right)
\]
satisfies
\[
\boxed{
T_n^2-X_n^2-Y_n^2=0.
}
\]

So every Dirichlet atom has an exact null-cone lift.

## 4. Partial sums and the cone defect [D]

Let
\[
Z_N(s)=\sum_{n\le N}n^{-s},
\qquad
H_N^{(\sigma)}=\sum_{n\le N}n^{-\sigma}.
\]

Summing the null vectors gives
\[
Q_N(s)=
\left(
\Re Z_N(s),
i\,\Im Z_N(s),
H_N^{(\sigma)}
\right).
\]

Its Lorentz quadratic form is
\[
\boxed{
q(Q_N)
=
|Z_N(s)|^2-
\left(H_N^{(\sigma)}\right)^2
\le0.
}
\]

Equivalently,
\[
\boxed{
-q(Q_N)
=
4\sum_{m<n\le N}
(mn)^{-\sigma}
\sin^2\!\left(
\frac t2\log\frac nm
\right).
}
\]

Thus the distance from the null boundary measures pairwise logarithmic-phase cancellation in the Dirichlet sum.

For \(\sigma>1\),
\[
Q_N(s)\to
Q_\zeta(s)
=
\left(
\Re\zeta(s),
i\Im\zeta(s),
\zeta(\sigma)
\right),
\]
with
\[
\boxed{
q(Q_\zeta(s))
=
|\zeta(s)|^2-\zeta(\sigma)^2.
}
\]

[G] This direct positive-weight cone sum is only absolutely convergent for \(\Re s>1\). It must not be substituted naively on the critical strip.

## 5. Centered functional-equation coordinate [D]

Introduce
\[
w=s-\frac12.
\]

Then
\[
s\mapsto1-s
\iff
w\mapsto-w.
\]

Define the centered logarithmic scale coordinate
\[
\boxed{
\widehat\tau_n
=
-\left(\sigma-\frac12\right)r_n
=
\tau_n+\frac{r_n}{2}.
}
\]

The boost coordinate remains
\[
\ell_n=-itr_n.
\]

Hence
\[
\widehat\tau_n+\ell_n
=
-r_nw.
\]

Under the functional-equation reflection
\[
s\mapsto1-s,
\]
one has
\[
\boxed{
(\widehat\tau,\ell)
\mapsto
(-\widehat\tau,-\ell).
}
\]

In the original uncentered coordinate,
\[
\boxed{
(\tau,\ell)
\mapsto
(-\tau-\log n,-\ell).
}
\]

Thus the affine term is exactly removed by centering at \(\sigma=1/2\).

## 6. The Xi V4 action [D]

Use the centered completed function
\[
\Xi(w)=\xi\!\left(\frac12+w\right),
\]
with
\[
\Xi(-w)=\Xi(w)
\]
and the reality symmetry
\[
\Xi(\bar w)=\overline{\Xi(w)}.
\]

Define
\[
C:w\mapsto\bar w,
\qquad
D:w\mapsto-\bar w,
\qquad
R=CD:w\mapsto-w.
\]

Equivalently on the \(s\)-plane,
\[
C:s\mapsto\bar s,
\]
\[
D:s\mapsto1-\bar s,
\]
\[
R:s\mapsto1-s.
\]

On centered cone coordinates,
\[
\boxed{
C:(\widehat\tau,\ell)\mapsto(\widehat\tau,-\ell),
}
\]
\[
\boxed{
D:(\widehat\tau,\ell)\mapsto(-\widehat\tau,\ell),
}
\]
\[
\boxed{
R:(\widehat\tau,\ell)\mapsto(-\widehat\tau,-\ell).
}
\]

Therefore
\[
\boxed{
V_4^{(\xi)}
=
\langle C,D\rangle
\cong C_2\times C_2.
}
\]

The orbit
\[
\{s,\bar s,1-\bar s,1-s\}
\]
maps exactly to the four sign patterns
\[
\{(+,+),(+,-),(-,+),(-,-)\}
\]
of \((\widehat\tau,\ell)\).

## 7. Xi logarithmic derivative and the odd characters [D]

Set
\[
L(s)=\frac{\xi'}{\xi}(s).
\]

Differentiating
\[
\xi(s)=\xi(1-s)
\]
gives
\[
\boxed{
L(1-s)=-L(s).
}
\]

Reality gives
\[
\boxed{
L(\bar s)=\overline{L(s)}.
}
\]

Hence
\[
L(1-\bar s)
=
-\overline{L(s)}.
\]

Write
\[
L=A+iB,
\qquad
A=\Re L,
\qquad
B=\Im L.
\]

Then the \(V_4\) character table is
\[
\boxed{
\begin{array}{c|cc}
& C & D\\ \hline
A=\Re(\xi'/\xi)&+&-\\
B=\Im(\xi'/\xi)&-&+
\end{array}}
\]

Thus
\[
\boxed{
\Re(\xi'/\xi)\in\chi_{+,-},
\qquad
\Im(\xi'/\xi)\in\chi_{-,+}.
}
\]

These exactly match the characters of the centered cone coordinates
\[
\boxed{
\widehat\tau\in\chi_{+,-},
\qquad
\ell\in\chi_{-,+}.
}
\]

[G] This is a symmetry-sector identification, not a numerical proportionality.

## 8. Completing the even character sectors [D]

On any simply connected zero-free neighborhood, choose a local branch
\[
G(w)=\log\Xi(w)=U(w)+iV(w),
\]
where
\[
U=\log|\Xi|,
\qquad
V=\arg\Xi
\]
locally.

Since
\[
\Xi(-w)=\Xi(w),
\]
the local logarithm is even modulo the fixed branch constant, while
\[
\Xi(\bar w)=\overline{\Xi(w)}
\]
gives
\[
G(\bar w)=\overline{G(w)}
\]
for a compatible local branch.

Therefore
\[
\boxed{
U=\log|\xi|\in\chi_{+,+},
}
\]
and
\[
\boxed{
V=\arg\xi\in\chi_{-,-}.
}
\]

Together with the two components of \(\xi'/\xi\), the complete analytic character table is
\[
\boxed{
\begin{array}{c|cc}
\text{analytic observable}&C&D\\ \hline
\log|\xi|&+&+\\
\Re(\xi'/\xi)&+&-\\
\Im(\xi'/\xi)&-&+\\
\arg\xi&-&-
\end{array}}
\]

No \(V_4\) character is missing.

## 9. Exact comparison with the logarithmic cone table [D]

From v13.703, the cone logarithmic coordinates split as
\[
\begin{array}{c|cc}
\text{cone coordinate}&F&C_{\rm cone}\\ \hline
\Re\tau&+&+\\
\Im\tau&+&-\\
\Re\ell&-&+\\
\Im\ell&-&-
\end{array}
\]

Therefore there is a character-preserving correspondence
\[
\boxed{
\begin{aligned}
\Re\tau
&\longleftrightarrow
\log|\xi|,
\\
\Im\tau
&\longleftrightarrow
\Re(\xi'/\xi),
\\
\Re\ell
&\longleftrightarrow
\Im(\xi'/\xi),
\\
\Im\ell
&\longleftrightarrow
\arg\xi.
\end{aligned}}
\]

[D] The representation-theoretic four-character match is exact after identifying the two abstract \(V_4\) generator pairs.

[G] No literal equality between these quantities is claimed.

## 10. Second logarithmic derivative consistency check [D]

Let
\[
M(s)=L'(s)
=
\left(\frac{\xi'}{\xi}\right)'(s).
\]

Differentiating
\[
L(1-s)=-L(s)
\]
gives
\[
\boxed{
M(1-s)=M(s).
}
\]

Reality gives
\[
M(\bar s)=\overline{M(s)}.
\]

Hence
\[
\boxed{
\Re M\in\chi_{+,+},
\qquad
\Im M\in\chi_{-,-}.
}
\]

Thus differentiation alternates the functional-equation parity:
\[
\boxed{
\log\xi
\to
(\log\xi)'
\to
(\log\xi)''
\to\cdots
}
\]
with
\[
\boxed{
\text{even}\to\text{odd}\to\text{even}\to\text{odd}\to\cdots.
}
\]

This independently recovers the two even character sectors.

## 11. Critical-line fixed locus [D/G]

On
\[
s=\frac12+it,
\]
one has
\[
1-s=\bar s.
\]

Hence
\[
\xi\left(\frac12+it\right)
=
\overline{\xi\left(\frac12+it\right)},
\]
so
\[
\boxed{
\xi\left(\frac12+it\right)\in\mathbb R.
}
\]

Away from zeros,
\[
\boxed{
\Re\frac{\xi'}{\xi}\left(\frac12+it\right)=0.
}
\]

On the centered cone,
\[
\boxed{
\widehat\tau=0.
}
\]

Thus the critical-line fixed locus is simultaneously characterized by
\[
\boxed{
\widehat\tau=0,
\qquad
\Re(\xi'/\xi)=0,
\qquad
\xi\in\mathbb R.
}
\]

[G] These are exact symmetry statements and do not imply that all nontrivial zeros lie on the critical line.

## 12. Cross-lane significance [D/O]

The project now has two independent realizations of the same four cone characters:

1. **Suzuki/operator lane**
   - canonical Fredholm scale coordinates;
   - Cayley/Weyl boost coordinates;
   - full four-character realization audited through v13.712.

2. **Xi/Zeta lane**
   - \(\log|\xi|\),
   - \(\Re(\xi'/\xi)\),
   - \(\Im(\xi'/\xi)\),
   - \(\arg\xi\).

Both map onto the same abstract \(V_4\) character basis inherited from the logarithmic cone.

[O] The major bridge problem is now:
\[
\boxed{
\text{Does there exist an exact determinant/intertwining identity connecting the Suzuki four-coordinate package to the Xi four-coordinate package?}
}
\]

No such identity is presently proved.

## 13. New Xi/Zeta lane — next gate [O]

The immediate next task is to derive the prime/von-Mangoldt cone current for
\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_{n\ge1}\frac{\Lambda(n)}{n^s}
=
\sum_{p}\sum_{k\ge1}
(\log p)\,p^{-ks}
\qquad(\Re s>1),
\]
then add the elementary and gamma-completion terms from the completed xi logarithmic derivative.

The target is an explicit decomposition
\[
\frac{\xi'}{\xi}(s)
=
\text{elementary completion}
+
\text{gamma current}
-
\text{prime/von-Mangoldt current},
\]
with each term tested under
\[
C:s\mapsto\bar s,
\qquad
D:s\mapsto1-\bar s,
\qquad
R:s\mapsto1-s.
\]

The gate passes only if the completed sum reproduces the exact
\[
\chi_{+,-}\oplus\chi_{-,+}
\]
odd-character pair intrinsically.

## 14. Guardrails

- The direct Dirichlet cone sum is controlled only in its convergence region unless analytically continued by a separate argument.
- Local \(\arg\xi\) and \(\log\xi\) require branch choices away from zeros.
- Character matching is not an operator identity.
- Nothing in this entry proves RH, constructs a Hilbert–Pólya operator, or identifies the Suzuki determinant with \(\xi\).
- Future claims connecting the Suzuki and Xi/Zeta lanes require an explicit formula or intertwiner, not shared symmetry alone.
