var interviewCntTags = [], interviewCnt = 0;

function interviewAddTags(question, text = "") {
    var divTags = document.getElementById('tags[' + question + ']');
    var name = 'tags[' + question + ']';
    divTags.innerHTML += "<input name='" + name + "' placeholder = 'Введите быстрый ответ' value='" + text + "'>";
    interviewCntTags[question]++;

}

function addQuestion(name = "", tags = []) {
    interviewCntTags.push(0);
    form_ = document.forms.interviewQuestions;

    form_.innerHTML += "<input name='name[" + interviewCnt + "]' placeholder = 'Введите вопрос' class='center-input'><br>";

    form_.innerHTML += "<div id='tags[" + interviewCnt + "]'class='quick_answer'></div>";
    for (var i = 0; i < tags.length; i++) {
        interviewAddTags(interviewCnt, tags[i]);
    }
    form_.innerHTML += "<input name='addTags[" + interviewCnt + "]' type='button' onclick='interviewAddTags(" + interviewCnt + ")' \
                    value='Добавить быстрый ответ' class='center-input'><br><br>";

    interviewCnt++;
}

document.addEventListener("DOMContentLoaded", () => {
    var btnAddQuestion = document.getElementById("interview-add_question");
    btnAddQuestion.onclick = () => {
        addQuestion();
    }
    var btnSaveForm = document.getElementById('interview-save_question');
    btnSaveForm.onclick = () => {
        var fd = new FormData(interviewQuestions);

        
        $.ajax({
            type: "POST",
            url: 'interview/new/ajax/',
            data: fd,
            contentType: false,
            processData: false
        }).done(function (result) {
            console.log(result)
        });
    }
})

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