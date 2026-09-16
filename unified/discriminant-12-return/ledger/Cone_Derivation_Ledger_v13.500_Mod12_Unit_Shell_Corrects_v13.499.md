# Cone Derivation Ledger v13.500 — The Mod-12 Unit Shell Supersedes the v13.499 QR-Doubling Construction

## Scope

Correction. v13.499 §4 constructed an ad hoc map (double a quadratic residue mod 12, halve, reduce to a canonical row label) to reproduce a claimed radius set \(\{1,3,4,6\}\), and flagged that construction as "a confirmed numeric match, not yet a derived mechanism." That flag was the right call on the construction as written, but the construction itself was unnecessary: the actual source of \(\{1,3,4,6\}\) (and of the companion set \(\{0,2,3,5\}\)) is already derived, exactly, in `unified/discriminant-12-return/papers/Discriminant_12_Return_v0.3.5.tex`, §"The mod-12 unit shell," and rendered in the existing figure `figures/mod12_v4_cone_triple.png` (generator: `figures/discriminant12_mod12_v4_cone_triple.py`). This entry replaces the v13.499 §4 construction with the correct one and re-examines the proposed QR(12) connection under it.

---

## 1. The exact construction (already published, re-verified here)

For \(r\in U(12)=\{1,5,7,11\}\), take the factor pair \((r,1)\) (equivalently \((1,r)\)) in the AM-GM cone
\[
\Pi_\pm(x,y)=\Bigl(\tfrac{x-y}2,\pm\sqrt{xy},\tfrac{x+y}2\Bigr).
\]
With \(x=r,y=1\):
\[
\boxed{T_r=\frac{r+1}2,\qquad X_r=\pm\frac{r-1}2,\qquad Y_r=\pm\sqrt r.}
\]
This is exact — no rounding, no auxiliary quadratic-residue map. Direct evaluation:

| \(r\) | \(X_r=(r-1)/2\) | \(T_r=(r+1)/2\) | \(Y_r^2=r\) |
|---|---|---|---|
| 1 | 0 | 1 | 1 |
| 5 | 2 | 3 | 5 |
| 7 | 3 | 4 | 7 |
| 11 | 5 | 6 | 11 |

so
\[
\boxed{\{X_r:r\in U(12)\}=\{0,2,3,5\},\qquad\{T_r:r\in U(12)\}=\{1,3,4,6\}.}
\]
Both target sets from the v13.499 exchange are reproduced exactly, as literal cone coordinates of the four totative unit-shell points, with no floor, ceiling, or doubling operation needed anywhere. Re-executed the generator script's arithmetic directly (`c=(r-1)/2`, `R=(r+1)/2`, `K4=r` in `discriminant12_mod12_v4_cone_triple.py`) and confirmed it matches this table and the rendered figure exactly (segment X-positions \(0,\pm2,\pm3,\pm5\) labeled \(\sqrt1,\sqrt5,\sqrt7,\sqrt{11}\); side-view heights \(1,3,4,6\)).

Consistency check against the cone identity: \(T_r^2-X_r^2=\left(\frac{r+1}2\right)^2-\left(\frac{r-1}2\right)^2=r=Y_r^2\), confirming \(X_r^2+Y_r^2=T_r^2\) holds exactly for all four points, as it must.

---

## 2. Why this supersedes v13.499 §4

v13.499 §4 built \(u(q)=2q\bmod12\) for \(q\in\mathrm{QR}(12)=\{0,1,4,9\}\) and took radius \(=u(q)/2\), landing on \(\{1,3,4,6\}\) — correct arithmetic, but the doubling map had no independent motivation, as that entry's own guardrail already said. The present construction shows the target numbers were never QR-shaped in origin at all: they are simply \((r\pm1)/2\) for the totatives \(r\) themselves, arising directly from the elementary cone map applied to the pair \((r,1)\). No detour through \(\mathrm{QR}(12)\) is needed to produce either \(\{0,2,3,5\}\) or \(\{1,3,4,6\}\).

\[
\boxed{X_r=\frac{r-1}2,\qquad T_r=\frac{r+1}2\qquad\text{directly, for }r\in\{1,5,7,11\}.}
\]

---

## 3. Re-examining the proposed link to \(\mathrm{QR}(12)=\{0,1,4,9\}\)

With the correct, exact derivation in hand, the question of whether \(\{0,2,3,5\}\) or \(\{1,3,4,6\}\) relate to \(\mathrm{QR}(12)\) can be asked cleanly, without an intervening construction to muddy it.

As sets:
\[
\{0,2,3,5\}\cap\{0,1,4,9\}=\{0\},\qquad \{1,3,4,6\}\cap\{0,1,4,9\}=\{1,4\}.
\]
Neither is a literal subset or equal to \(\mathrm{QR}(12)\); the overlap is partial and small. Both \(X_r\)-values and \(T_r\)-values are four-element subsets of a bounded integer range chosen by an arithmetic condition (unit-shell membership) unrelated by construction to quadratic residuosity mod 12 — the totatives satisfy \(r\equiv\pm1\pmod{2}\) and \(\gcd(r,12)=1\), not any square condition. Checked directly: \(r^2\bmod12=1\) for every totative (since \((\mathbf Z/12)^*\cong V_4\) is 2-torsion, per v13.478), so squaring the totatives themselves gives the single value \(\{1\}\), not \(\mathrm{QR}(12)\).

No linear map \(q\mapsto ar+b\pmod{12}\) sending the four totatives to the four QR values (in any order) exists either: solving for \(a,b\) from any two of the four required correspondences and checking against the rest fails for every attempted pairing (tested computationally; no consistent \((a,b)\) reproduces all four).

**Conclusion:** the \(X_r\) and \(T_r\) sets are genuine, exact, and already-published cone coordinates of the mod-12 unit shell. Their numeric resemblance to \(\mathrm{QR}(12)=\{0,1,4,9\}\) (small integers, small overlap, same cardinality) is not supported by any derivation found here, and a direct check rules out the simplest possible mechanism (an affine map mod 12). This should be treated as coincidence pending an actual construction, exactly as the published paper's own guardrail already insists for the unit-shell figure: *"The geometry carries the labels but does not define their modular group law."* The same discipline applies to any claimed quadratic-residue structure: not yet shown.

---

## 4. Guardrail

This entry corrects the derivation route in v13.499 §4; it does not change v13.499 §1–3 (the totative/antidiagonal-circle and \(\chi_{12}\)-evenness material), which stands independently and is untouched by this correction. The mod-12 unit-shell coordinates \(T_r,X_r,Y_r\) are exact and already part of the published paper text; no new theorem is promoted here. The question of whether \(\mathrm{QR}(12)\) plays any genuine role in the discriminant-12 geometry remains open and unresolved by this entry — it is flagged as checked-and-not-found-here, not disproved in general.
