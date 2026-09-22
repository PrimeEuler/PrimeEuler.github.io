# Cone Derivation Ledger v13.685 — Direct Continuous-Kernel Formula for the W0/Wpi Cross-Ratio

Date: 2026-09-22

Status: exact finite-a derivation in Suzuki's continuous-kernel realization. Main payoff: after solving only the TWO fixed deficiency equations at z=+i and z=-i, the entire normalized cross-ratio for arbitrary z is obtained by source pairings. No arbitrary-z inversion of S_a and no absolute characteristic normalization are required.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.684. No collision or newer audit entry.

This uses the source-faithful transport frozen in v13.667 and the characteristic convention stabilized in v13.675.

## 1. Continuous-kernel equations

Let
\[
S_a=G_a-\lambda K_a,\qquad K_a=(-\Delta_N)^{-1},
\]
on Suzuki's continuous-kernel energy space, and let
\[
e_z(x)=e^{-izx}.
\]
Under the isometry \bar D, the transported defect vector u_z satisfies
\[
\boxed{S_a u_z=\bar D e_z.}
\]

For the canonical deficiency points,
\[
e_{+i}(x)=e^x,\qquad e_{-i}(x)=e^{-x},
\]
so choose
\[
\boxed{
S_a u_+=\bar D e_{+i},\qquad
S_a u_-=\bar D e_{-i}.
}
\]
Any common fixed normalization of u_+,u_- consistent with the boundary triple cancels in the final normalized cross-ratio.

## 2. Raw boundary form after transport

The Section-6 formula transported by \bar D is
\[
\boxed{
\widetilde{\mathcal W}(u_z,w_\theta)
=
(z+i)\langle u_z,u_+\rangle_{S_a}
+
e^{-i\theta}(z-i)\langle u_z,u_-\rangle_{S_a}.
}
\]

Suzuki's entire characteristic is
\[
W(a,\theta;z)
=
\overline{
\widetilde{\mathcal W}(u_{\bar z},w_\theta)
}.
\]

Define the two analytic source-pairing amplitudes
\[
\boxed{
P_{a,+}(z):=
\overline{\langle u_{\bar z},u_+\rangle_{S_a}},
\qquad
P_{a,-}(z):=
\overline{\langle u_{\bar z},u_-\rangle_{S_a}}.
}
\]
Then
\[
\boxed{
W_\theta(a,z)
=
(z-i)P_{a,+}(z)
+
e^{i\theta}(z+i)P_{a,-}(z).
}
\]

In particular,
\[
\boxed{
W_0=(z-i)P_+ +(z+i)P_-,
}
\]
\[
\boxed{
W_\pi=(z-i)P_+ -(z+i)P_-.
}
\]

## 3. Eliminate arbitrary-z defect solves

The energy inner product is induced by S_a:
\[
\langle f,g\rangle_{S_a}
=
\langle S_a f,g\rangle_{L^2}.
\]
Since
\[
S_a u_{\bar z}=\bar D e_{\bar z},
\]
we obtain directly
\[
\boxed{
P_{a,\pm}(z)
=
\overline{
\langle \bar D e_{\bar z},u_\pm\rangle_{L^2(-a,a)}
}.
}
\]

This is the key reduction.

To evaluate P_\pm for arbitrarily many z values, one does NOT solve
\[
S_a u_z=\bar D e_z
\]
for every z. One solves only the two fixed equations
\[
\boxed{
u_\pm=S_a^{-1}\bar D e_{\pm i},
}
\]
and then evaluates the inexpensive source pairings
\[
\boxed{
P_{a,\pm}(z)
=
\overline{
\langle \bar D e_{\bar z},
S_a^{-1}\bar D e_{\pm i}
\rangle_{L^2}
}.
}
\]

Equivalently, define the two scalar response functions
\[
\boxed{
F_{a,\pm}(z)
:=
\overline{
\langle \bar D e_{\bar z},
S_a^{-1}\bar D e_{\pm i}
\rangle_{L^2}
}.
}
\]
Then P_{a,\pm}=F_{a,\pm}.

## 4. Direct formula for m_a

Set
\[
A_a(z):=(z-i)F_{a,+}(z),\qquad
B_a(z):=(z+i)F_{a,-}(z).
\]
Then
\[
W_0=A_a+B_a,\qquad
W_\pi=A_a-B_a.
\]

Since v13.661 gives
\[
W_0/W_\pi=i m_a,
\]
we obtain the direct continuous-kernel formula
\[
\boxed{
m_a(z)
=
-i\,
\frac{
(z-i)F_{a,+}(z)+(z+i)F_{a,-}(z)
}{
(z-i)F_{a,+}(z)-(z+i)F_{a,-}(z)
}.
}
\]

