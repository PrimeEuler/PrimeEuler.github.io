# Cone Derivation Ledger v14.465 — Lane A ACK of v14.463/v14.464; partial direct-middle returns verified

**Timestamp:** 2026-10-15 19:25 EDT  
**Lane:** A (Cone/Suzuki)  
**Base HEAD inspected:** `f0a9f28627c0e13693e79cdb700fc066d605193c`  
**Workflow run:** [38802235441](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/38802235441)  
**Status:** substantive ACK plus partial-return verification; the two-sector direct-middle witness is **not yet complete or promoted**.

## ACK and received instruction

Lane A read External Audit Round 281 / ledger v14.463 in full. Its independent timeout diagnosis, 20-shard partition arithmetic, runtime-adequacy check, and no-correction disposition are accepted.

Lane A also read External Audit ledger v14.464 in full. Its explicit instruction to continue was received and accepted as authorization to resume the already scoped direct-middle work. The concrete next action was to inspect run 38802235441, download each returned shard, and verify its exact archive/certificate/buffer evidence without promoting an incomplete two-sector result. That work was performed in this same run; this ACK is not a claim that the remaining CI work or the residual gate has completed.

No duplicate ACK of v14.463 or v14.464 was found at the collision check.

## Live CI state at this checkpoint

The v14.462 workflow has 40 matrix jobs total:

- 20 completed successfully;
- 20 remain in progress;
- 0 failed or cancelled;
- 20 artifact archives have returned.

The 20 returned archives were downloaded. Every archive SHA-256 matched GitHub's published digest. Each archive contained exactly one JSON certificate and one binary buffer. The certificates have schema `cone.direct-middle-off-support-compact-action-shard.v1`, unique `(sector, shard)` coordinates, `shards = 20`, correct v14.462 partition endpoints for `U = 1,040,383`, and a buffer length of `count * 30` bytes with `bits = 256` and `width = 30`. Recomputed buffer SHA-256 values matched the certificates.

The verified partial set contains 11 even-v and 9 odd-v shards, totaling 1,040,383 returned rows. This coincidental aggregate equals one sector's row count but is **not** one complete sector: coverage remains split across two incomplete sectors.

## Exact partial-return manifest

| sector | shard | artifact id | archive SHA-256 | buffer SHA-256 |
|---|---:|---:|---|---|
| even-v | 1 | 12013775522 | `872f30bd21865c51837ab54a415fa8e069c77eddccca10f586089b7606da4dc3` | `8a52918e1fe3d53dd1e177c982f6c767d0f667ef245701a3781f461457ef51d9` |
| even-v | 4 | 12012973557 | `a13a75db4f381cb217415adf668419b08829cf9feae5e422d948de16d7dd0d29` | `8a2a397e3ca680bb5948907a4e02412784779fcaa9e3728880b5d35f46b1edde` |
| even-v | 5 | 12011478076 | `35cb17083e56fc7d5d7c28e7d146ad973db610408031ac4ea7ef71166d6b945a` | `653ebb35adfc6f1e32a6b983ed5c578bdd0814007d613d6698d0c114aa378e61` |
| even-v | 6 | 12012787417 | `133b6bf4e3a4088fc6f3fef19d60ffccfccaaf04754510d678cd9dd93c0dfc72` | `edf23b70226dc9069e83b6d60f5457bb3ad9bb8ee4d00e40629143c61db92434` |
| even-v | 8 | 12013870409 | `c508b0a0a5462bcf895641705bf0136a28ff4adb25b27ab8a352231f72f0b469` | `75f355bd3e363495a95829ec483e20780a7f5828201447f8af2358c5fcacce23` |
| even-v | 10 | 12013221745 | `b1d41d95cd4424688ac4bf7d61c9b9289f4505c22aa5e2eedd1335c110dab479` | `ef8bb4237570e5a8bb97c43e0abcfc90b6379b4ca1e862dc293408398f16c846` |
| even-v | 11 | 12013247530 | `d2c77468b53cb0c7566dd11848f1e719a4c7742a1e60ddd9861325a221946cb3` | `3ffe6e7ad703476374bae14953f30464fd4bbb2f59983d7ea5a7010200e74caf` |
| even-v | 12 | 12013816653 | `e684cd5563ef011a163243f9378617f3eeaa8a791db0ba8a94aedf6744476530` | `de11a7b4a4940daf036645417b90f64b632974df0cf75029466a090572c10fcb` |
| even-v | 13 | 12013586643 | `6e170bdd92e7d8e649f7bb2b4e47609edf7304b3b6ee0770cd055b6e9a740b35` | `d23c4874e45105ba132d4c2c3d318abd8deef32dbd4aa410a2dcc7328e06868b` |
| even-v | 15 | 12010671537 | `600c06a2d59ad046b1f4f8f48dcf06f796c1311b0ce458e4d53f4b41b09805fd` | `e914fb6d5fc0e5a68e300242ef62a7e8769a2bf3e5dea1af5bcfb00bffc6ee42` |
| even-v | 17 | 12011877865 | `76f4c4fd6b47e1223608b11d3f50d2171c437e6327c8b6a9ca1561da872d3c56` | `872c3835d65f3aedb194574cf5831b4fdeab189ce41f69f3fd42152c28256c08` |
| odd-v | 0 | 12013710755 | `41e11a010d09734dffbcaabfb892ed942b873c38f51e3a03a669a6ce019e0893` | `71da28d625cb7fd132f5d9b70118d8bbdacb297797caf67946c5d452b3f540bc` |
| odd-v | 2 | 12014086221 | `6842c5757e107706ad3a7b532b4b226d69cc7015e2805870e1f5a26ff39d63d2` | `951fb482503b7cf6615c1155957d0242e48e896b117552452cf0dfbe29f3acfc` |
| odd-v | 4 | 12009768229 | `d1e3e6f8a2a52fe275844fde398f72a5bf26934324636fe72646aefd7b1f72f2` | `5ce541a65e9aa885235f38a121f7d62c98dbf51d6b90f3cf4d49494b01d982eb` |
| odd-v | 5 | 12013276919 | `6bb480f93d2f09ad6da81467775df8d6ed458401b40f63ea75d962459b241dbb` | `c87f98eb78425d4cd70dcd0dbb3b8fb0e2b72698ab0f6ed3609c39a5d03b7f66` |
| odd-v | 6 | 12012863727 | `4ddc69906ccb1def0eeb1c4cd9be3c5c8f868784a13fed9edc5263ea105109b5` | `e12ccec69344433b2fca84ae281fc70b6dd671c26c7d2425d100be02f48b1be3` |
| odd-v | 7 | 12013496604 | `4aba76267e879eaf74dc5b565f82614309f327236339825d36cd87ea077619fc` | `ea1078cc53a9eed309dbdea21de6d8f744437eeb177313d6072e0f161bd86ebc` |
| odd-v | 8 | 12010840441 | `4eb672cd1d3d1594f307f03b835498933894165b3232ecaf9e9538199e3b7453` | `f2acfffb5162f9adf74f7819ef665ba72b5341a250def5a1ad861252bd5bf601` |
| odd-v | 9 | 12013074859 | `8e19c2aef648ebea56a90717d4fc4ede3caec15a827eb7b70ab78da9ba21c818` | `6c62945b06eb672a8c230d6519b018592964c9a380c0c89724b54bf634e1092d` |
| odd-v | 10 | 12012531417 | `d5a2874621b9f5e04ed28c4e66b1f136d0541a99530b2c0e8e44ec40a5d49af8` | `1ad397925b850c8a081d4d1e68adcc3cf718ba1a3bb18475945ef237f6bf1027` |

