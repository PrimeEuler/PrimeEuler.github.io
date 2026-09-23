# Cone Derivation Ledger v13.704 — External Audit Round 80

Date: 2026-09-23

Auditor: independent external reviewer, verifying by fresh independent computation including direct symbolic matrix computation.

Scope: v13.696 (pronic successor dynamics on U(24)), v13.697 (RMS/Casimir fiber transfer vs Pell orientation), v13.698 (complex orientation selects 7), v13.699 (two primitive reflections compose to the chi12 half-turn), v13.700 (broader cone toolkit / non-D12 findings checkpoint), v13.701 (cyclotomic Z powers and the central C4 obstruction), v13.702 (continuous C* cone action and torsion slice), v13.703 (logarithmic torus involutions and semidirect product) — eight entries continuing directly from the Round 79 HM/GM/AM/QM revival into a substantial finite-reflection and continuous-group-theory program.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `a5d6ba0` (v13.703), no intervening commits. Highest ledger version is v13.703; this entry claims v13.704 / Round 80.

## 1. v13.696 — pronic successor dynamics: independently verified, PASS (including the negative result)

Independently recomputed the admissible-index set `m\in\{0,2,3,5,6,8,9,11\}\pmod{12}` (those with `6\mid m(m+1)`, i.e. `m\not\equiv1\pmod3`) and confirmed the doubled radii `r_m=2m+1\bmod24` trace the exact 8-cycle `1\to5\to7\to11\to13\to17\to19\to23\to1`. Independently recomputed the binary-coordinate form under `r(a,b,c)=5^a7^b(-1)^c` from scratch and confirmed it matches the claimed cycle `000\to100\to010\to110\to111\to011\to101\to001\to000` exactly.

The entry's central negative result — that the pronic successor `S` is **not** an affine `F_2^3` map of the already-established carrier — is a proof by contradiction (`S(000)=100`, `S(100)=010` force `M(110)=100`, hence affine linearity would predict `S(110)=000`, but the actual successor gives `S(110)=111`). Independently re-derived this contradiction from scratch and confirmed it: the affine prediction and the actual value disagree, closing the proof correctly. Also independently recomputed the `\chi_{12}` and sheet-character (`\sigma`) sign sequences along the 8-cycle using `\chi_{12}=(-1)^{a+b}`, `\sigma=(-1)^c` and confirmed both match exactly (`+,-,-,+,+,-,-,+` and `+,+,+,+,-,-,-,-` respectively). **PASS**, and this is a good example of the project correctly reporting a clean negative result rather than forcing a false positive.

## 2. v13.697-699 — the reflection triangle: independently verified, PASS

These three entries jointly establish `(5,\chi_{-3},R_X)(7,\chi_{-4},R_Y)=(11,\chi_{12},R_XR_Y)`. Independently checked the group arithmetic throughout: `5\cdot5\equiv1`, `5\cdot7\equiv11\pmod{12}` (multiplication table for the two candidate translators), the self-inverse property of `5` used in `5^{-1}7=5\cdot7=11`, and the binary-coordinate pairing `B(110,010)=1`, `B(110,100)=1` (both give `\chi_{12}=-1` on `5` and `7`, consistent with the independently-rebuilt character table from Round 79). Independently verified the explicit reflection composition in v13.699 §4: `R_X:(X,Y,T)\mapsto(-X,Y,T)`, `R_Y:(X,Y,T)\mapsto(X,-Y,T)`, and both orders of composition give `(X,Y,T)\mapsto(-X,-Y,T)`, i.e. `z\mapsto-z` — confirming `R_X,R_Y` commute and their product is the half-turn, exactly as claimed. The `\chi_{12}(11)=+1` self-pairing computation (`B(110,110)=1+1\equiv0\pmod2`) was independently reconfirmed. **PASS on all three entries**, including the appropriately hedged epistemic status in v13.697 §8-9 (explicitly flagging that the `\times7` choice needs independent justification before being called canonical) which v13.698-699 then correctly go on to supply and verify, rather than assuming it.

## 3. v13.700 — broader toolkit checkpoint: independently verified, PASS