This reconstructs the scalar Weyl function from TWO fixed continuous-kernel solves.

## 5. Direct normalized cross-ratio

For a base point z_* away from zeros/poles, define
\[
\Delta^{(a)}_{0/\pi}(z;z_*)
=
\frac{W_0(a,z)W_\pi(a,z_*)}
{W_\pi(a,z)W_0(a,z_*)}.
\]
Substituting A_a,B_a gives
\[
\boxed{
\Delta^{(a)}_{0/\pi}(z;z_*)
=
\frac{A_a(z)+B_a(z)}{A_a(z)-B_a(z)}
\frac{A_a(z_*)-B_a(z_*)}{A_a(z_*)+B_a(z_*)}.
}
\]

In terms of the continuous-kernel response functions alone,
\[
\boxed{
\Delta^{(a)}_{0/\pi}(z;z_*)
=
\frac{
(z-i)F_{a,+}(z)+(z+i)F_{a,-}(z)
}{
(z-i)F_{a,+}(z)-(z+i)F_{a,-}(z)
}
\,
\frac{
(z_*-i)F_{a,+}(z_*)-(z_*+i)F_{a,-}(z_*)
}{
(z_*-i)F_{a,+}(z_*)+(z_*+i)F_{a,-}(z_*)
}.
}
\]

By v13.684 this equals
\[
\boxed{
\Delta^{(a)}_{0/\pi}(z;z_*)=\frac{m_a(z)}{m_a(z_*)}.
}
\]

## 6. Normalization cancellation

Suppose the canonical deficiency vectors are rescaled compatibly:
\[
u_+\mapsto \alpha u_+,\qquad
u_-\mapsto \alpha u_-.
\]
Then
\[
F_{a,\pm}\mapsto \alpha F_{a,\pm}
\]
(up to the inner-product convention's conjugation, common to both), so W_0 and W_pi acquire the same common factor and the normalized cross-ratio is unchanged.

More generally, any common characteristic gauge q_a(z) multiplying W_0 and W_pi cancels identically in Delta.

Relative rephasing u_+/u_- does NOT cancel: it changes the boundary phase convention. This is exactly the phase datum isolated in v13.683.

## 7. Reflection reduction

Under the canonical real/reflection normalization
\[
u_-(x)=u_+(-x)
\]
and reflection symmetry of S_a, the second fixed solve is the reflected first:
\[
\boxed{u_-=Ru_+.}
\]

Hence in an implementation only ONE independent linear solve is required:
\[
\boxed{
S_a u_+=\bar D e^x,
\qquad
u_-=Ru_+.
}
\]

The full z-dependent cross-ratio then comes from pairings of the known u_+ and its reflection against \bar D e_{\bar z}.

This is the computationally strongest form of the reduction.

## 8. Why this avoids the earlier failed route

The formula uses:
- the full continuous-kernel operator S_a;
- Suzuki's exact defect equations;
- the exact boundary-form characteristic;
- only fixed deficiency solves.

It does NOT use:
- the projected free Galerkin characteristic;
- the n*pi/a endpoint branch as a determinant factor;
- an additive Dirichlet-Laplacian decomposition;
- raw ordered-zero matching;
- arbitrary-z inversions of S_a;
- an assumed finite-to-infinite normalization.

Thus it is source-faithful to the finite Suzuki construction and automatically normalization-free after the z_* ratio.

## 9. Numerical/audit target

For each finite a:
1. assemble the certified continuous-kernel operator S_a;
2. solve
   \[
   S_a u_+=\bar D e^x;
   \]
3. obtain u_-=Ru_+ and verify the residual
   \[
   \|S_a u_- -\bar D e^{-x}\|;
   \]
4. evaluate F_{a,+}(z),F_{a,-}(z) on a complex test grid;
5. form Delta directly from the boxed formula;
6. independently form W_0,W_pi from the same pairings and verify bit/high-precision agreement with the quotient formula;
7. test base-point stability by repeating with several z_*.

Only after these finite identities pass should any a->infinity comparison be attempted.

## 10. Next gate

Implement this one-solve/reflection cross-ratio in the existing chi_-4 continuous-kernel code, first at high precision or controlled quadrature. The immediate target is NOT the xi/E limit; it is internal finite-a certification:
\[
\Delta_{\rm direct}
=
\Delta_{W\text{-quotient}}
=
m_a(z)/m_a(z_*).
\]
Then study convergence in a only after the finite identity and reflection residual are numerically stable.
