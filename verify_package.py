"""Validate an immutable public deployment archive before Pages upload."""
import hashlib,json,pathlib,tarfile
config=json.loads(pathlib.Path('release.json').read_text());archive=pathlib.Path('site.tar.gz')
assert hashlib.sha256(archive.read_bytes()).hexdigest()==config['archiveSHA256'],'archive hash'
root=pathlib.Path('_site');root.mkdir();seen=set();total=0
with tarfile.open(archive,'r:gz') as tar:
 for item in tar.getmembers():
  p=pathlib.PurePosixPath(item.name)
  assert not p.is_absolute() and '..' not in p.parts and '\\' not in item.name and item.name not in seen
  seen.add(item.name);assert item.isfile() or item.isdir()
  total+=item.size;assert total<1_000_000_000
  target=root/p;assert target.resolve().is_relative_to(root.resolve())
  if item.isdir():target.mkdir(parents=True,exist_ok=True)
  else:
   target.parent.mkdir(parents=True,exist_ok=True)
   with tar.extractfile(item) as source,target.open('xb') as output:
    import shutil
    shutil.copyfileobj(source,output)
receipt=json.loads((root/'deployment.json').read_text())
actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
assert actual==set(receipt['files'])|{'deployment.json'}
for name,meta in receipt['files'].items():
 p=root/name;assert p.stat().st_size==meta['bytes'];assert hashlib.sha256(p.read_bytes()).hexdigest()==meta['sha256'],name
assert receipt['sourceCommit']==config['sourceCommit']
print('Verified',len(actual),'public files;',total,'expanded bytes')
