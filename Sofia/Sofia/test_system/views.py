from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from authsystem.models import Candidate, Company
from django.contrib.auth.models import User
from vacancy.models import Vacancy#, users_vacancy
from vacancy.forms import vacancy_form
from django.shortcuts import redirect

import json

def ret_info_user(request):
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
    return d

def test(request):
    d = ret_info_user(request)
    return render(request, 'user_page/index.html', d)

def all_vacancies(request):
    x = Vacancy.objects.all()
    d = ret_info_user(request)
    d['vacancies'] = x
    d['user_'] = request.user
    return render(request, 'vacancies_pages/all_vac.html', d)

def my_vac(request):
    d = ret_info_user(request)
    if d['status'] == 2:
        try:
            usr = User.objects.get(id=request.user.id)
            x = Vacancy.objects.filter(company=Company.objects.get(user=usr))
        except Exception:
            usr, x = None, None
        d['vacancies'] = x
        return render(request, 'vacancies_pages/my_vac.html', d)
    elif d['status'] == 1:
        usr = Candidate.objects.get(user=request.user.id)
        vacancies = Vacancy.objects.filter(candidates = usr)
        d['vacancies'] = vacancies
        return render(request, 'vacancies_pages/my_vac.html', d)

    else:
        return render(request, 'test', {})

def create_vac(request):
    d = ret_info_user(request)
    try:
        usr = User.objects.get(id=request.user.id)
        x = Vacancy.objects.filter(company=Company.objects.get(user=usr))
    except Exception:
        x, usr = None, None
    d['vacancies'] = x
    d['forms'] = vacancy_form

    return render(request, 'vacancies_pages/create_vac.html', d)

def add_new_vac(request):
    d = ret_info_user(request)
    try:
        usr = User.objects.get(id=request.user.id)
        x = Company.objects.get(user=usr)
    except Exception:
        usr, x = None, None
    d['vacancies'] = x
    dolzhnost = request.POST.get('name', '')
    description = request.POST.get('description', '')
    salary = request.POST.get('salary', '')
    new_vac = Vacancy.create(x, dolzhnost, description, salary)
    new_vac.save()
    return HttpResponse('ok')


def add_vac_to_user(request):
    vac_id = int(request.POST.get('vac_id', ''))
    vac = Vacancy.objects.get(pk=vac_id)
    usr = Candidate.objects.get(user=auth.get_user(request))
    print(vac)
    print(usr)
    vac.candidates.add(usr)

    return HttpResponse("Q")

    # new_users_vacancy = users_vacancy(candidate=usr, vacancy=vac)
    # new_users_vacancy.save()


def show_stage_to_user(request, id_vac):
    usr = Candidate.objects.get(user=auth.get_user(request))
    vac_num = id_vac

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

    x = int(vac_num)
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

    return render(request, 'vacancies_pages/stages_for_user.html', d)