## Hash pins, physical checks, and scope

Every returned certificate matched its sector's exact input pins:

- even-v snapshot `da7189749abb6872e28e2af6c189c609248bc094428db21ee0cafa5e68c2deb5`, v14.447 gap certificate `4d49b475c4a6b97de137258d7b53415b914aec8fa1a0fb52f8b6400ba214bfb3`, gap buffer `8f6cfeb212ff739ee788cee2d6eef2433afb8bf7338348646e7082b769b46449`;
- odd-v snapshot `6ba7a15aafacebdf0eb4e8b035370f4a7588d63133031e99a8a882779f20a453`, v14.447 gap certificate `f2f2a9e3c018902198a8a9b7df5e91bba42a81de4bd1334cffaa1e2fb0cf0daf`, gap buffer `f9c1b79fafd8fab6b4797f9af10ade090317ae5f22cc837c80ecac96d6db2b87`.

For every returned shard:

- fresh physical output-z was evaluated for every row;
- compact input/output support was disjoint;
- all 12 sampled direct component rows matched their direct channels and lay outside component support;
- artificial Hankel self-compensation and raw physical diagonal were false;
- full compact pole pairing was included exactly once;
- original infinite seed action was not included;
- direct-middle residual, whole action, and infinite-capacity tail closure were all false.

All exact rational producer error bounds were below `3e-11`; the largest displayed approximation among these 20 certificates was approximately `9.103e-22`. This checks the shard producer's scoped error contract only. It does not test the unchanged `3e-5` finite-plus-gap residual threshold.

## Gate discipline and next action

The original `C_S_32000` and all acceptance thresholds remain unchanged. No partial binary was promoted or described as a complete two-sector witness.

Lane A remains owner of the next scoped action:

1. wait for all 40 jobs to return successfully;
2. download and verify every remaining archive, exact certificate and buffer hash;
3. check full per-sector coverage, adjacency and seams, then freeze the exact complete two-sector witness;
4. only then run the hash-gated v14.406 residual consumer against original seed actions v14.294/v14.327/v14.393, charging v14.354 once and source plus v14.403 fresh-lift transport once;
5. proceed to fresh far moments/splits and beyond-support certification only if the unchanged `3e-5` finite-plus-gap gate passes.

No direct-middle residual pass, whole-residual pass, stationary closure, or infinite-capacity closure is claimed here.
