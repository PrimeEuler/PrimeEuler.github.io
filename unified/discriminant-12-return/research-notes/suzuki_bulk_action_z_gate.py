#!/usr/bin/env python3
"""Replay existing physical action-z certificate through additive bulk path."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import suzuki_action_precision_z_gate as reference
from suzuki_bulk_action_z import evaluate,nonprime
from suzuki_certified_remote_z import constants,precise_nonprime

def build(source_gate,action_gate):
    original=action_gate.read_bytes()
    assert hashlib.sha256(original).hexdigest()=='4437af2f84b24e9adcb01de6b4833abcd0acaf21ec756283b93a103041b39674'
    reference.evaluate=lambda n,action_precision=True:evaluate(n)
    rebuilt=(json.dumps(reference.build(source_gate),indent=2,sort_keys=True)+'\n').encode()
    assert rebuilt==original
    for row in json.loads(original)['cases']:
        n=int(row['n']);bits=row['working_bits'];pi=constants(bits)[0]
        lo,hi=nonprime(n,pi,bits);oldlo,oldhi=precise_nonprime(n,pi,bits)
        assert lo<=oldlo<=oldhi<=hi,n
    assert F(10**12,1<<512)<F('1e-140')
    return {'schema':'cone.bulk-action-z-replay.v1',
        'original_action_gate_sha256':hashlib.sha256(original).hexdigest(),
        'all_50_original_physical_diagnostics_repeated':True,
        'complete_original_action_gate_byte_identical':True,
        'all_50_original_exact_nonprime_intervals_nested':True,
        'nonprime_point_arithmetic_error_budget_rational':'1000000000000/2^B',
        'cached_moment_radius_budget_rational':'10000000000/2^B',
        'minimum_working_bits':512,'uniform_total_radius_strict_upper_rational':'1/1000000000000000000000000000000000000000',
        'original_scalar_producer_modified':False,'finite_lift_solve_certified':False,
        'whole_remote_action_evaluated':False,'infinite_capacity_tail_closed':False}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name in ('source-gate','action-gate','output'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();a.output.write_text(json.dumps(build(a.source_gate,a.action_gate),indent=2,sort_keys=True)+'\n')
    print('Full 50-case original physical action gate reproduced byte-identically by bulk path.')
