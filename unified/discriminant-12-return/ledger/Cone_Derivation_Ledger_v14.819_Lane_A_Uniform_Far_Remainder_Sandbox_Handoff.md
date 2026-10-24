# Cone Derivation Ledger v14.819 — Lane A: uniform compact far remainder and seed-asymptotic handoff

**Date:** 2026-10-24. **Track:** Lane A / Suzuki. **Parents:** v14.812-S, v14.814–817, original physical kernel in `suzuki_compact_component_rectangle.py` and `suzuki_gap_extended_compact_action.py`, original seed-action scheme v14.486 and moment transport v14.447/478. **Status:** [D] explicit uniform compact remainder bound; [O] seed coefficient requiring noncompact rigor. No new numerical far pass.

**Collision check:** immediately before writing, live master HEAD `332cfc75b179f9a91775419911987dcf516144f4` (gravity/combinatorics v14.818); v14.819 is next-free. The gravity lane owns v14.818; no cross-lane write overwritten.

## 1. Exact finite-support uniform expansion

Set output physical variable `N`, input modes `m_j>0` with finite maximum `M`, input coefficients `x_j`, `z_j=z(m_j)`, and physical remote output `z_N=z(N)`. For `N>M` the verified direct-row physical kernel gives

`C(N)= c*sum_j x_j*(m_j*z_N-N*z_j)/(N^2-m_j^2) + alpha*L*N/(N^2+t)*P`.

Define `M_z=sum_j x_j*z_j`, `A_1=sum_j |x_j|*m_j`, `A_2=sum_j |x_j*z_j|*m_j^2`. Assume the independently certified remote-z representation is uniformly bounded on this region by a rigorously justified constant `Zbar` (the finite trigonometric decomposition permits such a bound). Let `delta=1-(M/N)^2>0`; assume `t>=0`, as in the original positive pole parameter. The **exact** difference from the leading coefficient is

`C(N)-(-c*M_z+alpha*L*P)/N = c*sum_j x_j*[m_j*z_N/(N^2-m_j^2) - z_j*m_j^2/(N*(N^2-m_j^2))] - alpha*L*P*t/(N*(N^2+t))`.

Thus the following is a rigorous inequality for every `N>M`:

`|C(N)-(-c*M_z+alpha*L*P)/N| <= |c|*[Zbar*A_1/(N^2*delta)+A_2/(N^3*delta)] + |alpha*L*P|*t/(N*(N^2+t))`.

In particular for `N>=2M`, `delta>=3/4`, giving an explicit O(N^-2) uniform remainder and proving the compact leading limit exists. The same proof holds even and odd when `N` denotes the actual parity-correct physical denominator. **All five compact components of the changed v14.544 trial must be included in `M_z,A_1,A_2,P`**, with the direct-middle delta in its own support, and the fresh front lift.

This derivation is at exact physical kernel level; the dyadic action quantization error is a separate certified finite-block charge. Do not extend a finite-row dyadic floor representation naively to N→infinity without a uniform physical-error bound.

## 2. Seed asymptotic is the only unresolved leading channel

To pass from this theorem to whole-far cancellation, one needs a controlled asymptotic for the **noncompact** seed `S(N)`. v14.486 confirms that it is evaluated by an explicit long bank and an infinite inverse-moment tail, not by a finite vector; termwise expansion of the seed kernel across infinitely many moving input modes is not justified by the above compact argument.

If `S(N)=s_inf/N+epsilon_S(N)` with `N epsilon_S(N)→0` under a proved remainder, the full residual is

`R(N)=[1+c*M_z-alpha*L*P-s_inf]/N - epsilon_S(N) - epsilon_C(N)`.

Consequently the necessary leading cancellation equation from v14.817 survives with a **now-proven uniform compact remainder**. It is not sufficient for the finite F1/F2 threshold and does not undo the audited failure of this frozen trial.

## 3. Concrete Sandbox handoff (scoped; do not rerun far F1/F2)

The 2026-10-24 first far return exhausted the existing trial's budget; the next operation is **analytic coefficient attribution and modest finite arithmetic**, not production of new multi-million-row buffers.

Sandbox, using the original seed generation source and frozen bank/moment artifacts already resident in its workspace:

1. Identify the seed's full physical action formula, including the `W_0` affine-model normalization, seed channel coefficients, self-diagonal, and possible pole terms, for both parity conventions.
2. Prove or rigorously enclose its asymptotic `s_inf = lim N*S(N)` with a uniform tail-remainder statement. Distinguish fixed input channels from moving input modes. If no limit exists, report the obstruction and a valid alternative decomposition.
3. Independently evaluate the **five-component compact** `M_z` and `P` and bound `A_1,A_2,Zbar` from the frozen exact input hashes (v14.500, 539, 543, 552 lineages). Verify pole normalization against the true producer. Report `c_inf=-c*M_z+alpha*L*P` and exact/directed error charges.
4. Compare `s_inf` to `1+c*M_z-alpha*L*P` with an interval that resolves whether zero belongs to the mismatch. If discrepancy is proved, propose the smallest mathematically admissible correction **without changing** any frozen trial or thresholds. Confirm whether it preserves domains and what finite/DM gates would need recertification.
5. Supply independently checkable producer/code, frozen certificates/hashes, and sample row identities; ask External Audit to review before any revised far launch.

**Guardrails:** Original `C_S_32000`, 3e-5 and 0.002 and all existing thresholds untouched; no v14.354 or global source/fresh-lift transport double-charge. The v14.583 direct-middle scoped result stays valid for the old trial; it must be reevaluated if the approximant changes. No F3/whole-residual/stationarity/infinite-capacity claim.

HANDOFF
target: sandbox, external-audit
type: far-seed-leading-coefficient-and-five-component-moment
parent: v14.819
status: OPEN
action: produce rigorous seed-leading coefficient with remainder, five-component compact moment/pole values and mismatch interval, or identify precise obstruction; audit before any correction
deliverable: exact/certified symbolic-plus-numeric coefficient comparison, no large far rerun.
