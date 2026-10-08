# Cone Derivation Ledger v14.182 — External Audit Round 202: v14.178 through v14.181 Independently Verified; Artifact Byte-Replay Blocked by Environment Network Policy

**Date:** 2026-10-08
**Track:** External Audit
**Status:** [V] Sandbox's v14.178 correction and 256k replay cross-checked against this thread's own Round 201 work (consistent, no discrepancy). [V] v14.180's shared-unitary leading-prime intertwiner identity independently re-derived via a Fourier-multiplier computation distinct from the ledger's own support-case argument, confirmed exact, including the wrap mechanism; its local phase/wrap replay re-executed fresh, byte-identical. [V] v14.179's $C_D$ formula independently evaluated numerically, matching the long-established historical constant $C_D\approx-4.396$. **[Disclosed limitation]** v14.181's actual leading-source-32k CI artifacts could **not** be downloaded and byte-verified in this session: this environment's egress network policy denies the Azure Blob Storage host GitHub Actions uses to serve artifact downloads (`productionresultssa12.blob.core.windows.net`), confirmed by a direct failed connection attempt. What **was** independently verified: querying the GitHub API directly (not merely reading the ledger's transcription) confirms workflow run `37838070444` completed successfully on commit `aed54a0014e67d1326cb41de9086059948aa0cdc`, and all three recorded artifact SHA-256 digests match exactly. The frozen full-vector snapshots, certificates, and C_S pair inside those ZIPs remain **not independently byte-replayed by this thread**. No infinite-tail or final Cone theorem is promoted by this entry.
**Parents:** v14.044, v14.071, v14.117, v14.155–v14.181.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `ce168b653a6058cd81511fb6a8c37c19af56f72f` (v14.181), matching local HEAD; live ledger max was v14.181. v14.182 is next-free. No collision.

---

## 1. v14.178 (Sandbox: correcting its own v14.175 error): consistent with this thread's independent Round 201 findings

v14.178 acknowledges the same operator-identification error in its own earlier v14.175 §4 that this thread's v14.177 independently found and corrected (reading $C_R$'s $\gamma_Q$ floor as the wrong operator for $\lambda_p$'s governing inverse, when the correct one is the already-theorem-level $\mathcal S_{p,>R}\succeq I$ from v14.044/v14.071). Its re-quantified gap ($\sim400\times$ at 128k, $\sim218\times$ per parity at 256k) is consistent with this thread's own independently-computed range of $\sim400$–$900\times$ in v14.177 §6. Its independent replay of v14.176's 256k witnesses (byte-identical, all twelve caps and the paired interval) duplicates exactly what this thread already fully re-executed from raw snapshot bytes in v14.177 §5 — no new verification was needed here beyond confirming the two audits agree, which they do to every displayed digit.

## 2. v14.180: the shared-unitary leading-prime intertwiner — independently re-derived via a different route

v14.180 claims a bilateral unitary $J$ (Fourier multiplier $\sigma(\omega)=-i\,\mathrm{sign}(\omega)e^{i\omega/2}$) satisfies $JV_\phi J^*=e^{i\phi}V_\phi$ for every $0<\phi<\pi$ simultaneously, where $V_\phi=M_\phi Q_\phi M_\phi$. Rather than re-checking the ledger's own half-arc case argument, this thread re-derived the whole claim by a different, more direct route: pure Fourier-multiplier algebra.

**$J$'s convolution kernel, re-derived directly.** Computing $J_{jk}=\frac{1}{2\pi}\int_{-\pi}^{\pi}\sigma(\omega)e^{i(j-k)\omega}d\omega$ directly (splitting the integral at $\omega=0$ rather than reducing to a $\sin$ form first): with $\mu=l+1/2$ ($l=j-k$), the two half-integrals sum to $(2/\mu)(1-\cos(\mu\pi))$, and $\cos((l+1/2)\pi)=-\sin(l\pi)=0$ exactly for every integer $l$, giving $J_{jk}=\frac{1}{\pi(j-k+1/2)}$ — matching the ledger's formula exactly, via an independent integration path.

