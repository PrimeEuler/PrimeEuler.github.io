# Cone Derivation Ledger v13.511 — External Audit Round 39

## Scope

Independent audit of everything committed since my last push (`eaf7e5c`, v13.509) through the current head (`cdc633e`, v13.510): the response to Round 38's finding on v13.508.

**Headline: this is a good-faith, correct correction.** The project accepted Round 38's finding without dispute, reverted the over-promoted inequality, and replaced the unsupported certificate with a genuinely fail-closed scaffold containing zero hardcoded radii. One small, non-substantive numerical discrepancy found in the prose (not the code), noted below.

---

## 1. v13.510 (M16001 derived-radius rebuild gate) — verified

### 1.1 Acceptance and reversion

§1 explicitly accepts Round 38's finding ("v13.508's remote-Gram and far-tail radii were literals rather than outputs of a committed operation-count/magnitude derivation... its `[N-cert]` label and theorem promotion are unsupported") and restores
\[
\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,\qquad\operatorname{ind}_{\le0}(A_{a=1})\le6,
\]
matching exactly the reversion recommended in v13.509 §5.4. Confirmed correct.

### 1.2 Re-executed the replacement scaffold

`research-notes/suzuki_M16001_gamma_derived_radius_scaffold.py`, re-run directly:

```
u = 5.42101086242752217003726400434970855712890625E-20
gamma_7991 = 4.3319297801658348426383396946368578747878403877345991965161789854350858370867130E-16
remote row count = 991999
gamma_remote_rows = 5.3776...E-14
RuntimeError: FAIL-CLOSED: missing derived magnitude transcripts: finite_ldl, finite_schur, qn_formation, remote_gram, far_moments
```

- `gamma_7991` matches the entry's stated `4.331929780165835×10^-16` exactly to the digits given: confirmed.
- The `gamma_k = ku/(1-ku)` formula is the standard Higham floating-point dot-product error bound: correct.
- Read the full script source: the `TRANSCRIPT` dict has all five stage entries set to `None`, and `require_transcript()` unconditionally raises when any are missing. **No hardcoded QQ/QN/NN literal appears anywhere in this file** — confirmed by direct inspection, this is the structural fix Round 38 asked for: an empirical double/long-double discrepancy or a manually chosen safety multiplier is no longer an accepted input path at all, since the code has no slot for one.

### 1.3 One small discrepancy found

The entry's §2 states "the remote row count is 992000." Re-derived independently: rows run over odd `n` from 16003 to 1,999,999 inclusive (per v13.508 §1's stated `T={16003,16005,...}` stepping by 2, capped at 2,000,000), giving
\[
\frac{1{,}999{,}999-16{,}003}{2}+1=991{,}999,
\]
matching the script's own printed `991999`, not the prose's `992000`. This is a one-off transcription slip in the ledger text, not in the executable code (the code computes the correct value); it does not propagate anywhere since no certified quantity currently depends on it. Flagged for correction, not treated as a finding against the entry's substance.

---

## 2. Verdict

| Item | Status |
|---|---|
| Acceptance of Round 38's finding | Confirmed, unreserved, correctly reasoned |
| Reversion to `ind<=4` / `ind<=6` | Confirmed correct |
| New scaffold has zero hardcoded radii | Confirmed by direct source inspection |
| `gamma_7991` value | Re-executed, matches exactly |
| Remote row count in prose | Off by one (992000 vs. actual 991999); cosmetic only |

No further action needed on this round beyond the cosmetic note above. The exact next obligation stated in v13.510 §4 — instrument the M16001 replay to emit the five magnitude transcripts, then feed only those into the gamma scaffold — is the correct and only path back to the `ind<=3` claim, and nothing here suggests that obligation has been shortcut.

## Guardrail

No RH, GRH, or critical-line consequence follows from anything here. This entry only confirms that the Round 38 correction was made honestly and correctly, and notes one cosmetic slip for the record.
