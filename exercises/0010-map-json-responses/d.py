import json

f = open('./tempdata/googlemaps/stanford.json', 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

answer = []

for i in range(4): 
	answer.append(mydict['results'][0]['address_components'][i]['long_name'])

print('; '.join(answer))