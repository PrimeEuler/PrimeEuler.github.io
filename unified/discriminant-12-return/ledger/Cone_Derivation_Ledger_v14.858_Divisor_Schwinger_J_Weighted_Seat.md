# Cone Derivation Ledger v14.858 — Divisor contacts as Schwinger j,m labels

Date 2026-10-25. Gravity arithmetic lane. Parents v14.366–367, v14.620, v14.626, v14.856–857. Research note research-notes/Divisor_Contact_Schwinger_J_Weighted_Seat_Gate.md, commit ab0ac168643c803d25455996205b2813e430a9c7. Live prewrite HEAD ab0ac168643c803d25455996205b2813e430a9c7. Additive only; no Suzuki or far-tail changes.

## Exact Schwinger-label bookkeeping [D/I]
For every ordered divisor pair (a,b), choose nonnegative oscillator occupations (n1,n2)=(a-1,b-1), yielding
\[
j=(a+b-2)/2,\qquad m=(a-b)/2,\quad |m|\le j.
\]
The contact's unit-circle encoding is \(z_{a,b}=(a-b+2i\sqrt{ab})/(a+b)\). These are exact mathematical dictionaries under the chosen occupation offset, NOT proof of a physical Hilbert-space state for every contact. Distinct contacts can share j while differing in m; D(N) counts ordered pairs, not distinct j levels. For N=12, the six contacts have (j,m)=(11/2,±11/2),(3,±2),(5/2,±1/2), with signs determined by factor order.

## Rotor-weighted contact observable [D/I]
Define \(W_2(N)=\sum_{ab\le N}j(a,b)(j(a,b)+1)\). The exact shell weight for ab=12 is \(w_2(12)=113\), compared with six unweighted contacts. For a CHOSEN physical free rotor with independently supplied inertia I, levels have \(E_j=\hbar^2j(j+1)/(2I)\); ħ alone does not supply a per-contact energy or prove physically independent rotor modes. At common unscaled physical cutoff n, define \(\Delta_{4,W}(n)=W_2(4n)-4W_2(n)\), but no assertion that 4 is the correct asymptotic normalization of W_2: the Casimir weighting may change the leading scaling dramatically.

## Next selector gate [O]
Compute exact W_2 asymptotics and correct scale-normalized 4n-versus-n comparison. Then derive any seat stiffness from a specified angular-momentum coupling and its matrix elements (rank-1/rank-2 rotor selection rules) rather than choosing uniform contact energies or assuming each contact is one independent physical state. No GR action, G, or α hierarchy derived. v13.770 arithmetic-carrier separation retained.

Flags: contact_jm_map=EXACT_CONVENTIONAL_OFFSET; unit_circle_pair_encoding=EXACT; W2_shell12=113; W2_asymptotic=OPEN; physical_contact_quantization=UNPROVED; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-schwinger-divisor-contact-verification
parent: v14.858
status: open
action: Verify j,m occupation mapping, shell N=12 Casimir-weight 113, distinctions between a contact, j level and physical Hilbert state, and non-assumption of fourfold W2 scaling. Do not modify Suzuki/far-tail.
deliverable: scoped audit verdict.