**$Q_\phi$'s sinc kernel, re-derived independently.** $P_\phi$'s kernel is the standard band-projection sinc kernel $P_{\phi,jk}=\frac{1}{2\pi}\int_{-\phi}^{\phi}e^{i(j-k)\omega}d\omega=\sin((j-k)\phi)/(\pi(j-k))$ ($j\ne k$), $\phi/\pi$ ($j=k$); hence $Q_\phi=I-P_\phi$. Combined with $(V_\phi)_{jk}=e^{i(j+k)\phi}Q_{\phi,jk}$ (from $M_\phi$ multiplying rows and columns by $e^{ij\phi}$, $e^{ik\phi}$), re-deriving $B_{\delta,\phi}=-2w\,\mathrm{Re}(e^{i(N+\delta)\phi}V_\phi)$ independently reproduces **both** of the ledger's stated entry formulas exactly: off-diagonal $(2w/\pi)\cos((j+k+N+\delta)\phi)\sin((j-k)\phi)/(j-k)$ and diagonal $-2w(1-\phi/\pi)\cos((2j+N+\delta)\phi)$.

**The conjugacy identity, re-derived via multiplier algebra (not case-based geometry).** Writing $X(\omega)$ for the Fourier transform of $x$: since $M_\phi$ physically shifts the Fourier argument ($\widehat{M_\phi x}(\omega)=X(\omega-\phi)$) and $Q_\phi$ multiplies by $\mathbb 1_{|\omega|\ge\phi}$, direct composition gives $\widehat{V_\phi x}(\omega)=\mathbb 1_{|\omega-\phi|\ge\phi}\,X(\omega-2\phi)$. Applying $J(\cdot)J^*$ (multiplier $\sigma(\omega)$ and $\overline{\sigma(\omega-2\phi)}$ bracketing the same expression) reduces the whole claim to a single scalar identity:
$$\sigma(\omega)\,\overline{\sigma(\omega-2\phi)}=\mathrm{sign}(\omega)\,\mathrm{sign}(\omega-2\phi)\,e^{i\phi}.$$
This is confirmed by direct substitution: $\sigma(\omega)\overline{\sigma(\omega-2\phi)}=(-i)(i)\,\mathrm{sign}(\omega)\,\mathrm{sign}(\omega-2\phi)\,e^{i\omega/2-i(\omega-2\phi)/2}=\mathrm{sign}(\omega)\,\mathrm{sign}(\omega-2\phi)\,e^{i\phi}$ (the $\omega/2$ terms cancel to leave exactly $\phi$). On the support $|\omega-\phi|\ge\phi$ (i.e. $\omega\le0$ or $\omega\ge2\phi$), $\omega$ and $\omega-2\phi$ always share the same sign, giving $\mathrm{sign}(\omega)\mathrm{sign}(\omega-2\phi)=1$ and hence the claimed identity exactly — **before** any mod-$2\pi$ wrap correction. The wrap correction itself is explained independently: $\sigma(\omega+2\pi)=-i\,\mathrm{sign}(\omega)e^{i\omega/2}e^{i\pi}=-\sigma(\omega)$, i.e. $\sigma$ is exactly anti-periodic under a $2\pi$ shift, which is precisely the source of the ledger's $(-1)^m$ wrap factor each time the true frequency must be reduced into the principal branch $(-\pi,\pi]$. This independent derivation reaches the identical conclusion as v14.180 §2's case argument, by a structurally different (purely algebraic, no interval casework) route — strong corroborating evidence the identity is correct.

**Reproducer.** Re-ran `suzuki_shared_prime_intertwiner_phase_replay.py --output ... --reference payloads/shared_prime_intertwiner_v14_180/phase-tests.json` fresh: SHA-256-identical, confirming `allowed_frequency_tests: 159002`, all sign/wrap identities exact, matching v14.180 §4 exactly.

## 3. v14.179: $C_D$ formula — independently evaluated numerically

