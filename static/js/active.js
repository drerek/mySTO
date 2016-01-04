$(function () {
  $('#navbar ul li a').each(function () {
    if (window.location.href == this.href) {
      $(this).closest('li').addClass('active');
    }
  });
});