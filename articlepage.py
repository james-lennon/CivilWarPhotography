import markdown2
from util import *

def header(data=None, title=None):
	return """
<html>
<head>
  <!-- Standard Meta -->
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

  <!-- Site Properities -->
  <title>{}</title>

  <link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700|Open+Sans:300italic,400,300,700" rel="stylesheet" type="text/css">
  <link rel="stylesheet" type="text/css" href="../semantic/dist/semantic.css">

  <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.js"></script>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery.address/1.6/jquery.address.js"></script>
  <script src="../semantic/dist/semantic.js"></script>

  <link rel="stylesheet" type="text/css" href="../res/style.css">
  <script src="../res/script.js"></script>
</head>
<body>
<div class='ui text container'>
""".format(title if title else data['title'])

def footer(data=None):
	return """
</div>
</body>
</html>
"""


def gen_homepage(data_list):

	def link(data):
		return "[{}]({})\n".format(data['title'], get_pagename(data['title']))

	links = "\n".join(map(link, data_list))
	html  = header(title="Home") + markdown2.markdown(links) +  footer()

	# write to file
	with open("{}/index.html".format(GEN_URL), "w") as outfile:
		outfile.write(html)


def gen_page(data):
	
	# Generate HTML
	article  = markdown2.markdown(data["content"])
	pagename = get_pagename(data['title'])
	html     = header(data) + article + footer(data)

	with open("{}/{}".format(GEN_URL, pagename), "w") as outfile:
		outfile.write(html)

