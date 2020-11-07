function func(){
    let fd = new FormData(myform);
    let text = fd.get("answer");
    let trimed_text = $.trim(text);
    if (trimed_text.length == 0){
        alert('Вы ничего не ввели в поле для ответа');
        return;
    }

    fd.set("answer", trimed_text);
    
    $.ajax({
        type: "POST",
        url: '/open-form/write_openForm_ans/',
        data: fd,
        contentType: false,
        processData: false
    }).done(function (result) {
        if (result["status"] == "Ok"){
            $(".status").append("<div>Ваш ответ успешно отправлен</div>");       
        }else{
            $(".status").append("<div>Что-то пошло не так</div>");
        }
    });
}

$(document).ready(function() {
    let input = document.getElementById("file");
    input.onchange = () =>{
        file = input.files[0];
        if (file.size > 5 * 1024 * 1024){
            alert("Ваш файл слишком большой");
            input.value = '';
            return;
        }
    };
  
    let form  = document.getElementById("openFormAns");
    var csrftoken = form.elements.csrfmiddlewaretoken.value;

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
    
});