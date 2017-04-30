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

def article_link(data):
  return """
<div class="ui card project-card" href="{}">
  <div class="image">
    <img src="{}">
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
	return """<div class="ui container">

	<div class="ui center aligned grid">
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

def gen_homepage(data_list):

	def link(data):
		return "[{}]({})\n".format(data['title'], get_pagename(data['title']))

	links = "\n".join(map(article_link, data_list))
	html  = header() + grid(links) +  footer()

	# write to file
	with open("{}/index.html".format(GEN_URL), "w") as outfile:
		outfile.write(html)

# Homepage HTML

"""
<div class="ui top fixed secondary blurred menu" id="nav-menu">
	<div class="contact-open link item">
		<div class="ui contact-open mini image">
			<img class="ui mini circular image" src="{}">
		</div>
	</div>
	<div class="contact-open link item">
		<h3>Civil War Photography</h3>
	</div>
</div>


<div class="ui basic container segment stackable grid" id="title-bar">
	<div class="middle aligned row">
		<a class="two wide contact-open column" href="#">
			<img class="ui small circular image" src="/res/img/homepage/profile.jpg">
		</a>
		<div class="fourteen wide column">
			<a class="contact-open" href="#">
				<h1 class="ui left floated huge header">
					James Lennon
					<div class="sub header"><em>Sophomore at Harvard studying computer science and economics</em></div>
				</h1>
			</a>
		</div>
		<div class="five wide bottom aligned column">
			<!-- <div class="ui bottom right floated secondary stackable menu">
				<a class="item">Projects</a>
				<a class="item">About</a>
				<a class="contact-open item">Contact</a>
			</div> -->
		</div>
	</div>
	<div class="ui divider"></div>

</div>

<div class="ui container">

	<div class="ui center aligned grid">
		<div class="row">
			<div class="column">
				<div class="ui three stackable link cards">
					<? foreach ($projects as $project) {

						$this->load->view('components/project_preview',['project'=>$project]);

						print("<br>");
					}
					?>
				</div>
			</div>
		</div>

	</div>
</div>

<div class="ui basic long scrolling modal" id="project-modal">

	<div class="content">
		<div class="ui labeled icon button" id="modal-back">
			<i class="left arrow icon"></i>
			Back
		</div>
		<br>
		<br>
		<div id="project-info"></div>
	</div>
</div>

<div class="ui basic modal" id="image-modal">

	<div class="content">
		<div class="ui labeled icon button" id="image-modal-back">
			<i class="left arrow icon"></i>
			Back
		</div>
		<br>
		<br>
		<div class="ui huge image">
			<img src="" id="image-modal-img"/>
		</div>
	</div>
</div>

<div class="ui basic modal" id="contact-modal">

	<div class="content">
		<div class="ui labeled icon button" id="contact-modal-back">
			<i class="left arrow icon"></i>
			Back
		</div>
		<br>
		<br>
		<div class="ui basic container segment stackable grid" id="title-bar">
			<div class="middle aligned row">
				<div class="four wide column">
					<img class="ui small circular image" src="/res/img/homepage/profile.jpg">
				</div>
				<div class="twelve wide column">
					<div class="ui grid">
						<div class="row">
							<h1 class="ui left floated huge header">
								Contact:
							</h1>
						</div>
						<div class="row">
							<h5>Email: <a href="mailto:jameslennon321@gmail.com" target="_top">jameslennon321@gmail.com</a></h5>
						</div>
						<div class="row">
							<div class="ui buttons">
								<a class="ui blue icon button" href="https://www.facebook.com/james.lennon.3511" target="_blank" >
									<i class="facebook icon"></i>
								</a>
								<a class="ui cyan icon button" href="https://www.linkedin.com/in/james-lennon-30421078?trk=hp-identity-name" target="_blank">
									<i class="linkedin icon"></i>
								</a>
								<a class="ui black icon button" href="https://github.com/jameslennon321" target="_blank">
									<i class="github icon"></i>
								</a>
								<a class="ui yellow icon button" href="mailto:jameslennon321@gmail.com" target="_top">
									<i class="mail icon"></i>
								</a>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

<script type="text/javascript" src="<?= base_url() ?>res/js/portfolio.js"></script>

<? $this->load->view("templates/footer"); ?>
"""

