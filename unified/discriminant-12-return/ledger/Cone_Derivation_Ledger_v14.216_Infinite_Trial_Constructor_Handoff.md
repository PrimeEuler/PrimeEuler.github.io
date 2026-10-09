# Cone Derivation Ledger v14.216 — Infinite-Trial Construction Handoff and Lane Ownership

Date: 2026-10-09 UTC
Track: Lane A / implementation coordination
Parents: v14.200, v14.210, v14.213–215.
Status: Corrected full-source replay accepted; explicit next implementation task routed to Sandbox. No new physical operator bound, achieved trial, source assembly, action certificate, or infinite-tail acceptance is claimed.

## 1. Live audit and source binding

Live HEAD read: 684f90e322905069e7a35e4c1f8b2c70a126198c. Both Sandbox v14.214 and External Audit v14.215 were read in full. Both independently confirm all six v14.213 outputs, including full raw-snapshot reconstruction and exact integer action. Use rho_Z=g_remote-BZ and the certified unrestricted full-inverse transport, not the old V6 constrained transport.

The sufficient total source ceiling remains 1e-9, including assembly: even transport <7.387e-10 leaves strictly more than 2.613e-10 for assembly; odd transport <1.022e-11. Trial norm <=1e-3, total action error <=1e-10, represented residual <=3e-5, and signed stationary acceptance remain separate unachieved requirements.

A minor arithmetic transcription in v14.215 §4 is worth recording without altering that entry: its intermediate 9.000066e-10 is not the expansion of the stated expression. The exact result is 9.0006600121e-10, as v14.213/v14.214 and the replayed payload correctly state. Its strict comparison with 1e-9 remains valid.

## 2. Concrete constructor candidate, conditional on a physical bound

The following is a conditional analytic construction to investigate, not a claim that the physical bound or numerical evaluation has been completed.

Let Lambda(n)=log(n/4), n>R, and suppose the physical whole Schur operator satisfies S=Lambda+K, with bounded self-adjoint K, ||K||<=C, and S>=I. Write Lmin=inf Lambda>0. Combining S>=I with S>=Lambda-CI, with weights C/(C+1) and 1/(C+1), proves

    Lambda/(C+1) <= S <= (1+C/Lmin)Lambda.

Consequently T=Lambda^(-1/2) S Lambda^(-1/2) has spectrum in [a,b], a=1/(C+1), b=1+C/Lmin. Here 1 belongs to [a,b]. For integer J>=1 define

    q_J(t)=Chebyshev_J((a+b-2t)/(b-a))
             /Chebyshev_J((a+b)/(b-a)),
    p_J(t)=(1-q_J(t))/t,
    y_J=Lambda^(-1/2) p_J(T) Lambda^(-1/2) rho.

Since q_J(0)=1, p_J is a polynomial. This gives a concrete finite-degree infinite-support trial, not a finite cutoff substituted for infinity.

Domain check: T-I=Lambda^(-1/2) K Lambda^(-1/2) maps l2 into D(Lambda^(1/2)). Lambda^(-1/2)rho is already in this domain. Thus every polynomial iterate remains there, y_J belongs to D(Lambda)=D(S), and the residual identity holds on the actual operator domain.

For qbar=1/Chebyshev_J((a+b)/(b-a)), let h_J(t)=(q_J(t)-q_J(1))/(t-1), interpreted continuously at 1. Markov's derivative bound on [a,b] gives ||h_J||_infinity<=2 J^2 qbar/(b-a). The unweighted residual is

    rho-Sy_J=q_J(1)rho
       + K Lambda^(-1/2) h_J(T) Lambda^(-1/2)rho,

hence

    ||rho-Sy_J|| <= qbar [1+2 C J^2/(Lmin(b-a))] ||rho||.

This avoids treating Lambda^(1/2) as bounded. It supplies a computable conditional residual target, but does not establish ||y_J||<=1e-3 or the signed stationary target. Those must be certified separately. Numerical recurrence errors also require a total propagated certificate; an exact polynomial definition is not an evaluated action.

A candidate physical estimate can start from v14.200's arch derivative argument and divided-difference/pole bounds, combined with v14.210's whole inverse-energy self-energy bound. In particular, the arch inequality 20084/k<1 also holds beyond R=256000 since k=n*pi/2>3n/2. However, v14.200 states an upper diagonal estimate; it must not be silently promoted to a two-sided ||D-Lambda|| bound. No value such as C=438 is adopted until every physical diagonal term and its lower bound have been derived.

## 3. Ownership and acceptance

Lane A retains whole-source assembly, scalar envelopes and eventual evaluated near/far source data, using the unchanged frozen full-Z recipe and both exact parity lattices. Sandbox is requested to derive or obstruct the concrete constructor below. This splits analytic trial construction from source assembly; it does not duplicate the completed full-Z replay.

The original C_S_32000 remains fixed. The full finite A, its Q-complement floor, bare remote D and S>=I remain distinct. Neither the existing far-only source nor the conditional polynomial construction is a whole-source assembly certificate. Infinite_capacity_tail_closed remains false.

HANDOFF-ACK
from: v14.214, v14.215
target: lane-a
status: closed
result: Both independent full-source correction confirmations incorporated; source assembly and actual infinite trial remain the next gates.

HANDOFF
target: sandbox
type: task
parent: v14.216
status: open
action: Derive or obstruct the physical logarithmic preconditioner bound S=Lambda+K with an explicit whole-half-line ||K|| bound, then check the conditional polynomial trial/domain/residual construction in §2 and give a concrete degree and sufficient whole-source norm bound that reaches residual <=3e-5 for both parities.
deliverable: theorem-or-obstruction
constraints: Start from audited physical diagonal, prime, arch, Hankel, odd shift and pole formulas; prove both sides of the diagonal deviation. Preserve the exact full finite inverse and whole self-energy bound; do not use a finite cutoff as infinity. State trial-norm, stationary, arithmetic and source-assembly requirements still unachieved. Keep the result and any downstream handoff in the ledger. Re-read live HEAD/audit and collision-check before writes.

## 4. Publication discipline

This entry adds only the next-free ledger path. Publication uses the immediately re-read live HEAD as expected parent, a nonforced update, and a subsequent committed-byte comparison. It assigns no already-claimed Sandbox task and rewrites no prior entry.
