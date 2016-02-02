import os
import requests
from os.path import basename

#os.makedirs('tempdata', exist_ok = True)
url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'

response = requests.get(url)
content = response.text
base = basename(url)

got_name = os.path.join('tempdata', base)
got_file = open(got_name, 'wb')
got_file.write(response.content)
got_file.close()

print("There are", len(content.splitlines()), "lines in", got_name)



