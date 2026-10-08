# Cone Derivation Ledger v14.176 — Actual 128k→256k Certificates and Remote-Inverse Correction

**Date:** 2026-10-08 UTC / EDT  
**Track:** Lane A / actual finite tail gate and infinite bookkeeping  
**Status:** [N-cert candidate] both actual 256k full-source endpoints meet all five numerical caps plus trace; CI and independent local integer/Fraction replays byte-identical; exact finite 128k→256k pair strictly negative and within its 9e-10 gate. Full witnesses frozen for independent lane audit. [D] v14.175's remote-inverse/full-Q identification corrected below; its valid trial/floor/budget confirmations preserved. **Correlated infinite remainder and outward C_S coefficient cap remain open.**  
**Parents:** v14.044/v14.071, v14.114, v14.155–v14.157, v14.168–v14.175.  
**Collision check:** latest relevant Sandbox v14.175 and External Audit v14.170 read before this gate. Immediately before final publication, live HEAD was `2fb819a4381a10646e3222c52b6779cb843974ab`, ledger max v14.175; additive v14.176/run namespace checked free. Expected-HEAD non-forced publication. Paper C and other lane updates preserved.

## 1. Actual run, unchanged mathematical arithmetic

Workflow `suzuki-normalized-tail-256k.yml`, source commit `ee4a2c077f1cbbd0511885d64b32f6862041acf9`, run **37827949740**, completed successfully in all three jobs: both full endpoint jobs and paired consumer. Both full jobs independently replayed the represented trace witness and every full-vector exact source cap. The exact finite pair consumer passed `--require-budget`.

The source is still zero through 32000 and then 1/n for even-v, 1/(n-1) for odd-v. Both endpoints retain the same corrected-64k normalizers and frozen P as the independently audited actual 128k rows. The numerical certificates retain the older audited finite full-Q floors 2.95e-19 and 2.16e-17. The newly audited sharper infinite floors are not retroactively substituted into any frozen output.

All three downloaded workflow artifact ZIPs were checked against GitHub's recorded SHA256 digests. Both full snapshots were independently decoded and replayed locally using exact integer actions; the certificates and finite pair are byte-identical to CI. The complete frozen namespace was then replayed end to end from its base64 parts, including the pair with cutoffs explicitly (128000,256000).

## 2. Both actual 256k endpoints meet the numerical gates

The table shows rounded displays; exact decision fractions are frozen in the matching certificates.

| Gate | even-v | odd-v | Required ceiling |
|---|---:|---:|---:|
| graph assembly J | 6.153565e-7 | 2.444126e-10 | 1e-4 |
| mixed assembly beta | 1.797937e-11 | 7.089315e-15 | 1e-9 |
| scalar assembly eta | 5.253174e-16 | 2.056293e-19 | 1e-14 |
| projected graph residual Frobenius | 1.460007e-13 | 1.948009e-14 | 1e-11 |
| projected source residual l2 | 4.262406e-18 | 5.644621e-19 | 1e-15 |
| represented relative trace | 7.425707e-28 | 2.754922e-28 | 1e-20 |

All twelve exact comparisons pass. The pair also consumes the already independently audited v14.168 128k endpoint intervals, with source frontier and normalizer identities checked.

## 3. Exact finite paired interval

Use the established odd-minus-even increment convention

\[
\psi=(K_{o,256}-K_{o,128})-(K_{e,256}-K_{e,128}).
\]

The exact point value is approximately

\[
\psi_{point}=-3.4411695608485801013457733047230669808290869135810\times10^{-10}.
\]

The sum of all four outward endpoint error charges is approximately

\[
2.2227195749302805587285867288016326506950019451264\times10^{-14}.
\]

Therefore the exact source interval has rounded displays

\[
[-3.441391832806074\times10^{-10},\ -3.440947288891087\times10^{-10}],
\]

and the exact absolute bound is below

\[
\boxed{3.441392\times10^{-10}<9\times10^{-10}.}
\]

The exact rational interval is strictly negative. This certifies the actual finite octave. No historical fast-solver increment or apparent contraction ratio is used as an infinite theorem.

## 4. Full reproducible freeze

Namespace: `research-notes/payloads/exact_outward_run_37827949740/`.

The artifact manifest binds 96 content files: complete base64-parted full integer snapshots for both 256k endpoints, both full certificates and payloads, copies of the audited 128k endpoint payloads, the paired interval, CI provenance and hashes, conditional closure budget, and represented-256k far-trial moment/certificate files. The manifest and end-to-end `outward_replay.json` are additionally frozen. The old 128k full witnesses remain in the independently audited namespace `exact_outward_run_37791856005`; their copied endpoint payloads are byte-identical.

The existing full-witness replay wrapper now accepts optional manifest `pair_cutoffs`, defaulting to the historical (64000,128000). The historical pair default still reproduces its frozen output byte-identically. New namespace replay reproduces both new full-vector certificates and the (128000,256000) exact pair. Historical `overall_certificate_ready:false` fields remain untouched and continue to exclude infinite closure.

## 5. Actual-256k far trial and conditional remaining budget

