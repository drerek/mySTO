$(function () {
  $('#navbar ul li a').each(function () {
    if (window.location.href == this.href) {
      $(this).closest('li').addClass('active');
    }
	else{
		if(window.location.href == "http://127.0.0.1:8000/table/get/1" || window.location.href == "http://127.0.0.1:8000/table/get/2"|| window.location.href == "http://127.0.0.1:8000/table/get/3"|| window.location.href == "http://127.0.0.1:8000/table/get/4") {
			$('#price').addClass('active');
		}
	}
  });
});