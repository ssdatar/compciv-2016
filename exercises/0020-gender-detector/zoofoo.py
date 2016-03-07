from os.path import join
import json

folder = 'tempdata'
jsonfile = join(folder, 'wrangledbabynames.json')

def detect_gender(name):
    result = {}
    with open(jsonfile, 'r') as json_in:
        mydict = json.load(json_in) #load as Python object

        for obj in mydict:
            if name.lower() == obj['name'].lower(): #compare if name matches
                result = obj
                return result #return if it does

        #else return NA dict
        if not len(result):
            result = {'name': name, 
                          'gender': 'NA',
                          'ratio': None,
                          'males': None,
                          'females': None,
                          'total': 0}
        return result