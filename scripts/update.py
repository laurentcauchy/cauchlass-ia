"""Preview or apply a reviewer-approved bulletin locally. Does not publish."""
import argparse,datetime,json,os,tempfile
from pathlib import Path
from validate import validate
p=argparse.ArgumentParser();p.add_argument('candidate',type=Path);p.add_argument('--apply',action='store_true');p.add_argument('--approved-by');args=p.parse_args()
root=Path(__file__).resolve().parents[1];candidate=validate(args.candidate);current=root/'site/data/bulletin.json';old=validate(current)
assert candidate['date']>=old['date'],'A newer edition may not be replaced by an older one'
assert candidate['date']<=datetime.date.today().isoformat(),'Future-dated bulletin'
for s in candidate['sources']:
 if s['url'].startswith('sources/'):assert (root/'site'/s['url']).is_file(), 'Missing source document'
print('Candidate:',candidate['date'],'|',len(candidate['risks']),'risks | bilingual narrative complete')
if not args.apply:
 print('Preview only. No file changed. Laurent must review findings, indices, source documents and both translations.')
else:
 assert args.approved_by=='Laurent','Explicit editorial approval by Laurent is required'
 archive=root/'site/data/archive';archive.mkdir(exist_ok=True)
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
 (archive/(old['date']+'-'+stamp+'.json')).write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
 candidate['reviewer']='Laurent';candidate['reviewedAt']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=current.parent,delete=False) as f:
  json.dump(candidate,f,ensure_ascii=False,indent=2);f.write('\n');temp=f.name
 os.replace(temp,current)
 print('Local update applied and previous version archived. GitHub has not been contacted.')
