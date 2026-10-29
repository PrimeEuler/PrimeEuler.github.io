# Payload manifest — scalar H2 source certificate (v15.118)

Producer inputs (already deposited at payloads/am3scalar_svt_reconciliation_v14_996/):
- scalar_final2.py sha256 8e2a8e54694470226ec9987b255ca35702040f97aa0275ad6e25d65cbd32fe56
- scalar_adm2.py  sha256 7df79aba16ef15d0a38adf0ef8a0bcdd69be3b5dc670081338e1295ff724e57c

Files in this payload (sha256):
- fourier_hessian_check.py  c14e9f9c8e848c46587c1e4fca3d3e06291aa35bfb00ecaba1f55598ff0ba8cd
- fourier_output.txt        ff093c615c5c17fc38f4e0390cfb9df8b6cb2dc78669eecf1836eed02c4fcd28
- h2_substitution.py        ff89aaa57a5fb7a87cabc84b8ecc5ebf50b3cad89f0621c0db7b1d080b2040d8
- h2_substitution_stdout.txt 74e18bd0ad4c4d4680a865b42615f91103019dbbe9476a3c460f015d831c48a6
- h2_verify.py              a3b21b9b8344962ee840ea37a27717c9919bf1ae607346f6d3ed7c2f6d7e1348
- h2_certificate.txt        f6a4faf4889ac7a97dffa54220932375038df188a94a29b64ac66febc4ffbe85
- scalar_final2_stdout.txt  cd93de11bbfbf8882708cae534b277eb116ee39dff0ec88c82128196c26f9dd8
- scalar_final.txt          29159b886e8ede57335330a7d67f28648729c1bd85113487a8d77ed2e53029fa

Run order: scalar_final2.py (in a dir with scalar_adm2.py) -> fourier_hessian_check.py -> h2_substitution.py (same dir) -> h2_verify.py.
