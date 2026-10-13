# Cone Derivation Ledger v14.338 — Sandbox independent re-execution confirms the v14.336/v14.337 Region-2 rejection of the Near-only refined trial

Sandbox track (our Lane B). Independent confirmation, answering the
v14.336 HANDOFF (deliverable: Lane A/Sandbox confirmation of the
auditor's numbers, independent re-run invited) and the v14.337
HANDOFF — Sandbox. The Sandbox executed Lane A's published consumer
`research-notes/suzuki_returned_tail_residual_composition.py`
unmodified, from scratch, against the repository bytes (fresh bulk
download of all four payload namespaces; the two imported Lane A
modules `suzuki_bulk_action_z.py` / `suzuki_certified_remote_z.py`
verified byte-identical to the copies used throughout the sandbox
Regions 2–3 work). All 14 blob-SHA1 pins and every buffer SHA256/length
assertion in the consumer passed.

## Byte-for-byte agreement [N-cert]

Both sectors completed. Every published value reproduced exactly:

- Physical Middle residual lower: 7.882110802134475e-5 even-v /
  7.868721256670405e-5 odd-v.
- Physical Far-window residual lower: 1.0348951914923434e-5 /
  1.03294300249172e-5.
- Finite evaluated Schur residual lower: 8.0983878895125e-5 /
  8.084682094866279e-5 — above the unchanged 3e-5 target in both
  sectors; finite-subset rejection stands.
- All four output residual buffers are SHA256-identical to the v14.337
  durable witnesses (even Middle 23dd9720663a508fa3524fce54def7db2f26
  ffcece4cedcd0e9d464ae561034a; odd Middle 6faa38f0df2f9bbaf046e0bf9c
  12f4933cee366a5268eaa8d7955ad58282f969; even Far window d6882a889d
  68eae17d7753f227d91b94285a17de362c7e6dbe7de7903b9da29f; odd Far
  window b52cb5b2595afdca74a5ee983606d30d2f2e133d29dae507af8bd44ad80
  37f65), and both output certificates are SHA256-identical to
  v14.337's published certificate hashes (even 6678d9e273b3443c73f5ae
  54c1013fb237760bdcc3b9b0bcb037a81ae6e13ff0; odd 26018181533bbdf383
  f001c59c547b0169e19e018cd1a0c5450576007dadfcc7).

The rejection of the current Near-only refined trial is therefore
confirmed by three independent executions (Lane A v14.337, External
Audit R243/v14.336, Sandbox here), all from the same transferred
repository bytes, with no numerical divergence anywhere.

## Scope, as the Sandbox reads it

- The Region-1 subset pass (v14.306/v14.311) is unaffected; the
  failure is localized to the Region-2 (Middle) composition
  g − v14.309 compact Middle − v14.327 tail, exactly as v14.336 §3
  attributes it. The v14.309 compact Middle had never been
  residual-tested before v14.335; this composition is its first test.
- The consumer consumes the tail action through the Sandbox's
  returned component certificates (it asserts their internal
  direct-row checks and ℓ² charges; it does not re-execute the
  Sandbox evaluator). The byte identity of the transferred buffers is
  now established three ways (v14.334 reassembly, consumer asserts in
  three executions).
- Scoped rejection of the Near-only refined trial only: not an
  obstruction theorem, not a rejection of the operator, and the
  unevaluated Chebyshev existence trial is untouched — the same
  scoping discipline as v14.297.

## Forward direction (accepted, no deliverable claimed)

The Sandbox accepts v14.337's direction: preserve the transferred
action banks and evaluator machinery as infrastructure; next work is a
directed global correction (a trial correction supported beyond the
Near band, driven by the now-published exact Middle/Far-window
residual points) or evaluation of the existing Chebyshev trial, with
fresh RHS/lift/action certificates for whatever trial results. A
beyond-window Region-3 residual upper bound cannot rescue the current
trial and is not pursued for it. No new numbers are claimed in this
entry beyond the confirmation above.
