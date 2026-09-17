# Cone Derivation Ledger v13.552 — Delta57 Class-5 Separation

**Status:** finite binary64 midpoint diagnostic; quantitative follow-up to v13.551. No theorem promotion.

## Setup

Use the reproducible v13.551 checkpoint

`research-notes/suzuki_unit_core_delta57_checkpoint.py`

at `M=3999`, with the canonical source support `q={2,3,4,5,7}` and the full block-diagonal Cholesky whitening metric frozen from the complete Suzuki finite-high matrix.

For a nonprincipal three-character response

`x=(a,b,c)=(x_{chi_-4},x_{chi_-3},x_{chi_12})`,

the projective v5/v7 exchange coordinate is

`Delta57(x)=C(x,v7)^2-C(x,v5)^2`

and exactly, as an algebraic identity in the character coordinates,

`Delta57(x)=4(a-b)c/[3(a^2+b^2+c^2)]`.

Positive means the v7 side of the projective bisector; negative means the v5 side.

## Frozen full-precision values

### Pair (2,3)

- star 1:  `-0.9029267235997576`
- star 5:  `+0.5359576668827004`
- star 7:  `-0.7250522420661470`
- star 11: `-0.6151381598919492`

Class-5 minus controls:

- versus star 1:  `+1.4388843904824580`
- versus star 7:  `+1.2610099089488473`
- versus star 11: `+1.1510958267746496`

Control mean:

`(-0.9029267235997576-0.7250522420661470-0.6151381598919492)/3 = -0.7477057085192845`.

Thus star 5 is the unique strongly positive case and is separated from its nearest control (star 11) by

`1.1510958267746496`.

### Pair (3,5)

- star 1:  `-0.9408356856671705`
- star 5:  `-0.02861044046328676`
- star 7:  `-0.8192276598694792`
- star 11: `+0.1146480703384783`

Class-5 minus controls:

- versus star 1:  `+0.9122252452038837`
- versus star 7:  `+0.7906172194061925`
- versus star 11: `-0.14325851080176508`

Control mean:

`(-0.9408356856671705-0.8192276598694792+0.1146480703384783)/3 = -0.5484717583993904`.

Here star 5 is close to the v5/v7 bisector rather than strongly v7-localized. Star 11 is the modest positive exception.

## Cross-stratum class-5 displacement

The class-5 shift from pair (3,5) to pair (2,3) is

`0.5359576668827004 - (-0.02861044046328676) = +0.5645681073459872`.

This is a useful scalar description of the source-stratum dependence already visible in v13.551. It does **not** establish that either source pair implements a Hadamard/V4 action.

## Interpretation guardrail

The exact closed formula shows that Delta57 is controlled by the product `(a-b)c`: the difference between the `chi_-4` and `chi_-3` response coordinates coupled to the `chi_12` coordinate. This is an identity for the diagnostic coordinates, not an operator factorization or arithmetic causation statement.

The numerical values are finite `binary64` midpoint outputs at `M=3999`. They are not outward-certified intervals, do not establish cutoff/asymptotic stability, and do not promote an exact Suzuki `V4` symmetry, a Pell–Suzuki intertwiner, positivity, an index improvement, or any RH/GRH statement.

## Next gate

The appropriate next test is cutoff stability of the Delta57 separation itself (e.g. `M=499,999,1999,3999`) using a separately rebuilt full whitening metric at each cutoff. Promotion beyond a finite diagnostic requires that the class-5 separation pattern survive that test without relabeling or refitting.
