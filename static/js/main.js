
var redireccion = function(){
	var url = $(this).data('url');
	window.location=url;
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
var validDelete=function(){
	var validate=confirm("Esta seguro de borrar este registro, si continua esta acción no se podra revocar");
	return validate	
}
$('a.toggleLink').on('click',menuHidden);
$('.redirect').on('click',redireccion);
$('.delete').on('click', validDelete)
$(document).on('ready', inicio)