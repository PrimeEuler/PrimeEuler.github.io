# Ledger v15.009 — Erratum to v15.008 (Sandbox): one garbled formula, entry otherwise unchanged

In v15.008's aggregate list, the harmonic volume was printed with a
garbled exponent ("A^{m−m+1}…"). The correct formula, as in the
payload NOTE and verified by ladder.py at m = 10, 12, is:

  prod H = ((m−1)!)² / A^(m−1),   A = m/2

(m = 12: 118580000/27; m = 10: 5267275776/78125.) No result, verdict,
or flag in v15.008 is affected. Additive erratum only; v15.008 and
its payload are unedited.
