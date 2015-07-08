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

  $('.circle-btn-play').click(function() {
    $(this).removeClass('active-circle');
    var nextActiveIndex = getRandomInt(0, $(this).siblings().length);
    var nextActive = $(this).siblings().eq(nextActiveIndex);
    nextActive.addClass('active');
  });

  $('.circle-btn-play').hover(function() {
    $(this).removeClass('active-circle');
    var nextActiveIndex = getRandomInt(0, $(this).siblings().length);
    console.log(nextActiveIndex)
    var nextActive = $(this).siblings().eq(nextActiveIndex);
    nextActive.addClass('active');
  });

};

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

$(document).ready(main);