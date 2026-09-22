# Cone Derivation Ledger v13.680 — External Audit Round 76: Source PDF Confirms Corollary 1.6

Date: 2026-09-22

Auditor: independent external reviewer. This round is different from prior ones: the project owner uploaded `research-notes/2606.09096v2.pdf`, the actual arXiv PDF of Suzuki's paper, directly into the repository. This is the first round in this citation dispute where the auditor has genuine, direct, inspectable source access rather than relying on any thread's prose transcription.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `5a0c053` (the PDF upload commit), no intervening commits. Highest ledger version is v13.679; this entry claims v13.680.

## 1. Corollary 1.6 is definitively `\xi/(\xi+\xi')` — the four-way citation dispute is closed

Extracted and independently rendered page 7 of the PDF (both as plain text and as a high-resolution page image, cross-checked against each other). The verbatim text of Corollary 1.6, equation (1.12), reads:

> **Corollary 1.6.** If one can choose `\theta=\theta(a)` and `\phi(a,z)` (`\neq\infty` for any `a>0` and `z\in\mathbb C`) such that
> `\lim_{a\to\infty}e^{\phi(a,z)}W(a,\theta;z)=\dfrac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)}` (1.12)
> holds uniformly on every compact subset `K\subset\mathbb C`, then RH holds.

This is unambiguous, and it **confirms v13.280 and v13.666, and refutes v13.279 and v13.660**. The four-way flip (v13.279 -> v13.280 -> v13.660 -> v13.666, tracked across Rounds 73-74 of this audit) is now closed with a definitive source check, not another prose claim:

\[
\boxed{
R_{\rm Suz}(z)=\frac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)}.
}
\]

Consequence: **every entry in the v13.667-v13.679 chain, which was built on this exact target after v13.666's retraction, was using the correct asymptotic target all along.** That work does not need to be redone on this account.

## 2. The finite boundary-triple formulas (Section 6.5) are verbatim-confirmed exactly as transcribed

Rendered page 22 as a high-resolution image (the plain-text extraction mangles the overbar/hat diacritics on this page, which briefly looked like a discrepancy before the image render resolved it — see Section 4). The verbatim equations (6.2)-(6.3) are:

\[
W(v_z,w_\theta)=(z+i)\langle v_z,v_+\rangle_{T_a}+(z-i)e^{-i\theta}\langle v_z,v_-\rangle_{T_a}=0,
\]
\[
\langle v_z,v_\pm\rangle_{T_a}=\overline{\langle v_\pm,v_z\rangle_{T_a}}=\overline{\widehat v_\pm(\bar z)}=\int_{-a}^a\overline{v_\pm(x)}\,e^{-izx}\,dx.
\]

Both match v13.675 §3's transcription exactly, including the conjugate bar in (6.3) that a plain-text extraction pass had appeared to omit. **v13.675's Section 3 derivation — the conjugation convention `W(a,\theta;z)=\overline{\mathcal W(v_{\bar z},w_\theta)}` — is confirmed to be a correct, faithful reading of Suzuki's own equations, not a plausible-looking guess.** This is a strong result for the source thread: the specific methodological fix Round 74 asked for was not just internally consistent, it is actually correct against the primary source.

## 3. Section 7.8's raw boundary-form formula is verbatim-confirmed exactly

Rendered page 27 as a high-resolution image. The reproducing kernel, boundary form, and `C_\theta` formulas read exactly:

\[
K(w,z)=\frac{E(z)\overline{E(w)}-E^\sharp(z)\overline{E^\sharp(w)}}{2\pi i(\bar w-z)},\qquad E(z)=\xi(1/2-iz)+\xi'(1/2-iz),
\]
\[
W(K(\bar z,\cdot),W_\theta)=(z+i)K(\bar z,-i)+e^{-i\theta}(z-i)K(\bar z,i)=-\frac{e^{-i\theta/2}}{\pi i}\big(C_\theta E(z)-\overline{C_\theta}E^\sharp(z)\big),
\]
\[
C_\theta=\xi(3/2)\cos(\theta/2)+i\xi'(3/2)\sin(\theta/2),
\]

with the `\theta=\pi` specialization stated explicitly as `(2i/\pi)\xi'(3/2)\xi(1/2-iz)`. This matches the `B_\theta`/`C_\theta` formulas used throughout v13.670, v13.675, and v13.676 exactly, including the `\theta=\pi` value. **Confirmed exact.**

## 4. Auditor's own false alarm from Round 75, resolved

Round 75 (v13.679 §2) flagged a specific, hedged concern that a scalar prefactor might flip sign under the `\sharp` operation in a way that would contradict v13.675 §4. Re-examining with the actual source page image now available: that concern was based on this auditor's own assumption about how `\sharp` distributes over a coefficient-times-function product, applied to a text-extracted (and, as Section 2 shows, diacritic-mangled) version of the surrounding material. With the clean page image in hand, no such discrepancy is visible in Suzuki's own stated formulas — the concern is **withdrawn**, not because the underlying algebra was checked and found wrong, but because its premise (a specific claimed mismatch) is not actually supported once the source is read cleanly.

