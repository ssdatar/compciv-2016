import requests

r = requests.get('https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/')

print(r.status_code)
print(len(r.text))
print(r.url)