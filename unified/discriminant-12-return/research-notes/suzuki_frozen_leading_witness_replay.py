#!/usr/bin/env python3
"""Decode complete leading-source snapshots and replay the finite C_S certificate."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import tempfile
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_exact_leading_source_certificate import certificate,capacity_interval
from suzuki_exact_leading_coefficient_pair import analyze

def replay(root):
    manifest=json.loads((root/'artifact_manifest.json').read_text())
    assert manifest['source_contract']=='finite-leading-w1'
    for x in manifest['files']:
        raw=(root/x['file']).read_bytes()
        assert len(raw)==x['bytes'] and hashlib.sha256(raw).hexdigest()==x['sha256']
    rows=[]
    with tempfile.TemporaryDirectory() as d:
        for x in manifest['snapshots']:
            encoded=''.join((root/p).read_text() for p in x['base64_parts'])
            raw=base64.b64decode(encoded,validate=True)
            assert len(raw)==x['bytes'] and hashlib.sha256(raw).hexdigest()==x['sha256']
            p=Path(d)/x['snapshot_file'];p.write_bytes(raw)
            meta,s,v,P=read_snapshot(p)
            assert meta['remote_start']==0 and meta['normalizer']['offset_scale']=='0'
            cert=certificate(s,v,P,meta['normalizer'],meta['sector'],meta['kernel_bits'])
            cert['leading_capacity_interval']=capacity_interval(cert)
            out=(json.dumps(cert,indent=2,sort_keys=True)+'\n').encode()
            assert out==(root/x['certificate_file']).read_bytes()
            payload=json.loads((root/x['payload_file']).read_text())
            assert payload['certificate']==cert and payload['snapshot_sha256']==x['sha256']
            assert payload['normalizer']==meta['normalizer']
            rows.append({'sector':cert['sector'],'cutoff':cert['cutoff'],
                         'certificate_sha256':hashlib.sha256(out).hexdigest(),
                         'all_six_numerical_targets_met':cert['all_six_numerical_targets_met'],
                         'leading_capacity_interval':cert['leading_capacity_interval']})
    pair=analyze(root/manifest['even_certificate'],root/manifest['odd_certificate'])
    assert (json.dumps(pair,indent=2,sort_keys=True)+'\n').encode()==(root/manifest['pair_reference']).read_bytes()
    return {'schema':'cone.frozen-leading-source-replay.v1','rows':rows,'pair':pair,
            'all_certificates_and_pair_byte_identical':True,'infinite_capacity_tail_closed':False}

def main():
    p=argparse.ArgumentParser();p.add_argument('--payload-root',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--compare-reference',action='store_true')
    a=p.parse_args();o=replay(a.payload_root);raw=(json.dumps(o,indent=2,sort_keys=True)+'\n').encode()
    if a.compare_reference:assert raw==(a.payload_root/'leading_replay.json').read_bytes()
    a.output.write_bytes(raw)
    print(json.dumps({'byte_identical':True,'C_S_abs_le_640_exact':o['pair']['C_S_abs_le_640_exact'],
                      'infinite_capacity_tail_closed':False},indent=2))
if __name__=='__main__':main()