## 5. A more important, structural finding: the finite-to-infinite `W_\theta^\infty` construction (v13.668 onward) is the project's own extension, not a literal transcription of Suzuki

This is worth stating plainly, because it changes how the v13.667-v13.679 chain should be read going forward, without at all undermining its correctness as independent mathematics.

Suzuki's own Section 7.8 is explicitly titled **"Heuristics for formula (1.12)"** — his own word, "heuristic," in the section heading. Reading the full page: Suzuki does **not** construct an explicit infinite-volume analogue `W_\theta^\infty(z)` and relate it to `B_\theta(z)` via `W_\theta^\infty=B_\theta^\sharp}`, the way v13.668 §2 assumes ("Now use the Section-6 convention: `W_\theta^\infty(z)=\overline{B_\theta(\bar z)}=B_\theta^\sharp(z)`"). Instead, Suzuki's own route is more indirect: he defines `f_z` via `\widehat f_z(t)=K(\bar z,t)/E(t)`, shows `f_z\in V(0)\subset L^2(0,\infty)`, and relates it to the finite-`a` construction through an explicit but different substitution `v_z:=\pi f_z/E(\bar z)` (visible at the very bottom of page 27) plus results **cited from reference [14]** rather than re-derived in this paper. His derivation of the `\theta=\pi` special case gives `(z-i)\widehat f_{+i}(z)-(z+i)\widehat f_{-i}(z)=\frac{2\xi'(3/2)}{\pi^2i}\cdot\frac{\xi(1/2-iz)}{E(z)}`, and the paper's own words immediately after are: "this identity **strongly suggests** (1.12)" — not "proves," not "equals."

**This means the `W_\pi^\infty`, `W_0^\infty`, `E_a^{HB}`, and the finite Hermite-Biehler apparatus built in v13.667-v13.679 are the project's own reasonable and self-consistent mathematical construction, built to be compatible with Suzuki's heuristic and his `\theta=\pi` formula, but they are not a line-by-line transcription of an argument that exists in the paper.** This is not a criticism — building an independent, rigorous finite-`a` de Branges/boundary-triple theory that is *consistent with* a heuristic asymptotic target is legitimate and useful work, arguably more valuable than the heuristic itself, and the finite-`a` results (v13.661, v13.667, v13.676, v13.677 — all independently verified by this audit in Rounds 74-75) stand on their own regardless of this distinction. But the *labeling* matters: future entries should describe the `W_\theta^\infty`/`E_a^{HB}` construction as "the project's boundary-triple model of Suzuki's heuristic," not as "Suzuki's formula," to avoid a future round mistaking project-original modeling for source transcription (the way this exact confusion happened with the Corollary 1.6 target across four prior entries).

## 6. Summary

| Claim | Verification | Outcome |
|---|---|---|
| Corollary 1.6 target `=\xi/(\xi+\xi')` | verbatim quote from the actual PDF, page 7, text and image cross-checked | **DEFINITIVELY CONFIRMED — closes the 4-way citation dispute** |
| v13.675 §3 conjugation convention, eq. (6.2)-(6.3) | verbatim quote, page 22 image | **PASS, exact — confirms Round 75's positive assessment** |
| Section 7.8 `B_\theta`/`C_\theta` raw formula | verbatim quote, page 27 image | **PASS, exact** |
| Round 75's flagged sign concern (v13.675 §4) | re-examined against clean source image | **withdrawn — no longer supported** |
| `W_\theta^\infty=B_\theta^\sharp` construction (v13.668 onward) | checked against Suzuki's actual Section 7.8 argument | **is the project's own extension of Suzuki's explicitly-labeled "heuristic," not a transcription — relabel accordingly, does not invalidate the finite-`a` results** |

## 7. Recommendation

1. Update the standing citation for Corollary 1.6 across the ledger (v13.279, v13.660, and any entry inheriting their target) to point to this entry and v13.666/v13.675 as the settled source, rather than leaving four contradictory historical entries as the most recent word.
2. The uploaded PDF at `research-notes/2606.09096v2.pdf` is now the authoritative, inspectable source artifact this audit has been requesting since Round 73 — future citation disputes on this paper should be resolved by reading it directly (page images render cleanly via `PyMuPDF`/`fitz`; plain-text extraction loses diacritics on overbars/hats and should not be trusted alone for equations with conjugation).
3. Going forward, label the `W_\theta^\infty`/`E_a^{HB}` finite-de-Branges apparatus as the project's own model consistent with Suzuki's heuristic (Section 5 above), not as his own construction.

## 8. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `5a0c053`. No new commits landed while writing this entry. `git ls-tree` confirms v13.680 remains free.
