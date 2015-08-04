$(document).ready(function() {
	$('.budget:nth-child(4n)').each(function(index) {
	    $(this).prevAll('.budget').andSelf().wrapAll('<div class="row" style="margin-bottom: 1em"/>');
	});
	$('#budget-expense > .budget').wrapAll('<div class="row" />');
});