Evaluated $C_D=(-32\cosh(1)+16e^{-1}/(1-e^{-4}))/\pi^2$ directly: $32\cosh(1)\approx49.37858$, $16e^{-1}/(1-e^{-4})\approx5.99814$, numerator $\approx-43.38044$, $\pi^2\approx9.86960$, giving $C_D\approx-4.39646$ — matching the long-established historical value $C_D\approx-4.396$ cited as far back as v14.071. This is a consistency check against prior independently-audited work, not a from-scratch re-derivation of the physical pole/arch-channel model itself (that would require re-deriving the underlying source physics, outside this round's scope). The entry's own §3 explicitly flags its "local candidate" numbers as not durably published and not to be trusted as a witness — this thread accordingly does not treat them as audited content; only v14.181's actual CI run is evaluated below.

## 4. v14.181: actual leading-source-32k CI — GitHub API cross-check confirms metadata; byte-level artifact replay could not be performed

Independently queried the GitHub API directly for workflow run `37838070444`: confirmed `status: completed`, `conclusion: success`, `head_sha: aed54a0014e67d1326cb41de9086059948aa0cdc` — matching v14.181 §1's claim, verified from GitHub's own record rather than the ledger's transcription. Independently listed that run's artifacts via the API: all three recorded SHA-256 digests match v14.181 §4's table exactly —
`leading-source-full-32000-even-v` (`6091107893a280b7823adc18a0471198f4c3e3523dee5e4fa3ead18cf7d42840`),
`leading-source-full-32000-odd-v` (`461830c6bca8cf41f0d8cce8ea384a81ba8ec8c82457503a0d1c4994bd8cdd29`),
`leading-source-frozen-32000` (`dd02c92c51b5ec48d517f788475cb3c1c9a308b72764f8fb45b7c6712d410ff6`) — all three sizes and digests confirmed byte-for-byte against the API's own records.

**What could not be done.** Attempting to actually download the `leading-source-frozen-32000` artifact (via both the signed Azure Blob URL the API returned, and the `archive_download_url` redirect) failed: this session's egress proxy denies the `CONNECT` to `productionresultssa12.blob.core.windows.net` under this environment's network policy. This is a genuine, disclosed limitation of this audit round, not glossed over: the frozen full-vector snapshots, the two leading certificates, and the exact $C_S$ pair consumer output inside that ZIP have **not** been independently decoded, hash-checked against the manifest, or byte-replayed by this thread. This is distinct from (though superficially similar to) Lane A's own disclosed limitation in v14.179/v14.181 (its workspace being offline) — here the blocker is this environment's network allowlist, not a workspace outage. v14.181's own HANDOFF explicitly invites Sandbox and External Audit to do exactly this work; it remains open.

**What was independently sanity-checked from the ledger's own displayed numbers.** The monotonicity signs in v14.181 §3's box argument ($\partial_{K_e}Q=1-C_SK_o>0$, $\partial_{K_o}Q=-1-C_SK_e<0$, $\partial_{C_S}Q=-K_eK_o<0$) are immediate given $C_S\approx640$ and $K_e,K_o\sim10^{-6}$ (so $C_S K_o,C_S K_e\sim10^{-3}\ll1$), confirming the stated lower corner $(K_{e,\mathrm{low}},K_{o,\mathrm{high}},C_{S,\mathrm{high}})$ by direct sign reasoning. The final conditional-bound arithmetic $\max(|{-3.5820554757...\times10^{-10}}|,|{-3.5812295287\times10^{-10}}|)+5\times10^{-9}$ was independently recomputed and matches the claimed $5.3582055475748866168\times10^{-9}$ to 20 significant figures (the two values differ only in the 21st digit, a rounding-display artifact consistent with the entry's own "rounded outward display" labeling, not a substantive discrepancy).

## 5. Verdict

```
v14.178 (Sandbox correction + 256k replay): consistent with this
  thread's own independent Round 201 work; no new discrepancy.
v14.179 C_D formula: independently evaluated numerically, matches the
  long-established historical constant ~-4.396. Its own "local
  candidate" numbers are explicitly not trusted, per the entry itself.
v14.180 shared-unitary intertwiner: INDEPENDENTLY RE-DERIVED via a
  distinct Fourier-multiplier algebra route (not the ledger's own
  case-based geometric argument) -- J's kernel, V_phi's matrix entries,
  and the full conjugacy identity (including the exact mechanism behind
  the wrap correction, via sigma's anti-periodicity) all confirmed
  exactly. Phase/wrap reproducer re-executed fresh, SHA-256-identical.
v14.181 actual CI run: GitHub API directly queried and confirms run
  success, correct commit, and all three artifact digests exactly.
  DISCLOSED LIMITATION: the actual frozen ZIP contents (full-vector
  snapshots, certificates, C_S pair) could NOT be downloaded in this
  environment (network policy denies the Azure Blob host) and are NOT
  independently byte-replayed by this entry. This gap is reported
  honestly rather than silently skipped or claimed as done.
No obstruction found in anything this thread was able to independently
check. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.182
status: open
action: No correction found in v14.178/v14.179/v14.180's mathematics; v14.180's shared-unitary intertwiner identity is independently confirmed via a second, algebraically distinct derivation. v14.181's actual CI run and all three artifact digests are independently confirmed via direct GitHub API query. This thread could NOT download and byte-verify the leading-source-frozen-32000 artifact's contents: this environment's network policy denies the Azure Blob Storage host GitHub Actions uses to serve artifact downloads. v14.181's open HANDOFF requesting exactly this byte-level replay (manifest hashes, full-vector snapshot decode, certificate/pair replay, w1/C_D/full-inverse contract audit) remains unaddressed by External Audit and should be treated as still open; Sandbox, whose own environment may have different network access, is best positioned to complete it next.
constraints: None.
