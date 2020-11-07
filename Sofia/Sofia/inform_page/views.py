from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from authsystem.models import Candidate, Company
from vacancy.models import Vacancy
from .models import Text
import json 

def index(request, id_vac):
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
            x = Text.objects.get(pk=id_vac)
            d['text'] = x
            d['ID'] = x.vacancy_id.pk
            d['ID_IMG'] = id_vac
            print(d['ID'])
        except Exception:
            x = None
    return render(request, 'index1.html', d)

def add_text(response):
    text = response.POST.get('text_for_user', '')
    status = response.POST.get('id_vac', '')
    num = response.POST.get('num', '')
    print(status)
    a = Vacancy.objects.get(pk=int(status))
    q = Text.objects.get(pk=num)
    q.html_text = text
    q.save()
    return HttpResponse('ok')

def get_text(response):
    stage_num = response.POST.get('num', '')
    vac_id = response.POST.get('v_id', '')
    print(stage_num)
    print(vac_id)
    try:
        a = Text.objects.get(pk=vac_id).get_text()
    except Exception:
        print(Exception)
        a = 'None'

    return HttpResponse(a)