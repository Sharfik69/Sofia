var divCollection = []
var countCol = 0

function cc(elem){
    console.log(elem.id);
    let ln = $('#btnAns' + elem.id).children().length;
    $('#btnAns' + elem.id).append('<input type="text" id="ans' + ln + '" name="a' + elem.id + '"/>')
}

function addColumn(){
    $(".collection").append('<div id="quest">'+
        '<h2>Вопрос</h2>'+
        '<textarea id="quest_' + countCol + '"></textarea>'+
        '<br><h2>Ответ</h2>'+
        '<div id="btnAns' + countCol + '">'+
        '<input type="text" id="ans0" name="a' + countCol + '"/>'+
        '</div><input id="' + countCol + '" type="button" value="+" onclick="cc(this)"></div>');
    countCol++;
}

function submitData(id_test){
    console.log(id_test);

    let data = new FormData();
    data.append("id_test", id_test);
    data.append("quest", id_test);
    data.append("id_test", id_test)


    $.ajax({
      type: "POST",
      url: "cp_post/" + id_test,
      data: data,
      success: success,
      dataType: dataType
    });
}