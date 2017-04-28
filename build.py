import markdown2
import os

METADATA = ["title", "category", "content"]

def gen_homepage(data_list):
	pass

def gen_page(data):
	pass

def inflate(path):

	# Load file contents
	with open(path, "r") as infile:
		contents = infile.read()

	parts = contents.split("@")[1:]

	if len(parts) < len(METADATA):
		print "ERROR: Not enough metadata in file {}".format(path)
		return {}

	# Construct metadata dict
	data = {k : v for k, v in zip(METADATA, parts)}

	# Generate HTML
	html = markdown2.markdown(data["content"])
	pagename = data['title'].lower().replace(" ","_")[:20]
	with open("./gen/{}.html".format(pagename), "w") as outfile:
		outfile.write(html)
		print html

	return data

def build(directory):

	# Load contents from directory
	paths = os.listdir(directory)
	paths = filter(lambda f: f.endswith(".md"), paths)
	paths = map(lambda f: os.path.join(directory, f), paths)

	results = map(inflate, paths)

	print results


if __name__ == '__main__':
	build("contents")