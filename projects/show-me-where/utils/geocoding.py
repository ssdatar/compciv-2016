import json
import requests

def geocode(location):
    """
    Attempt to geocode a location string using Mapzen Search API

    The input:
    ----------------
    You have to feed it a location as a string. E.g. Mumbai, India or Stanford, CA.
    
    It also expects the variable `CREDS_FILE` to point to an existing file
    that contains a valid Mapzen Search key.

    What it does:
    -------------
    It opens and reads the file at CREDS_FILE to get the API key.

    It calls the Mapzen Search API via a HTTP request, using the API key, 
    and the user-provided `location` string as the `text` parameter.

    It then converts the received JSON object into a Python dictionary
    using the JSON library.

    What it returns:
    ----------------
    A dictionary containing these key-value pairs:

    - query_text: the `location` string provided by the user
    - label: The string label that Mapzen provides in describing the found location
    - confidence: A float representing the confidence value that Mapzen has in its result.
    - latitude: a float representing the latitude coordinate
    - longitude: a float representing the longitude coordinate
    - status: "OK", a string that indicates a result was found. Else, None

    """

    answer = {}
    API_response = fetch_mapzen_response(location)
    answer = parse_mapzen_response(API_response)
    answer['query_string'] = location

    return answer

def fetch_mapzen_response(location):
    """
    `location` is a string that will be passed onto Mapzen API for geocoding

    This will give you (return) JSON-formatted data from Mapzen
    """
    mykey = get_credentials()
    myparams = {'text': location, 'api_key': mykey}

    URL = 'https://search.mapzen.com/v1/search'
    resp = requests.get(URL, params = myparams)
    return resp.text

def parse_mapzen_response(txt):
    """
    This function takes the json response sent by Mapzen and converts it
    into a dictionary with key-value pairs.

    It returns the dictionary
    """

    parsed = {} #empty dictionary

    data = json.loads(txt)

    if data['features']:
        parsed['status'] = 'OK'
        feature = data['features'][0]
        props = feature['properties']  # just for easier reference
        parsed['confidence'] = props['confidence']
        parsed['label'] = props['label']

        # now get the coordinates
        coords = feature['geometry']['coordinates']
        parsed['longitude'] = coords[0]
        parsed['latitude'] = coords[1]
    else:
        parsed['status'] = None

    return parsed

def get_credentials():
    filename = 'creds_mapzen.txt'
    API_key = open(filename).read().strip()
    return API_key



