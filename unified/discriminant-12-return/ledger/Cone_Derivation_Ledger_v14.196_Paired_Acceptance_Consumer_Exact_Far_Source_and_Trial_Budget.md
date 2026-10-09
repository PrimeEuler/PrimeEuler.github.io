# Cone Derivation Ledger v14.196 — Exact Paired Acceptance Consumer, Physical Far-Residual Lower Bounds, and Concrete Trial Budgets

Date: 2026-10-09 EDT
Track: Lane A
Status: [D/N-cert] v14.195 transport upgrades the stored far-residual lower certificates to the exact constrained physical residual; [D] zero-remote-trial independent-box obstruction; [V] reusable exact paired corner consumer and 3699 rational interior checks; [D] explicit sufficient numerical trial budget. The v14.195 analytic transport audit is pending. No nonzero remote trial or infinite capacity closure is claimed.
Parents: v14.173/v14.176, v14.185–195.
Collision check: live HEAD 11c22c84eaf5ca7daa4e081bc8ebb1b47590296f; latest Sandbox v14.193 and External Audit v14.194 read, plus Lane A v14.195. Live max v14.195; v14.196 and all three publication paths are free. Expected-HEAD non-forced update.

## 1. Exact physical far-source lower certificate

Let F project to n>2R. The represented-trial physical far certificate in v14.176 includes the physical scalar uncertainty but originally excluded finite-inverse transport. With eta_new from v14.195,

    ||F rho_star|| >= max(0, lower_norm(F rho_u)-eta_new).

The archived far input files and the transport payload are hashed in the new output. Exact rational arithmetic yields strict downward lower energies (display rounded down):

| exact physical residual far energy lower | Even | Odd |
|---|---:|---:|
| ||F rho_star||^2 | 1.0898838307e-6 | 1.0878808700e-6 |

Both exceed 1e-6 exactly. This closes the previously missing finite-inverse uncertainty component of these lower bounds, subject to independent review of the v14.195 theorem. It does not construct an upper enclosure for the near/far residual and does not lower-bound inverse-weighted lambda.

## 2. A zero remote trial cannot close the independent variational box

For y=0, v=0 and r=rho_star. Any certified upper gap E_even>=||rho_even||^2 must exceed the exact far lower energy, hence E_even>1e-6. An independent epsilon box contains the corner (epsilon_even,epsilon_odd)=(1e-6,0). With the actual outward finite K_odd<2e-6 and C_S<=640,

    H(1e-6,0)=1e-6(1-C_S K_odd)
              >1e-6(1-640*2e-6)>0.99e-6>5e-9.

Thus a y=0 producer cannot pass the v14.190 independent-box gate even with perfect source assembly. This is a limitation of that enclosure, not a claim that the actual pair attains this corner, not a lower bound on actual lambda, and not a negative conclusion about actual DeltaQ. Nonzero trials or an additional correlated gap theorem are necessary.

## 3. Exact corner consumer with paired stationary input

The reusable `suzuki_paired_variational_acceptance.py` exports enclose(c,ke,ko,ve,vo,Ee,Eo,h0=None), all rational intervals. It produces two valid enclosures and intersects them:

1. Direct 32-corner evaluation of H(lambda_even,lambda_odd,C,K_even,K_odd), with lambda_p in [max(0,v_p,lo), v_p,hi+E_p]. A negative upper endpoint is rejected as inconsistent, not promoted as a negative capacity.
2. H0 plus the exact 128-corner remainder from v14.190's H-correction identity. If the producer supplies a paired H0 interval, its correlation is retained here; otherwise H0 is itself enclosed by its 32 corners.

Both polynomials are separately affine in every box variable, so extrema occur at corners. The positivity clipping may weaken the direct enclosure but is valid. The separate H0/remainder enclosure may lose dependence but is valid; their intersection is valid when both input contracts are sound. No favorable sign of v or a correction coefficient is assumed.

Checks include 3699 exact rational interior values across negative-v and coefficient-sign-reversal boxes, plus an independent zero-gap point identity. These check the consumer arithmetic; the corner theorem is the displayed multilinearity argument. Two builds of the actual input contract are byte-identical.

`payloads/actual256-paired-variational-input-contract.json` contains outward 192-bit dyadic K_even/K_odd and C_S intervals from the independently audited actual finite witnesses, whole-tail finite-inverse transport charges, exact far lower bounds, hashes, and explicit null entries for the missing remote trial, assembly eta, operator delta, stationary scalar and residual upper data. The current remote-trial-ready and infinite-closure flags are false. The point-file's historical coefficient-audit-pending flag is not rewritten; v14.187/v14.188 supply that audit provenance externally.

## 4. Concrete sufficient next-producer budget

The following bounds are sufficient, not necessary, and give a specific producer target rather than a generic weighted-comparison request:

    total source uncertainty eta_total <=2e-10,
    operator-action uncertainty delta <=1e-10,
    trial norm ||y|| <=0.01,
    represented residual norm ||r_rep|| <=3e-5,
    exact stationary intervals 0<=v_p<=1e-5,
    exact paired stationary |H0|<=2.9e-9.

Then E_p<=(3e-5+2e-10+1e-10)^2<1e-9. The actual positive K_p<2e-6 and C_S<=640 give

    |T_even|<=E_even,
    |T_odd|<=(1+640*(2e-6+1e-5))*E_odd=1.00768 E_odd,
    |T_cross|<=640 E_even E_odd.

Therefore

    |DeltaQ| <=2.9e-9+1e-9+1.00768e-9+640e-18
              =4.90768064e-9<5e-9.

The stationary uncertainty from eta_total and delta is <=5e-12 per parity at ||y||<=0.01. A bound on a represented paired H0 must still charge both stationary errors and any finite K/C arithmetic; do not identify its interval with the exact H0 without that propagation. The current even transport leaves more than 2e-11 of source-assembly allowance inside eta_total<=2e-10, and the odd allowance is larger. The script independently checks these budget inequalities with exact fractions.

This clears the acceptance-interface and source-transport arithmetic gates. It does not assert that a trial satisfying these inequalities has been constructed. Lane A's next numerical work is the physical represented source/action and nonzero admissible remote trial; the near octave cannot be omitted and finite octave ratios cannot replace the infinite action bound.

HANDOFF
target: sandbox
type: audit
parent: v14.196
status: open
action: Review the upgraded exact physical far lower bounds, the precisely scoped zero-trial box obstruction, the correlated-H0 corner consumer and its rational checks, and the explicit sufficient nonzero-trial budget. Read this together with the separate v14.195 transport audit; report any correction before numerical trial use.
deliverable: audit-or-correction
constraints: Do not treat residual-energy lower bounds as inverse-weighted lambda lower bounds or box corners as physically attained. Preserve the missing-data nulls and false closure flags. Lane A owns source/action assembly and actual trial execution. Check current ledger/audit and collisions before writes.
