#! /usr/bin/env python

import markdown2
import os
import articlepage
import homepage
from util import *

METADATA = ["title", "image", "category", "content"]

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
	data = {k : v.strip().decode("utf-8").encode("ascii", "ignore")
		for k, v in zip(METADATA, parts)}

	return data


### Building website B)

def build(directory):

	# Create 'gen' directory
	if not os.path.exists(GEN_URL):
		os.makedirs(GEN_URL)

	print "Loading files..."

	# Load contents from directory
	paths = os.listdir(directory)
	paths = filter(lambda f: f.endswith(".md"), paths)
	paths = map(lambda f: os.path.join(directory, f), paths)

	results = map(inflate, paths)

	print "Generating pages..."

	# generate home page
	homepage.gen_homepage(results)

	# generate pages
	map(articlepage.gen_page, results)

	print "[ Build Succeeded ]"


if __name__ == '__main__':
	build("contents")


