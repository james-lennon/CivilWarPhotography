$(document).ready(function() {

	$(".project-card").click(function() {
    	page_url        = $(this).attr("href");
    	window.location = page_url
    });


	/* Homepage animations */

	var viewed = false;

	$("#articles-grid").appear();

	$.each($(".project-card"), function(key, value) {
		$(value).hide();
	});

	$(document.body).on('appear', function(){
		if (!viewed) {
			viewed = true;
			$.each($(".project-card"), function(key, value) {
				$(value).delay(key * 100 + 500).fadeIn();
			});
		}
	});

	

	/* Article animations */

	$("h1").hide();
    $("p").hide();

    $("h1").transition("fade up", '500ms');
    $("p").delay(500).transition('fade up', '500ms');

    if ($(window).width() > 1100) {
    	$("#home-button").addClass("stuck");
    }


});

