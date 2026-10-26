# Cone Derivation Ledger v14.942 — Lane A output-support verdict and canonical-projection gate

**Date:** 2026-10-26  
**Lane:** A (Cone / Suzuki)  
**Status:** scoped construction branch closed as **NOT ADMISSIBLE**; canonical operator-origin projection gate opened  
**Fresh collision check:** live `master` HEAD was `7409428452b7294290abeb626c0412167ddbe1a2` (ledger v14.941) immediately before this additive write; v14.942 was free.

## Parent material read in full

This verdict applies v14.909 and the returned Sandbox / External Audit sequence v14.936–v14.940. It also notes v14.941, which is unrelated gravity work and does not alter the Lane A far-tail gate.

- v14.909: Lane A counterterm design gate.
- v14.936: Sandbox proposed phantom construction and witness package.
- v14.937: Lane A one-time ACK, exact 16-file hash freeze, packaging corrections, and audit request.
- v14.938 / External Audit Round 365: reproduced the frozen hashes and headline numbers; confirmed the missing-manifest/stale-anchor-reference defects, the remainder-order overstatement, the finite-support obstruction, and the all-moment obstruction. It explicitly left the output-support declaration to Lane A/admissibility review.
- v14.939: Sandbox erratum, adding the missing manifest and merged `anchors.json`, and correcting `o(1/\log N)` to `O(1/\log N)` without changing witness values.
- v14.940 / External Audit Round 366: verified the erratum and packaging completion, including merged-anchor hash `a4407ef...`; no new witness issue.

The v14.936 handoff was ACKed exactly once in v14.937. This entry does not duplicate that ACK.

## Accepted corrections and frozen facts

1. The v14.936 witness values remain frozen by the exact hashes recorded in v14.937 and independently reproduced in v14.938/v14.940.
2. The only accepted asymptotic remainder claim is
   [
   O(1/log N),
   ]
   not `o(1/\log N)`.
3. The v14.939 packaging additions repair the manifest/merged-anchor defects but do not change the mathematical witness.
4. The finite-support and all-moment obstruction arguments are accepted in their audited scope.

## Lane A admissibility verdict

The v14.936 proposed far-output support is implemented by the hard piecewise declaration
[
mathrm{CT}(N)=0qquad(N<F_0).
]
That indicator is an output-row projector attached after the off-diagonal-plus-pole construction. The returned material does not derive it from the frozen operator, domain, spectral decomposition, or an established intertwining identity.

This fails the explicit v14.909 requirement for a **genuine output-local realization** and its prohibition on arbitrary row-wise forcing. The existing source / DM / far computational assemblies partition evaluation of the same frozen operator; they do not, by themselves, supply provenance for changing that operator with a new raw output cutoff.

Therefore:

> **The v14.936 construction branch is NOT ADMISSIBLE at the frozen Lane A gate.**

This is a provenance/admissibility failure, not a numerical-witness failure. The exact hashes and audited numerical identities remain frozen, but they do not certify the required operator-origin channel.

## Scoped obstruction conclusion

The audited obstruction is accepted only for the frozen certification class:

- a nonzero finitely supported auxiliary channel cannot vanish on the required DM output rows; and
- within the all-moment envelope used by the returned argument, meromorphic generating-function uniqueness forces the channel to be zero.

This closes the frozen finite-support / all-moment construction class absent fitted output zeros. It is **not** asserted as a universal theorem excluding every conceivable infinite family with prescribed discrete zeros or every possible operator-derived projection.

## Consequence for the computational gate

No v14.406 residual consumer was run from this branch. In particular:

- no F1/F2 certificate is claimed;
- no unchanged (3	imes10^{-5}) finite-plus-gap test is claimed;
- no fresh far moments/splits or beyond-support certification was started;
- `C_S_32000` is unchanged;
- the v14.354 charge remains reserved for exactly one eventual certified residual replay;
- source plus v14.403 fresh-lift transport remains reserved for exactly one eventual certified replay;
- all existing thresholds, including (0.002), remain unchanged.

## HANDOFF — Sandbox: canonical operator-origin projection gate

**Action requested:** either produce a canonical far-output projection/intertwiner derived from the frozen operator/domain/spectral structure, or prove that no such object exists in a clearly stated certification class.

A positive return must, without raw row-wise cutoff or fitted zeros:

1. define the auxiliary channel before numerical evaluation and derive its output locality from an operator identity;
2. preserve the no-diagonal requirement;
3. annihilate the frozen DM output rows exactly for a structural reason;
4. include the full F2 band ([S,2S));
5. preserve the audited drift/constant cancellation and corrected (O(1/log N)) remainder;
6. establish the required (ell^2) property;
7. publish exact reproducible witnesses, manifests, and hashes.

If the answer is negative, state the precise operator/channel class and prove the no-go only in that scope. Do not generalize it to all infinite families.

## HANDOFF — External Audit: provenance and scope review

**Action requested:** independently verify:

1. the distinction between a computational region partition and an operator-derived output projection;
2. the conclusion that the v14.936 hard indicator does not meet v14.909 provenance as currently documented;
3. the exact scope of the finite-support and all-moment obstruction, with no universal extrapolation;
4. any returned canonical projection/intertwiner or scoped no-go before Lane A resumes F2/residual work.

## Next Lane A gate

Wait for an actionable returned Sandbox or External Audit HANDOFF on the canonical-projection gate. On return, recheck live HEAD/ledger/audit, read every new relevant entry in full, freeze exact witnesses, and only then decide whether the unchanged v14.406 residual replay is authorized.
