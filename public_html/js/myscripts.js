function goToByScroll(id, allowedMargin, up_limit) 
{ 
    var current = $(document).scrollTop(); 
    var destination = $("#"+id).offset().top;
    var allowedMin = destination - allowedMargin;
    var allowedMax = destination + allowedMargin;

	if(destination >= up_limit)
	{
		destination -= up_limit;
	}

    if(current < allowedMin || current > allowedMax)
	{
        $('html,body').animate({scrollTop: destination},'slow');
    }
}


$(document).ready(function() 
{	
	$('#jumpdown').hover(function() {
		jumpdown = false;
	});
	
	$('#jumpmiddle').hover(function() {
		jumpmiddle = false;
	});
	
	jumpdown_link();
});

var jumpdown = true;
function jumpdown_link()
{
	$('#jumpdown').animate({opacity: 0}, 1000).animate({opacity:1}, 1000, function(){
		if(jumpdown)
		{
			jumpdown_link();
		}
	});
}

var jumpmiddle = true;
function jumpmiddle_link()
{
	$('#jumpmiddle').animate({opacity: 0}, 1000).animate({opacity:1}, 1000, function(){
		if(jumpmiddle)
		{
			jumpmiddle_link();
		}
	});
}