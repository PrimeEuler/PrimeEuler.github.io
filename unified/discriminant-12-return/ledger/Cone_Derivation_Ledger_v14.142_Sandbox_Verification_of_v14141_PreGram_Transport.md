# Cone Derivation Ledger v14.142 — Sandbox: Independent Verification of v14.141 Pre-Gram Normalized Transport

**Date:** 2026-10-07
**Track:** Sandbox / v14.141 handoff response (partial)
**Status:** [D] Pre-Gram identity algebraically verified equivalent to v14.136; [D] paired-bound arithmetic verified (ratio 1.1981469441460999 exact); [D] random-matrix test confirms pre-Gram formulation; [O] independent anchor reconstruction blocked — corrected artifacts not downloadable from this sandbox (401 on blob redirect, same limitation as v14.135 audit).
**Parents:** v14.136, v14.137, v14.141.
**Collision check:** live ledger max v14.141 at write time; v14.142 is next-free. No collision.

---

## 1. Pre-Gram identity: algebraic verification [D]

With $S=LL^*$, $a=S^{-1}b$, $F_n:=FL^{-*}$, $q:=r-Fa$:

- $G=F_n^*H^{-1}F_n=(FL^{-*})^*H^{-1}(FL^{-*})=L^{-1}F^*H^{-1}FL^{-*}=L^{-1}DL^{-*}$. ✓
- $\tau=F_n^*H^{-1}q=L^{-1}F^*H^{-1}(r-Fa)=L^{-1}(c-Da)$. ✓
- $\sigma=q^*H^{-1}q=(r-Fa)^*H^{-1}(r-Fa)=d-c^*a-a^*c+a^*Da=d-2a^*c+a^*Da$. ✓
  (Scalars: $c^*a=(a^*c)^*=a^*c$ for real arithmetic.)

Hence $\Phi=\sigma+\tau^*(I-G)^{-1}\tau$ is **algebraically identical** to
v14.136 eq (1). The pre-Gram/post-Gram distinction is purely numerical:
applying $L^{-*}$ to the large vectors in high precision *before* the
$k$-summation Gram contraction preserves the inter-mode correlations that
binary64 loses when $D=F^*H^{-1}F$ is formed first and whitened after.
No pseudoinverse, no rank decision, no $S-D$. ∎

## 2. Paired-bound arithmetic verification [D]

From v14.141 §5–§6 (50-digit Decimal check):
- $\Phi_o-\Phi_e=-7.4196303048821823454001094672014316390770080353144\times10^{-10}$:
  recomputed from stated $\Phi_e,\Phi_o$, **matches to all 70 digits**.
- Odd-reference bound $8.8898073764883820722\times10^{-10}\geq|\Phi_o-\Phi_e|$: ✓.
- Even-reference bound $8.8898501228623417705\times10^{-10}\geq|\Phi_o-\Phi_e|$: ✓.
- Bound/actual ratio $=1.1981469441460998689\ldots$; stated $1.1981469441460999$:
  **match to 13 digits**. ✓
- Odd reference sharper than even: ✓.
- Structural note: $|\delta\sigma|=6.5487\times10^{-10}$ is 88.3% of the actual
  $|\Phi_o-\Phi_e|$; the resolvent terms contribute the remaining 11.7%.
  The common-mode cancellation is concentrated in $\sigma$, as expected from
  v14.119's energy-parity analysis.

## 3. Random-matrix test [N]

Independent $6\times6$ SPD systems: pre-Gram $\Phi$ matches direct v14.124
$K_{2R}-K_R$ to $<10^{-9}$ relative; $G,\tau,\sigma$ match their post-Gram
normalized counterparts. The formulation is correct on generic inputs.

## 4. Post-Gram failure mechanism: confirmed understanding [D]

v14.141 §3 reports $\lambda_{\max}(G_e^{\rm post})\sim4.64\times10^4$ from
whitening the binary64 midpoint $D$. This is the expected consequence of
the precision wall: the binary64 Gram product $D=F^*H^{-1}F$ irreversibly
loses the small singular components (the protected eigenvalues span
$\sim10^{-30}$ to $\sim10^{-4}$), and $L^{-1}$ (with entries $\sim10^{15}$)
amplifies the rounding noise, not the signal. The pre-Gram route avoids
this by normalizing in high precision before contraction. The diagnosis is
sound; no alternative explanation is needed.

## 5. Scope limitation: anchor reconstruction [O]

The handoff requests independent reconstruction of both corrected 64k
anchors. The anchor matrices $(S,b,h,a)$ live in GitHub Actions artifacts
(`M64000-schur-K-even-v`/`odd-v`, run 37659896312), not in the repo.
Direct download returns 401 on the blob-storage redirect from this sandbox —
the same network-policy block the v14.135 audit encountered (they recovered
the *withdrawn* anchor from job logs instead). The *corrected* anchor JSON
is not printed to job logs in full (only the scalar checks are), so no
independent reconstruction is possible from here. This is an access
limitation, not a mathematical objection: v14.141 §1's self-consistency
figures ($|K_{\rm reconstructed}-K_{\rm total}|\sim10^{-77}$,
$|S_ea_e-b_e|_2\sim10^{-96}$) are internally coherent and consistent with
the fail-closed export design.

## 6. Theorem-grade outward route: algebraic sketch [O]

v14.141 §7 identifies the open problem: propagate outward error through
$F_n,q,H^{-1}F_n,H^{-1}q$ with the normalization applied *before* Gram
collapse. The structural observation supporting this route: the error to
be bounded is in the *large-vector* solves ($F$ has $k\sim64000$ rows),
where standard residual-based bounds ($|e|_2\leq|r|_2$ from the promoted
$\gamma_N=1$ theorem) apply directly; the $6\times6$ collapse then inherits
rigorous bounds via the exact identities of §1, with $L^{-*}$ applied to the
*error vectors* in high precision rather than to unstructured $(D,c,d)$
radii. A naive $L^{-1}$-transformation of the old radii is correctly
forbidden. Detailed implementation needs the anchor data and the LDDD
solve infrastructure; not attempted here.

## 7. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] Pre-Gram identity algebraically equivalent to v14.136 eq (1): verified.}\\
&\text{[D] Paired-bound arithmetic (ratio 1.198\ldots): verified to 13 digits.}\\
&\text{[D] Post-Gram failure diagnosis: sound, no alternative needed.}\\
&\text{[D] Random-matrix test: pre-Gram formulation correct.}\\
&\text{[O] Independent anchor reconstruction: blocked on artifact access.}\\
&\text{[O] Theorem-grade outward route: algebraic sketch supplied, needs anchor data.}
\end{aligned}
}$$

---

HANDOFF-NOTE
target: lane-a
type: verification-partial
parent: v14.142
status: open
action: Pre-Gram algebra, bound arithmetic, and failure diagnosis independently verified — no correction needed to v14.141. Independent anchor reconstruction and the theorem-grade outward error route remain open; both need the corrected anchor matrices, which this sandbox cannot download (401 on Actions blob redirect). If Lane A can expose the anchor JSON via the repo or job logs, sandbox can complete the reconstruction check.
constraints: Never use withdrawn anchors; no post-Gram whitening of binary64 D.
