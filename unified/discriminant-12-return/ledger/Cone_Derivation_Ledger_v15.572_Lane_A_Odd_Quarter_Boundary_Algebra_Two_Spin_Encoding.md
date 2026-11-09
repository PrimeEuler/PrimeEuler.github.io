# Cone Derivation Ledger v15.572 — Lane A: odd-quarter boundary algebra and exact two-spin encoding

Date: 2026-11-09. Parents: v15.135, v15.140, v15.143, v15.544 (corrected per audit v15.571). Status **[D] exact finite-matrix/closed-form operator identities; [C] chosen cross-carrier coordinate assignment; [O] physical intertwiner**. Prewrite HEAD 74ed19111119ed239e19dff52629d08b7e0dc694, no collision at v15.572. Additive; frozen Suzuki/far-tail untouched.

## 1. Four-state first odd-quarter shell [D/C]

Refined mesh j=3/4: ordered magnetic nodes m=(-3/4,-1/4,1/4,3/4). J_z^q=diag(m), and J_+^q has precisely two nonzero entries: rows/columns (2,0) and (3,1), both sqrt(3/2), with zero-based indexing. J_-^q=(J_+^q)^dagger.

Choose the **ordered-coordinate identification**, not yet a physical intertwiner, with the bicone spin-half tensor basis |++>,|+->,|-+>,|-->. Define J_{1z}=sigma_z tensor I/2, J_{2z}=I tensor sigma_z/2, L_z=J_{1z}+J_{2z}, A_z=J_{1z}-J_{2z}. Then exactly:

J_z^q= -J_{1z} - (1/2)J_{2z}=-(3/4)L_z-(1/4)A_z,

J_+^q= sqrt(3/2)(sigma_- tensor I), J_-^q=(J_+^q)^dagger.

For D=[J_+^q,J_-^q]-2J_z^q and E=j(j+1)I-(J_x^q)^2-(J_y^q)^2-(J_z^q)^2, where J_{x,y}^q=(J_+^q +/- J_-^q)/(2,2i), exact substitution gives

D=-A_z=diag(0,-1,1,0),

E=A_z^2/2=diag(0,1/2,1/2,0).

Thus not only E but the full defective quarter-shell raising/lowering and magnetic-coordinate matrices are representable in the two-bicone-spin full matrix algebra, with unequal roles for the two factors. **Not an SU(2) intertwiner:** D is nonzero, whereas any full unitary SU(2) representation has D=0, and J_z^q and diagonal-bicone L_z have different spectra. No unique geometrically sourced choice of cross-carrier basis is claimed.

## 2. General odd-quarter boundary theorem [D]

Let n>=1, j=(2n-1)/4, m_i=-j+i/2 for i=0,...,2n-1. J_+ raises m by one on the refined shell, and therefore preserves the parity s=i mod 2, leaving two open chains of length n. Write i=2k+s, k=0,...,n-1, s in {0,1}. The exact squared weight for i -> i+2 (k<=n-2) is

w_{s,k}^2=(n-1/2-k-s/2)(k+1+s/2).

Consequently w_{0,k}^2=w_{1,n-2-k}^2: the two chains are mirror-reversed, but neither is a closed unitary spin-(n-1)/2 multiplet under the original J generator.

Let c=j+1/4=n/2, and P_- and P_+ project on the two open-end nodes m=-j+1/2 and m=j-1/2, respectively. Their magnetic labels are distinct for all odd quarters including j=1/4. On all odd-quarter shells:

D=c(P_+ - P_-),
E=(c/2)(P_+ + P_-).

Hence rank E=2, D^2=4E^2, tr D^2=2c^2, tr E^2=c^2/2. The proof is cancellation of every internal ladder contribution and two missing boundary links, each with squared escape weight c. All identities were independently evaluated with exact SymPy arithmetic on n=1,...,9. For n=3 (j=5/4), the six-state chain-weight squares are (5/2,3) and (3,5/2); boundary defect eigenvalues are +/-3/2. The n=2 four-state encoding does NOT lift to a universal four-dimensional bicone identification: already at j=5/4, the carrier has six dimensions.

## 3. Rank-two bridge and scope

Under the **conditional** four-state identification E=A_z^2/2, the bicone identity [L_+,[L_+,E]]=A_+^2 (and mirror) transports the axial quadratic to the m=+/-2 quadrupole. This internal algebraic transport uses no adjustable coefficients. The *separate* spin-1 rotor projected transverse tidal normalization is 5/2 per independently audited v15.571 (correcting old 5/4); it is not a physical coupling.

There is **no established boundary-preserving unitary map** from the odd-quarter module to closed diagonal SU(2) (commutator obstruction), no canonical cone/bicone/Suzuki carrier dictionary, no particle mass hierarchy, generation interpretation, G, or gravitational source strength. Distinguish an encoding in the **full two-spin operator algebra** from a genuine intertwiner to a representation of the **diagonal SU(2)**.

HANDOFF target: external-audit; type: new odd-quarter boundary-algebra theorem; status: open; requested checks: verify n=2 full 4x4 operator identity; prove general w_{s,k} and D/E boundary formulas including n=1; verify n=3 deformed weights and obstruction; inspect any hidden reliance on a noncanonical basis identification. No production/far-tail changes.
