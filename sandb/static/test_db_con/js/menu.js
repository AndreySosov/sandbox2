  $('.menu-btn').on('click', function(e) {
    e.preventDefault();
    $('.menu').toggleClass('menu_active');
    $(this).toggleClass('menu-btn_active');
    $('.menu-nav').toggleClass('menu-nav_active');
    // $('.content').toggleClass('content_active');
  })