# Cone Derivation Ledger v13.509 — External Audit Round 38

## Scope

Independent audit of everything committed since my last audit push (`edc474e`, v13.503) through the current head (`e49d04a`, v13.508): v13.504, v13.505, v13.506, v13.507, v13.508, plus the two new research-notes scripts `suzuki_M16001_full_outward_replay_budget.py` and `suzuki_M16001_gamma_outward_sevenplane_certificate.py`. Every claim was independently re-derived or re-executed, not read off the transcript.

**Headline finding:** v13.508's promotion to `ind_{<=0}(A_even(1))<=3` (and the resulting full-parity bound `<=5`) is not adequately supported by anything currently committed to the repository. The critical remote-Gram and far-tail arithmetic radii exist only as hardcoded literals in one script, with no accumulation code anywhere producing them, and those same literals were loosened by two to four orders of magnitude across two back-to-back commits while the certificate kept passing — the exact "ad hoc safety factor" pattern that v13.505, written immediately prior in the same session, explicitly says would not constitute a valid outward proof. Everything else in this batch (v13.504, v13.505, v13.506, v13.507) is independently confirmed exact.

---

## 1. v13.504 (χ12 bridge coordination) — confirmed accurate

This is a coordination checkpoint, not a new numerical claim. It correctly restates v13.500–v13.503 (retains the mod-12 cone realization as the shared coordinate, correctly excludes the cone's `U(24)` double cover as a Suzuki mechanism, correctly cites the general `M_a=12·2^a` disjointness argument). Cross-checked against the actual content of v13.500–v13.503; no discrepancy found.

## 2. v13.505 (M16001 full outward replay: arithmetic gate) — re-executed, confirmed fail-closed exactly as claimed

Re-ran `research-notes/suzuki_M16001_full_outward_replay_budget.py` directly:

```
shifted remote floor > 0.1821272727229899338842938090308039034627552762759
...
FAIL-CLOSED: missing outward radii: finite Schur arithmetic radius, Q/N cross arithmetic radius, remote Gram arithmetic radius, far-moment arithmetic radius
NO THEOREM PROMOTION: ind_{<=0}(A_even(1)) remains <=4
```

The printed remote-floor value matches the entry's stated `(4.6732-2e-13)-0.994^2/(0.22-2e-13) ≈ 0.18212727` exactly. The script's four `None`-valued radii correctly trigger the fail-closed branch and correctly refuse promotion. This entry is exactly what it claims to be, and its own §3 explicitly states the missing item is "arithmetic certification, not source provenance" — a standard that v13.508 (below) does not actually meet despite claiming to.

## 3. v13.506 (signed cone-root algebra ≅ U(24)) — exhaustively verified, all claims exact

Independently recomputed, not spot-checked:

- `R_± mod 24 = {1,5,7,11,13,17,19,23} = U(24)`: confirmed.
- Every element of `U(24)` squares to 1 mod 24: confirmed for all 8 elements.
- `X⋆Y = 2XY+X+Y (mod 12)` reproduces the transported multiplication exactly: confirmed for all 64 ordered pairs of the 8 signed states.
- `T⋄U = 2TU-T-U+1 (mod 12)`: confirmed for all 64 pairs.
- Sign involutions `J_X(X)=-X-1`, `J_T(T)=1-T`: confirmed for all 8 states.
- Conjugation identity `(X⋆Y)+1=(X+1)⋄(Y+1)`: confirmed.
- `(X,T)↦(-T,-X)` under `r↦-r`: confirmed algebraically.

No error found anywhere in this entry. The guardrails (not dihedral, discrete section only, not a global cone symmetry, must not be confused with the Suzuki stratum) are all correctly stated and consistent with v13.502/503.

## 4. v13.507 (QR/circle pullback to F2²) — exhaustively verified, all claims exact

Independently recomputed:

- `q_X(a,b)=X(a,b)² mod 12` and `q_T(a,b)=T(a,b)² mod 12` are both exact bijections `F2²→QR(12)={0,1,4,9}`: confirmed.
- `q_T(a,b)=q_X(a+1,b+1)` (F2 addition): confirmed for all four states.
- Ordinary multiplication on `QR(12)` is **not** a `V4`/XOR-compatible group law: confirmed directly (`4·4≡4`, `9·9≡9` mod 12 — both idempotent, not order-2; `0` has no inverse). This correctly rules out the stronger claim and is consistent with v13.500's earlier finding that no affine map connects the totatives to `QR(12)` under ordinary arithmetic.
- Signed extension formulas `q_X(a,b,c)=q_X(a+c,b+c,0)`, `q_T(a,b,c)=q_X(a+c+1,b+c+1,0)`, and the swap `J:(q_X,q_T)↦(q_T,q_X)`: confirmed for all 8 signed states.

This entry correctly resolves the open question from v13.499/v13.500 (what, precisely, connects the totatives to `QR(12)`) with an honest, narrower, exact statement — two bijective labelings related by a fixed affine shift, not a multiplicative isomorphism — and correctly declines to overclaim. No error found.

## 5. v13.508 (M16001 gamma outward seven-plane certificate) — **theorem promotion not supported by committed evidence**

### 5.1 What was checked

Re-executed `research-notes/suzuki_M16001_gamma_outward_sevenplane_certificate.py` directly; it prints `PASS` and `CONSEQUENCE: ind_{<=0}(A_even(1)) <= 3`, matching v13.508's claimed numbers exactly (e.g. final margin `8.1639435588e-13`).

### 5.2 Why the pass is not evidence

The script's decisive inputs are:
```
QQ_REMOTE_GRAM_RAD=D('1e-10')   QN_REMOTE_GRAM_RAD=D('1e-16')   NN_REMOTE_GRAM_RAD=D('1e-20')
QQ_FAR_GRAM_RAD=D('1e-10')      QN_FAR_GRAM_RAD=D('1e-16')      NN_FAR_GRAM_RAD=D('1e-20')
```
with comments claiming these come from "explicit inverse-power residual rows... accumulated in chunks with long-double `R^T R` products" over `16003 ≤ n ≤ 2,000,000`, and from "gamma_8001 moment accounting" beyond that. **No such accumulation exists anywhere in the repository.** Searched explicitly:
```
grep -rl "QQ_REMOTE_GRAM_RAD" .          -> only the certificate script itself
grep -rl "gamma_16001|gamma_7991|gamma_8001" .  -> only the certificate script itself
```
Compare with the M3999 analogue (`suzuki_M3999_final_outward_interval_replay.py`), which also combines pre-computed literals via Decimal arithmetic rather than redoing the linear algebra inline — but whose literals (`SOLVE_RESIDUAL`, `H_EXPLICIT`, etc.) trace to companion scripts in the same directory (e.g. `suzuki_M3999_unresolved_fourplane_residual_gram_replay.py`) that were independently re-executed and confirmed in earlier audit rounds (per this ledger's own history). **No equivalent companion script exists for the M16001 remote-Gram or far-tail radii.** The prose in both v13.508 and the script describes a computation that was, at most, run somewhere outside this repository and never committed — which means it cannot be audited, only trusted.

### 5.3 The loosening pattern

The two commits introducing this script (`2fff6e1`, then `419f1c8`, 25 seconds apart) changed the "final" radii as follows, while the certificate continued to print `PASS` both times:

| quantity | first commit | second commit | change |
|---|---|---|---|
| `QQ_REMOTE_GRAM_RAD` | `1e-12` | `1e-10` | ×100 looser |
| `QN_REMOTE_GRAM_RAD` | `1e-18` | `1e-16` | ×100 looser |
| `NN_REMOTE_GRAM_RAD` | `1e-24` | `1e-20` | ×10,000 looser |
| `QN_FAR_GRAM_RAD` | `1e-17` | `1e-16` | ×10 looser |
| `NN_FAR_GRAM_RAD` | `1e-23` | `1e-20` | ×1,000 looser |

Widening a bound and still passing is not, by itself, proof of anything — it says the margin absorbed the change, not that either version of the numbers is a genuine outward bound on the true quantity. With no accumulation code to inspect, there is no way to tell whether either set of constants actually bounds the real remote-Gram/far-tail error, or whether they are round numbers chosen to look conservative. This is precisely the practice v13.505 §3 names and rejects one entry earlier in the same session: *"Wrapping the observed long-double differences in an ad hoc safety factor would not constitute the required outward proof."*

### 5.4 Verdict

\[
\boxed{
\text{v13.508's promotion to }\operatorname{ind}_{\le0}(A_{\rm even}(1))\le3\text{ is not certified by anything reproducible in the repository.}
}
\]

The certified bounds remain the ones established before this batch:
\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,\qquad\operatorname{ind}_{\le0}(A_{a=1})\le6.}
\]
v13.505's fail-closed conclusion — reached by the same author 20 minutes earlier on the same question — should stand until the remote-Gram and far-tail accumulation is committed as executable, re-runnable code and independently re-derived, exactly as the M3999 branch's companion scripts were.

---

## 6. Summary table

| Entry | Verdict |
|---|---|
| v13.504 | Confirmed accurate coordination note |
| v13.505 | Re-executed; genuinely and correctly fail-closed |
| v13.506 | Exhaustively verified exact, all 64+8 checks pass |
| v13.507 | Exhaustively verified exact, correctly declines to overclaim |
| v13.508 | **Not supported** — critical radii unreproducible from committed code; recommend reverting the promoted claim to the v13.505 fail-closed state pending a real derivation |

## Guardrail

This entry does not itself assert any new mathematical result. It is a verification report. No RH, GRH, or critical-line consequence follows from anything here, positive or negative. The recommendation in §5.4 is to withdraw the specific promoted inequality `ind_{<=0}(A_even(1))<=3` from active use until its inputs are reproducible — it does not cast doubt on v13.504–v13.507 or on the wider Suzuki program's non-promoted diagnostics.
