# Cone Derivation Ledger v13.503 — General Even-Stratum Modulus Formula, and Why Mod 48 Changes Nothing on Either Side

## Scope

v13.423/v13.432 established the mod-24 doubling lift for the first even ramified Suzuki stratum (\(v_2(k)=1\)): \(k=2u\), \((u,6)=1\), and \(k\bmod24\) exactly recovers \(u\bmod12\). v13.432 §8 left open "the minimal modulus required to recover \(u\bmod12\) on each fixed \((v_2,v_3)\) stratum." This entry answers that in closed form for all strata \(v_2(k)=a\ge1\) at once, checks the \(a=2\) (mod 48) case explicitly as requested, and settles — generally, not just at mod 24 — whether the cone's unit-group double-cover construction (v13.501) can ever connect to any Suzuki even stratum (it cannot, for a structural reason that holds at every level, superseding the single mod-24 check in v13.502).

---

## 1. General modulus formula \([D]\)

For \(k\) with \(v_2(k)=a\ge1\) and \(3\nmid k\), write \(k=2^au\) with \((u,6)=1\), i.e. \(u\) a totative mod 12. Take
\[
\boxed{M_a=12\cdot2^a.}
\]
Since \(u=12m+r\) for \(r\in\{1,5,7,11\}\), and \(2^a\cdot12=M_a\),
\[
k=2^au=2^a(12m+r)=M_a\,m+2^ar,
\]
so
\[
\boxed{k\bmod M_a=2^a\,(u\bmod12),}
\]
exactly, with no ambiguity — reduction mod \(M_a\) recovers \(u\bmod12\) by dividing out the known power \(2^a\). This is the closed-form answer to v13.432 §8 target 1: **the minimal modulus for stratum \(a\) is \(12\cdot2^a\)**, and it works by the same clean mechanism as the \(a=1\) case (v13.423), not a new argument at each level.

Verified directly for \(a=1,2,3,4\) (\(M_a=24,48,96,192\)):

| \(a\) | \(M_a\) | residues \(2^a\{1,5,7,11\}\bmod M_a\) | \(\gcd(k,M_a)\) | recovered \(u\bmod12\) |
|---|---|---|---|---|
| 1 | 24 | \(\{2,10,14,22\}\) | 2 | \(\{1,5,7,11\}\) |
| 2 | 48 | \(\{4,20,28,44\}\) | 4 | \(\{1,5,7,11\}\) |
| 3 | 96 | \(\{8,40,56,88\}\) | 8 | \(\{1,5,7,11\}\) |
| 4 | 192 | \(\{16,80,112,176\}\) | 16 | \(\{1,5,7,11\}\) |

confirming the exact recovery and the residues' gcd with the modulus in every case.

---

## 2. The mod-48 case, as requested

For \(a=2\): \(k=4u\), \(k\bmod48\in\{4,20,28,44\}\), recovering \(u\bmod12\in\{1,5,7,11\}\) exactly — the direct analogue of the \(a=1\)/mod-24 lift, one stratum up, confirming this is legitimate and exactly the same style of doubling the totatives that v13.423 already used.

---

## 3. Why this never reaches the cone's unit group, at any level \([D]\)

v13.502 showed \(U(24)\cap\{2,10,14,22\}=\varnothing\) because every element of the Suzuki stratum residue set is even. That argument generalizes immediately:
\[
\gcd\bigl(2^ar,\,M_a\bigr)\ge2^a\ge2\qquad\text{for every }a\ge1,\ r\in\{1,5,7,11\},
\]
since \(2^a\mid2^ar\) and \(2^a\mid M_a=12\cdot2^a\). So the Suzuki-side residue at *every* stratum \(a\ge1\) is never a unit mod \(M_a\) (or mod any modulus divisible by 2), hence never lies in \(U(M_a)\) or any cone-realized unit group built the way v13.228/v13.501 built \(U(24)\).
\[
\boxed{
\text{For every }a\ge1:\quad
\{2^ar:r\in\{1,5,7,11\}\}\cap U(M_a)=\varnothing.
}
\]
This forecloses the whole family of "what about mod 48, mod 96, mod 192, …" questions at once: the answer is the same negative result as v13.502, for the same reason, at every stratum, not something that needs to be re-checked level by level.

---

## 4. Why the cone picture itself doesn't gain new content at mod 48 either

Separately from the unit-group question: the AM-GM cone realization (v13.500/v13.501) is built from \(u\bmod12\) directly (the four totatives, via the pair \((u,1)\)); it has no dependence on \(a\), \(b\), or the raw index \(k\). v13.432 §5 already established that the unit-core label \(u\bmod12\) (and hence \(\chi(u)\)) is the *same* invariant object on every \((a,b)\) stratum — only the modulus needed to *read* it off the raw Suzuki index changes (§1 above). Consequently there is no separate "mod-48 cone picture" to derive: the four cone points \((X_r,Y_r,T_r)\) for \(r\in\{1,5,7,11\}\) already are the complete geometric content, regardless of which stratum of the Suzuki construction is asking for the label.

---

## 5. Summary

| Question | Answer |
|---|---|
| Minimal modulus to recover \(u\bmod12\) on stratum \(v_2(k)=a\) (v13.432 §8 target 1) | \(M_a=12\cdot2^a\), closed form, verified \(a=1..4\) |
| Does the mod-48 (\(a=2\)) doubling lift work the same way as mod-24 (\(a=1\))? | Yes, confirmed directly |
| Does the cone's \(U(24)\)/\(U(48)\)/… unit-group double cover ever meet any Suzuki even-stratum residue set? | No, at any level, by \(\gcd(2^ar,M_a)\ge2^a\ge2\) |
| Does going to mod 48 add new cone geometry beyond v13.500/v13.501? | No — the cone depends only on \(u\bmod12\), which is stratum-independent |

## Guardrail

This closes the "try the next modulus" line of inquiry in general, not just for 48. It does not revisit or weaken v13.423/v13.430/v13.432 (whose stratum lift is exact and useful on the Suzuki side on its own terms), nor v13.500/v13.501 (whose cone realization stands independently). It only settles, generally, that the two constructions' moduli are structurally different objects and will not coincide by going further in the same direction.
