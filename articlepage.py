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
  <link rel="stylesheet" type="text/css" href="./semantic/dist/semantic.min.css">

  <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.js"></script>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery.address/1.6/jquery.address.js"></script>
  <script src="./semantic/dist/semantic.min.js"></script>

  <link rel="stylesheet" type="text/css" href="./res/style.css">
  <script src="./res/script.js"></script>
</head>
<body>
<a href="index.html">
<div class="left aligned">
  <button id="home-button" class="ui labeled icon button">
    <i class="home icon"></i>
    Home
  </button>
</div>
</a>
<div class="ui text container">
<div class='ui center aligned grid'>
<div class='row'>
<div class='left aligned column'>
""".format(title if title else data['title'])

def footer(data=None):
	return """
</div>
</div>
</div>
</div>
</body>
</html>
"""


def gen_page(data):
	
	# Generate HTML
	article  = markdown2.markdown(data["content"])
	pagename = get_pagename(data['title'])
	html     = header(data) + article + footer(data)

	with open("{}/{}".format(GEN_URL, pagename), "w") as outfile:
		outfile.write(html)

