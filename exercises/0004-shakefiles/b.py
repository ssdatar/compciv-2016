import requests
import os

url = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'
response = requests.get(url)
print('Downloading:', url)

filename = os.path.join('tempdata', 'matty.shakespeare.tar.gz')

fileopen = open(filename, 'wb')
fileopen.write(response.content)
print('Writing file:', filename)

fileopen.close()