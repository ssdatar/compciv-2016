import requests

r = requests.get('https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/')
speech = r.text

print(speech.count('Applause'))
print(speech.lower().count('applause'))
print(speech.count('<p>'))