"""Validate a complete bilingual editorial snapshot; no network or publication."""
import json,sys,datetime,re
from pathlib import Path
from urllib.parse import urlsplit
DAILY=('level','state','threshold','thresholdText','signal','signalText','factTitle','factText','interpTitle','interpText','hypTitle','hypText','disputeText')
def validate(path):
 d=json.loads(Path(path).read_text(encoding='utf-8'))
 datetime.date.fromisoformat(d['date'])
 assert isinstance(d['automationConnected'],bool), 'automationConnected must be boolean'
 assert d['vigilance']=='very-high', 'New vigilance scale needs editorial/UI review'
 ids=[x['id'] for x in d['sources']];assert len(ids)==len(set(ids))
 for x in d['sources']:
  u=x['url'];assert isinstance(x['label'],str) and x['label']
  assert (u.startswith('https://') and urlsplit(u).netloc) or re.fullmatch(r'sources/[\w.\-]+',u), 'Unsafe URL'
 for lang in ('fr','en'):
  assert all(isinstance(d['content'][lang][k],str) and d['content'][lang][k] for k in DAILY), 'Missing daily translation'
 riskids=[]
 for x in d['risks']:
  assert re.fullmatch(r'N\d{2,}',x['id']);riskids.append(x['id'])
  assert type(x['score']) is int and 1<=x['score']<=5
  assert type(x['historical']) is bool
  assert x['source'] in ids and type(x['row']) is int and x['row']>=2
  for field in ('domain','title','detail','qualification'):
   assert all(isinstance(x[field][l],str) and x[field][l] for l in ('fr','en'))
 assert len(riskids)==len(set(riskids))
 for x in d['events']:
  datetime.date.fromisoformat(x['date']);assert x['source'] in ids
  for field in ('title','text'):assert all(x[field].get(l) for l in ('fr','en'))
 return d
if __name__=='__main__':
 validate(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'site/data/bulletin.json')
 print('Bulletin FR/EN valide ; indices et références cohérents.')
