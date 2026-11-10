# Cone Derivation Ledger v15.599 — Lane A: null-target geometric selector, parity check, and oscillator amplitude obstruction

**Date:** 2026-11-10. **Parents:** v15.180 boundary staircase, v15.572–574 open-quarter structure, v15.595–598 cross-shell mapping, Paper C v1.1, Casimir Null Diamond v2.1. **Status:** [D] exact auxiliary Fock algebra; [C] null target as candidate geometric selection criterion; [O] physical interaction, field coupling and AM–GM normalization. **Live prewrite HEAD** d349d3ad3273d63b76acd88ed44a0b504573a119; no v15.599 collision. **Additive-only**, no Suzuki frozen/production modification.

## Gate 58: exact null-target projection

On auxiliary Fock states |a,b> with nonnegative integer occupations N=a+b=4j, the proposed minimal quartics O+=(a†)^3 b and O-=(b†)^3 a have coordinate changes (+3,-1) and (-1,+3). Define P_null on the destination tower by the condition a'=0 or b'=0. At a fixed source N, P_null O+ P_N acts only on the single source |N-1,1>, sending it to |N+2,0>; P_null O- P_N acts only on |1,N-1>, sending it to |0,N+2>. Hence the **target** null-axis geometry supplies the precise boundary support that was previously imposed with P_(b=1) and P_(a=1). This is an identity conditional on selecting P_null as final-state criterion; neither the quartic Hamiltonian nor the null-cone paper establishes dynamical projection to the null axis. The auxiliary occupation axes should not be silently identified with physical lightlike trajectories or Paper C's shifted factor dictionary.

For N odd the two sources are distinct, matching the two odd-quarter boundary legs of T_j (v15.595). For N=2 they COINCIDE in |1,1> but land at distinct orthogonal targets; therefore one cannot claim a rank-two source projector for all even N. This is consistent with the existing even-shell 'closed particle chain plus open companion' decomposition, rather than proof of odd-quarter exclusivity.

## Gate 59: boundary selection does not single out odd quarters, and does not fix amplitude

The exact null-target condition also holds for every even N. Thus the boundary condition by itself does not discriminate odd-quarter from even-class shells. The quartic operators change total occupation by +2 and hence preserve N mod 2, but no preference for a parity is derived.

For either leg from a source of total N, the raw squared Fock matrix element is N(N+1)(N+2). The old-shell odd-quarter missing-edge AM–GM squared amplitude is c=(N+1)/4. The norm-rescaling needed to match is 1/[2 sqrt(N(N+2))], which varies with N. Projecting to the null destination removes interior transitions but does **not** create that normalization. The selected-normalized W_± of v15.598 still requires spectral number-dependent factors; no physical canonical coupling has been sourced.

## Falsifiable scope / remaining selectors

The null boundary is a meaningful geometric *postselection* of the auxiliary quartic process. It does not yet establish a dynamical absorption/emission mechanism. To advance, exhibit an already-defined cone Hamiltonian, constraint, or conserved charge that physically restricts the final Hilbert space to the null axis, and separately derive the relative amplitude normalization. Alternatively record a hard negative result for that class. The existing transition-state staircase of v15.180 already gives geometric incidence of boundary points but no such coupling selector. Nothing here proves actual photons, gravity, an intrinsic chirality choice, a new G value or a Suzuki intertwiner.

**Verification:** independent rational/integer Fock-number enumeration for N=1 through 11, both odd and even, checks exact two null-directed legs per shell, source labels, amplitude ratio c, and N=2 shared-source subtlety. Reproducer in response archive cone_null_selector_gates_58_59.zip.

**HANDOFF:** external-audit; type null-target boundary projector test; status open; verify P_null O± P_N support, even-N counterexample to odd-quarter uniqueness, N=2 rank subtlety, raw amplitude and N-dependent normalization; assess whether the null-target projection or oscillator realization has been inadvertently promoted to a dynamical law. Frozen Suzuki work unchanged.
