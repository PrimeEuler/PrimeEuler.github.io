# v15.108 — Explicit integrated complete quadratic Hamiltonian source

Date 2026-10-29. Gravity parent v15.107. Checked live HEAD; no returned audit of v15.107 at this check. Additive gravity-only; protected Suzuki and Sandbox work untouched.

With conformal h_ij=a²(1−2ψ)δij, lapse N=1+α, contrav shift β, triplet φI=zi+πI, κC=1, define Sij=(∂iβj+∂jβi)/2 and θ=divβ. From the complete first-order-generated quadratic Hamiltonian source v15.107:
H2=a^-2(16ψΔψ+6|∇ψ|²)+6dotψ²+24Hαdotψ+18H²α²−24Hψdotψ+12Hβ·∇ψ+4dotψ θ+8Hαθ+θ²−SijSij −(2/3)|dotπ−β|²−(2/(3a²))(|∇π|²+4ψdivπ+12ψ²).
Periodic integration (or matching boundary flux vanishing) yields ⟨16ψΔψ+6|∇ψ|²⟩=−10⟨|∇ψ|²⟩ and ⟨β·∇ψ⟩=−⟨ψ θ⟩. Thus
⟨H2⟩=−10a^-2⟨|∇ψ|²⟩+6⟨dotψ²⟩+24H⟨αdotψ−ψdotψ⟩+18H²⟨α²⟩−12H⟨ψθ⟩+4⟨dotψθ⟩+8H⟨αθ⟩+⟨θ²−SijSij⟩−(2/3)⟨|dotπ−β|²⟩−(2/(3a²))⟨|∇π|²+4ψdivπ+12ψ²⟩.
This is an exact integrated expression for the full quadratic source *in this conformal ansatz*, not an explicit evaluation on certified constrained linear solutions, and not the full order-two Hamiltonian (which has H1[U2]). Terms have indefinite sign and their correlations are governed by lapse/shift constraints. Therefore one cannot deduce universal nonzero obstruction, automatic cancellation, or full nonlinear stability from this integrated expression alone.

On periodic T³, quadratic first-order sources have zero output contribution governed by total high-high convolution (Parseval); first-order linear scalar ψ has inverse-|k|² reconstruction, so imposing an unweighted strain oscillator norm does not certify the integrability of every correlation. For genuine full second-order data H1[U2]+H2[U1]=0, hence periodic mean from previous gate 12H⟨dotψ2⟩+12H²⟨ψ2+α2⟩=⟨H2[U1]⟩, within conformal gauge and appropriate homogeneous modes. This is a necessary algebraic balance but not full initial-data solvability or gauge propagation.

NEXT: insert fully consistent first-order α,β,ψ from corrected v14.996 variables, respecting source h=a²(1−2ψ) convention, and explicitly compute each bilinear mode convolution and zero-mode source; check momentum compatibility and time growth. Independent audit of full extrinsic source v15.107 and current integrated result is required. No collision, Suzuki physical weld parked.
