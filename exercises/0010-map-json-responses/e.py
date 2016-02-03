import json

f = open('./tempdata/googlemaps/stanford.json', 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

faddress = mydict['results'][0]['formatted_address']
x = mydict['results'][0]['geometry']['location']['lat']
y = mydict['results'][0]['geometry']['location']['lng']

print(faddress + ';' + str(x) + ';' + str(y))