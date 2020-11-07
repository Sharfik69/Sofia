var divCollection = []
var countCol = 0

function addRow(elem){
    console.log(elem.id);
    let chld = $('#btnAns' + elem.id);
    let ln = chld.children().length;
    chld.append('<input type="text" id="ans' + ln + '" name="a' + elem.id + '"/>'+
        '<div><input type="checkbox" name="ansl' + ln + '">'+
        '<label for="ansl' + ln + '">Правильный ответ?</label></div>'+
        '')
}

function delColumn(elem){
    console.log(elem.id);
    let index = parseInt(elem.id.toString().slice(2, elem.id.toString().length));
    console.log(index);
    $('.collection > div#quest').eq(index).remove();
    countCol -= 1;
    if(countCol === 0){
        $('input#savebtn').hide();
    }
    for (let i=index;i<$('.collection > div#quest').length;i++){
        let parent = $('.collection > div#quest').eq(i);

        parent.children('textarea').attr('id', 'quest' + (i).toString());
        parent.children('input#selectedFile' + (i+1).toString()).attr('id', 'selectedFile' + (i).toString());
        parent.children('input#selectedFileBtn' + (i+1).toString()).attr('onclick', 'document.getElementById(\'selectedFile' + (i).toString() + '\').click();');
        parent.children('div').attr('id', 'btnAns' + (i).toString());
        console.log(parent.children('div > input').attr('name'));
        //parent.children('div > input').attr('name', 'a' + (i).toString());
        parent.children('div').children('input[type="text"]').attr('name', 'a' + (i).toString());;
        parent.children('input#' + (i+1).toString()).attr('id', '' + (i).toString());
        parent.children('input#dc' + (i+1).toString()).attr('id', 'dc' + (i).toString());
    }

}

function addColumn(){
    if(!$('input#savebtn').is(":visible")){
        $('input#savebtn').show();
    }
    $(".collection").append('<div id="quest" style="margin:15px" class="col-md-2">'+
        '<hr><h2>Вопрос</h2>'+
        '<input type="file" id="selectedFile' + countCol + '" style="display: none;">'+
        '<input type="button" id="selectedFileBtn' + countCol + '" value="Загрузить картинку..." onclick="document.getElementById(\'selectedFile' + countCol + '\').click();" >'+
        '<textarea id="quest' + countCol + '"></textarea>'+
        '<br><h2>Ответ</h2>'+
        '<div id="btnAns' + countCol + '">'+
        '<input type="text" class="ansinput" id="ans0" name="a' + countCol + '"/>'+
        '<div><input type="checkbox" name="ansl0">'+
        '<label for="ansl0">Правильный ответ?</label></div>'+
        '</div><input id="' + countCol + '" type="button" value="Добавить ответ" onclick="addRow(this)"><br>'+
        '<input id="dc' + countCol + '" type="button" value="Удалить вопрос" id="DeleteCol" onclick=delColumn(this)><br></div>');
    countCol++;
}

function submitData(id_test){
    //console.log($('#quest').children('#quest0').val());

    let ln_qst = $('.collection > div#quest').length;
    console.log('len #quest', ln_qst);

    fd = new FormData()
    fd.append('len', ln_qst);

    for(let i=0;i<ln_qst;i++){
        let ln = $('#quest > #btnAns' + i).children('div').length;
        console.log(ln);
        let chld = $('#quest > #btnAns' + i + ' > input');
        let j_ans = '{ "ans": ["' + chld.eq(0).val();
        for (let i=1;i<ln;i++){
            j_ans += '", "' + chld.eq(i).val() + ''
        }
        j_ans += '"]}';
        console.log(j_ans);
        chld = $('#quest > #btnAns' + i + ' > div > input');

        let count_true = 0;
        let quest_type = 1;
        let j_is_tr = '';
        if (ln > 1) {
            j_is_tr = '{ "ans": ["' + chld.eq(0).is(":checked");
            for (let j = 1; j < ln; j++) {
                j_is_tr += '", "' + chld.eq(j).is(":checked") + ''
            }
        }else{
            j_is_tr = '{ "ans": ["' + $('#quest > #btnAns' + i + ' > input').val();
        }
        for (let j = 0; j < ln; j++) {
            if (chld.eq(j).is(":checked")) {
                count_true++;
            }
        }
        j_is_tr += '"]}';
        console.log(count_true, quest_type);
        if(count_true > 1){
            quest_type = 0
        }else if(ln === 1){
            quest_type = 2
        }
        console.log(count_true, quest_type);
        console.log(j_is_tr);
        let name = $('div#quest').children('textarea#quest'+i.toString()).val();
        console.log(name, ' - ', '#quest'+i);
        let img = document.getElementById('selectedFile'+parseInt(i));
        //console.log(img.files[0]);
        fd.append("quest"+i+".id_test", id_test);
        fd.append("quest"+i+".quest", name);
        fd.append("quest"+i+".type", quest_type);
        fd.append("quest"+i+".jsn_ans", j_ans);
        fd.append("quest"+i+".jsn_is_true", j_is_tr);
        fd.append("quest"+i+".img", img.files[0]);

    }
    $.ajax({
      type: "POST",
      url: "/q_test/cp_post/" + id_test + "",
      data: fd,
      contentType: false,
      processData: false,
    }).done(function (result){

    });
}