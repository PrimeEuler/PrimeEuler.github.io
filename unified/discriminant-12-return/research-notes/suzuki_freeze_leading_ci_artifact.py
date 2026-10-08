#!/usr/bin/env python3
"""Freeze complete CI leading-source vectors into hash-bound text parts."""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import shutil

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-root',type=Path,required=True)
    p.add_argument('--output-root',type=Path,required=True);a=p.parse_args()
    root=a.output_root;root.mkdir(parents=True,exist_ok=False)
    m={'schema':'cone.full-leading-source-artifact-manifest.v1',
       'source_contract':'finite-leading-w1','files':[],'snapshots':[],
       'even_certificate':'leading-32000-even-v.certificate.json',
       'odd_certificate':'leading-32000-odd-v.certificate.json',
       'pair_reference':'leading-C_S-32000.json',
       'source_commit':os.environ.get('GITHUB_SHA'),'run_id':os.environ.get('GITHUB_RUN_ID')}
    for sector in ('even-v','odd-v'):
        stem=f'leading-32000-{sector}'
        for suffix in ('.json','.certificate.json'):
            shutil.copyfile(a.input_root/(stem+suffix),root/(stem+suffix))
        raw=(a.input_root/(stem+'.full.zip')).read_bytes()
        enc=base64.b64encode(raw).decode('ascii');parts=[]
        for j,start in enumerate(range(0,len(enc),800000)):
            name=f'{stem}.full.zip.part{j:03d}.b64'
            (root/name).write_text(enc[start:start+800000],encoding='ascii');parts.append(name)
        m['snapshots'].append({'snapshot_file':stem+'.full.zip','bytes':len(raw),
                              'sha256':hashlib.sha256(raw).hexdigest(),'base64_parts':parts,
                              'certificate_file':stem+'.certificate.json','payload_file':stem+'.json'})
    for name in ('leading-C_S-32000.json','actual256-finite-Q-with-leading-certificate.json'):
        shutil.copyfile(a.input_root/name,root/name)
    for path in sorted(root.iterdir()):
        raw=path.read_bytes();m['files'].append({'file':path.name,'bytes':len(raw),
                                               'sha256':hashlib.sha256(raw).hexdigest()})
    (root/'artifact_manifest.json').write_text(json.dumps(m,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'files':len(m['files']),'bytes':sum(x['bytes'] for x in m['files']),
                      'source_commit':m['source_commit'],'run_id':m['run_id']}))
if __name__=='__main__':main()
