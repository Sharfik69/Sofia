function func(){
    let form  = document.getElementById("openFormAns");
    let id = form.elements.id.value;
    let answer = form.elements.answer.value;
    let file = form.elements.file.files[0];
    
    console.log(id);
    console.log(answer);
    console.log(file);

    var fd = new FormData(myform);
    // fd.append("id", id);
    // fd.append("answer", answer);
    // fd.append("file", file);
    // fd.append('q', file);
    fd.append('image', file);


    $.ajax({
        type: "POST",
        url: '/open-form/write_openForm_ans/',
        data: fd,
        contentType: false,
        // contentType: "multipart/form-data",
        processData: false
    }).done(function (result) {
        console.log(result)
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
        // console.log(file);
        // image = new Image();
        // image.src = URL.createObjectURL(file);
        // input.value = image;


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