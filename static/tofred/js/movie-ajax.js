$(document).ready(function() {
	

	$('#likes').click(function(){
	        var movid;
	        movid = $(this).attr("data-movid");
	         $.get('/movie/like_movie/', {movie_id: movid}, function(data){
	                   $('#like_count').html(data);
	                   $('#likes').hide();
	               });
	    });


    	$('#suggestion').keyup(function(){
		var query;
		query = $(this).val();
		$.get('/movie/suggest_movie/', {suggestion: query}, function(data){
                 $('#movs').html(data);
		});
	});

    
	$('.movie-add').click(function(){
	    var movid = $(this).attr("data-movid");
        var url = $(this).attr("data-url");
        var title = $(this).attr("data-title");
        var me = $(this)
	    $.get('/movie/auto_add_page/', {movie_id: movid, url: url, title: title}, function(data){
	                   $('#pages').html(data);
	                   me.hide();
	               });
	    });

});
