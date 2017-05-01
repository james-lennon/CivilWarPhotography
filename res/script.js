
$(document).ready(function() {

	$(".project-card").click(function() {
    	page_url        = $(this).attr("href");
    	window.location = page_url
    });


	/* Homepage animations */

	$.each($(".project-card"), function(key, value) {
		$(value).hide();
		$(value).delay(key * 100).fadeIn();
	});

	/* Article animations */

	$("h1").hide();
    $("p").hide();

    $("h1").transition("fade up", '500ms');
    $("p").delay(500).transition('fade up', '500ms');



});

