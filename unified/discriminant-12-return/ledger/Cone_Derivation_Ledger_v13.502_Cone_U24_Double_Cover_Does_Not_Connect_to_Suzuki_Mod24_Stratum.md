# Cone Derivation Ledger v13.502 — The Cone's U(24) Double Cover Does Not Connect to the Suzuki Mod-24 Stratum

## Scope

v13.501 realized the already-proven \(U(24)/U(12)\) double cover (v13.228) on the AM-GM cone. Before handing that picture to the χ12 phase-bridge thread as a candidate Suzuki-side input, check directly whether it says anything about the existing Suzuki mod-24 diagnostics (v13.423, v13.430, v13.432, v13.433). It does not — the two constructions use "mod 24" for two disjoint, non-overlapping arithmetic reasons. This entry records the check so the connection is not re-attempted without new input.

---

## 1. Two different mod-24 residue sets

**Cone/algebra side (v13.228, v13.501):** the multiplicative unit group
\[
U(24)=\{1,5,7,11,13,17,19,23\},\qquad|U(24)|=8,
\]
all odd, all coprime to 24, split as \(A\times B\) with \(A=U(12)\)-lift, \(B=\{1,13\}\).

**Suzuki side (v13.423, v13.432 §4):** the first even ramified stratum, indices \(k\) with \(v_2(k)=1\), \(3\nmid k\), written \(k=2u\) with \((u,6)=1\). On this stratum \(k\bmod24\in\{2,10,14,22\}\), i.e.
\[
S=\{2,10,14,22\},\qquad|S|=4.
\]

Direct check:
\[
\gcd(k,24)=2\quad\text{for every }k\in S,
\]
so **every element of \(S\) is even and shares a factor of 2 with 24** — none of them is a unit mod 24. Consequently
\[
\boxed{U(24)\cap S=\varnothing.}
\]

---

## 2. Why they look similar but aren't the same object

Both constructions ultimately recover the same four V4 labels \(\{1,5,7,11\}\) and the same character table \((\chi_0,\chi_{-4},\chi_{-3},\chi_{12})\) via \(H_4\) — but by two structurally different maps:

- Cone/algebra: \(r\in U(24)\) is itself a unit; the sheet label is read off by \(r\bmod12\) directly (reduction of a unit to a unit).
- Suzuki: \(k\in S\) is *not* a unit; the label is read off by first dividing out the forced factor of 2 (\(u=k/2\)) and only then reducing \(u\bmod12\). The mod-24 residue is doubled precisely *because* one power of 2 has already been stripped from the index — an artifact of the 2-adic stratification (v13.432 §5, the general \((a,b;u\bmod12)\) decomposition), not a use of the unit group \(U(24)\) at all.

So the numeral "24" plays two different roles: on the cone/algebra side it is the modulus of an extended *unit group*; on the Suzuki side it is the modulus needed to see a *doubled odd label* after removing one factor of 2 — the same reason the (now-superseded) v13.499 §4 "double the QR value" construction produced numerically plausible-looking but ultimately unmotivated matches. Here the doubling is well-motivated on the Suzuki side (it's forced by \(v_2(k)=1\)), but that motivation is internal to the Suzuki construction and has no counterpart in the cone's unit-group double cover.

---

## 3. Consequence for the sheet-translation picture

v13.501's finding — that the \(B=\{1,13\}\) sheet action realizes as the cone translation \((X,T)\mapsto(X+6,T+6)\) — has no image under the Suzuki side's labeling map, because \(S\) contains no elements of \(U(24)\) for the sheet action to act on. There is consequently no natural way to ask "does the sheet shift preserve the Suzuki class structure," because the Suzuki stratum was never built from \(U(24)\) in the first place.

\[
\boxed{
\text{The cone's }U(24)\text{ double cover (v13.501) and the Suzuki mod-24 unit-core stratum (v13.423/432) are unrelated constructions that happen to share the modulus 24 and the labels }\{1,5,7,11\}.
}
\]

---

## 4. What would be needed to actually connect them

Not attempted here, flagged only as the honest next question if this is worth pursuing further: the Suzuki side already asks (v13.432 §8, "next exact targets") for the minimal modulus recovering \(u\bmod12\) on higher \((v_2,v_3)\) strata. If a *higher* even stratum (e.g. \(v_2(k)=3\)) turned out to require exactly mod 24 unit-group information rather than a further doubling, that would be a genuine point of contact — but this has not been checked, and nothing in v13.432 suggests it, since the stratification there is organized by valuation, not by the unit group of an extended modulus.

## Guardrail

This is a negative/checked-not-found result. It does not weaken v13.501 (the cone realization stands on its own) or v13.430/432 (the Suzuki diagnostics stand on their own). It exists to stop the χ12 phase-bridge thread — or any future entry — from re-proposing this specific connection without new structural input beyond "both use mod 24."
