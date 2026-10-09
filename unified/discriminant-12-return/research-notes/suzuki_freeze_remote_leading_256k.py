#!/usr/bin/env python3
"""Lossless, hash-pinned freeze of the completed actual-256k CI archive."""
import argparse, base64, hashlib, json
from pathlib import Path
EXPECTED_MANIFEST = '46fbe78e59f96f7ec2ce7848e9cfb2ac4d7eabe67f4a7eccf9df80dff59df139'
SOURCE_COMMIT = '0aaff9b4d0225679d02d3d031515f8f578bb6b4c'
RUN_ID = 37965642729
ARTIFACT_ID = 11634776766

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def freeze(source, output):
    raw_manifest = (source/'manifest.json').read_bytes()
    assert digest(raw_manifest) == EXPECTED_MANIFEST, 'CI manifest pin mismatch'
    manifest = json.loads(raw_manifest)
    assert manifest['schema'] == 'cone.remote-leading-ci-byte-manifest.v1'
    entries = manifest['files']
    names = [x['path'] for x in entries]
    required = ['remote-leading-selfenergy-256000.json']
    for sector in ('even-v', 'odd-v'):
        required += [f'leading-256000-{sector}{suffix}' for suffix in
                     ('.json', '.certificate.json', '.replayed.json', '.preflight.json',
                      '.full.zip', '.trace.json.gz')]
    assert sorted(names) == sorted(required) and len(set(names)) == 13
    assert sorted(p.name for p in source.iterdir()) == sorted(names+['manifest.json'])
    for x in entries:
        raw = (source/x['path']).read_bytes()
        assert len(raw) == x['bytes'] and digest(raw) == x['sha256']
    for sector in ('even-v', 'odd-v'):
        stem = f'leading-256000-{sector}'
        cert_bytes = (source/(stem+'.certificate.json')).read_bytes()
        assert cert_bytes == (source/(stem+'.replayed.json')).read_bytes()
        cert = json.loads(cert_bytes)
        assert cert['sector'] == sector and cert['cutoff'] == 256000
        assert cert['remote_start'] == 0 and cert['all_six_numerical_targets_met']
        assert all(cert['checks_exact'].values())
        payload = json.loads((source/(stem+'.json')).read_bytes())
        assert payload['certificate'] == cert
        assert payload['snapshot_sha256'] == digest((source/(stem+'.full.zip')).read_bytes())
    pair = json.loads((source/'remote-leading-selfenergy-256000.json').read_bytes())
    assert pair['cutoff'] == 256000
    assert not pair['original_C_S_32000_replaced']
    assert not pair['infinite_operator_action_certified']
    assert not pair['infinite_capacity_tail_closed']
    output.mkdir(parents=True, exist_ok=False)
    frozen = {'schema':'cone.remote-leading-frozen-archive.v1',
              'source_commit':SOURCE_COMMIT, 'run_id':RUN_ID, 'artifact_id':ARTIFACT_ID,
              'ci_manifest_sha256':EXPECTED_MANIFEST, 'cutoff':256000,
              'all_original_files_reconstructed_and_hash_verified':True, 'files':[]}
    for name in sorted(names+['manifest.json']):
        raw = (source/name).read_bytes()
        row = {'file':name, 'bytes':len(raw), 'sha256':digest(raw)}
        if name.endswith('.json'):
            json.loads(raw)
            (output/name).write_bytes(raw)
            row['encoding'] = 'raw-utf8'
            row['parts'] = [name]
        else:
            encoded = base64.b64encode(raw).decode('ascii')
            parts = []
            for j, start in enumerate(range(0,len(encoded),800000)):
                part = f'{name}.part{j:03d}.b64'
                (output/part).write_text(encoded[start:start+800000], encoding='ascii')
                parts.append(part)
            row['encoding'] = 'base64'
            row['parts'] = parts
        restored = b''.join((output/p).read_bytes() for p in row['parts'])
        if row['encoding'] == 'base64':
            restored = base64.b64decode(restored, validate=True)
        assert restored == raw and digest(restored) == row['sha256']
        row['part_hashes'] = [{'file':p, 'bytes':(output/p).stat().st_size,
                              'sha256':digest((output/p).read_bytes())} for p in row['parts']]
        frozen['files'].append(row)
    (output/'artifact_manifest.json').write_text(json.dumps(frozen,indent=2,sort_keys=True)+'\n')
    return frozen

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--input-root', type=Path, required=True)
    p.add_argument('--output-root', type=Path, required=True)
    a = p.parse_args()
    result = freeze(a.input_root,a.output_root)
    print(json.dumps({'original_files':len(result['files']), 'run_id':RUN_ID,
                      'lossless_reconstruction_verified':True}))
