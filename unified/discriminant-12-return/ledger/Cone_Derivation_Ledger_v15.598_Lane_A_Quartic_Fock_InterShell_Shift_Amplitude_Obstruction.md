# Cone Derivation Ledger v15.598 — Lane A: quartic oscillator candidate for odd-quarter cross-shell boundary shifts; exact amplitude/selector obstruction

**Date:** 2026-11-10. **Parents:** Paper C v1.1; v13.583, v14.865–868, v15.572–574, v15.595–597 (External Audit Round 520 confirmed v15.595–596 without corrections). **Status:** [D] exact normal-ordered bosonic algebra in explicitly chosen auxiliary embedding; [C] energy interpretation within that oscillator model; [O] physical/canonical identification, coupling, unique coefficient and boundary selection. **Prewrite HEAD:** 287001d0a92ad2000865f823d9e77b7f46a01ad4. No v15.598 path collision. Additive only; frozen Suzuki and far-tail production untouched.

## 1. A chosen doubled-number embedding, not the native Paper-C dictionary

For a refined shell j=N/4 (N positive integer), basis m_i=-j+i/2, i=0,...,N, choose an auxiliary Fock embedding |j,m_i> -> |n_a=i,n_b=N-i>. This gives n_a=2(j+m), n_b=2(j-m), n_a+n_b=4j=N. Under its ordinary Schwinger SU(2) action, the actual spin is N/2=2j, which is the **different, closed half-step** construction of v15.574, not an identification of the original defective step-one spin-j ladder with a physical Fock multiplet. In particular this is NOT automatically Paper C's shift x=n1+1,y=n2.

At the upper open endpoint of any odd-quarter j=N/4 with N odd, source m=j-1/2 has (n_a,n_b)=(N-1,1) and the v15.595 next-shell destination m'=j+1/2 in j'=j+1/2 has (n'_a,n'_b)=(N+2,0). Their number change is (+3,-1), with the mirror branch (-1,+3).

## 2. Minimal bosonic word and oscillator energy [D/C]

The lowest-degree normally ordered monomial with (+3,-1) weight is O_+=(a†)^3 b (degree 4), with O_-=(b†)^3 a. For the auxiliary harmonic Hosc=ℏω(N_a+N_b+1), exactly

[Hosc,O_+]=2ℏω O_+, [Hosc,O_-]=2ℏω O_-.

The adjoints reverse that energy. This is a definite **oscillator-model** energy gap, not an independently derived physical energy of the original quarter-shell. O_± change total number by 2, preserving its parity. Ordinary Schwinger J_± preserve total number; Gaussian quadratic generators (including Paper C's SU(1,1) squeezing generators) have no direct (+3,-1) matrix element. Their Lie commutators stay quadratic. Products/sequences can reach this endpoint, so the obstruction concerns **one quadratic generator**, not all Gaussian-unitary multi-step amplitudes.

For example J_+² K_+ = (a†)^3 b²b†, with J_+=a†b and K_+=a†b†; on source n_b=1, this acts like 2(a†)^3 b, showing a composite quadratic route exists but its amplitude is neither independent of occupations nor the required boundary weight.

## 3. Nontrivial normalization and boundary support obstruction [D]

At upper source |n_a=N-1,n_b=1>, the unnormalized monomial has squared amplitude

||O_+|N-1,1>||²=N(N+1)(N+2).

The exact old-shell AM–GM missing-edge target is c=j+1/4=(N+1)/4, because T_j†T_j=2E_j (v15.595–597). The required squared normalization is

c/[N(N+1)(N+2)]=1/[4N(N+2)],

which varies with N. A single universal constant cannot match T_j for all odd-quarter shells.

An explicit but **chosen** exact normalization/projector realization on this auxiliary tower is

W_+=(a†)^3b [2sqrt((N_a+1)(N_a+3))]^{-1} P_(N_b=1) P_(N_a+N_b odd),

with its mirror W_-=(b†)^3a [2sqrt((N_b+1)(N_b+3))]^{-1}P_(N_a=1)P_(N_a+N_b odd), where rightmost factors act first. The restriction to odd occupation number and to a single quantum in the depleted mode reproduces precisely the two endpoint legs of T_j at every odd N, and W†W=2E as a direct-sum identity on that selected sector. These non-polynomial spectral functions/projectors are **added selectors**, not derived from the quadratic oscillator algebra. Without them O_± also act on interior states and on different occupation sectors; no exact unique edge map follows simply from the monomial's shift.

More generally a finite normally ordered polynomial with net (+3,-1) cannot be nonzero at n_b=1 and vanish at every n_b≥2 across an unbounded tower without non-polynomial filtering or an external energy/charge restriction: for any fixed allowed n_a, its amplitude divided by the universal bosonic falling/rising factors is polynomial in n_b, and a nonzero polynomial cannot have infinitely many roots.

## 4. Consequences and handoff

Positive: a minimal *non-Gaussian quartic* monomial supplies the right direction, oscillator total-number change, and a definite conditional 2ℏω energy. Negative: the existing quadratic Schwinger/squeezing Lie generators do not alone give this direct jump; raw amplitude grows as sqrt(N(N+1)(N+2)), not sqrt((N+1)/4); boundary-only action and exact normalization require added selectors. The fact that the oscillator construction works after selecting projectors does not make the original v15.595 T a canonical physical absorption/emission operator, and supplies no electromagnetic photon, actual source field, chirality, mass law or G.

Reproducer: exact rational verification over odd N=1,3,5,7,9,11,13, in Gate 56–57 response archive cone_inter_shell_oscillator_gate56_57.zip. No project production changes.

**Next discriminating gate:** examine whether the existing cone parity/null-row-col boundary operators already enforce the single-quantum spectator condition P_(N_b=1) and its mirror, and whether any established Hamiltonian dynamically excludes the interior transitions. If not, record the failure of the proposed operator's canonicity explicitly.

**HANDOFF** target external-audit; type oscillator quartic candidate and obstruction; status open; verify number-shift uniqueness (lowest degree), [Hosc,O], exact N-dependent squared amplitude/normalization, composite J_+²K_+ ordering, the auxiliary embedding's distinction from native Paper C, and projector-dependence of endpoint support. Frozen Suzuki untouched.
