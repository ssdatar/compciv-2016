from os.path import join, basename
from glob import glob
import json

output_file = 'printout.html'

html_file = open(output_file, 'w')
html_file.write('<html><title>IBM Watson</title><body>')
html_file.write('<head><link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css"</head>')
html_file.write('<body>')
html_file.write('<div class="container">')
html_file.write('<div class="row">')
html_file.write("<h1>This is Saurabh's IBM Watson analysis</h1>")

for json_response in glob(join('responses', '*.json')):
	# print('Reading: ', json_response)
	j = json.load(open(json_response))

	img = j['images'][0]
	caption = img['image']
	html_file.write("<h2>{}</h2>".format(caption))
	html_file.write("<br>")

	filename = join('pics', caption)
	html_file.write('<img src="{}">'.format(filename))

	scores = j['images'][0]['scores']
	# print(scores)
	# break
	k = 0
	for i in scores:
		html_file.write('<p>{}) {} -- {}</p>'.format(k + 1, i['name'], i['score']))
		k += 1

html_file.write('</div></div></body>')

html_file.close()