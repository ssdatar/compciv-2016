import requests
import os

photos = ['https://upload.wikimedia.org/wikipedia/commons/6/68/Donald_Trump_mural.jpg',
		'http://cdn.loc.gov/service/pnp/highsm/04400/04460r.jpg',
		'https://c2.staticflickr.com/2/1638/24902500570_25c1894293_b.jpg',
		'http://www.lifeofpix.com/wp-content/uploads/2015/12/Life-of-Pix-free-stock-photos-subway-girl-reflection-macnicolae.jpg',
		'https://farm8.staticflickr.com/7511/15798317460_450c890d87_o.jpg'
		]
names = ['trump', 'lights', 'potus', 'train', 'ski']

os.makedirs ('pics', exist_ok=True)

i = 0

for photo in photos:
	print('Getting', photo)
	r = requests.get(photo)
	file_name = 'pics/' + names[i] + '.jpg'
	i += 1

	with open(file_name, 'wb') as fname:
		fname.write(r.content)