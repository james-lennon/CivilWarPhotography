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

  <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700|Open+Sans:300italic,400,300,700" rel="stylesheet" type="text/css">
  <link rel="stylesheet" type="text/css" href="./semantic/dist/semantic.css">

  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.address/1.6/jquery.address.js"></script>
  <script src="./semantic/dist/semantic.js"></script>

  <link rel="stylesheet" type="text/css" href="./res/style.css">
  <script src="./res/appear.js"></script>
  <script src="./res/script.js"></script>
</head>
<body>
<img id="image-header" style="background-image: url('./img/12.jpg')">

</img>
<div class='ui text container'>
"""

def footer():
	return """
</div>
</body>
</html>
"""

def article_link(data):
  return """
<div class="ui card project-card" href="{}">
  <div class="image">
    <img src="" class="article-img" style="background-image: url('{}')">
  </div>
  <div class="content">
    <div class="header">{}</div>
    <div class="meta">
      <span class="date">{}</span>
    </div>
  </div>
</div>
""".format(get_pagename(data['title']), data['image'], data['title'], data['category'])

def grid(links):
	return """
<br>
<div>
	<h2>Articles</h2>
</div>
<hr>
<div class="ui container">
	<div class="ui center aligned grid" id="articles-grid">
		<div class="row">
			<div class="column">
				<div class="ui three stackable link cards">
					{}
				</div>
			</div>
		</div>
	</div>
</div>
""".format(links)

# background: http://civilwarsaga.com/wp-content/uploads/2011/08/Civil-War-Photographers-2.jpg

def intro():
	return """
<h1 id="title-header">
	Civil War Photography
</h1>
<hr>
<p align="left" class="indented">
	This website explores the influence of
	photography in the Civil War period, and the ways which photography was able to
	give social autonomy to the marginalized. Before photography, artists had a lot
	of influence as to how public figures were represented. The advent of the
	daguerreotype provided a more realistic and honest way to portray people and
	events. Frederick Douglass marveled at the extreme detail of the daguerreotype:
	"The dullest vision can see and comprehend at a glance the full effect of a
	point which may have taxed the wit and skill of the artist many hours, and
	days." The ability of the photograph to capture extreme detail with relative
	ease sparked radical changes for image portrayal and the ability for many to
	have a voice.
</p>"""

def authors():
	return """
<br>
<div>
	<h2>Authors</h2>
</div>
<hr>
<div class="ui stackable centered cards">
  <div class="ui left aligned card">
    <div class="content">
      <img class="left floated medium ui image" src="./img/collin.png">
      <div class="header">
        Collin Price
      </div>
      <div class="meta">
        Co-Author
      </div>
      <div class="description">
        <b>Harvard '19 - Eliot House</b>
      </div>
    </div>
  </div>
  <div class="ui left aligned card">
    <div class="content">
      <img class="left floated medium ui image" src="https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-1/c222.27.634.634/s320x320/16114690_1774815029445973_1127067855622924014_n.jpg?oh=0d5bf32e4cfe9da4699a0b2e9f18b392&oe=5989EB5C">
      <div class="header">
        James Lennon
      </div>
      <div class="meta">
        Co-Author
      </div>
      <div class="description">
        <b>Harvard '19 - Cabot House</b>
      </div>
    </div>
  </div>
</div>
<br><br>
"""

def gen_homepage(data_list):

	links = "\n".join(map(article_link, data_list))
	html  = header() + intro() + grid(links) + authors() + footer()

	# write to file
	with open("{}/index.html".format(GEN_URL), "w") as outfile:
		outfile.write(html)

