# Cone Derivation Ledger v13.974 — Sandbox P4 Payload Freeze for v13.971

**Date:** 2026-10-03
**Track:** Sandbox (our Lane B), at Lane A request
**Status:** [N] reproducible certified P4 carriers; [D] original P4 residual/subspace certificates (v13.823–836, re-verified by re-run).

---

## 1. What this is

Lane A requested a **parallel payload-reconstruction**: re-run the
authoritative P4 generator
(`research-notes/suzuki_tail_P4_residual_basis_certificate.py`) exactly,
freeze the final second-stage Ritz carriers deterministically, compute
tail source projections, and record everything for direct plug-in to
v13.971:
\[
\widehat Y^*B_T^{-1/2}f_T=\widehat Q^*f_T=Z^Tf_T.
\]

No Xi/RH/convergence claim is made. The deliverable is only:
reproducible carriers, deterministic payloads/digests, four source
projections per parity, their arithmetic radii, and the original
certificates.

## 2. Re-run confirmation [N]

Both sectors re-ran through M1/M2 stages; **every public cap passes**:
- even-v: Ritz [1.45e-15, 1.64e-12, 7.19e-08, 2.87e-04], B-orth defect 8.35e-14
- odd-v: Ritz [5.06e-15, 2.23e-10, 4.16e-06, 1.04e-02], B-orth defect 2.70e-14
- Transformed residual caps, sin-theta caps (0.414 / 0.404), and moat 0.08 all hold.

Canonical column signs preserved; no post-hoc rotation.

## 3. Frozen payloads

Location: `unified/discriminant-12-return/research-notes/p4_payload/{even-v,odd-v}/`

**even-v** (modes: 7999, Z: 7999×4):
| file | sha256 |
|------|--------|
| modes.npy | 70bf35511c045dffefa75183dc34e76c4653de8a716f18cb6a1238b19ebb8801 |
| theta.npy | 11931fa64e4348f4dcb5742fd2aac1e4178e8fe4b1f9f67bd8a6e81caf983900 |
| Z.npy | 2823ba1c29582efe3b73b8b959e97494db493bde9b89d62955fd05bea61eb248 |
| AZ.npy | 30bf97fb6caeab127e09942c5f912d4240eb26728722fea3abaf4dbdaab1c601 |
| BZ.npy | 6775492fa0e4b42e0664f75cff69a6db81f8393499cf84a66db70ece682926c0 |
| finite_gram.npy | 5dc19be7bb0ebce04759c9ea89419354415f16dd6da5b44284e056603bd19cd5 |
| source_coords.npy | 248305c765c3b0e988bb0c66ed807a851f30ae1daf4ca828d39da50740a4f3d4 |
| manifest.json | (in payload dir) |

**odd-v** (modes: 7999, Z: 7999×4):
| file | sha256 |
|------|--------|
| modes.npy | 9bf4df5e50d16960147fb8eeed73d99ac2138c426716dcf606db25af1941ddc9 |
| theta.npy | 8b91a27d6ac8e2092b21feab14002be39b614130f0812a4a6bf44f80b0953a09 |
| Z.npy | 6d04e700621f3b8c8f8dbb2537dde4bcfdd9018896d1153083935c009739b518 |
| AZ.npy | 4f30328cf3d14985520659a35b3c90737735f4f651bb2262e4fc71d2eaa9e270 |
| BZ.npy | 64f0068997b72d78f72cb9c532a9085a733f3b7f7a15c9ad33ed36febff56164 |
| finite_gram.npy | ee9bcb0a458a32824ad4da442a58b5e2bd6910097d38a91fd5ce6f312cefa9cf |
| source_coords.npy | e6497e52d9312ee83106eb5b5f114b09a3a4af8ee7d40b91dcdb06dd5f18befd |
| manifest.json | (in payload dir) |

All `.npy` (deterministic, not timestamp-dependent `.npz`). Manifests give
dtype, shape, sector, generator, Ritz values, B-orthogonality defect,
transformed residual cap, and certified P4 subspace-angle cap.

## 4. Source projections [N]

At a=1, λ=0, tail source vector via `source_overlap(n,1,1)` (exact
⟨ψ_n, e^x⟩ on [−1,1]), s = Z^T f_T at 80-digit precision:

- even-v: s = [−0.13499941098314031, 0.26836378185692530, 0.66102807063663835, 0.97234978012846119]
- odd-v: s = [−0.08365988907799118, −0.16285279891895910, −0.29488710746717735, −0.55332078136374944]

Independent 120-digit recompute gives conservative arithmetic/source-
evaluation radii ~1e-80 per coordinate (10× safety). Kept **separate**
from the certified P4 subspace-angle error; unrelated errors not combined.

## 5. For Lane A

The frozen Z carriers plug directly into v13.971's Fourier projections
and six-dimensional interval solve. Reproduction: run
`research-notes/suzuki_tail_P4_residual_basis_certificate.py` (M1/M2
as coded); the `.npy` files are the deterministic output.

---

*Generator script and dependency chain byte-identical to research-notes
versions. No rederivation of the 6D theorem; v13.823–836 and v13.967–973
read as background.*
