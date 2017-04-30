
$(document).ready(function() {

	$(".project-card").click(function() {
    	page_url        = $(this).attr("href");
    	window.location = page_url
    });

});

