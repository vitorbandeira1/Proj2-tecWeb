// Fonte de referencia: https://www.geeksforgeeks.org/django-form-submission-without-page-reload/

$(document).on('submit', '#formOutput',function(e){
  e.preventDefault(); //prevent the page of getting refreshed
  
  $.ajax({
    type:'POST',
    url:'',
    data:
    {
        id_api:$("#id_api").val(),
        title:$("#title").val(),
        rating:$("#rating").val(),
        link:$("#link").val(),
        img:$("#img").val(),
        type_of:$("#type_of").val(),
        taskAdd:$("#taskAdd").val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    },
    success:function(){
          alert('Saved');
            }
    })
});

$(document).on('submit', '#form-imdb',function(e){
  e.preventDefault(); //prevent the page of getting refreshed
});
