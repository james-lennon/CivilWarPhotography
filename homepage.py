from util import *
import markdown2

def header():
	return """
<html>
<head>
  <!-- Standard Meta -->
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

  <!-- Site Properities -->
  <title>Civil War Photography</title>

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
"""

def footer():
	return """
</div>
</body>
</html>
"""


def gen_homepage(data_list):

	def link(data):
		return "[{}]({})\n".format(data['title'], get_pagename(data['title']))

	links = "\n".join(map(link, data_list))
	html  = header() + markdown2.markdown(links) +  footer()

	# write to file
	with open("{}/index.html".format(GEN_URL), "w") as outfile:
		outfile.write(html)



