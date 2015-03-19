var main = function() {

    
  $('.circle-btn').click(function() {
    $(this).addClass('active-circle');
    $(this).siblings().removeClass('active-circle');
    var pos = $(this).index();
    var displayContent = $('.articles').children().eq(pos);
    displayContent.addClass('active');
    displayContent.siblings().removeClass('active');
  });

  $('.circle-btn').hover(function() {
    $(this).addClass('active-circle');
    $(this).siblings().removeClass('active-circle');
    var pos = $(this).index();
    var displayContent = $('.articles').children().eq(pos);
    displayContent.addClass('active');
    displayContent.siblings().removeClass('active');
  });

};

$(document).ready(main);