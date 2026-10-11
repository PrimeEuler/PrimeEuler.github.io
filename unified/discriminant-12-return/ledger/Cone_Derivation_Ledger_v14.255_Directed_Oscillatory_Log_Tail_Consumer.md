# Cone Derivation Ledger v14.255 — Directed Oscillatory Log-Tail Scalar Consumer

Date: 2026-10-10
Track: Lane A
Status: [V] evaluated directed scalar primitives; [O] zero-frequency primitive and complete infinite RHS/action assembly.
Parents: v14.250, v14.253–254.

Read live HEAD 7dcd2962adab080c90ff3fda54cfe4f7b92c9614 before this gate; no newer ledger response was present. Immediately before publication, recheck HEAD, ledger number and all new paths. The immediate pre-publication check detected External Audit v14.254 at HEAD 65b337aab6359f35a3fa4760102624e633b7767e; that entry was read in full and this new gate renumbered to v14.255 before any write. It independently confirms v14.253 and explicitly retracts the earlier structural-obstruction inference. This is additive work under the user's authorization to continue gates without waiting for another prompt.

## Scalar primitive

For a≥512001, integer p≥2 and nonzero prime-frequency vector v, evaluate

F_p(theta,a)=sum_{k≥0} exp(i*theta*(a+2k))*(a/(a+2k))^p/log((a+2k)/4),
theta=(pi/2)*sum_{r in {2,3,5,7}} v_r*log(r).

The n^-p normalization has been moved into (a/n)^p for stable coefficient representation. The q=4 physical prime term is represented by twice the log-2 frequency. These are mathematical oscillatory sums, with directed prime/log/pi phase intervals; no machine sine or quadrature is used.

## Convergent finite-difference expansion

Let q=exp(2i*theta), f_k=(a/(a+2k))^p/log((a+2k)/4), and Delta f_k=f_(k+1)−f_k. Summation by parts gives

sum q^k f_k = sum_{j<J} q^j*Delta^j f_0/(1−q)^(j+1)
               + q^J/(1−q)^J*sum q^k*Delta^J f_k.

The original primitive also contains the phase exp(i*theta*a). Every complex interval operation is rounded outward at 512 bits. Finite differences are formed from directed evaluations of the J initial f values. The final real/imaginary enclosures are rounded outward at 160 bits.

A complete remainder, not a numerical convergence guess, follows from complete monotonicity. For x>4,

f(x)=a^p*integral_0^infinity 4^t*x^(-p-t)dt.

Each x^(-p-t) is a positive Laplace mixture; so is f. On the step-two lattice Delta^J has sign (-1)^J in this positive mixture. For any unit q and 0≤r≤1, abs(1−q*r)≥abs(1−q)/2 (minimizing squared distance on the unit radial segment proves this directly). Consequently, with d a directed positive lower bound for abs(1−q),

abs(remainder) ≤ 2*abs(Delta^J f_0)/d^(J+1).

The derivative integral and the step-two difference integral give

abs(Delta^J f_0) ≤ (2/a)^J*sum_{k=0}^J binom(J,k)*(p+J)^(J−k)*k!/11^(k+1).

Indeed (p+t)_J≤(p+J+t)^J and log(a/4)>11; integrate the resulting polynomial against exp(−log(a/4)*t). The positive mixture justifies the interchange by Tonelli and supplies absolute convergence of the displayed oscillatory sums for p≥2. The computed remainder is rounded upward at 512 bits before serialization.

## Evaluated coverage and checks

The five prime frequencies (including twice log2) and all pairwise sums/differences produce 28 distinct nonzero frequencies up to sign. The negative frequencies follow by conjugation. The zero frequencies are excluded explicitly and need a separate consumer.

The new producer evaluates all 28 frequencies at both parity starts 512001/512002 and powers 2/128, using J=32: 112 directed cases. Every real and imaginary component has radius below 1e-40; the largest returned component radius is 2^-161 (approximately 3.422e-49). Each actual case records its directed chord lower bound and analytic remainder. This endpoint-power coverage does not claim the intermediate powers or all inverse moments have already been enumerated; the producer accepts arbitrary integer p≥2 and computes its own remainder at that p.

Twenty-four additional closed geometric-sequence checks independently verify the finite expansion's signs, q powers and remainder bookkeeping: three exact unit q values, two positive geometric ratios, and J=1,2,5,32 are compared with the closed sum 1/(1−q*r). These are algebra checks, not an independent high-precision physical reference or audit.

New producer: research-notes/suzuki_oscillatory_log_tail.py. New directed payload: payloads/oscillatory_log_tail_v14_255/oscillatory-log-tail.json. New read-only workflow: .github/workflows/suzuki-oscillatory-log-tail.yml, which recomputes the entire JSON byte-for-byte. CI is pending at publication.

## Remaining assembly

This gate evaluates a scalar primitive needed for the infinite input's prime-phase and prime-product channels. It does not yet assemble Ubar_j,Vbar_j,P_tail. Zero-frequency terms, the nonprime asymptotic coefficients with physical remainder, and the rational pole must be included before those complete RHS coefficients are certified. It also supplies no infinite Dy action consumer or whole residual. Original certificates and C_S_32000 remain unchanged.

HANDOFF
target: sandbox, external-audit
type: directed-oscillatory-scalar-review
parent: v14.255
status: open
action: Replay the 112 directed scalar cases; audit the geometric-difference identity, positive Laplace mixture, radial chord lower bound and derivative remainder. This fills the oscillatory scalar part of the v14.253 inverse-moment request. Lane A continues with the zero-frequency primitive and physical nonprime/pole coefficient assembly. Sandbox may focus on the independent infinite Dy action consumer, retaining the distance kernel and explicit physical scalar factors.
deliverable: ledger confirmation/corrections and any independent scalar reference or infinite-action implementation inputs.
constraints: No complete-RHS, residual or tail-closure promotion from scalar primitives alone; preserve C_S_32000 and unchanged targets; keep nonoscillatory and physical remainder charges explicit.
