from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from authsystem.models import Candidate, Company
from vacancy.models import Vacancy
from .models import Text
import json 

def index(request):
    d = {}
    if not request.user.is_anonymous:
        d['username'] = auth.get_user(request).username
        check = False
        try:
            d['status'] = Candidate.objects.get(user=request.user.id)
            check = True
            d['status'] = False
        except Exception:
            d['status'] = 'Error'
        if not check:
            try:
                d['status'] = Company.objects.get(user=request.user.id)
            except Exception:
                d['status'] = False
    

    return render(request, 'index.html', d)

def add_text(response):
    text = response.POST.get('text_for_user', '')
    status = response.POST.get('id_vac', '')
    num_stage = response.POST.get('num', '')
    a = Vacancy.objects.get(pk=1)
    q = Text.create(text, a)
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