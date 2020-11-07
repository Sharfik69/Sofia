function func(){
    let fd = new FormData(myform);

    $.ajax({
        type: "POST",
        url: '/open-form/write_mark_to_tast/',
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

