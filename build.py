#! env python

import markdown2
import os

METADATA = ["title", "category", "content"]

def get_pagename(title):
	return title.lower().replace(" ","_")[:20]


### Generating HTML

def gen_homepage(data_list):
	pass

def gen_page(data):
	
	# Generate HTML
	html = markdown2.markdown(data["content"])
	pagename = get_pagename(data['title'])
	with open("./gen/{}.html".format(pagename), "w") as outfile:
		outfile.write(html)


### Loading from data files

def inflate(path):

	# Load file contents
	with open(path, "r") as infile:
		contents = infile.read()

	parts = contents.split("@")[1:]

	if len(parts) < len(METADATA):
		print "ERROR: Not enough metadata in file {}".format(path)
		return {}

	# Construct metadata dict
	data = {k : v.strip() for k, v in zip(METADATA, parts)}

	return data


### Building website B)

def build(directory):

	# Load contents from directory
	paths = os.listdir(directory)
	paths = filter(lambda f: f.endswith(".md"), paths)
	paths = map(lambda f: os.path.join(directory, f), paths)

	results = map(inflate, paths)

	# generate home page
	gen_homepage(results)

	# generate pages
	map(gen_page, results)

	print results


if __name__ == '__main__':
	build("contents")


