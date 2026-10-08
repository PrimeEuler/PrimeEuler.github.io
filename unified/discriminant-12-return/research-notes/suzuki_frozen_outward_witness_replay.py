#!/usr/bin/env python3
"""Decode hash-bound full snapshots and independently replay every outward cap."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import tempfile
from suzuki_exact_outward_certificate import replay_snapshot
from suzuki_exact_outward_pair_certificate import analyze


def replay(root):
    manifest = json.loads((root/'artifact_manifest.json').read_text())
    for item in manifest['files']:
        raw = (root/item['file']).read_bytes()
        assert len(raw) == item['bytes']
        assert hashlib.sha256(raw).hexdigest() == item['sha256']
    rows = []
    with tempfile.TemporaryDirectory() as scratch:
        for item in manifest['snapshots']:
            encoded = ''.join((root/part).read_text() for part in item['base64_parts'])
            raw = base64.b64decode(encoded, validate=True)
            assert len(raw) == item['bytes']
            assert hashlib.sha256(raw).hexdigest() == item['sha256']
            snapshot = Path(scratch)/item['snapshot_file']; snapshot.write_bytes(raw)
            cert = replay_snapshot(snapshot)
            replayed = (json.dumps(cert,indent=2,sort_keys=True)+'\n').encode()
            assert replayed == (root/item['certificate_file']).read_bytes()
            payload = json.loads((root/item['payload_file']).read_text())
            matched = [r for r in payload['rows'] if r['sector']==cert['sector'] and r['cutoff']==cert['cutoff']]
            assert len(matched)==1 and matched[0]['outward_numerical_certificate']==cert
            assert matched[0]['M_trial_midpoint']==cert['M_point_decimal']
            assert matched[0]['outward_snapshot']['sha256']==item['sha256']
            assert cert['all_six_numerical_targets_met']
            rows.append({'sector':cert['sector'],'cutoff':cert['cutoff'],
                         'certificate_sha256':hashlib.sha256(replayed).hexdigest(),
                         'bounds_display':cert['bounds_display'],'checks_exact':cert['checks_exact'],
                         'relative_trace_fro_upper_rational':cert['relative_trace_fro_upper_rational']})
    result = {'schema':'cone.frozen-outward-replay.v1','rows':rows,
              'all_rows_meet_all_six_numerical_targets_exactly':True,
              'all_certificates_byte_identical':True,'overall_certificate_ready':False}
    if 'pair_inputs' in manifest:
        pair = analyze([root/name for name in manifest['pair_inputs']])
        pairraw = (json.dumps(pair,indent=2,sort_keys=True)+'\n').encode()
        assert pairraw == (root/manifest['pair_reference']).read_bytes()
        result['pair'] = pair
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--payload-root',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True);ap.add_argument('--compare-reference',action='store_true')
    args=ap.parse_args();out=replay(args.payload_root)
    raw=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode()
    if args.compare_reference: assert raw == (args.payload_root/'outward_replay.json').read_bytes()
    args.output.write_bytes(raw)
    print(json.dumps({'all_rows_meet_all_six_numerical_targets_exactly':True,
                      'all_certificates_byte_identical':True,
                      'reference_byte_identical':args.compare_reference,
                      'overall_certificate_ready':False},indent=2))


if __name__=='__main__':main()