Independently re-derived the new mean-algebra identities in §8 from the definitions `A=(x+y)/2`, `D=(x-y)/2`, `G=\sqrt{xy}`, `H=2xy/(x+y)`, `Q=\sqrt{(x^2+y^2)/2}`, `C=(x^2+y^2)/(x+y)`: confirmed `AC=Q^2` (from `C=2Q^2/(2A)`), `H+C=2A` (reduces exactly to the previously-verified `2A^2=G^2+Q^2`, itself confirmed via `G^2=A^2-D^2` and `Q^2=A^2+D^2` summing to `2A^2`), the mirror-parabola pair `H=A-D^2/A`, `C=A+D^2/A`, and the fixed-`G` rapidity identity `Q^2=G^2\cosh(2s)` (via the standard hyperbolic double-angle identity `\cosh^2s+\sinh^2s=\cosh2s`). All confirmed exact. The checkpoint's guardrails (§11, §14: no HP/RH claim, D12 treated as a specialization not the ambient theory, real compactification vs analytic continuation kept distinct) are consistent with the actual content of the entries reviewed and are not overreach. **PASS.**

## 4. v13.701 — cyclotomic Z powers, central C4 resolved: independently verified by direct symbolic computation, PASS

This is the round's most consequential result, and this audit verified it by direct symbolic matrix computation rather than by re-reading the algebra. Built the exact matrices from the foundation document (`g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix}`, `H=g_{12}-2I`, `\mathcal Z=(H+iI)/2`) independently in `sympy` and computed:

- `H^2=3I` — confirmed exactly;
- `\mathcal Z^3=iI` — confirmed exactly (not approximately);
- `\mathcal Z^6=-I`, `\mathcal Z^9=-iI`, `\mathcal Z^{12}=I` — all confirmed exactly;
- `\mathcal Z\overline{\mathcal Z}=I` — confirmed exactly;
- eigenvalues of `\mathcal Z` are `e^{i\pi/6}` and `e^{i5\pi/6}`, both primitive 12th roots of unity (`\gcd(1,12)=\gcd(5,12)=1`), matching the foundation's claim.

This closes, by direct independent computation rather than argument-checking, the repeatedly-reopened question of whether the central scalar `C_4=\langle iI\rangle` of the complexified cone closure equals the cyclotomic quarter generated by `\mathcal Z`. It does, exactly: `\mathcal Z^3=iI`. The entry's careful distinction between this scalar identification and the separate, still-obstructed question of whether the arithmetic lift `A` (with `A^2=R_Y`) equals `\mathcal Z^3` (with `(\mathcal Z^3)^2=-I\ne R_Y`) is correct and appropriately preserved rather than glossed over. The `C(iI)C^{-1}=-iI` dihedral relation was independently re-derived from the antilinearity of `C` and confirmed exact. **PASS, exact — a genuine resolved result.**

## 5. v13.702 — continuous C* cone action: independently verified, PASS (including its own negative result)

Independently verified the core construction: `B(w):x\mapsto wx,y\mapsto w^{-1}y,Y\mapsto Y` preserves `xy` identically (trivial), hence preserves the full complexified quadratic form `\det Q=xy-Y^2`, giving a genuine one-parameter subgroup of `SO(2,1;\mathbb C)`. Independently verified `a(w)^2-b(w)^2=1` for `a(w)=(w+w^{-1})/2`, `b(w)=(w-w^{-1})/2` (algebraic identity, `(a-b)(a+b)=w^{-1}\cdot w=1`), and the logarithmic-generator form `\rho(e^\ell)=e^{\ell K_X}` via `\cosh(i\phi)=\cos\phi`, `\sinh(i\phi)=i\sin\phi` (standard).

Independently recomputed the entry's own negative result in §7: at `w=i`, `a(i)=(i+i^{-1})/2=(i-i)/2=0`, `b(i)=(i-i^{-1})/2=i`, giving `\rho(i):(T,X,Y)\mapsto(iX,iT,Y)`. Applying twice gives `(-T,-X,Y)`, and a fourth application returns identity — confirmed exactly. Critically, this map is **not** the scalar `iI` (which would send `(T,X,Y)\mapsto(iT,iX,iY)`, scaling every coordinate including `Y`, whereas `\rho(i)` swaps and scales only `T,X` while leaving `Y` untouched entirely) — independently confirmed `\rho(i)\ne iI` by direct comparison of the two maps. **PASS**, and correctly reports this as a genuine "FAIL" for the naive identification of the boost-torsion `\mu_4` with the scalar cyclotomic `\mu_4=\langle\mathcal Z^3\rangle`, rather than silently assuming they must coincide because both are order-4.

## 6. v13.703 — logarithmic torus involutions: independently verified, PASS

