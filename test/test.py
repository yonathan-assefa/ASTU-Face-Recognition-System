from pathlib import Path

fol = Path("./../logs/").rglob('*.lf')


to = []
for i in fol:
	ddv=open('./'+str(i))
	pr = ddv.read().split('|')
	
	for i in pr:
		t = i.split('$')
		try:
			to.append(t[0]+' ' + t[1])
		except:
			pass


print(to)
