# Cone Derivation Ledger v13.654 — Correction and Explicit Deficiency-Basis Boundary Triple for Suzuki W

Date: 2026-09-22

Status: exact correction of v13.647 Section 4 plus explicit deficiency-coordinate boundary triple. The external audit v13.648 found a real Cayley-sign error in v13.647. This entry corrects it before extending the bridge.

## 0. Live collision/relevance check

The live ledger was fetched before this derivation and has advanced through v13.653. The relevant new entry is v13.648 External Audit Round 69, which independently PASSed v13.640, v13.641, v13.644, and the Suzuki W factorization in v13.647, but found the Cayley identity in v13.647 Section 4 algebraically inconsistent. Entries v13.649-v13.653 are other lanes. This entry takes v13.654.

## 1. Correct Cayley convention

Keep the standard Krein denominator
[
	au-m_A(zeta).
]
Define
[
s_A(zeta)=rac{m_A(zeta)-i}{m_A(zeta)+i}.
]
To factor tau-m with a boundary phase, the consistent convention is
[
oxed{e^{i	heta}=rac{	au+i}{	au-i},qquad 	au=cot(	heta/2).}
]
Then direct algebra gives
[
1-e^{i	heta}s_A
=
rac{2i(	au-m_A)}{(	au-i)(m_A+i)},
]
hence
[
oxed{
	au-m_A(zeta)
=
rac{	au-i}{2i}[m_A(zeta)+i]
[1-e^{i	heta}s_A(zeta)].
}
]
This is the corrected replacement for v13.647 Section 4.

The v13.647 convention e^{i theta}=(tau-i)/(tau+i) instead factors tau+m, exactly as v13.648 found.

## 2. Canonical deficiency coordinates

Let S_A be closed symmetric with deficiency indices (1,1), and choose equal-norm deficiency vectors
[
u_+inker(S_A^*-i),qquad u_-inker(S_A^*+i),
qquad |u_+|=|u_-|=1.
]
Every f in D(S_A^*) has the von Neumann decomposition
[
f=f_0+c_+u_+ + c_-u_-,qquad f_0in D(S_A).
]
The Green form is
[
langle S_A^*f,gangle-langle f,S_A^*gangle
=2i(c_+ar d_+-c_-ar d_-).
]

One valid ordinary scalar boundary triple is
[
oxed{Gamma_0 f=c_+ + c_-,qquad
Gamma_1 f=i(c_+-c_-).}
]
It obeys
[
langle S_A^*f,gangle-langle f,S_A^*gangle
=Gamma_1f,overline{Gamma_0g}
-Gamma_0f,overline{Gamma_1g}.
]

The reference extension ker Gamma_0 is the von Neumann phase c_-=-c_+. Whether this reference is literally Suzuki's Friedrichs extension is an additional identification and must be checked from his domain convention; it is not automatic from the deficiency decomposition.

## 3. Phase versus real boundary parameter in this triple

For the extension
[
Gamma_1 f=	auGamma_0 f,
]
the deficiency coefficients obey
[
i(c_+-c_-)=	au(c_++c_-),
]
so
[
oxed{
rac{c_-}{c_+}
=
-rac{	au-i}{	au+i}.
}
]
Thus if Suzuki's extension is written c_-=e^{iartheta}c_+, then
[
e^{iartheta}=-rac{	au-i}{	au+i}.
]
This phase is NOT the same theta convention used in Section 1 unless one absorbs the fixed minus sign/conjugation into the definition of the boundary parameter. This is precisely why the phase convention cannot be guessed from the abstract Cayley transform.

## 4. Weyl function in deficiency coordinates

Let H_ref=ker Gamma_0. For zeta in rho(H_ref), the defect vector gamma(zeta) is uniquely normalized by Gamma_0 gamma(zeta)=1. Its Weyl function is
[
m_A(zeta)=Gamma_1gamma_A(zeta).
]
If
[
gamma_A(zeta)=f_0(zeta)+c_+(zeta)u_++c_-(zeta)u_-,
]
then normalization gives c_++c_-=1 and therefore
[
oxed{m_A(zeta)=i[c_+(zeta)-c_-(zeta)].}
]
Solving,
[
c_+=rac{1-im_A}{2},qquad
c_-=rac{1+im_A}{2}.
]
Hence the defect-coordinate ratio is
[
oxed{
rac{c_-}{c_+}
=
rac{1+im_A}{1-im_A}
=
-rac{m_A-i}{m_A+i}
=-s_A(zeta).
}
]
Therefore the Cayley/Schur function has an exact deficiency-coordinate meaning:
[
oxed{s_A(zeta)=-c_-(zeta)/c_+(zeta).}
]

## 5. Comparison with Suzuki's Fourier characteristic

The independently audit-PASSed identity from v13.647 is
[
W_A(	heta;z)
=(z-i)F_{A,+}(z)
[1-e^{i	heta}s_A^{Suz}(z)],
]
with
[
oxed{
s_A^{Suz}(z)=-
rac{(z+i)F_{A,-}(z)}
{(z-i)F_{A,+}(z)}.
}
]

Thus the exact Weyl/Suzuki bridge reduces to showing that the Fourier quantities are the defect-coordinate amplitudes:
[
c_+(zeta)propto (z-i)F_{A,+}(z),qquad
c_-(zeta)propto (z+i)F_{A,-}(z),
]
with the SAME nonzero proportionality factor and the correct spectral-variable map. If this holds, then
[
s_A(zeta)=-c_-/c_+=s_A^{Suz}(z)
]
exactly.

The present ledger does not yet contain a source-derived proof of those two amplitude identities. Therefore the equality s_A=s_A^{Suz} remains OPEN, but it has now been reduced to a concrete pair of coefficient identities rather than a heuristic phase match.

## 6. What is now exact

Exact:
- corrected Cayley factorization of tau-m;
- explicit ordinary boundary triple in normalized deficiency coordinates;
- exact relation s_A=-c_-/c_+;
- exact Suzuki algebraic factor s_A^{Suz}=-(z+i)F_- / ((z-i)F_+);
- exact statement of the remaining bridge needed.

Not yet established:
- that ker Gamma_0 in this particular coordinate triple is Suzuki's Friedrichs extension;
- the precise map between zeta and Suzuki's z;
- c_+ proportional to (z-i)F_+ and c_- proportional to (z+i)F_- with a common scalar;
- therefore s_A=s_A^{Suz}.

## 7. Next gate

Derive the Fourier-amplitude identities directly from Suzuki's transform/operator definitions (not from matching zeros), and identify which von Neumann phase corresponds to the Friedrichs extension. Only then promote W_A as the exact Krein boundary perturbation determinant.
