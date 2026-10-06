"""Validate actual JSON schemas, frozen hashes, and packet reproducibility (stdlib)."""
from pathlib import Path
import json, subprocess, sys, tempfile
p=Path(__file__).resolve().parents[1]
r=p.parents[1]
def check(x,s,where):
 t=s.get('type')
 types={'object':dict,'array':list,'string':str}
 if t in types: assert isinstance(x,types[t]), f'{where}: expected {t}'
 if t=='object':
  assert set(s.get('required',[]))<=set(x), f'{where}: missing fields'
  if s.get('additionalProperties') is False: assert set(x)<=set(s.get('properties',{})),f'{where}: extra fields'
  for k,v in x.items():
   if k in s.get('properties',{}): check(v,s['properties'][k],where+'.'+k)
 if t=='array':
  for i,v in enumerate(x): check(v,s.get('items',{}),f'{where}[{i}]')
subprocess.run([sys.executable,str(r/'tools/check_frozen_core.py')],check=True)
for kind,schema in [('cases','input_schema.json'),('responses','output_schema.json')]:
 s=json.loads((r/'core'/schema).read_text())
 for f in sorted((p/kind).glob('*.json')):
  check(json.loads(f.read_text()),s,f.name)
  print('FULL SCHEMA PASS:',kind+'/'+f.name,flush=True)
  if kind=='responses': subprocess.run([sys.executable,str(r/'tools/validate_response.py'),str(f)],check=True)
with tempfile.TemporaryDirectory() as d:
 for f in sorted((p/'cases').glob('*.json')):
  out=Path(d)/'packet.txt'
  subprocess.run([sys.executable,str(r/'tools/build_prompt.py'),'--agent',str(p),'--case',str(f),'--out',str(out)],check=True,stdout=subprocess.DEVNULL)
  assert out.read_bytes()==(p/'prompts'/f'{f.stem}_v1.0.txt').read_bytes()
  print('PACKET REPRODUCTION PASS:',f.stem)
a=json.loads((p/'responses/primary_response.json').read_text())
b=json.loads((p/'responses/contrast_1_response.json').read_text())
assert a['general_et_finding']==b['general_et_finding']
assert a['application_finding']!=b['application_finding']
assert a['organization_specific_finding']!=b['organization_specific_finding']
print('CONTRAST STRUCTURE PASS (qualitative interpretation: test_record.md)')
print('PACKAGE VALIDATION PASSED')
