function func(){
    let fd = new FormData(myform);
    let text = fd.get("answer");
    let trimed_text = $.trim(text);

    fd.set("answer", trimed_text);
    
    $.ajax({
        type: "POST",
        url: '/open-form/save_form_edition/',
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

function saveTmp(){
    let modal_textarea = document.getElementById("tmpAnswer");
    let textarea = document.getElementById("textarea");
    textarea.value = modal_textarea.value;
}

$(document).ready(function() {

    let modal = document.getElementById("myModal");

    let span = document.getElementsByClassName("close")[0];

    span.onclick = () => {
        modal.style.display = "none";
    }

    window.onclick = (event) => {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    let description = document.querySelector(".description");
    description.addEventListener('dblclick', () => {
        let modal_textarea = document.getElementById("tmpAnswer");
        let textarea = document.getElementById("textarea");
        modal_textarea.value = textarea.value;
        modal.style.display = "block";
      });

     

});