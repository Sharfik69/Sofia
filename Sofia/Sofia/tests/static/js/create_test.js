var divCollection = []
var countCol = 0

$(document).ready(function() {
// CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

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

function cc(elem){
    console.log(elem.id);
    let chld = $('#btnAns' + elem.id);
    let ln = chld.children().length;
    chld.append('<input type="text" id="ans' + ln + '" name="a' + elem.id + '"/>'+
        '<div><input type="checkbox" name="ans' + ln + '">'+
        '<label for="ans' + ln + '">Правильный ответ?</label></div>'+
        '')
}

function addColumn(){
    $(".collection").append('<div id="quest">'+
        '<h2>Вопрос</h2>'+
        '<textarea id="quest' + countCol + '"></textarea>'+
        '<br><h2>Ответ</h2>'+
        '<div id="btnAns' + countCol + '">'+
        '<input type="text" id="ans0" name="a' + countCol + '"/>'+
        '<div><input type="checkbox" name="ans0">'+
        '<label for="ans0">Правильный ответ?</label></div>'+
        '</div><input id="' + countCol + '" type="button" value="+" onclick="cc(this)"></div><br>');
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
        let j_is_tr = '{ "ans": ["' + chld.eq(0).is(":checked");
        for (let j=1;j<ln;j++){
            j_is_tr += '", "' + chld.eq(j).is(":checked") + ''
        }
        j_is_tr += '"]}';
        console.log(j_is_tr);
        let name = $('div#quest').children('textarea#quest'+i.toString()).val();
        console.log(name, ' - ', '#quest'+i);
        fd.append("quest"+i+".id_test", id_test);
        fd.append("quest"+i+".quest", name);
        fd.append("quest"+i+".type", 0);
        fd.append("quest"+i+".jsn_ans", j_ans);
        fd.append("quest"+i+".jsn_is_true", j_is_tr);
    }

    $.ajax({
      type: "POST",
      url: "/q_test/cp_post/" + id_test + "",
      data: fd,
      dataType:'blob',
      contentType: false,
      processData: false,
    }).done(function (result){

    });
}