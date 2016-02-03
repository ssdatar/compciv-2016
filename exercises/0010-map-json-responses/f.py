import json

f = open('./tempdata/mapzen/stanford.json', 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
main_keys = sorted(mydict.keys())

query_keys = sorted(mydict['geocoding']['query'].keys())

print(main_keys[3] + ':', mydict[main_keys[3]])
print(query_keys[4] + ':', mydict['geocoding']['query'][query_keys[4]])
print(query_keys[3] + ':', mydict['geocoding']['query'][query_keys[3]])
print(query_keys[0] + ':', mydict['geocoding']['query'][query_keys[0]])

