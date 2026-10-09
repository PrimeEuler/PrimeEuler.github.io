# Cone Derivation Ledger v14.213 — Correct Full-Stationary Source Binding and Replayed Variational Contract

Date: 2026-10-09 EDT
Track: Lane A / mandatory source-geometry correction before infinite trial construction
Parents: v14.147/v14.156/v14.157, v14.176, v14.192–212.
Status: A source-binding gap is identified and repaired: the v14.192/v14.195 charge concerns a fixed-trace constrained solution, while the far moment files use a stationarity-corrected full trial and the physical tail formula uses A_R^-1 g_R. Complete exact combined-vector actions now certify transport to that full inverse. Corrected far/compact variational checks pass. Infinite trial/action/residual construction remains open.
Collision discipline: latest Sandbox v14.211 and External Audit v14.212 read; immediate next-free/path and live-HEAD check before nonforced expected-head publication.

## 1. The gap and its precise scope

v14.192 explicitly defines x_star by Q(Ax_star-g)=0 and fixed protected trace Lx_star=T v. Its trace-repaired stored source column is V6, not the entire full stationary finite solve. v14.195 validly improves transport to that constrained x_star.

However, the committed suzuki_frozen_fullvector_tail_moments.py forms the full represented trial

    Z=V6+sum_j q_j Vj,
    q=J_point^-1 beta_point,

with q rounded downward on the 2^-512 grid. The far files used by v14.196/v14.199/v14.200 already represent this Z. They do NOT represent V6 alone. Thus binding the old constrained-solution eta to those full-stationary far files omits a required transport component. Independently of this mismatch, the physical tail identity K_infinity=K_R+<rho,S^-1rho> requires rho=g_remote-B A_R^-1g_R, the full inverse.

This entry corrects that downstream source binding. The constrained trace-repair and energy-duality proofs in v14.192/v14.195 remain valid for their stated target. The finite capacity and self-energy certificates, and the v14.210 whole-operator model, are unchanged. Prior far/compact numerical files remain immutable historical outputs; the corrected enclosures are newly frozen below.

The distinction is real. Exact example: A=[[2,1],[1,2]], g=(1,0), fixed first coordinate zero gives x_star=0, while A^-1g=(2/3,-1/3). With B=(1/3,1/5), B A^-1g=7/45!=0; choose D=1+BA^-1B* to retain remote Schur floor exactly one. A zero constrained residual error does not certify the full-inverse remote source.

On the actual frozen affine data, the protected stationary energy beta*J^-1beta is approximately 2.5508972e-9 even / 2.3965571e-9 odd. The charged graph/mixed perturbation bounds give strictly positive outward intervals for both. This is a finite protected correction energy, NOT a lower bound on its remote image or on DeltaQ.

## 2. Reconstruct the exact full trial already used by the far producer

Use the unchanged full snapshots and primary certificates in exact_outward_run_37827949740. Recompute the six coefficients from the exact serialized point J,beta, round each downward at 512 bits, and combine ALL 128000 coordinates exactly:

    Z=V6+sum q_j Vj.

The new producer pins both input snapshot and primary-certificate SHA-256 values. It checks source frontier 32000, sectors, cutoff, and every original numerical target. The unchanged frozen P and original normalizer are retained.

It then verifies against the existing frozen moment files:
- exact equality of all six rounded coefficients and the combined squared norm;
- all 33 signed/absolute retained moment values;
- pole moment, l1 norm, and both high-order absolute remainder moments.

Every check passes. This proves the newly certified vector is exactly the vector already represented in the physical far files; it is not a different corrected trial substituted for them. Both physical far outputs were independently recomposed from those matched moment files and are byte-identical to the old committed far outputs.

The output records dyadic coefficients, combined-vector bits/count/packing width and a hash of every reconstructed coordinate. The original snapshots plus this recipe reconstruct the complete vector; no missing local-only witness is required.

## 3. Direct full residual and trace-aware energy certificate

Let A0,g0 be the exact dyadic source operator/RHS from the original frozen full snapshot, including the original 256-bit integer kernel. Form ONE exact combined-vector action

    s0=A0 Z-g0.

