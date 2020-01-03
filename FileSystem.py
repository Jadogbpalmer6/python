from time import*
from pathlib import Path
a=Path('django')
print(a.exists())
try:
        b=Path('jad0123')
        b.mkdir()
except FileExistsError:
        print('the file exists and it is going to be deleted instead')
        b.rmdir()
c=Path('jado')
print(c.exists())
if c.exists() :
        print('directory named jado exists')
else :
        print ('directory named jado does not exists it is going to be created')
        c.mkdir()
d=Path('django/mysite')
for item in d.glob('*'):
        print(item)

sleep(10)
