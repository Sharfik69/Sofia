var index = 0;
var len_quest = 0
var answer = []

function progressStep(shift, step){
    let prgbar = $(".progress-bar");
    let val = 0;
    if (step === 100){
        val = 100;
    }else{
        val = parseInt(prgbar.attr("aria-valuenow")) + (shift * step);
    }
    prgbar.attr({"aria-valuenow":val.toString(), "style":"width: " + val.toString() + "%"});
    prgbar.text(val.toString() + "%");
    if (val >= 100){
        prgbar.attr("class", "progress-bar bg-success");
    }else{
        prgbar.attr("class", "progress-bar");
    }
}

$(document).ready(function() {

    var mp = 150;

    var particleColors = {
        colorOptions: ["DodgerBlue", "OliveDrab", "Gold", "pink", "SlateBlue", "lightblue", "Violet", "PaleGreen", "SteelBlue", "SandyBrown", "Chocolate", "Crimson"],
        colorIndex: 0,
        colorIncrementer: 0,
        colorThreshold: 10
    }

    let elem = $('div#quest');
    // elem.hide();
    len_quest = elem.length;
    answer.length = len_quest;
    console.log(answer);
    elem.eq(index).show("fast");
    $('input#backbtn').hide();
    if(len_quest == 1){
        $('input#nextbtn').hide();
        $('input#submitData').show();
    }

    $('input#nextbtn').click(function (){
        progressStep(1, Math.round(100 / len_quest));
        let tx = '{ "ans": ["'
        //if($(".progress-bar").attr("class", "progress-bar bg-success");)
        let elem_div = elem.eq(index).children('div#ans_inp').children('input');
        if (elem_div.attr('type') !== 'text') {
            tx +=  elem_div.eq(0).is(':checked');
            for (let i = 1; i < elem_div.length; i++) {
                tx += '", "' + elem_div.eq(i).is(':checked');
            }
        }else{
            tx += elem_div.val();
        }
        tx += '"]}'

        answer[index] = tx;
        console.log(tx);
        console.log('index: ', index);
        if(index < len_quest-1){
            index++;
            elem.hide("fast", function() {
                // Animation complete.
              });
            elem.eq(index).show("fast");
            if(index > len_quest-2) {
                $('input#nextbtn').hide();
                $('input#submitData').show();
            }
            if (!$('input#backbtn').is('visible')){
                $('input#backbtn').show();
            }
        }else{
            console.log('Вы завершили тест');
        }
    });
    $('input#backbtn').click(function (){
        progressStep(-1, Math.round(100 / len_quest))
        //console.log('index: ', index);
        if(index > 0){
            index--;
            elem.hide("fast");
            elem.eq(index).show("fast");
            if (!$('input#nextbtn').is('visible')){
                $('input#nextbtn').show();
                $('input#submitData').hide();
            }
            if(index < 1){
                $('input#backbtn').hide();
            }
        }else{

        }
    });
});

function submitData(id_test, id_vacancy, order){
    let elem = $('div#quest');
    let tx = '{ "ans": ["'
    //if($(".progress-bar").attr("class", "progress-bar bg-success");)
    let elem_div = elem.eq(index).children('div#ans_inp').children('input');
    if (elem_div.attr('type') !== 'text') {
        tx +=  elem_div.eq(0).is(':checked');
        for (let i = 1; i < elem_div.length; i++) {
            tx += '", "' + elem_div.eq(i).is(':checked');
        }
    }else{
        tx += elem_div.val();
    }
    tx += '"]}'

    answer[index] = tx;
    progressStep(1,100);
    fd = new FormData();
    fd.append('candidate', 0);
    fd.append('id_test', id_test);
    fd.append('vacancy', id_vacancy);
    fd.append('len', answer.length);
    for(let i=0; i<answer.length;i++){
        fd.append('ans'+i, answer[i]);
    }
    fd.append('order', order);

    console.log(id_test, id_vacancy, order);
    $.ajax({
      type: "POST",
      url: "/q_test/cd_post/" + id_test + "",
      data: fd,
      dataType:'blob',
      contentType: false,
      processData: false,
    }).done(function (result){
        console.log(result)
        alert('Вы прошли тестю Ваш результат:' + result['ans']);
    });
    $('#startConfetti').trigger('click');
}
