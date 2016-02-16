import os
import requests
from os.path import basename

#make the directory
os.makedirs('tempdata', exist_ok = True)
url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'

#download content
response = requests.get(url)
content = response.text
base = basename(url)

#open file
baby_name = os.path.join('tempdata', base)
baby_file = open(baby_name, 'wb')
baby_file.write(response.content)
baby_file.close()

print("There are", len(content), "characters in", baby_name)