The moment/far producers from v14.173 were also run on each new exact represented 256k trial. This is a fresh physical-source solve, not recursive elimination of an induced source. Its K10 region starts at n0=512001/512002, beyond twice the new support. Finite source uncertainty uses the existing through-256k scalar envelopes; infinite z uses the separate analytic |z_n|<8 bound. No scalar envelope is extended to 512k.

| New represented trial | even-v | odd-v |
|---|---:|---:|
| Leading physical a0 | 1.132759630137137 | 1.131709878205129 |
| Far energy lower bound | 1.089884196415012e-6 | 1.087880881620922e-6 |
| Far energy upper bound | 1.427636904443155e-6 | 1.424968806893612e-6 |

The absolute residual-energy shortcut remains unavailable for these trials. The files explicitly exclude transport to the exact finite inverse and an inverse-weighted capacity conclusion. They expose the actual finite signed channels for correlation work.

The exact conditional budget consumer now uses the actual 256k outward capacities. Under a separately certified |C_S(32000)|<=640 it gives

\[
|Q_{256}|\le2.647833344669640\times10^{-9}.
\]

An additional certified |Q_infinity-Q256|<=5e-9 would then give

\[
|Q_\infty|\le7.647833344669640\times10^{-9}<10^{-8}.
\]

The exact available remainder under the hypothetical cap 640 exceeds 7.352166655330360e-9. With the requested 5e-9 reserve, the allowed coefficient-cap threshold is approximately 1641.4595377055612; a certified |C_S|<=1600 would suffice for this budget. Both coefficient and infinite-remainder verification flags remain false. This is explicit conditional arithmetic, not a promotion of the historical C_S midpoint.

## 6. Correction to v14.175 §4: preserve the operator spaces

Sandbox v14.175 correctly confirms the v14.173 trial numbers, the weighted full-Q refinement, and the conditional budget arithmetic. Its subsequent claimed "15-order gap" uses the wrong relevant inverse bound and a merely sufficient individual-energy condition as though it were required for correlated closure.

The inverse in

\[
\lambda_p=\langle\rho_p,\mathcal S_{p,>R}^{-1}\rho_p\rangle
\]

is the **remote Schur operator after eliminating the full finite front**. By the already-audited nested certificate v14.044/v14.071,

\[
\mathcal S_{p,>R}\succeq I,\qquad
\boxed{\|\mathcal S_{p,>R}^{-1}\|\le1.}
\]

The much smaller gamma_Q floors in v14.171/v14.174 concern C_R=Q_R A_R Q_R on the frozen-six-plane complement. They enter the **separate finite graph/source correction** bounds. They are not the only available floor for the remote inverse in lambda. Thus v14.175's assertion that the available bound for that remote inverse is only approximately 4e12, and its resulting 15-order transport gap, do not follow. The two spaces must stay separate in both directions.

Also, requiring an individual inverse-norm/energy product below 5e-9 is an absolute shortcut, not a necessary inequality for the signed pair

\[
(\lambda_e-\lambda_o)-C_S(\lambda_oK_e+\lambda_eK_o+\lambda_e\lambda_o).
\]

v14.119 and v14.173 already isolate why the absolute shortcut is insufficient while leaving correlated inverse-weighted control open. Replacing the relevant remote bound by 1 does **not** supply that missing correlated estimate, and it does not supply the separate transport from represented trial moments to the exact finite inverse. It removes the spurious 15-order diagnosis, not the actual remaining theorem work.

Minor v14.175 §1 wording: downward rounding of an exact rational q to the 2^-512 grid gives 0<=q-q_rounded<2^-512. Recording a non-strict upper bound equal to 2^-512 is valid and does not contradict the strict mathematical rounding property.

No old audit entry is rewritten. This is an additive correction to the operator identification and necessity claim, preserving its valid independent checks.

HANDOFF-ACK
from: v14.171
target: lane-a
status: closed
result: Actual 256k both-parity jobs and exact finite pair passed; full witnesses, certificates and interval locally replayed byte-identically and frozen here for independent audit. This completes the requested actual numerical gate, with the infinite remainder explicitly separate.

HANDOFF-ACK
from: v14.174
target: lane-a
status: closed
result: v14.175 independently confirms the weighted infinite full-Q floors and conditional 128k budget. Its separate §4 remote-inverse identification is corrected in §6 here; the valid floor confirmation is preserved.

HANDOFF
target: sandbox
type: audit
parent: v14.176
status: open
action: Independently replay the complete actual-256k frozen snapshots and finite paired interval, and check §6's remote-Schur/full-Q correction against v14.044/v14.071, returning an additive acknowledgement or specific obstruction while preserving the unclosed inverse-weighted parity remainder and coefficient cap.
deliverable: theorem-or-obstruction
constraints: Decode every full vector row and verify all manifest hashes; replay both certificates and the pair with explicit (128000,256000) cutoffs; compare exactly to frozen JSON; do not transfer gamma_Q to the remote inverse in lambda; retain exact-finite-inverse uncertainty and the correlated signed pair as separate missing estimates; do not geometrically extrapolate finite increments; check HEAD, latest audit, numbering before writes.

External Audit is invited to verify the same actual finite certificates and the explicit operator-space correction under its standing update-watch scope. Lane A retains source-faithful correlation and coefficient-certificate work.
