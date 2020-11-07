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
            alert("Все ок");      
        }else{
            alert("Что-то пошло не так");
        }
    });
}

