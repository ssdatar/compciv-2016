import os
import requests

path1 = os.path.join('tempdata', 'googlemaps')
path2 = os.path.join('tempdata', 'mapzen')
os.makedirs(path1, exist_ok = True)
os.makedirs(path2, exist_ok = True)

url1 = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
url2 = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'

file1 = os.path.join(path1, 'stanford.json')
file2 = os.path.join(path2, 'stanford.json')

data1 = requests.get(url1).text
data2 = requests.get(url2).text
linenum1 = len(data1.splitlines())
linenum2 = len(data2.splitlines())

print("---")

ffile1 = open(file1, 'w')
ffile1.write(data1)
ffile1.close()
print("Downloading from:", url1)
print("Writing to:", file1)
print("Wrote",linenum1, "lines and", len(data1),"characters")

print("---")

ffile2 = open(file2, 'w')
ffile2.write(data2)
ffile2.close()
print("Downloading from:", url2)
print("Writing to:", file2)
print("Wrote",linenum2, "lines and", len(data2),"characters")