from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from authsystem.models import Candidate, Company
from vacancy.models import Vacancy
from tests.models import Test, TestQuestion
from inform_page.models import Text
from interview.models import Interview
from open_form.models import OpenForm
import json 

def create_stage(request, id_vac):
    d = {}
    if not request.user.is_anonymous:
        d['username'] = auth.get_user(request).username
        check = False
        try:
            d['status'] = Candidate.objects.get(user=request.user.id)
            check = True
            d['status'] = 1
        except Exception:
            d['status'] = 0
        if not check:
            try:
                d['status'] = Company.objects.get(user=request.user.id)
                check = True
                d['status'] = 2
            except Exception:
                d['status'] = 0
    if d['status'] == 2:
        try:
            x = Vacancy.objects.get(pk=id_vac)
            d['pk_id'] = id_vac
        except Exception:
            x = None
        if x == None:
            d['status'] = 0
        else:
            d['vacansy'] = x
    try:  
        test_a = Test.objects.filter(vacancy=x)
    except Exception:
        test_a = None
        pass
    try:
        text_a = Text.objects.filter(vacancy_id=x)
    except Exception:
        text_a = None
        pass
    try:
        interview_a = Interview.objects.filter(vacancies=x)
    except Exception:
        interview_a = None
        pass
    try:
        open_form_a = OpenForm.objects.filter(vacancy_id=x)
    except Exception:
        open_form_a = None
        pass
    d['Tests'] = test_a
    d['Texts'] = text_a
    d['Interviewes'] = interview_a
    d['OpenForms'] = open_form_a
    
    return render(request, 'index.html', d)

def add_by_number(request):
    print('asdasdasds')
    num = int(request.POST.get('id_stage', ''))

    num_vac = request.POST.get('num_vac', '')
    num_order = request.POST.get('num_order', '')
    try:
        vac = Vacancy.objects.get(pk=num_vac)
    except Exception:
        HttpResponse(json.dumps("'status': 'bad'"), content_type="application/json")
    if num == 1:
        new_test = Test(vacancy=vac,order=num_order)
        new_test.save()
        return HttpResponse(json.dumps("'Добавление': 'ok'"), content_type="application/json")
    elif num == 2:
        new_text = Text(html_text='', vacancy_id=vac, stage=num_order)
        new_text.save()
        return HttpResponse(json.dumps("'Добавление': 'ok'"), content_type="application/json")
    elif num == 3:
        new_form = Interview(vacancies=vac, order=num_order, name='')
        new_form.save()
        return HttpResponse(json.dumps("'Добавление': 'ok'"), content_type="application/json")
    elif num == 4:
        new_big_form = OpenForm(vacancy_id=vac, order=num_order, description='')
        new_big_form.save()
        return HttpResponse(json.dumps("'Добавление': 'ok'"), content_type="application/json")
    return HttpResponse(json.dumps("'Добавление': 'не ok'"), content_type="application/json")
    