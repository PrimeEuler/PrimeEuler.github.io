# Second-order ADM scalar momentum and near-zero Fourier output
Date 2026-10-27. Parent v15.003; External Audit v15.004 verifies v15.000–003. Checked current HEAD 3308824f728c8fee92e53fc8a2bb4e1953ed8adf. Additive gravity only, protected lanes unchanged.

Use exact ADM scalar momentum p_I=(2C/3)(√h/N)(dotφI−N^j∂jφI), lapse N=1+α, shift N^i=β^i, spatial h_ij=a²(δij+εij), φI=zi+πI, background α=β=ε=π=0. Perturbation expansion in order-tagged first-order fields (suppress superscripts on first-order):
p_I^(1)=(2C/3)a³(dotπI−βI).
p_I^(2)=(2C/3)a³[(dotπI^(2)−βI^(2))+(tr ε/2−α)(dotπI−βI)−β^j∂jπI].
Here p^(2) denotes the coefficient of second-order perturbative degree under convention that φ=φbar+π^(1)+π^(2), not 1/2 times φ^(2). h^(2), lapse^(2), etc do not enter p2 multiplied by zeroth scalar velocity since dotφbar=0, except β^(2). First-order metric-volume trace yields √h=a³[1+trε/2+O(2)], and 1/N=1−α+O(2). Gauge caveat: shift β^i is contravariant ADM shift; using covariant N_i requires conversion and metric correction.

Matter momentum constraint expansion: p_I ∂iφI = p_i^(1) + p_i^(2) + p_I^(1)∂iπI + O(3). Hence quadratic source includes p_i^(2)+p_I^(1)∂iπI, with lapse/shift/metric products and genuine second-order velocity/shift unknowns. Fourier product [(trε/2−α)(dotπ−β)] etc convolves input p and K−p without an obligatory prefactor K. Thus no automatic output-K divisibility from matter canonical sector alone; full ADM gravitational part Π^{jk}∂i h_jk and second-order lapse/shift solution could constrain or cancel it. The exact global integrated balance from v15.003 applies to admissible compact-domain initial data. Zero-mode solvability is distinct from uniform K→0 continuity on noncompact R³.

No second-order full Einstein constraint operator inverses computed here: source is complete *matter canonical* quadratic expansion in this ADM variable convention, not claimed full constrained elimination or proof nonlinear IR stability. Need compute gravity Π^(1)∂h^(1), Π^(2) and solve coupled ADM constraints with complete inverse metrics (lesson v14.996). Suzuki physical quarter weld PARKED.
