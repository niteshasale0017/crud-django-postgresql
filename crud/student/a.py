
d = {'shirt':{'1':'1','B':'OK','C':'C','2':'2'},'pant':{'2':'2','3':'3','4':'4'}}
print(d)


for i,j in d['shirt'].items():
	print(i+''+'='+''+j)
if 'shirt' in d:
	if 'B' in d['shirt']:
		k=d['shirt']['B']
		print(k)