Independently re-derived the full involution algebra from the definitions. Checked `FB(w)F^{-1}=B(w^{-1})` by direct computation: `(FB(w)F)(x,y)=F(B(w)(y,x))=F(wy,w^{-1}x)=(w^{-1}x,wy)=B(w^{-1})(x,y)` — confirmed exactly. Checked `CS(\lambda)C^{-1}=S(\bar\lambda)` and `CB(w)C^{-1}=B(\bar w)` from the antilinearity of `C`, both confirmed exactly. Checked `FC=CF` (immediate since `F` has real matrix entries, so conjugation commutes with it) and independently recomputed the composite action `FC:(\tau,\ell)\mapsto(\bar\tau,-\bar\ell)`, translating to real coordinates `(a,\alpha,s,\phi)\mapsto(a,-\alpha,-s,\phi)` — confirmed exactly by direct substitution `\tau=a+i\alpha,\ell=s+i\phi`.

Independently rebuilt the `C_2^2` character table of the four real logarithmic directions (`F=\mathrm{diag}(1,1,-1,-1)`, `C=\mathrm{diag}(1,-1,1,-1)`, `FC=\mathrm{diag}(1,-1,-1,1)` on `(a,\alpha,s,\phi)`) directly from the `(\tau,\ell)`-level action and confirmed it matches the entry's table exactly, entry-by-entry. The entry's guardrail in §8 (distinguishing the "coefficient conjugation `C`" of this entry from the earlier real-linear `R_Y` reflection label, which coincide only after a representation identification) is a careful and necessary precision, consistent with this audit's own reading of v13.698-699. The final distinction between the two commuting-but-distinct `D_8` mechanisms (boost-torus torsion under `F`, versus cyclotomic scale-torsion under `C`, per v13.701) is consistent with the negative result independently confirmed in Section 5 above. **PASS.**

## 7. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.696 | 8-cycle pronic successor; not affine on `U(24)\cong F_2^3` | independent enumeration + independent reproduction of the contradiction proof | **PASS, including the negative result** |
| v13.697-699 | Reflection triangle `(5,\chi_{-3},R_X)(7,\chi_{-4},R_Y)=(11,\chi_{12},R_XR_Y)` | independent group arithmetic + explicit `(X,Y,T)` composition | **PASS, exact** |
| v13.700 | Extended mean-algebra identities (`AC=Q^2`, `H+C=2A`, fixed-`G` rapidity form) | independent algebraic re-derivation | **PASS, exact** |
| v13.701 | `\mathcal Z^3=iI`; central `C_4` = cyclotomic quarter | independent symbolic matrix computation (sympy), exact | **PASS, exact — resolves a repeatedly-reopened question** |
| v13.702 | Continuous `\mathbb C^\times_{\rm boost}` action preserves quadratic form; its `\mu_4` torsion `\ne` scalar `\mu_4` | independent algebraic verification, including the negative result | **PASS, including the negative result** |
| v13.703 | Full `(\mathbb C^\times)^2\rtimes C_2^2` semidirect product; two distinct `D_8` mechanisms kept apart | independent re-derivation of all stated commutation relations and the character table | **PASS, exact** |

## 8. Assessment

This is a substantial and unusually error-free round: eight entries spanning finite modular-arithmetic dynamics, a full reflection-triangle synthesis, and a genuine continuous-group-theory construction (a `(\mathbb C^\times)^2` action on the complexified cone with an exact semidirect extension by two involutions), including direct symbolic verification of the central algebraic result (`\mathcal Z^3=iI`) via matrix computation on the actual foundation-document matrices, not just re-reading the stated algebra. No errors were found in any of the eight entries.

Two aspects of this round's craftsmanship stand out. First, the project correctly produced and kept two genuine negative results (v13.696: the pronic successor is not affine; v13.702: the boost-torsion `\mu_4` is not the scalar cyclotomic `\mu_4`) rather than forcing false unifications — both are proven by explicit contradiction/counterexample, not asserted. Second, v13.701's resolution of the long-standing "central `C_4` vs. cyclotomic `\mathcal Z`" question is a genuine, exact, previously-unresolved result (`\mathcal Z^3=iI`, confirmed here independently by direct matrix computation), and the entries that follow it (v13.702-703) correctly avoid overgeneralizing that result — they explicitly keep the resolved scalar-torsion identification separate from the still-distinct boost-torus torsion, producing a precise map of which `D_8` mechanism lives where rather than collapsing them.

No corrections or open concerns are raised against v13.696-703 in this round.

## 9. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `a5d6ba0`. No new commits landed while writing this entry. `git ls-tree` confirms v13.704 remains free.
