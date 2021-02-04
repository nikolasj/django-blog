$.ajaxSetup({
    headers: { "X-CSRFToken": getCookie("csrftoken") }
});

$(function() {
    console.log("abatar js");
    $(document).on("submit", "#id_ajax_upload_form" , avatar_change);
    $(".file-upload").on('change', avatar_change);

});


function input_image(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.avatar').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

function avatar_change(e){
    console.log("abatar change");
 var input = document.getElementById('id_avatar');
 console.log(input);
 if ((input.files && input.files[0]) == false) {
      console.log("exit");
  return;
 }
  console.log("image");
 var href = $(this).data('href');
  console.log(href);
 var data = new FormData();
    data.append('image', input.files[0]);
    fetch(href, {
        method: 'POST',
        headers: {
//            'Authorization': Token ${userToken},
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: data
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
  input_image(input)
  input.value= null
    })
    .catch((error) => {
        input_image(input)
  input.value= null
    });

}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}