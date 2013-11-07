var csrftoken = $.cookie('csrftoken');
var boxLoad = function(){
	var url = $(this).attr('href');
	var title= $(this).data('title');
	$.get(url, {}, function(html){
		$('#modalbox').html(html).attr('title', title).dialog({ modal: true});
	});
	
	return false;
} 

var inicio =function(){
	$("form").jqTransform();
}
var menuHidden=function(){
	if ($(this).text()=='+') {
		$(this).text('-');
		$(this).parent().next('aside .menu, aside .menu-usuarios').slideDown('slow');
	}else{
		$(this).text('+');
		$(this).parent().next('aside .menu, aside .menu-usuarios').slideUp('slow');
	}

}
var redireccion = function(){
	var url = $(this).data('url');
	window.location=url;
}
var validDelete=function(){
	var validate=confirm("Esta seguro de borrar este registro, si continua esta acción no se podra revocar");
	return validate	
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$('a.toggleLink').on('click',menuHidden);
$('.boxLoad').on('click', boxLoad);
$('.redirect').on('click',redireccion);
$('.delete').on('click', validDelete)
$(document).on('ready', inicio)

