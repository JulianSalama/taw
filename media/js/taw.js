
taw = {}

// namespace taw.menues
taw.menues = {}

taw.menues.show_first = function() {
  $('ul#smnu').each(function() {
    $(this).find('li').each(function(i,e){
      if(i > 2) {
	$(this).hide();
      }
    }); 
  });
}

taw.menues.onHover = function() {
  $('ul#smnu').each(function() {
    $(this).hover(function() {
      $(this).find('li').show();
    }, function() {
      taw.menues.show_first();
    });
  });
}

taw.menues.initMenues = function() {
  taw.menues.show_first();
  taw.menues.onHover();
}

taw.slides = {}
var slide = 0;
taw.slides.init = function(user_slide) {
  slide = user_slide;
  $('div.slide').each(function(e, i) {
    $(this).wrap("<div class=\"textbody\"></div>")
    if(e > slide) {
      $(this).hide();
    }
    else if (e < slide) {
      $(this).find('div.next').hide();
    }
    else {
      $(this).parent().addClass("textlast");
    }
  });
}

taw.slides.show_next_slide = function() {
  ajaxsetup();
  $.ajax({
    type: "POST",
    url: "set_user_slide/",
  });
  $($('div.slide')[slide]).parent().removeClass('textlast');
  $($('div.slide')[++slide]).show().parent().addClass('textlast');
}


taw.form = {}

taw.form.init = function(user_posts) {
  $.each(user_posts, function(index, value){
    var p = $($('form.inactive')[value.split("_")[1]])
    p.find('input').val(p.find('.answer').first().text());
    p.find('input').addClass('valuetext').attr('disabled', true);
  });

  $('form.inactive').each(function(i, e) {
    $(this).submit(function(e){
      e.preventDefault();
    });
    var div_answer = $(this).find('.answer');
    var answer = $(this).find('.answer').text();
    var post_name = $.trim($('span.each_title').text()) + '_' + i;

    $(this).find('input').width(answer.length * 8 + 30);
    //text in the middle and padding on the input
    div_answer.detach();    
    $(this).keyup(function(e){
      if(e.keyCode == 13){
	var post_value = $(this).find('input').val();
	ajaxsetup();
	$.ajax({
	  type: "POST",
	  url: "set_user_post/",
	  data: { name: post_name, value: post_value  },
	  success: function(data) { }
	});

      if(answer == $(this).find('input').val() && !$(this).hasClass('answered')){
	$(this).find('input').addClass('valuetext');
	$(this).find('input').attr('disabled', true);
	if($(this).parent().hasClass('triger')) {
	  taw.slides.show_next_slide();
	}
	$(this).addClass("answered");
      }
      else {
	//$(this).show_hint();
      }
    }
    });
  });
}

taw.link = {}

taw.link.init = function() {
  $('div.link').click(function(e) {
    if($(this).children().first().hasClass('window')) {
      window.open($(this).children().attr('id'));
    }
    if($(this).parent().hasClass('triger') && !$(this).hasClass('answered')){
      taw.slides.show_next_slide();      
    }
    if($(this).hasClass('next')){
      $(this).hide();
    }
    $(this).addClass("answered");
  });
}

taw.next = {}

taw.next.init = function() {
  $('div.next').click(function(e){
    $(this).hide();
    taw.slides.show_next_slide();
  });
}

ajaxsetup = function() {
$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

}