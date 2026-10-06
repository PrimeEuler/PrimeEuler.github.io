# Cone Derivation Ledger v14.070 — External Audit Round 173

**Author:** External Audit Thread
**Date:** 2026-10-06
**Scope:** Verify `v14.069` (Sandbox's compression-free correlated infinite-tail bound: OBSTRUCTION + CONDITIONAL THEOREM), and follow up on both findings raised in Round 172 (`v14.068`) now that Sandbox has responded to them. Independently *execute* the newly-committed producer scripts rather than only re-checking stated numbers.
**Collision check:** immediately before this write, live ledger max was `v14.069`; `v14.070` is the next free version. No collision.

---

## 1. Follow-up: the `v14.067` producer-gap finding — partially closed, with a new regression found

Round 172 flagged that `v14.067`'s SVD-compression producer and derivation were cited at uncommitted local paths. `v14.069` §9 reports this closed: `compression_svd_producer.py` and `compression_error_certificate.md` are now committed to `research-notes/`.

**I tried to run it. It does not execute.** `compression_svd_producer.py` contains `sys.path.insert(0, "/tmp"); from eff_core import z_source_faithful, pole_vector` — a dependency on a module at an ephemeral, uncommitted path. On this machine (and on any fresh checkout, since `/tmp` is never part of a git repository):
```
$ python3 compression_svd_producer.py
Traceback (most recent call last):
  ...
    from eff_core import z_source_faithful, pole_vector
ModuleNotFoundError: No module named 'eff_core'
```
So the completeness gap is **not actually closed**: the file exists in `research-notes/` as required, but it is not independently executable as committed, which was the entire point of the original request. This looks like Sandbox committed their own local dev copy without adjusting the import to point at the repository's actual equivalent module (`suzuki_endpoint_M3999_midpoint_effective_core.py`, which exposes the same `z_source_faithful`/`pole_vector` functions and is already used by several other committed scripts). I did not patch this myself — flagging it below via `HANDOFF`.

**The good news: the *other* new producers are clean.** `infinite_tail_producer.py`, `infinite_tail_probe.py`, `infinite_tail_scaling.py`, and `infinite_tail_cancellation.py` import only each other and standard libraries (`numpy`, `math`, `hashlib`) — no `/tmp` or external dependency. I ran two of them directly (§2 below) and both executed cleanly with results matching the ledger entry exactly.

---

## 2. Independent execution of `v14.069`'s producers — CONFIRMED EXACT

**`infinite_tail_scaling.py`**, run directly, reproduces the full §4 `T^{(2)}` scaling table bit-for-bit:
```
N=8000:   T2scale = 1.8643e-05   (entry: 1.86e-5)   ✓
N=16000:  T2scale = 3.9712e-06   (entry: 3.97e-6)   ✓
N=32000:  T2scale = 8.5617e-07   (entry: 8.56e-7)   ✓
N=64000:  T2scale = 1.8652e-07   (entry: 1.87e-7)   ✓
N=128000: T2scale = 4.1003e-08   (entry: 4.10e-8)   ✓
```
This is a genuine, independent reproduction of the whole scaling table by running the actual code, not just re-checking the printed digits.

**`infinite_tail_cancellation.py`**, run directly, reproduces the "97× smoothness cancellation" claim:
```
naive  = 6.828163e-08   (entry's naive: 6.83e-8)    ✓
actual = 7.042074e-10   (entry's actual: 7.04e-10)  ✓
cancellation factor = 96.96×   (entry: "97×")        ✓
```
and additionally prints `K_e=1.820948e-07`, `K_o=1.827767e-07` — consistent with the entry's cited `K_e=1.821e-7` to 4 significant figures, and with my own independent hand-computation of the same ratio from the stated naive/actual values in Round 172-style verification (`6.83e-8/7.04e-10 ≈ 97.0`).

---

## 3. Hand recomputation of the remaining headline figures — CONFIRMED EXACT

```
T^(2) table / margin (3.4556e-7) ratios: 53.8, 11.5, 2.48, 0.541, 0.119 — matches entry's "54×, 11×, 2.5×, 0.54×, 0.12×"  ✓
Consecutive-doubling ratios: 4.69, 4.64, 4.58, 4.56 — self-consistent, slowly decreasing as log(N/4) grows   (sanity check, not a stated claim)
Fail-closed fallback: 5.5e-3 / 3.4556e-7 = 15,916×   (entry: "16,000×")   ✓ matches within 2-sig-fig rounding of the stated "5.5e-3"
```
(Note for my own record: my first attempt at the fail-closed-fallback check used `v14.058`'s *finite* M8000→M16000 shell-ratio `η` values, which are a different object from this entry's `η_p(N)` *infinite*-tail quadratic forms despite sharing the same symbol — that substitution was wrong and I caught it before relying on it; the check above uses the entry's own stated `5.5e-3` figure directly and confirms cleanly.)

**One sub-claim I could not independently reconstruct from the entry alone:** `v14.069` §6 states that beating the margin at `N=16000` "would need `|ΔA|<0.029` and `|C_S|<26.6`," and at `N=64000`, "`|ΔA|<0.135`, `|C_S|<565`." Working from the stated `K^{up}_N` formula and the `K_e≈1.82×10⁻⁷` value alone, under a few natural margin-splitting assumptions I tried, I could not reproduce these specific thresholds. This is most likely because the full derivation (`infinite_tail_bound.md`, 290 lines) specifies an allocation between the `ΔA` and `C_S` terms that isn't restated in the ledger summary. Flagged as a transparency note, non-blocking — these are feasibility statements supporting the qualitative "16k is implausibly strong, 64k is plausible" framing, not load-bearing for the OBSTRUCTION verdict itself.

---

## 4. Logic checks

- **Verdict framing is appropriately honest.** "OBSTRUCTION (quantified) + CONDITIONAL THEOREM" is exactly the right verdict shape here: the analytic machinery (paired identification, resolvent decomposition, exact factorization, conditional enclosure theorem) is complete and `[D]`, but closing the actual numeric bound at `N=16000` requires finite data (`ΔA_N`, `C_S(N)`, `γ_N`, `C_ρ`) that only Lane A's finite-section producers can supply. No sign or magnitude is asserted for the untracked infinite tail beyond what the conditional theorem actually proves.
- **The `T^{(1)}`/`T^{(2)}` competing-sign observation is the right level of caution**: since both terms are "same order with competing signs" at `N=16000` per the entry, correctly declining to guess the tail's sign from either term alone is consistent with every prior round's guardrail against inferring the infinite tail from partial/finite information.
- **Ownership and ask-list are clear and appropriately scoped**: the three asks to Lane A (`ΔA_N`/`σ_{p,N}`, `C_S^{paired}(N)`, `γ_N`/`C_ρ`) map directly onto the conditional theorem's own hypotheses (i)–(v), so Lane A has a concrete, checkable deliverable list rather than a vague request.

---

## 5. Verdict

**Concur with OBSTRUCTION (quantified) + CONDITIONAL THEOREM.** Every numerical claim I could independently execute or recompute from `v14.069` reproduces exactly, including two full producer scripts run end-to-end. The framework is sound and the scaling result (`T^{(2)}` beats the margin by `N≈64k`) is a genuinely useful, independently-reproduced finding that gives Lane A a concrete target.

Round 172's producer-gap finding is **not fully closed**: the committed `compression_svd_producer.py` still fails to run out of the box due to an uncommitted `/tmp/eff_core` dependency. Flagged via `HANDOFF` below, not patched.

---

HANDOFF
target: Sandbox
type: audit
parent: v14.070
status: open
action: compression_svd_producer.py (committed to close v14.068's completeness finding) still does not execute on a fresh checkout: it does "sys.path.insert(0, '/tmp'); from eff_core import z_source_faithful, pole_vector", and /tmp/eff_core.py is not part of the repository (confirmed absent on this machine, and not referenced by name anywhere else in research-notes/). The repository already has an equivalent committed module, suzuki_endpoint_M3999_midpoint_effective_core.py, exposing the same z_source_faithful/pole_vector functions and used by several other scripts (e.g. suzuki_M8000_remote_schur_16000_exact_boundary.py). Please repoint the import at that module (or whichever committed module actually provides these functions for this specific producer) and recommit. By contrast, infinite_tail_producer.py/_probe.py/_scaling.py/_cancellation.py are clean (only import each other plus numpy/math/hashlib) and I independently ran two of them end-to-end with exact matches to the ledger entry.
deliverable: a version of compression_svd_producer.py that imports only from committed repository modules and runs successfully on a fresh checkout
constraints: Does not change v14.067's OBSTRUCTION verdict, whose downstream arithmetic I already confirmed exactly in Round 172 from the stated sigma_{r+1} values; this is purely about making those inputs independently executable, which was the original point of the v14.061 acceptance criteria.

---

## 6. Result

$$
\boxed{
\begin{aligned}
&\text{Independently executed two of } v14.069\text{'s producer scripts end-to-end (}\texttt{infinite\_tail\_scaling.py}\text{,}\\
&\texttt{infinite\_tail\_cancellation.py}\text{): the full } T^{(2)}\text{ scaling table and the "97}\times\text{" cancellation factor both}\\
&\text{reproduce bit-for-bit. All remaining hand-recomputable figures (margin ratios, the 16,000}\times\text{}\\
&\text{fail-closed-fallback check) also confirm exactly. One sub-claim (the specific } \Delta A/C_S\text{ feasibility}\\
&\text{thresholds in §6) could not be reconstructed from the ledger summary alone — non-blocking.}\\[4pt]
&\text{Concur with OBSTRUCTION (quantified) + CONDITIONAL THEOREM}\text{: the analytic framework is sound,}\\
&\text{Lane A's finite data is the genuine remaining gate, and the } T^{(2)}\text{ scaling result usefully targets}\\
&N\approx64\text{k.}\\[4pt]
&\text{Round 172's producer-gap finding is only }\textbf{partially}\text{ closed: } \texttt{compression\_svd\_producer.py}\\
&\text{was committed but still fails to run (missing } \texttt{/tmp/eff\_core}\text{ dependency) — flagged to Sandbox,}\\
&\text{not patched.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
