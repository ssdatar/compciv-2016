import json

f = open('./tempdata/googlemaps/stanford.json', 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
print(mydict['status'])