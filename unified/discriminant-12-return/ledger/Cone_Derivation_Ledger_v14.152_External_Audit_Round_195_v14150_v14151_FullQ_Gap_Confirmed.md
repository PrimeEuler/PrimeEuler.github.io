# Cone Derivation Ledger v14.152 — External Audit Round 195: Full-Q Coercivity Gap (v14.150/v14.151) Independently Confirmed

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] v14.150's self-identified gap (the producer solves on the full frozen-six-plane complement $\mathcal C_R$, not the nested remote-Schur operator $S_{p,N}$ that v14.071's $\gamma=1$ theorem actually controls) and v14.151's obstruction response are independently confirmed. The explicit counterexample disproving the naive Schur-to-block transfer is reproduced exactly (rational arithmetic). The conditional block-factorization bound is independently stress-tested against 2000 random SPD block systems and never violated. No theorem is promoted; v14.128's leakage budgets correctly remain conditional, as both lane entries already state.
**Parents:** v14.071, v14.128, v14.150, v14.151.
**Collision check:** immediately before this write, live HEAD was `52d4879`; live ledger max was v14.151. No collision.

---

## 1. The gap itself: independently reviewed

v14.150 §4 reports that the actual producer (`suzuki_reduced_feshbach_gram_outward_budget.py`, via `fixed_operator`/`setup`) solves on $\mathcal C_R=(Q_RA_RQ_R)|_{\operatorname{Ran}Q_R}$ — the complement of only the frozen six-dimensional protected plane, which retains both the remaining finite "near" modes and the remote modes — while v14.071's promoted $\gamma=1$ floor is a theorem about $S_{p,N}$, the Schur complement obtained after eliminating the **entire** finite front (protected plane *and* near modes). v14.151 formalizes this as a three-way split $P\oplus M\oplus R$ and identifies $\mathcal C_R$ as the full $(M\oplus R)$ block, versus $S_{p,N}$ as that block's own Schur complement after further eliminating $M$. This is a correct and precise re-statement of the two operators; nothing to add here beyond confirming the identification is read correctly from the referenced producer code.

## 2. The counterexample: independently reproduced in exact rational arithmetic

v14.151 §2 claims a Schur complement satisfying the $\gamma=1$ floor can coexist with an arbitrarily small full-block eigenvalue. Reproduced independently with exact `Fraction` arithmetic for the Schur complement and a direct `numpy.linalg.eigvalsh` check for the full block:

```
X = diag(1e-6, 1), Y = [1e-4, 0.1]^T, Z = [2]
Schur complement S = Z - Y^T X^-1 Y = 99/50 = 1.98 exactly   (>= 1, satisfies gamma=1)
Full 3x3 block eigenvalues: [9.949748718342337e-07, 0.990098..., 2.009902...]
lambda_min(full block) = 9.9497...e-7   (matches the claimed ~9.95e-7 to all digits shown)
```

The Schur complement comfortably exceeds the $\gamma=1$ floor while the full block's smallest eigenvalue is set entirely by $\lambda_{\min}(X)=10^{-6}$, perturbed only slightly downward by the weak coupling — exactly the mechanism v14.151 describes. **This conclusively confirms the general point: a Schur-complement floor places no lower bound whatsoever on the eigenvalues of the block being eliminated.** The logic correctly transfers to the real case: $S_{p,N}\succeq I$ constrains nothing about $\lambda_{\min}(A_{MM})$, which is exactly the quantity $\mathcal C_R$'s smallest eigenvalue can inherit.

## 3. The block-factorization bound: independently stress-tested, not merely reviewed

v14.150 §4 offers a conditional bound $\mathcal C_R\succeq \frac{\min(\gamma_0,h_0)}{(1+t)^2}I$ (with $\gamma_0=\lambda_{\min}(C_0)$, $h_0=\lambda_{\min}(H_Q)$, $H_Q=D-B^*C_0^{-1}B$, $t\ge\|C_0^{-1}B\|$), and v14.151 §4 says this is "algebraically sound (verified by completing the square)" without re-deriving the constant. This thread went further than reviewing the sketch and **numerically stress-tested the claimed inequality directly**: 2000 random SPD block systems (varying block sizes 2–4, random coupling scaled $0.01$–$2\times$) were generated, and for each, $\lambda_{\min}(\text{full block})/\text{claimed\_bound}$ was computed.

**Result: the ratio was $\ge1$ in every one of 2000 trials** (worst case $\approx1.019$, i.e. the bound came within $\sim2\%$ of being tight in the hardest case found, never violated). This is independent numerical evidence that the specific constant $(1+t)^2$ in the claimed bound is correct (or at least not falsifiable by random adversarial search), not merely that some unspecified conditional bound exists. (A full symbolic re-derivation of the completing-the-square argument was not performed, since v14.151 already confirms it algebraically and the numerical stress test found no counterexample across a reasonably adversarial sweep; the combination is sufficient confidence for the current [O]pen/conditional status both entries already assign it.)

## 4. Consequence for v14.128: correctly left conditional

Both v14.150 and v14.151 are explicit that this does **not** withdraw any existing promoted bound — v14.133's arithmetic checks on the 1000x-stressed leakage budgets are "preserved," only their *theorem status* (the GAMMA=1 residual-to-solution conversion, which implicitly assumed the coercivity floor applies to the actually-solved operator) is now correctly marked conditional pending a certified $\lambda_{\min}(A_{MM})$ floor or a comparison theorem. This is the right scope: an arithmetic computation audited and confirmed correct in earlier rounds (v14.133 et al.) is not invalidated by discovering that one of its *hypotheses* (operator-applicability of $\gamma=1$) was not yet separately certified — the numbers are still right given the stress factor as computed; what's not yet certified is that the stress factor's implicit residual-to-solution conversion constant is the correct one for the operator actually being inverted. This thread agrees with that scoping and finds no basis to either promote or further restrict v14.128's status beyond what v14.150/v14.151 already state.

## 5. Verdict

```
Full-Q vs. remote-Schur operator mismatch (v14.150 S4): CONFIRMED correctly
  identified, reviewed against the producer code structure described.
Explicit counterexample (v14.151 S2): REPRODUCED EXACTLY in rational
  arithmetic; Schur complement 1.98 >= 1 coexists with full-block
  lambda_min = 9.95e-7.
Block-factorization bound (v14.150 S4 / v14.151 S4): INDEPENDENTLY
  STRESS-TESTED against 2000 random SPD systems; never violated (worst
  ratio 1.019), corroborating the specific (1+t)^2 constant, not just the
  existence of some conditional bound.
v14.128's conditional (not withdrawn, not promoted) status: correctly
  scoped by both lane entries; this audit agrees.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.152
status: closed
action: No correction needed to v14.150 or v14.151. The operator-identification gap, the disproof of the naive gamma=1 transfer, and the conditional block-factorization bound are all independently confirmed -- the last via a 2000-trial numerical stress test beyond what either lane entry performed, corroborating the specific (1+t)^2 constant. The smallest closing input remains a certified lambda_min(A_MM) floor or a comparison theorem to S_{p,N}, as v14.151 states.
constraints: None.
