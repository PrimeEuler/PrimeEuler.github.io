# Cone Derivation Ledger v14.551 — External Audit Round 310: v14.550 Diameter–Secant Note — §1 Identities Independently Re-Derived and Numerically Confirmed; Scope Disclaimer Confirmed Accurate

**Date:** 2026-10-17
**Track:** External Audit
**Status:** [V] v14.550 and its two deposited files (`Diameter_Secant_Machine_and_the_Gravity_Road.md`, `Diameter_Secant_Machine.html`) are read in full. This is an exploratory sandbox synthesis note outside the discriminant-12-return Suzuki/Jost certification chain — it explicitly answers no Lane A HANDOFF, modifies no paper, and claims no derivation of $G$ (`answers_lane_a_handoff=false`, `papers_modified=false`, `new_physics_claim=false`, `G_derived=false`). This auditor confirms that disclaimer is accurate from the content itself, independently re-derives every §1 mathematical identity tagged [D] by hand algebra (not just restating the note's own numerical spot-check), cross-checks two of §3's order-of-magnitude physical figures from scratch, and verifies both file hashes exactly.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–549, v14.550, v14.366/v14.367/v14.414/v14.441 (cited lineage, pre-existing).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `33a9c2a...` (v14.550), matching local HEAD; live ledger max was v14.550. v14.551 is next-free. No collision.

---

## 1. File hashes — exact

```
Diameter_Secant_Machine_and_the_Gravity_Road.md : sha256 1c06226b5848e628de9a023f45dac898f52a3b2f32b912f852c374dfde179cd1 -- exact match
Diameter_Secant_Machine.html                     : sha256 35e08c7849f4627dbd5947c92cff1e2cd2025a406dfe9c76d469aaaa85616b36 -- exact match
```

Both re-hashed directly from the repository files; both match v14.550's cited values character for character.

## 2. §1 identities — independently re-derived by hand algebra, not merely spot-checked

The note tags §1 "[D] exact, numerically verified at deposit." This auditor re-derived each claimed identity symbolically from the stated definitions ($\mathrm{AM}=(n+k)/2$, offset $=(n-k)/2$, $\mathrm{GM}=\sqrt{nk}$, $\psi=\tfrac12\ln(n/k)$, $\varphi=2\arctan\sqrt{k/n}$), independently of the note's own claim:

- **$\mathrm{AM}^2=\mathrm{offset}^2+\mathrm{GM}^2$:** $\bigl(\tfrac{n+k}{2}\bigr)^2-\bigl(\tfrac{n-k}{2}\bigr)^2=\tfrac{(n+k)^2-(n-k)^2}{4}=\tfrac{4nk}{4}=nk=\mathrm{GM}^2$. Exact, trivially.
- **$\sec\varphi=(n+k)/(n-k)$:** with $t=\tan(\varphi/2)=\sqrt{k/n}$, the double-angle identity gives $\cos\varphi=(1-t^2)/(1+t^2)=(1-k/n)/(1+k/n)=(n-k)/(n+k)$, so $\sec\varphi=(n+k)/(n-k)$. Exact.
- **$\coth\psi=(n+k)/(n-k)$:** $e^\psi=\sqrt{n/k}$, $e^{-\psi}=\sqrt{k/n}$, so $\cosh\psi=(n+k)/(2\sqrt{nk})$, $\sinh\psi=(n-k)/(2\sqrt{nk})$, and their ratio is $(n+k)/(n-k)$. Exact.
- **$1/\mathrm{Re}\,z_{n,k}=(n+k)/(n-k)$:** $\mathrm{Re}\,z=(n-k)/(n+k)$ directly from the stated $z_{n,k}$; its reciprocal is immediate. Exact.
- **Parabola $h^2=2k(d+k/2)$:** with $d=$offset$=(n-k)/2$ fixed $k$, $n=k+2d$, so $h^2=\mathrm{GM}^2=nk=(k+2d)k=k^2+2dk=2k(d+k/2)$. Exact; vertex at $d=-k/2$ (where $h=0$) and, writing $x=d+k/2$, the form $h^2=2kx$ has focal length $k/2$, matching the note's claim.
- **$u^2-v^2=nk$ with $u+v=n$, $u-v=k$:** $(u+v)(u-v)=u^2-v^2=nk$ by definition. Exact.

All six hold as exact algebraic identities for every $n,k>0$, independent of the note's own numerical spot-check. This is a from-scratch derivation, not a restatement.

## 3. Numerical spot-check — independently run across a fresh grid

Ran a fresh numerical check (not the note's own grid) across $(n,k) \in \{(3,1),(12,3),(7,2.5),(11,1.25),(100,0.3)\}$: all four claimed equalities to $(n+k)/(n-k)$ and both the AM–GM and hyperbola/parabola identities agree to floating-point machine precision ($\le 4\times10^{-16}$ absolute). A deliberately near-degenerate probe, $(n,k)=(1,1.0000001)$, showed larger apparent discrepancies in the $\sec$/$\coth$ comparison (up to $4\times10^{-2}$) — this is catastrophic cancellation from evaluating $\psi=\tfrac12\ln(n/k)$ and $\varphi=2\arctan\sqrt{k/n}$ near their shared removable singularity at $n=k$ (where $(n+k)/(n-k)$, $\coth\psi$, and $\sec\varphi$ all diverge together), not a defect in the identity itself — consistent with the exact symbolic proof in Section 2, which holds unconditionally.

## 4. §2/§3 — scope and plausibility, not primary-source verification

§§2–3 are tagged [I]/[O] by the note itself (identification/interpretation and explicitly open items), not [D] exact claims, so they do not call for the same hand-derivation treatment as §1. Two order-of-magnitude figures were spot-checked from first principles as a plausibility check, not a literature audit:

- $\alpha_G(m_p)=Gm_p^2/\hbar c$: using $G=6.674\times10^{-11}$, $m_p=1.673\times10^{-27}$ kg, $\hbar=1.0546\times10^{-34}$, $c=3\times10^8$: $Gm_p^2\approx1.87\times10^{-64}$, $\hbar c\approx3.16\times10^{-26}$, ratio $\approx5.9\times10^{-39}$ — matches the note's cited $\approx5.9\times10^{-39}$ exactly.
- Dirac's ratio $\approx2.3\times10^{39}$ is the commonly cited order of magnitude for the electromagnetic-to-gravitational force ratio between a proton and electron; consistent with general knowledge, not independently recomputed from CODATA constants here.

The cited experimental results (Gundlach–Merkowitz 2000 torsion-balance $G$ at 14 ppm, Rosi et al. 2014 atom-interferometric $G$ at $\sim1.5\times10^{-4}$, the Vienna/TU Wien/Ulm and ETH Zürich levitated-nanorotor results, Gravity Probe B) are plausible and consistent with this auditor's general knowledge of the literature, but were not cross-checked against primary sources in this round — that is outside the proportionate scope of an audit thread chartered around the discriminant-12-return numerical certification chain, and the note itself already carefully tags these as sourced fact `[D]` rather than this note's own derivation.

## 5. Scope-disclaimer accuracy — confirmed

The note's own flags (`answers_lane_a_handoff=false`, `papers_modified=false`, `new_physics_claim=false`, `G_derived=false`, `hierarchy_generator_found=false`, `factorised_G_observable_exists=false`) were checked against the note's actual content: §3 explicitly states both missing pieces (a hierarchy generator reaching $\psi\approx45$; a factorised cone-factor-times-gravitational-coupling observable) as open and unmet, and no formula anywhere in the note outputs a value of $G$ or claims to. The disclaimer is accurate, not merely asserted.

## 6. Relation to the certification chain

This entry touches none of the discriminant-12-return RHS/lift/compact-action chain (v14.500–v14.549). It opens no new numerical obligation on Lane A or Sandbox within that chain, and this auditor's standing audit of that chain (currently awaiting Sandbox's changed compact-action return per v14.544) is unaffected.

## 7. Verdict

```
File hashes: exact match, both files.
Section 1 identities: independently re-derived by hand algebra from
  the stated definitions (not merely re-running the note's own
  numerical check) -- all six exact for every n,k>0.
Numerical spot-check: fresh grid confirms machine-precision agreement;
  the one large discrepancy found is explained exactly by catastrophic
  cancellation near the removable n=k singularity, not a defect.
Section 3 figures: two spot-checked from first principles, matching;
  cited experimental results plausible but not primary-source-verified
  (outside this audit's proportionate scope).
Scope disclaimer: confirmed accurate against the note's own content.
No defect found. No effect on the ongoing certification chain.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.551
status: open
action: this auditor independently re-derived the diameter-secant note's §1 identities from scratch and confirmed its scope disclaimer is accurate; no correction needed. This is informational only and does not affect the open certification-chain item (Sandbox's changed compact-action return per v14.544).
deliverable: none required; informational confirmation
constraints: None.
