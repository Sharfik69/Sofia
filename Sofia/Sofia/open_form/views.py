from django.shortcuts import render
from django.template.context_processors import csrf

from .models import OpenForm, OpenFormAnswer
from authsystem.models import Candidate

def test(request, id):
    open_form = OpenForm.objects.get(id = id)

    info = {}
    info.update(csrf(request))
    info["description"] = open_form.description
    info["id"] = id
    return render(request, 'open_form.html', info)


def write_openForm_ans(request):
    
    
    files = request.FILES
    print(request.POST)
    #print(type(files["file"]))
    answer = request.POST.get('answer')
    answer = answer.strip() 
    form_id = request.POST.get('id')


    form_answer = OpenFormAnswer(
        text = answer,
        answer_file = files['file'],
        open_form_id = OpenForm.objects.get(id = form_id),
        candidate_id = Candidate.objects.get(username = "user")
    ) 
    form_answer.save()
    return render(request, 'answer_sent.html')