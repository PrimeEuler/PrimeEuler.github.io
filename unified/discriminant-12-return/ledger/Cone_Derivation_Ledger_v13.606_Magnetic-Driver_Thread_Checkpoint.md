# Cone Derivation Ledger v13.606 — Magnetic-Driver Thread Checkpoint

Date: 2026-09-21

Status: coordination checkpoint. This entry freezes the current state of the magnetic-driver lane so work can resume in a fresh chat without reconstructing the long thread.

## 0. Collision check

Immediately before writing, the latest numbered ledger commit found was v13.605 ("freeze N orthonormalization and fail exact P normalization"). Therefore v13.606 was free.

This checkpoint coordinates with the already-promoted magnetic-driver entries, especially:
- v13.595: resonant magnetic-driver weighted multiplet.
- v13.598: off-resonant magnetic-driver binomial transfer law.

No claim below should override later independent audits if one appears after this checkpoint.

## 1. Certified / promoted magnetic-driver core

For a circular transverse field
\[
B_x=B_1\cos\omega t,\qquad B_y=B_1\sin\omega t,
\]
with \(\Omega_0=-\gamma B_0\) and \(\Delta=\omega-\Omega_0\), the exact rotating-frame Hamiltonian is
\[
\boxed{H_r=-\Delta J_z-\gamma B_1J_x.}
\]

At resonance,
\[
\boxed{H_r=-\gamma B_1J_x=-\frac{\gamma B_1}{2}A_j,}
\]
where in the \(J_z\) basis
\[
(A_j)_{q,q+1}=Y_q,
\qquad
Y_q=\sqrt{(j-q)(j+q+1)}.
\]

Using
\[
X_q=q+\frac12,\qquad T=j+\frac12,
\]
the edge weight obeys
\[
\boxed{Y_q^2=T^2-X_q^2.}
\]

For \(j>1/2\), the edge scales are not independent autonomous two-level systems when the full resonant multiplet is driven. The exact full Hamiltonian is one irreducible SU(2) rotation.

## 2. Promoted off-resonant extremal-state law (v13.598)

Let
\[
g=\gamma B_1,\qquad
\Omega=\sqrt{\Delta^2+g^2}.
\]

Define
\[
\boxed{
p(t)=
\frac{g^2}{\Delta^2+g^2}
\sin^2\left(\frac{\Omega t}{2}\right).
}
\]

For an initial lowest-weight state \(|j,-j\rangle\),
\[
\boxed{
P_{-j\to-j+r}(t)
=
\binom{2j}{r}p(t)^r[1-p(t)]^{2j-r},
\qquad r=0,\ldots,2j.
}
\]

At resonance,
\[
p(t)=\sin^2\frac{|g|t}{2},
\]
recovering the previously checked \(j=1\) and \(j=3/2\) formulas.

The detuning ceiling is
\[
\boxed{
P_{-j\to+j}^{\max}
=
\left(\frac{g^2}{\Delta^2+g^2}\right)^{2j}.
}
\]

Guardrail: the binomial law is the symmetric-power law of one SU(2) rotation, not a model of independent physical edge transitions.

## 3. Linear polarization versus exact circular drive

For a linearly polarized transverse field
\[
B_x=B_1\cos\omega t,\qquad B_y=0,
\]
the field decomposes into equal co-rotating and counter-rotating circular components, each of amplitude \(B_1/2\).

In the same rotating frame the exact Hamiltonian is
\[
\boxed{
H_{\rm lin}(t)
=
-\Delta J_z
-\frac{g}{2}J_x
-\frac{g}{4}
\left(e^{2i\omega t}J_+ + e^{-2i\omega t}J_-\right).
}
\]

The near-resonant RWA drops the fast \(2\omega\) term:
\[
\boxed{
H_{\rm RWA}
=
-\Delta J_z-\frac{g}{2}J_x.
}
\]

Thus, for equal peak field \(B_1\), the resonant edge Rabi scale is
\[
\boxed{
\Omega_{R,q}^{\rm circ}=|g|Y_q,
\qquad
\Omega_{R,q}^{\rm lin,RWA}=\frac{|g|Y_q}{2}.
}
\]

The factor of two comes from the fact that a real linear field contains two circular helicities and only one is co-rotating near resonance.

The cone-derived path shape \(Y_q\) is unchanged; polarization rescales its common coefficient.

## 4. Numerical exact-versus-RWA scan to preserve

The long thread numerically compared the exact linearly driven dynamics with the RWA at bare resonance
\[
\omega=\Omega_0=1,\qquad \Delta=0,
\]
for
\[
\epsilon=|g|/\omega=0.02,\ 0.05,\ 0.10,\ 0.20
\]
and \(j=1/2,1,3/2\), starting from the lowest-weight state and following one nominal RWA inversion time
\[
T_\pi=\frac{2\pi}{|g|}.
\]

The reported scan found:
- maximum instantaneous population discrepancy \(E_{\rm pop}^{\max}=O(\epsilon)\);
- gauge-fixed multiplet phase spread at \(T_\pi/2\) approximately
\[
\boxed{
\Delta\phi_j(T_\pi/2)
\simeq
\frac{j}{4}\epsilon;
}
\]
- nominal inversion infidelity approximately
\[
\boxed{
1-P_{-j\to+j}(T_\pi)
\simeq
\frac{j}{32}\epsilon^2.
}
\]

Representative reported values:

| epsilon | j | max population error | phase spread at T_pi/2 | inversion infidelity |
|---:|---:|---:|---:|---:|
| 0.02 | 1/2 | 0.2496% | 0.002500 | 6.25e-6 |
| 0.02 | 1 | 0.3247% | 0.005000 | 1.25e-5 |
| 0.02 | 3/2 | 0.3884% | 0.007500 | 1.88e-5 |
| 0.05 | 1/2 | 0.6250% | 0.006251 | 3.91e-5 |
| 0.05 | 1 | 0.8147% | 0.012502 | 7.82e-5 |
| 0.05 | 3/2 | 0.9748% | 0.018752 | 1.17e-4 |
| 0.10 | 1/2 | 1.2492% | 0.012507 | 1.565e-4 |
| 0.10 | 1 | 1.6327% | 0.025013 | 3.129e-4 |
| 0.10 | 3/2 | 1.9631% | 0.037520 | 4.694e-4 |
| 0.20 | 1/2 | 2.4871% | 0.025053 | 6.288e-4 |
| 0.20 | 1 | 3.2959% | 0.050106 | 1.257e-3 |
| 0.20 | 3/2 | 3.9237% | 0.075159 | 1.885e-3 |

IMPORTANT STATUS GUARDRAIL: these numerical values were produced in the conversation and were not accompanied by a repository-side reproducible script/certificate in this checkpoint. Treat them as empirical observations to be independently recomputed before promotion to certified numerical data.

## 5. Floquet/Magnus derivation reached immediately before this checkpoint

At bare resonance write
\[
H(t)=H_0+V(t),
\qquad
H_0=-\frac g2J_x,
\]
\[
V(t)=
-\frac g4
\left(e^{2i\omega t}J_+ + e^{-2i\omega t}J_-\right).
\]

The fast frequency is
\[
\nu=2\omega,
\]
with Fourier components
\[
H_{+1}=-\frac g4J_+,
\qquad
H_{-1}=-\frac g4J_-.
\]

Using \([J_+,J_-]=2J_z\), the first high-frequency commutator gives, in the convention used in the thread,
\[
\boxed{
H_F
=
-\frac g2J_x
+
\frac{g^2}{16\omega}J_z
+
O\left(\frac{g^3}{\omega^2}\right).
}
\]

The thread then interpreted the corresponding slow-axis tilt as
\[
\boxed{
|\eta|=\frac{|g|}{8\omega}+\cdots
}
\]
relative to the RWA transverse coefficient \(|g|/2\).

This gives the observed leading phase spread
\[
\boxed{
\Delta\phi_j(T_\pi/2)
=
2j|\eta|
=
\frac{j}{4}\frac{|g|}{\omega}
+\cdots
}
\]
and, using the extremal symmetric-power relation,
\[
P_j^{\rm inv}=(P_{1/2}^{\rm inv})^{2j},
\]
the leading inversion infidelity
\[
\boxed{
1-P_{-j\to+j}(T_\pi)
=
2j\eta^2+\cdots
=
\frac{j}{32}
\left(\frac{g}{\omega}\right)^2
+\cdots .
}
\]

The same discussion attributed the \(O(g/\omega)\) maximum population discrepancy during the pulse to fast \(2\omega\) micromotion.

## 6. Critical re-audit requirement for the fresh thread

The Floquet/Magnus section above is a handoff of the derivation reached in conversation, NOT yet a fully independently certified ledger theorem.

Before promoting its coefficients as exact asymptotic statements, the fresh thread should independently rederive:
1. the Fourier-component sign/order convention in the first Floquet term;
2. the first kick/micromotion operator and its Floquet-gauge dependence;
3. how the kick and effective Hamiltonian combine at the specific observation times \(T_\pi/2\) and \(T_\pi\);
4. the claimed remainder orders, especially whether the inversion remainder is correctly \(O(\epsilon^4)\) or whether an \(O(\epsilon^3)\) term can occur under the chosen timing/gauge convention;
5. the numerical scan with an explicit reproducible integration script.

Do not promote the \(j/4\) and \(j/32\) coefficients beyond checkpoint status until that independent re-audit is complete.

## 7. Exact SU(2) structural fact that should guide the continuation

Even with the exact linearly polarized time-dependent field,
\[
H(t)=\mathbf h(t)\cdot\mathbf J.
\]

Therefore the time-ordered propagator remains the spin-j representation of a single fundamental SU(2) propagator:
\[
\boxed{
U_j(t)=D^{(j)}[U_{1/2}(t)].
}
\]

Thus higher-j errors are not independent edge errors. Once the exact fundamental error rotation is known, the \(j=1\) and \(j=3/2\) behavior follows by representation theory. In particular, for extremal transfer,
\[
\boxed{
P_j=(P_{1/2})^{2j}.
}
\]

This structural fact is the safest route for the next audit.

## 8. Recommended first task in the new chat

Start by reading this checkpoint and the relevant prior magnetic-driver ledger entries (v13.595 and v13.598), then check the live ledger for later collisions.

Next perform an independent Floquet/Magnus re-audit of the exact linear-drive Hamiltonian. Derive the effective Hamiltonian and kick operator with one fixed convention, explicitly evaluate the physical propagator at \(T_\pi/2\) and \(T_\pi\), and test the resulting asymptotic coefficients against a fresh numerical integration for \(\epsilon=0.02,0.05,0.1,0.2\).

Only after that check should the numerical scan and coefficients be promoted from checkpoint observations to certified magnetic-driver results.