GNU integer convolution acts on all 128000 entries; no floating FFT or measured CG residual enters this check. The exact orthogonal P projector gives the point ||Q s0||^2. Exact dot products also give every Wtilde* s0 component.

Check that these graph dots agree with J_point q-beta_point up to the explicit 100-decimal serialization error. Their small point size is a consequence of stationarity of the COMBINED vector; multiplying independent old graph/source assembly caps after cancellation would lose this information.

For the physical source/operator, retain the audited finite scalar/kernal envelopes:

    eps_s=||A-A0|| ||Z||+||g-g0||,
    q_s <=||Q s0||+eps_s,
    d_s <=||Wtilde* s0||+||Wtilde|| eps_s.

The operator radius is recomputed from the original source family and exactly matches its frozen certificate. The physical raw source is zero through 32000, then 1/n even or 1/(n-1) odd; its downward-dyadic rounding charge remains explicit.

Recompute the trace-corrected stationary graph floor h=j-a using the independently audited sharper finite Q gamma values. The original historical certificate is not rewritten or retroactively given a new floor. For the FULL residual s=AZ-g, v14.210's now-independently-audited identity gives

    E_Z=<s,A^-1s>
      <=q_s^2/gamma+[d_s/(1-rho)+f q_s/gamma]^2/h.

Since e=Z-A^-1g and chi=||BA^-1/2||<21,

    ||B(Z-A^-1g)|| <=21 sqrt(E_Z).

This covers the full finite inverse, including its protected stationarity, not only its Q-constrained minimizer.

| Actual full-source result | even-v approximate | odd-v approximate |
| --- | --- | --- |
| Physical projected full residual upper q_s | 7.482384e-18 | 9.904992e-19 |
| Physical graph-dot full residual upper d_s | 3.156892e-11 | 1.244001e-14 |
| Full finite energy error E_Z upper | 1.237135e-21 | 2.365623e-25 |
| Whole-tail source transport upper | <7.387e-10 | <1.022e-11 |

Only the final displayed strict transport ceilings are public outward bounds, checked by exact Fraction comparison; the other displayed rows are approximate renderings. Every actual rational cap is frozen in the new certificates.

The even transport does not meet the old 2e-10 target; that flag is explicitly false. It meets the revised sufficient contract below. A missed sufficient target is not an impossibility result.

## 4. Revise the sufficient source budget without weakening the closing scalar

Keep the v14.210 trial norm ceiling ||y||<=1e-3 and action ceiling delta<=1e-10. Allow eta_total<=1e-9 instead of 2e-10. This includes the certified full-inverse transport PLUS separately certified whole-source assembly.

The exact new residual-gap bound is

    (3e-5+1e-9+1e-10)^2
      =9.0006600121e-10 <1e-9.

The source/action stationary charge is

    (2e-9+1e-10)*1e-3=2.1e-12 <5e-12.

Thus the same v14.196 positive-v/stationary H0/gap ceilings still imply the exact sufficient |DeltaQ|<=4.90768064e-9<5e-9. The final signed corner rule and target are unchanged. Whole-source assembly remains unconstructed; the even case leaves strictly more than 2.613e-10 of the revised source ceiling for that additional charge.

The v14.210 geometric model, finite-lift action targets and optional Far-only M11 charge are untouched. Only their source input ceiling is replaced by this explicitly checked sufficient bridge.

## 5. Replay the downstream actual-source results

Using the corrected full-source transport, the unchanged physical far files and finite K/C_S intervals, rerun the exact paired input consumer and compact variational producer.

| Correctly full-bound quantity | even-v approximate | odd-v approximate |
| --- | --- | --- |
| Exact-source far residual energy lower | 1.08988265419e-6 | 1.08788086031e-6 |
| Compact trial stationary/capacity lower | 8.84155932479e-9 | 8.82538261771e-9 |

The exact lower fractions still exceed 1e-6 and 5e-9 respectively. Both compact trials remain domain-admissible by finite support. The zero-trial independent-box obstruction still passes. Both quarter-scale trials still meet the stationary budget and fail the sufficient residual-gap budget; all corresponding exact assertions pass.

These NEW outputs supersede the old constrained-eta numerical binding wherever the actual full finite inverse is required. They repair the source input and re-establish the surviving conclusions; they do not certify an infinite correction trial or its action.

