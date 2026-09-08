#!/usr/bin/env python3
"""Fixed rational 10x6 stiff-subspace candidate for the effective core.

The columns below are the N=155 nominal stiff eigendirections rounded to 12
decimal places.  They are not used as certified eigenvectors.  They are simply
a fixed rational subspace candidate V.  Once a rigorous effective-core interval
matrix F is available, it suffices to certify

    V^T F V > 0.

Then span(V) is automatically six-dimensional and positive, hence the
nonpositive index of F is at most four.

Nominal projected eigenvalues with the rounded V are approximately

    4.32680308e-8,
    2.55123446e-4,
    8.31001272e-1,
    1.70560298,
    2.01774663,
    2.35191099.

The first projected gap therefore retains the same ~4.3e-8 scale as the fifth
nominal effective eigenvalue.  This is numerical targeting data only until the
interval F is instantiated.
"""

V = (
( 0.103946720000,  0.041291162100, -0.008344436550, -0.002373498220,  0.000517611510, -0.002538620890),
( 0.298233491000,  0.122947853000, -0.025655126100, -0.007498188960,  0.001591465740, -0.007953484740),
( 0.451515706000,  0.201570614000, -0.045037325200, -0.013981779700,  0.002792791730, -0.014537457300),
( 0.535787432000,  0.274091185000, -0.068746748700, -0.023824253000,  0.004199848240, -0.023751685200),
( 0.000487824682, -0.000338258405,  0.073333925600,  0.247459693000,  0.928825880000, -0.265832587000),
( 0.366754819000,  0.363235436000, -0.153828840000, -0.095729115700,  0.016798457900, -0.075657588400),
(-0.210233081000,  0.083071501100, -0.323362347000, -0.819703835000,  0.138754346000, -0.367469020000),
(-0.335652197000,  0.415281858000, -0.651652135000,  0.470370249000, -0.129808387000, -0.196213432000),
(-0.337647595000,  0.718971436000,  0.388658727000, -0.146750159000,  0.128227572000,  0.417357437000),
( 0.062782796200, -0.197995600000, -0.532172164000, -0.118644588000,  0.290562836000,  0.758316135000),
)

NOMINAL_PROJECTED_EIGS=(4.32680308e-8,2.55123446e-4,0.831001272,1.70560298,2.01774663,2.35191099)

if __name__=='__main__':
    print('fixed rational 10x6 candidate loaded; certify V^T F V > 0')
