from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from authsystem.models import Candidate, Company
from django.contrib.auth.models import User
from vacancy.models import Vacancy
from vacancy.forms import vacancy_form
import json

def ret_info_user(request):
    d = {}
    check = False
    if not request.user.is_anonymous:
        x = User.objects.get(id=request.user.id)
        
        try:
            d['status'] = Candidate.objects.get(user=x)
            check = True
        except Exception:
            check = False
        if not check:
            try:
                d['status'] = Company.objects.get(user=x)
            except Exception:
                d['status'] = False
        d['username'] = auth.get_user(request).username
    return d

def test(request):
    d = ret_info_user(request)
    return render(request, 'user_page/index.html', d)

def all_vacancies(request):
    x = Vacancy.objects.all()
    d = ret_info_user(request)
    d['vacancies'] = x
    return render(request, 'vacancies_pages/all_vac.html', d)

def my_vac(request):
    d = ret_info_user(request)
    usr = User.objects.get(id=request.user.id)
    x = Vacancy.objects.filter(company=Company.objects.get(user=usr))
    d['vacancies'] = x
    return render(request, 'vacancies_pages/my_vac.html', d)

def create_vac(request):
    d = ret_info_user(request)
    usr = User.objects.get(id=request.user.id)
    x = Vacancy.objects.filter(company=Company.objects.get(user=usr))
    d['vacancies'] = x
    d['forms'] = vacancy_form

    return render(request, 'vacancies_pages/create_vac.html', d)

def add_new_vac(request):
    d = ret_info_user(request)
    usr = User.objects.get(id=request.user.id)
    x = Company.objects.get(user=usr)
    d['vacancies'] = x
    dolzhnost = request.POST.get('name', '')
    description = request.POST.get('description', '')
    salary = request.POST.get('salary', '')
    new_vac = Vacancy.create(x, dolzhnost, description, salary)
    new_vac.save()
    return HttpResponse('ok')