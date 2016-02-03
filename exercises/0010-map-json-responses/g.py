import json

f = open('./tempdata/mapzen/stanford.json', 'r')
txt = f.read()
f.close()

myarray = json.loads(txt)['features']

for i in myarray:
	label = i['properties']['label']
	ci = i['properties']['confidence']
	x = i['geometry']['coordinates'][0]
	y = i['geometry']['coordinates'][1]
	print(';'.join([label, str(ci), str(x), str(y)]))