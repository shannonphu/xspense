$(document).ready(function() {
	$('.budget:nth-child(4n)').each(function(index) {
	    $(this).prevAll('.budget').andSelf().wrapAll('<div class="row"/>');
	});
	$('#budget-expense > .budget').wrapAll('<div class="row" />');

	// CHANGE NAV BAR COLOR ON SCROLL
	function checkScroll(){
	    var startY = $('.navbar').height() * 2; //The point where the navbar changes in px

	    if($(window).scrollTop() > startY){
	        $('.navbar').addClass("scrolled");
	    }else{
	        $('.navbar').removeClass("scrolled");
	    }
	}

	if($('.navbar').length > 0){
	    $(window).on("scroll load resize", function(){
	        checkScroll();
	    });
	}

});