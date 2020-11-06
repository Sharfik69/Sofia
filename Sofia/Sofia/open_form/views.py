from django.shortcuts import render
from django.template.context_processors import csrf
from django.http import JsonResponse

from .models import OpenForm, OpenFormAnswer
from authsystem.models import Candidate

def show_open_form(request, id):
    open_form = OpenForm.objects.get(id = id)
    info = {}
    info.update(csrf(request))
    info["description"] = open_form.description
    info["id"] = id
    return render(request, 'open_form.html', info)


def write_openForm_ans(request):
    try:
        files = request.FILES
        answer = request.POST.get('answer')
        form_id = request.POST.get('id')
        
        form_answer = OpenFormAnswer(
            text = answer,
            open_form_id = OpenForm.objects.get(id = form_id),
            candidate_id = Candidate.objects.get(username = "user")
        )
       
        #проверка на пустоту
        if len(files) == 0: 
            form_answer.save()
        else:
            file_ = files['file']
            form_answer.answer_file = file_
            form_answer.save()

        return JsonResponse({
            'status': 'Ok'
        })
    except:
        return JsonResponse({
            'status': 'Fail'
        })
    # return render(request, 'answer_sent.html')