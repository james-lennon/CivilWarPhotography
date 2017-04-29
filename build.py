#! /usr/bin/env python

import markdown2
import os
import articlepage
from util import *

METADATA = ["title", "category", "content"]

# ### Generating HTML

# def gen_page(data):
	
# 	# Generate HTML
# 	html = markdown2.markdown(data["content"])
# 	pagename = get_pagename(data['title'])
# 	with open("{}/{}".format(GEN_URL, pagename), "w") as outfile:
# 		outfile.write(html)


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

	# Create 'gen' directory
	if not os.path.exists(GEN_URL):
		os.makedirs(GEN_URL)

	# Load contents from directory
	paths = os.listdir(directory)
	paths = filter(lambda f: f.endswith(".md"), paths)
	paths = map(lambda f: os.path.join(directory, f), paths)

	results = map(inflate, paths)

	# generate home page
	articlepage.gen_homepage(results)

	# generate pages
	map(articlepage.gen_page, results)

	print results


if __name__ == '__main__':
	build("contents")


