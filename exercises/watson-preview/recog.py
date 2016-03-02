import requests
import os
from os.path import basename
from glob import glob
import json

endpoint = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify'

os.makedirs('responses', exist_ok=True)

DEFAULT_PARAMS = {
    'version': '2015-12-02'
}
DEFAULT_HEADERS = {
    'Accept': 'application/json'
}

creds = json.load(open('creds_watson_visual.json', 'r'))
my_username = creds['credentials']['username']
my_password = creds['credentials']['password']
myauth = (my_username, my_password)

for pic in glob(os.path.join('pics', '*.jpg')):
    current_path = pic
    # print(basename(pic))
    
    with open(pic, 'rb') as data:
        mydict = {}
        mydict['images_file'] = (pic, data)
        # print(mydict)
        resp = requests.post(endpoint, params=DEFAULT_PARAMS,
                        auth=myauth, headers=DEFAULT_HEADERS,
                        files=mydict)

    if resp.status_code == 200:
        # print(os.path.join('responses', basename(pic + '.json')))
        ibm_json = os.path.join('responses', basename(pic + '.json'))

        with open(ibm_json, 'w') as output:
        	output.write(resp.text)
    else:
    	print('Error code:', resp.status_code)