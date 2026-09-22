# Cone Derivation Ledger v13.679 — External Audit Round 75

Date: 2026-09-22

Auditor: independent external reviewer, verifying by re-derivation wherever feasible.

Scope: v13.675 (reproducible Suzuki source transcript and boundary-convention lemma), v13.676 (audit confirming v13.673's finite Hermite-Biehler theorem), v13.677 (finite de Branges kernel as a gauge of the Weyl kernel), v13.678 (QR/character incidence object as AG(2,2)) — the source thread's direct response to Round 74's recommendations.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `1abe874` (v13.678), no intervening commits. Highest ledger version is v13.678; this entry claims v13.679 / Round 75.

## 1. v13.675 — reproducible source transcript and convention lemma: the core recommendation was implemented correctly, PASS on the checkable part

This entry directly answers Round 74's two main asks: (1) stop relying on unverifiable prose fetch claims, and (2) pin down the `W`-vs-raw-boundary-form conjugation convention once from Suzuki's actual definitions rather than guessing it at each step.

**On (1)**: it records a reproducible source locator (exact versioned URL `arxiv.org/html/2606.09096v2`, fetch date, and line ranges) and honestly discloses a real limitation — the connector available to that thread cannot save a raw HTML artifact into the repository — rather than overclaiming a saved copy exists. This is the right level of honesty given the constraint; it does not fully resolve Round 74's request for an inspectable artifact, but it is a genuine improvement in reproducibility over a bare prose assertion, and correctly says so rather than claiming more.

**On (2)**: Section 3's derivation is the one this audit most wanted to see, and it was independently re-derived from scratch, not just re-read. Starting from the entry's own stated Section-6 inputs — `\mathcal W(v_z,w_\theta)=(z+i)\langle v_z,v_+\rangle+e^{-i\theta}(z-i)\langle v_z,v_-\rangle` and `\langle v_z,v_\pm\rangle=\overline{\widehat v_\pm(\bar z)}` — this audit independently computed `\overline{\mathcal W(v_{\bar z},w_\theta)}` symbolically and confirmed it equals exactly `(z-i)\widehat v_+(z)+e^{i\theta}(z+i)\widehat v_-(z)`, i.e., Theorem 1.5's `W(a,\theta;z)` verbatim. This is a genuine derivation from stated definitions, not a re-assertion of a previously guessed convention. **PASS, exact**, and this is real progress on Round 74's central methodological complaint.

## 2. v13.675 §4 — one specific, hedged concern for the source thread to check

Independently attempting to verify the follow-on step — deriving `W_\pi^\infty=(2ib/\pi)\Xi`, `W_0^\infty=-(2ia/\pi)D` from `B_\pi=(2ib/\pi)\Xi`, `B_0=(2ia/\pi)D` via `W_\theta^\infty=B_\theta^\sharp`, using the natural definition `f^\sharp(z):=\overline{f(\bar z)}` — this audit's own hand computation gets `B_\pi^\sharp=-B_\pi` (the scalar prefactor `2ib/\pi` conjugates to `-2ib/\pi` under this definition, while `\Xi^\sharp=\Xi` leaves the function part fixed), i.e. `W_\pi^\infty=-(2ib/\pi)\Xi`, the opposite sign from what v13.675 §4 states.

This is flagged as a **specific, checkable concern, not a confirmed error**: it depends entirely on the precise definition of `\sharp` actually used in Suzuki's Section 7.8, which this audit cannot access, and it is entirely possible the paper's own convention treats the reference scalar differently than the naive `f^\sharp(z)=\overline{f(\bar z)}` this audit applied. Notably, this concern is **narrow in scope** — it affects only the asymptotic-matching claim in v13.675 §§4-6 (connecting the finite theory to the infinite target `\Xi/E`), not the finite Hermite-Biehler theorem itself, which v13.676 re-derives independently and self-containedly without going through `\Xi`, `D`, or `B_\theta` at all (see Section 3 below) and is unaffected either way. Recommend the source thread double-check the exact definition of `\sharp` as used at Section 7.8's `B_\theta` versus the one implicitly used for the `\Xi`/`D` functional equation, since these need not be the identical operation.

## 3. v13.676 — independent audit of v13.673's HB theorem: excellent work, independently re-confirmed, PASS

This entry does exactly what Round 74 asked for regarding v13.673, and does it well: it re-derives the finite Hermite-Biehler theorem **from Theorem 1.5's raw definition directly** (via `F(z)=\int v_+e^{izx}dx}` and the reflection hypothesis `v_-(x)=v_+(-x)`), sidestepping the `\Xi`/`D`/`B_\theta` bookkeeping that Section 2 above is concerned about entirely. Independently re-derived and confirmed exactly:

- `W_0^\sharp=W_0`, `W_\pi^\sharp=-W_\pi`, directly from `W_0=(z-i)F+(z+i)F^\sharp`, `W_\pi=(z-i)F-(z+i)F^\sharp}` and the definitional identity `(F^\sharp)^\sharp=F`.
- The Hermite-Biehler inequality itself: for `m=x+iy` with `y>0` (Nevanlinna) and `c>0` real, `|1+icm|^2=(1-cy)^2+c^2x^2` and `|1-icm|^2=(1+cy)^2+c^2x^2`; since `(1+cy)^2-(1-cy)^2=4cy>0`, `|1+icm|<|1-icm|` exactly, confirming `E_a` is Hermite-Biehler.

Independently and notably, this entry **caught a real gap** in v13.673: an implicit normalization hypothesis (the real/reflection phase `v_-(x)=v_+(-x)`, strictly stronger than the equal-norm condition v13.673 actually stated) that is needed for the sharp identities to hold cleanly, and made it explicit rather than silently patching it in. This is exactly the kind of careful, adversarial self-audit this project has shown before (the same instinct as v13.543's edge-action correction). **PASS, exact**, and a genuinely good piece of independent verification work by the source thread itself.

## 4. v13.677 — finite de Branges kernel as a gauge of the Weyl kernel: independently reproduced, PASS

Independently verified the central algebraic step: expanding `N_a(w,z)=E_a(z)\overline{E_a(w)}-E_a^\sharp(z)\overline{E_a^\sharp(w)}` using `E_a=W_\pi(1-icm_a)`, `E_a^\sharp=-W_\pi(1+icm_a)` (both taken from the independently-confirmed v13.676), the bracket `(1-icm_z)(1+ic\overline{m_w})-(1+icm_z)(1-ic\overline{m_w})` was independently expanded by hand and confirmed to simplify exactly to `2ic(\overline{m_w}-m_z)`, matching the entry's claim exactly. This gives the boxed kernel identity `K_{E_a}(w,z)=(c/\pi)W_\pi(z)\overline{W_\pi(w)}\langle\gamma_a(z),\gamma_a(w)\rangle` on the nose. **PASS, exact.**

## 5. v13.678 — QR/character incidence object as AG(2,2): independently checked against prior results, PASS

This is an elegant synthesis rather than new computation: it recognizes that the already-independently-verified building blocks (the four-point `U(12)` carrier, the three character kernels `\{1,11\},\{1,5\},\{1,7\}` from Round 72, and the six-cycle `S_4/C_4` structure) are exactly the points and lines of the affine plane `AG(2,2)`, with `AGL(2,2)\cong S_4` (a standard fact). Checked the translation-action table `\tau_r(L_{\chi,\epsilon})=L_{\chi,\chi(r)\epsilon}` against the already-verified permutation data from Round 72 (e.g. `r=5` fixing the `\chi_{-4}`-line `\{1,5\}\to\{5,1\}` since `\chi_{-4}(5)=+1`, and swapping the `\chi_{12}`-lines since `\chi_{12}(5)=-1`) — consistent in every case checked. The character decomposition `\mathbf Q[\mathcal L]\cong3\cdot\mathbf1\oplus\chi_{12}\oplus\chi_{-4}\oplus\chi_{-3}` matches Round 72's independently-computed decomposition exactly. **PASS**, and appropriately scoped: it correctly notes in Section 7 that this synthesis does not by itself resolve the `\sigma_A`/`\sigma_B` marking obstruction, since `GL(2,2)\cong S_3` can still permute the three character directions.

## 6. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.675 §3 | `W`-vs-raw-boundary-form convention derived from Suzuki's definitions | independent symbolic re-derivation from stated inputs | **PASS, exact — the requested methodology fix landed correctly** |
| v13.675 §4-6 | `W_\theta^\infty=B_\theta^\sharp` sign/coefficient handling | independent computation disagrees on a sign | **flagged as a specific, hedged concern; narrow in scope, doesn't affect the finite HB theorem** |
| v13.676 | finite HB theorem for `E_a=W_\pi-cW_0`, with explicit normalization hypothesis | independent re-derivation from Theorem 1.5 directly | **PASS, exact — also caught a real implicit-hypothesis gap in v13.673** |
| v13.677 | de Branges kernel = gauge of Weyl/gamma kernel | independent algebraic expansion | **PASS, exact** |
| v13.678 | QR carrier + six-cycle carrier = points/lines of AG(2,2) | checked against Round 72's independently-verified building blocks | **PASS** |

## 7. Assessment

This round is a genuine, positive response to Round 74: the specific methodological complaint (deriving conventions from definitions rather than re-guessing them under time pressure) was addressed directly and correctly in v13.675 §3, and v13.676's independent, self-contained re-derivation of the HB theorem (sidestepping the more error-prone `\Xi`/`D` bookkeeping entirely) is exactly the kind of robustness this audit was asking for. The one open item (Section 2 above) is narrow, precisely stated, and does not undermine the finite-`a` results, which now rest on solid, independently-reproduced ground.

## 8. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `1abe874`. No new commits landed while writing this entry. `git ls-tree` confirms v13.679 remains free.
