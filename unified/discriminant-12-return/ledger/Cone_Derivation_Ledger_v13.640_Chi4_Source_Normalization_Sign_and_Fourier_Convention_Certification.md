# Cone Derivation Ledger v13.640 — chi_-4 Source-Normalization Sign and Fourier-Convention Certification

Date: 2026-09-21

Status: exact convention audit for the frozen primitive chi_-4 screw-function formula. This closes the source-normalization blocker identified in v13.635/v13.637, conditional only on using Suzuki's stated Fourier convention for the Weil distribution.

## 0. Live collision/relevance check

The live ledger was checked immediately before this write. It has advanced through v13.639. v13.638 is an audit addendum about an analog-simulation question and v13.639 is magnetic-driver work; neither collides with this chi_-4 source-normalization gate. This entry therefore takes v13.640.

## 1. Suzuki convention that fixes the global sign

Suzuki's screw-function convention satisfies, distributionally,
[
-g''(t)=W(t),
]
where W is the Weil distribution, and for a test function phi,
[
int (-g(t))phi''(t),dt=W(phi).
]

This fixes the sign that cannot be determined by merely differentiating the Lerch antiderivative internally. In Suzuki's explicit zeta formula the prime-power ramp enters g with a PLUS sign:
[
+sum_{nle e^{|t|}}rac{Lambda(n)}{sqrt n}(|t|-log n),
]
while the archimedean linear and Lerch pieces enter with the signs displayed in Eq. (1.3). The pole contribution is the separate zeta-specific elementary term.

For a primitive nonprincipal Dirichlet L-function, the same explicit-formula convention replaces the Euler-product coefficient by chi(n)Lambda(n)/sqrt(n), replaces the completed gamma/conductor factor appropriately, and removes the zeta pole term because L(s,chi) is entire.

## 2. Completed chi_-4 factor

For the primitive odd real character modulo 4,
[
L(s,chi_{-4})=beta(s),qquad q=4,qquad a_chi=1.
]
A standard completed factor is
[
Lambda(s,chi_{-4})=
left(rac{4}{pi}ight)^{(s+1)/2}
Gamma!left(rac{s+1}{2}ight)eta(s)
]
(up to an s-independent normalization, irrelevant to the logarithmic derivative).

On the critical line s=1/2+iz the gamma argument is
[
rac{s+1}{2}=rac34+rac{iz}{2}.
]
Hence the completed logarithmic derivative contributes
[
rac12lograc4pi+rac12psi!left(rac34+rac{iz}{2}ight).
]

Therefore the frozen linear coefficient is forced to be
[
-rac{|t|}{2}left[psi(3/4)+log(4/pi)ight].
]

## 3. Euler-product term

For Re(s)>1,
[
-rac{eta'}{eta}(s)
=sum_{nge1}rac{chi_{-4}(n)Lambda(n)}{n^s}.
]
With the critical-line centering n^{-1/2}, twice integration of the corresponding delta masses gives
[
+sum_{nle e^{|t|}}
rac{chi_{-4}(n)Lambda(n)}{sqrt n}
(|t|-log n).
]
The PLUS sign agrees with Suzuki's global convention -g''=W.

Because beta(s) is entire, there is no analogue of Suzuki's zeta pole term
[
-4(e^{t/2}+e^{-t/2}-2).
]

## 4. Gamma/Lerch term and exponential

Set a=3/4 and T=|t|. The gamma kernel expands as
[
rac{e^{-2aT}}{1-e^{-2T}}=sum_{mge0}e^{-2(m+a)T}.
]
The twice-integrated term normalized to vanish at T=0 is
[
L_a(T)=-rac14left[
Phi(1,2,a)-e^{-2aT}Phi(e^{-2T},2,a)
ight].
]
Indeed,
[
L_a''(T)=rac{e^{-2aT}}{1-e^{-2T}},
]
so for a=3/4 the exponential is exactly
[
e^{-2aT}=e^{-3T/2}.
]

The factor -1/4 follows from integrating exp[-2(m+a)T] twice: each mode contributes 1/[4(m+a)^2]. The subtraction at T=0 fixes g(0)=0 in this sector.

Thus the frozen archimedean term is exactly
[
-rac14left[
Phi(1,2,3/4)-e^{-3T/2}Phi(e^{-2T},2,3/4)
ight].
]

## 5. Certified frozen formula

Combining Sections 1-4 gives
[
oxed{
g_{-4}(t)=
sum_{nle e^T}rac{chi_{-4}(n)Lambda(n)}{sqrt n}(T-log n)
-rac{T}{2}left[psi(3/4)+log(4/pi)ight]
-rac14left[Phi(1,2,3/4)-e^{-3T/2}Phi(e^{-2T},2,3/4)ight],
quad T=|t|.
}
]

This matches the frozen implementation in
research-notes/suzuki_chi4_zeeman_kernel_compression.py coefficient-for-coefficient:
- prime-power sign: PASS;
- chi_-4 twist: PASS;
- n^{-1/2} centering: PASS;
- no pole term: PASS;
- gamma parameter 3/4: PASS;
- conductor/gamma linear coefficient: PASS;
- Lerch prefactor -1/4: PASS;
- Lerch sign: PASS;
- exponential e^{-3T/2}: PASS;
- normalization g(0)=0: PASS.

## 6. Scope

This certifies the source formula in the Suzuki/Weil Fourier-sign convention; it does not prove RH, beta-zero convergence, or the correctness of any finite-A arithmetic identification. The negative finite-A results v13.620/v13.627 remain unchanged.

The blocker identified in v13.635/v13.637 is now closed. The next admissible chi_-4 gate is to DERIVE the free/endpoint factor or relative Fredholm characteristic before testing any A-robustness of a renormalized object. A numerical quotient W_full/W_free should not be promoted before that derivation.
