
$(document).ready(function() {

	$(".project-card").click(function() {
    	page_url        = $(this).attr("href");
    	window.location = page_url
    });

	$("h1").hide();
    $("p").hide();

    $("h1").transition("fade up", '500ms');
    $("p").delay(500).transition('fade up', '500ms');

});

