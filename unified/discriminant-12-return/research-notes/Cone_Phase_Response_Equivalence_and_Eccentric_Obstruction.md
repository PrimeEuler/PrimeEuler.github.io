# Gravity lane — cone phase-response equivalence and the eccentric-family obstruction

*Dedicated gravity lane, 2026-10-22. Parents: v14.680–681, v14.696–700. Producer: \`cone_phase_response_obstruction.py\`.*

This gate asks whether the **actual phase-integral construction** can produce a gravity response that is not already ordinary SO(3), and whether the eccentric deformation of v14.696/698 supplies a physical escape route.

Nothing here derives \(G\). The separatrix logarithm and apex/initial-seat ideas remain separate hypotheses.

## 1. \(\rho=1\): the phase-integral states are the standard angular states up to normalization and rephasing [D]

v14.696 closed the rephasing caveat with

\[
I_{jm}(\theta)
=
(-i)^m\frac{j!}{(j+m)!}P_j^m(\cos\theta)
\]

for the standard harmonic identification (with the audit extending the check to negative \(m\)).

Attach the usual azimuthal factor \(e^{im\phi}\). Then the full cone-generated angular function is

\[
\Psi_{jm}^{\rm cone}(\theta,\phi)
=
A_{jm}(-i)^m P_j^m(\cos\theta)e^{im\phi},
\]

with \(A_{jm}=j!/(j+m)!\) times the conventional normalization conversion.

After normalizing each state, the positive statewise amplitude disappears. What remains is only the phase

\[
(-i)^m=e^{-im\pi/2}.
\]

Thus

\[
|\widehat\Psi_{jm}^{\rm cone}\rangle
=
e^{-im\pi/2}|Y_{jm}\rangle
\]

up to the fixed normalization convention.

This is a diagonal unitary rephasing,
\[
U=e^{-i(\pi/2)J_z/\hbar},
\]
i.e. the phase of a quarter-turn about the quantization axis.

Therefore any operator, Hamiltonian, resolvent, or response function transformed consistently with the state identification is unitarily equivalent to the standard spherical-harmonic theory:

\[
H_{\rm cone}=U H_{\rm std}U^\dagger,
\qquad
O_{\rm cone}=U O_{\rm std}U^\dagger.
\]

So spectra, transition probabilities, static susceptibilities, and all basis-invariant observables are unchanged.

**Obstruction:** the \(\rho=1\) phase integral cannot by itself generate a new rank-1/rank-2 gravitational or tidal observable. It exactly reconstructs the standard angular Hilbert-space rays.

This strengthens v14.700: the negative novelty result is not merely an artifact of having chosen an ordinary rigid-rotor Hamiltonian. Once the v14.680/v14.696 harmonic identification is taken literally as a state identification, its angular response is standard theory by unitary equivalence.

## 2. \(\rho\neq1\): the eccentric family is genuinely deformed but is not orthogonal in the standard spherical metric [D/N]

The v14.698-corrected eccentric family is

\[
I_{jm}(\theta;\rho)
=
\frac1{2\pi}
\int_0^{2\pi}
e^{-im\chi}
\left(\cos\theta+i\rho\sin\theta\cos\chi\right)^j
\,d\chi,
\]

with
\[
\rho=\sqrt{\frac{1-e}{1+e}}.
\]

For \(\rho=1\), this is the standard associated-Legendre state above. For \(\rho\neq1\), v14.698 correctly found a state-dependent taxonomy: some states are invariant, some only rescale, and some genuinely change shape.

The first exact orthogonality witness is already at \(m=0\):

\[
I_{00}=1,
\]

\[
I_{20}
=
\left(1+\frac{\rho^2}{2}\right)x^2-\frac{\rho^2}{2},
\qquad x=\cos\theta.
\]

Using the standard spherical inner product (common \(2\pi\) azimuthal factor omitted),

\[
\langle I_{00},I_{20}\rangle
=
\int_{-1}^{1}I_{20}(x)\,dx
=
\boxed{\frac23(1-\rho^2)}.
\]

Hence the states are orthogonal only at \(\rho=1\). At the v14.698 example \(\rho=0.5\),

\[
\langle I_{00},I_{20}\rangle=\frac12.
\]

The producer verifies this exact formula and computes normalized Gram matrices through \(j=6\). At \(\rho=1\), the off-diagonal Gram residual is at quadrature roundoff (\(\sim10^{-14}\)); at \(\rho=0.8\) and \(0.5\), large off-diagonal overlaps appear for \(m=0,1,2\).

This is not a numerical accident.

## 3. Why orthogonalization collapses the deformation back toward standard harmonics [D]

For fixed \(m\ge0\), the Fourier-moment expansion shows

\[
I_{jm}(x;\rho)
=
(1-x^2)^{m/2}
\times
\left[\text{polynomial of degree }j-m\text{ with the usual parity}\right]
\]

for any \(\rho>0\).

Thus, for fixed \(m\), the eccentric functions form a triangular basis of the same polynomial flag spanned by the associated Legendre functions \(P_j^m(x)\).

Under the **standard spherical inner product**, Gram-Schmidt orthogonalization of that flag returns the unique associated-Legendre orthogonal family (up to normalization/sign). So if one insists that the eccentric functions are energy eigenstates of a self-adjoint angular Hamiltonian in the ordinary \(L^2(S^2)\) metric, orthogonalizing them removes the deformation and recovers the standard harmonic basis.

Therefore a physically distinct \(\rho\neq1\) response theory requires at least one genuinely new ingredient:
- a nonstandard \(\rho\)-dependent inner product/metric;
- a self-adjoint Hamiltonian whose eigenstates are not simply the raw \(I_{jm}\);
- a different observable map in which the \(I_{jm}\) are not being interpreted as orthogonal stationary states;
- or an explicitly open/non-Hermitian/coherent-state interpretation.

None of those structures is supplied by v14.696/698.

## 4. Consequence for the gravity objective [I/P]

The eccentric deformation remains mathematically interesting and is the only current route in this arc that is not immediately a pure SO(3) re-expression.

But it does **not yet produce a physical gravitational prediction**. Before using \(\rho\) to alter the rank-1/rank-2 response, the program must justify what physical object \(I_{jm}(\rho)\) is:
- an eigenstate,
- a coherent/nonorthogonal state,
- a response kernel,
- a classical orbit transform,
- or something else.

Until that is fixed, inserting the eccentric family into a gravitational Hamiltonian would amount to choosing the desired deformation rather than deriving it.

## 5. Separatrix logarithm and apex seat remain separate

The elliptic separatrix asymptotic

\[
K(e)\sim\frac12\ln\frac{16}{1-e^2}
\]

remains a valid mathematical identity. This gate does not challenge that identity.

What remains unestablished is the physical step connecting the eccentricity \(e\) of this phase-integral family to a gravitational/cosmological degree of freedom that controls an experimentally measurable rotor response.

Likewise, the apex/initial-seat construction remains an interpretive initial-condition hypothesis. No Hilbert-space argument here fixes that seat or turns it into a coupling constant.

## 6. Verdict

**Mathematical identity [D]:**
At \(\rho=1\), the phase-integral states are normalized standard spherical harmonics up to the unitary phase \(e^{-im\pi/2}\).

**Numerical/analytic obstruction [D/N]:**
At \(\rho\neq1\), the raw eccentric family is not orthogonal in the standard spherical inner product; the exact witness is
\[
\langle I_{00},I_{20}\rangle=\frac23(1-\rho^2).
\]

**Interpretation [I]:**
The eccentric family may still encode useful classical/response geometry, but it cannot yet be treated as a new stationary quantum basis without extra physics.

**Physical-prediction status [P]:**
No new gravitational/tidal observable follows from the phase integral alone. Any new prediction must enter through a physically justified \(\rho\)-dependent dynamics, metric, coupling, or state interpretation.

## 7. Next gate

The next mathematical gate is now sharply posed:

> Can the eccentric phase-integral family be obtained as the eigenstates or response kernel of a self-adjoint operator derived from Cone geometry, with a physically fixed inner product and with \(\rho\) determined dynamically rather than inserted?

A successful construction must:
1. specify the Hilbert space and inner product;
2. produce the \(\rho\)-family from an operator or variational principle;
3. recover \(\rho=1\) as the standard harmonic limit;
4. yield an observable correction not removable by a unitary/basis transformation;
5. connect \(\rho\) to a gravitational source without inserting the measured value of \(G\).

Absent that, the eccentric/separatrix route remains a mathematically suggestive but physically unclosed hypothesis.
