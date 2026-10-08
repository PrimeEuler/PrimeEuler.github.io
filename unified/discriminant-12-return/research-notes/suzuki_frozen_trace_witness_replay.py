#!/usr/bin/env python3
"""Decode and verify frozen CI trace witnesses; standard library only."""
import argparse
import base64
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import tempfile

from suzuki_exact_represented_trace_certificate import replay
from suzuki_trace_congruence_replay import display


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--payload-root', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--compare-reference', action='store_true')
    args = ap.parse_args()
    manifest = json.loads((args.payload_root / 'artifact_manifest.json').read_bytes())
    assert manifest['schema'] == 'cone.frozen-normalized-joint-trace-run.v1'
    rows = []
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        for item in manifest['files']:
            assert Path(item['stored_file']).name == item['stored_file']
            assert Path(item['file']).name == item['file']
            raw = (args.payload_root / item['stored_file']).read_bytes()
            if item['encoding'] == 'base64':
                raw = base64.b64decode(b''.join(raw.split()), validate=True)
            else:
                assert item['encoding'] == 'utf8'
            assert hashlib.sha256(raw).hexdigest() == item['sha256']
            assert len(raw) == item['bytes']
            (root / item['file']).write_bytes(raw)
        for cutoff in (64000, 128000):
            for sector in ('even-v', 'odd-v'):
                payload = root / f'joint-{cutoff}-{sector}.json'
                witness = root / f'joint-{cutoff}-{sector}.trace-{cutoff}.json.gz'
                certificate = replay(witness, payload)
                assert certificate['relative_defect_target_met_exact']
                rho = F(certificate['relative_defect_fro_upper_rational'])
                rows.append({'cutoff': cutoff, 'sector': sector,
                             'certificate': certificate,
                             'relative_cap_display': display(rho),
                             'target_margin_display': display(F('1e-20') / rho),
                             'parent_payload_sha256': hashlib.sha256(payload.read_bytes()).hexdigest(),
                             'replay_matches_parent_exactly': True})
    out = {'schema': 'cone.actual-cutoff-exact-trace-replay.v1',
           'run_id': manifest['run_id'], 'run_head_sha': manifest['run_head_sha'],
           'all_four_targets_met_exactly': True,
           'artifact_zip_digests_verified_at_acquisition': manifest['artifact_zip_digests_verified_at_acquisition'],
           'rows': rows,
           'overall_certificate_ready': False}
    # The artifact ZIP digests describe the acquisition check. Frozen files
    # are independently checked above; offline replay does not download ZIPs.
    encoded = json.dumps(out, indent=2, sort_keys=True) + '\n'
    if args.compare_reference:
        assert encoded.encode() == (args.payload_root / 'actual_cutoff_trace_replay.json').read_bytes()
    args.output.write_text(encoded)
    print(json.dumps({'all_four_targets_met_exactly': True,
                      'reference_byte_identical': args.compare_reference,
                      'overall_certificate_ready': False}, sort_keys=True))


if __name__ == '__main__':
    main()
