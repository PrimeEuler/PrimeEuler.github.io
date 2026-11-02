# Cone Derivation Ledger v15.303 — Lane A: full-K inertia via exact infinite-tail Schur complement

Date: 2026-11-02. Lane: A. Parents: v15.129–132 (chosen ell2 self-adjoint K), v15.141, v15.227, v15.232, v15.237, v15.302. Status: [D] abstract exact infinite-dimensional Schur inertia and resolvent criterion; [O] certified tail inertia/resolvent data needed to instantiate. No Sandbox dependency or return claimed.

## Live state and provenance
At start of analysis master HEAD was 61cb40576551 (v15.302); full-K transfer remains INCONCLUSIVE. The earlier v14.405 compact-action pair is recovered, v14.406 finite-plus-gap PASSED (v14.442–443), and the later finite-far gate FAILED (v14.814). Do not rerun those objects. v15.227 provides certified J=100 finite-block inertia but no full-K transfer.

## Gate A: an exact decomposition that does not equate block and full inertia

On deliberately chosen counting-measure H=ell2, let K=D+B be self-adjoint with compact resolvent and bounded below. For any finite-rank coordinate projection P, Q=1-P, write H=P H direct-sum Q H. The domain of K is Dom(D) and P preserves it. Define
A=PKP|PH, V=QBP:PH->QH, T=QKQ|QH=D_Q+QBQ on Dom(D_Q).

T is self-adjoint bounded below with compact resolvent. Fix real energy x with x in rho(T). Define Feshbach/Schur matrix on PH:
S_P(x)=A-x I_P - V* (T-x I_Q)^(-1) V.
By bounded invertible block triangular congruence of the quadratic forms of K-x, the negative index satisfies the EXACT identity

n_-(K-x) = n_-(T-x) + n_-(S_P(x)).

All three counts are finite because K and T have compact resolvent and are bounded below. Likewise x in rho(K) iff 0 in rho(S_P(x)); as S is finite, equivalently det S_P(x) != 0, PROVIDED x in rho(T). At x in rho(T), eigenvalue multiplicities of K at x equal nullity S_P(x). No claim is made that n_-(T-x)=0. This corrects the naive full=finite inertia promotion obstructed by v15.227.

## Gate B: rigorous interval acceptance inequalities

Assume a candidate approximation R_Q(x) to (T-x)^(-1) with a justified operator-norm enclosure
||R_Q(x)-(T-x)^(-1)||<=epsilon_Q.
Then the approximate finite matrix
S_hat=A-x-V*R_Q(x)V
obeys
||S_P(x)-S_hat||<=||V||² epsilon_Q.
For an interval of energies x in [a,b], independently certify:
(1) [a,b] subset rho(T), and the finite integer n_-(T-x) is constant through the interval;
(2) norm enclosure epsilon_Q(x), using actual tail structure rather than diagonal-only tau_S;
(3) rigorous symmetric finite-matrix eigenvalue enclosures for S_hat(x) enlarged by ||V||² epsilon_Q(x).
If 0 is excluded from all expanded S eigenvalue intervals at both endpoints and continuity/resolvent membership is certified across [a,b], K has no eigenvalues there. If endpoint inertia indices of S change, total full inertia changes by exactly that difference, adjusted by the known tail count.

An isolated endpoint sign test alone does NOT certify absence of eigenvalues between endpoints; one needs uniform invertibility or monotonicity. On any connected interval contained in rho(T), the exact derivative is
S'_P(x)=-I_P - V*(T-x)^(-2)V <= -I_P,
so S_P is strictly decreasing in Loewner order. Thus a sufficient full-K gap test on [a,b] with the T resolvent condition is: S_P(a) and S_P(b) have the SAME negative inertia (and both invertible). Strict monotonicity rules out an interior zero if the endpoint inertias agree. If they differ, the difference counts crossings of full-K eigenvalues while T contributes none. This is an exact route to count eigenvalues in (a,b) without a common resolvent of the old diagonal-preserving cutoff.

## What the theorem DOES NOT give

At energies x≈10.3–10.45 from v15.227, Q for the first 100 physical modes has many tail diagonal values in that region. The theorem does not prove x in rho(T), nor a usable ||(T-x)^(-1)|| bound. Because QBQ is nontrivial, the diagonal near-pole is NOT proof x lies in spec(T) either. It identifies the needed alternate certificate: **tail resolvent and tail inertia** from a genuinely coupled tail operator. Any attempt to assume positive T-x or a Neumann series around its diagonal here repeats the failed gate.

Resource-saving candidate: choose P containing a certified collection of resonant modes (not necessarily a contiguous prefix), then use interval block inversion / structured tail estimates on Q; this is only a strategy until Q resolvent bounds and inertia are certified.

## Gate status and next direct calculation

FULL_K_TRANSFER=INCONCLUSIVE. Next Lane A-only gate: derive an exact certified-block truncation criterion for T-x using two-level Feshbach decomposition and an explicit remainder norm bound; perform no unverified numerical promotion.

No source-native Suzuki Phi; chosen ell2 only. No whole-residual/stationarity/capacity conclusion. Protected C_S_32000, thresholds 3e-5 and .002, all frozen hashes and exactly-once charges unchanged.