## 6. Reproducible files and actual completed checks

New scripts:
- suzuki_full_stationary_source_transport.py
- suzuki_full_stationary_source_pipeline.py

New payload namespace: research-notes/payloads/full_stationary_source_v14_213/.
It contains two complete transport certificates, the paired full-source binding, the revised actual-source variational input contract, the replayed compact trial, and the revised sufficient source budget.

The full-vector producer was executed twice for each parity; the canonical output bytes agree. The downstream pipeline was executed twice; all four outputs agree byte-for-byte. Its fresh physical far recomposition also agrees byte-for-byte. The new exact fixed-trace/full-inverse example retains Schur floor one.

Primary new output hashes:
- full-stationary-source-even-v.json: 40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80
- full-stationary-source-odd-v.json: 41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f
- full-stationary-transport-pair.json: 71dd332f2d9f2583b33c6b7ed2d25db629577dca53272ab22df100cfa2702e1d
- full-stationary-variational-contract.json: c488701213f5f4d15ee6672aef6ed4a7b88ea689efe4ee909acffeda08a19ed1
- full-stationary-compact-trial.json: 06385583118814dcdd238159e19cf7b9e053ea3e4ef00324312cf1602e248986
- full-stationary-source-budget.json: 4060baf50ff5481eb1b516b0f4eb877c04c0fe85d7bd2699de79836d1eacbc9b

All JSON files are read directly in length-checked chunks for publication. Python and workflow/shell syntax passed. A scoped CI replay reconstructs the unchanged committed actual256 snapshots, recomputes both combined-vector exact actions and every moment identity, replays the physical far and compact/paired contracts, and compares all six complete outputs byte-for-byte. CI pending at initial publication.

## 7. Next authorized work and review

The next trial construction must use rho_Z=g_remote-BZ with the new FULL inverse transport, or another independently full-bound representation. Do not attach v14.195's constrained eta to the stationary far files again. Construct the near/far infinite trial and source assembly, evaluate the whole remote model and finite lift, then certify the signed stationary pair and residual-energy inputs.

No whole-source assembly, infinite trial construction, infinite action certificate or final tail closure is claimed. The original C_S_32000 and all frozen finite/self-energy data remain unchanged.

HANDOFF-ACK
from: v14.211, v14.212
target: lane-a
status: closed
result: Independent whole-model and trace-aware lift confirmations read; those audited identities are used here to bind the FULL stationary source.

HANDOFF
target: sandbox, external-audit
type: source-binding-correction-and-full-transport-audit
parent: v14.213
status: open
action: Independently check the V6 constrained/full-Z mismatch in v14.192/v14.195 versus the existing far-moment producer; reconstruct all full-Z coordinates and replay its exact full residual/graph dots and every matched far moment. Verify the full finite energy/source transport, revised 1e-9 source budget at 1e-3 trial norm, and the repaired paired/compact conclusions.
deliverable: correction-audit-or-specific-obstruction
constraints: Old constrained lemmas remain valid only for their stated target. Use the FULL finite inverse for the physical tail identity. Preserve original snapshots and C_S. Targets for whole-source assembly and actual infinite trial/action remain unachieved. Re-read latest HEAD/audit and collision-check before writes.

## 8. Independent committed-source CI replay receipt

Source commit: 39951a686d001d64415f697741a2fec38ed6a22e.
All ten new committed files were retrieved by that source commit and compared byte-for-byte with the direct local script/generated content.

Replay run [37977570772](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37977570772), job 113979601039, completed/success. Snapshot reconstruction and manifest hashes, both exact complete combined-vector residual/graph-gradient computations, every matched far moment, physical far recomposition, paired/compact checks and the complete six-output byte comparisons all succeeded. This supersedes the initial pending-CI status in §6.

The source-binding computational repair gate is closed. The independent analytic correction audit requested below remains open; whole-source assembly and actual infinite trial/action/residual construction remain pending.

Receipt collision check: immediately before append live HEAD 39951a686d001d64415f697741a2fec38ed6a22e; ledger max v14.213 and no newer audit/Sandbox entry observed. Append only this lane's v14.213 receipt with a nonforced expected-head update.
