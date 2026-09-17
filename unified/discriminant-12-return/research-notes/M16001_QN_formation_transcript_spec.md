# M16001 Q/N formation transcript contract

Status: audit scaffold; fail closed; no theorem promotion.

The actual M16001 replay must emit `qn_mid`, `qn_absprod=sum_i abs(x_i*y_i)`, and scalar/entrywise integer `qn_k` for every normalized Q/N entry used by the seven-plane Schur calculation. The checker derives `rad_ij=gamma_k*qn_absprod_ij`, `gamma_k=k*u/(1-k*u)`, and conservatively uses `||B_QN||_2 <= ||B_mid||_F+||Rad||_F`; it contains no accepted Q/N radius literal.

The transcript must instrument the actual formation path. If scaling, normalization, subtraction, or another rounded stage follows the dot product, its intermediate magnitude and operation count must also be emitted and charged before this gate can close. Empirical binary64/long-double differences or safety multipliers are not certificates.
