from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
# from .models import CompanyForm, Company, Candidate, CandidateForm
from .models import Company, Candidate, CandidateForm
from .forms import Company_new_form, Employer_new_form


def auth_login(request):
    if request.POST:
        username = request.POST.get('Uname', '')
        password = request.POST.get('Pass', '')
        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user)
            #Тут должен быть редирект на какую-то мейн страницу 
            return redirect('/test')
        else:
            return render(request, 'login.html', {'status': 'ERROR'})
    return render(request, 'login.html', {})
    # return HttpResponse('<h1> Ti sosal chlen </h1>')

def auth_logout(request):
    auth.logout(request)
    return redirect('/test')

def sign_up(request):
    #Это реализация через формы джанго, там сразу есть валидация пароля и вроде че-то свое можно добавить
    d = {}
    d.update(csrf(request))
    whois = request.POST.get('whois', '')
    if whois == '1':
        d['form_for_candidate'] = Employer_new_form()
    elif whois == '2':
        d['form_for_company'] = Company_new_form()
    else:
        d['form_for_company'] = Company_new_form()
        d['form_for_candidate'] = Employer_new_form()
    if request.POST:
        print(request.FILES)
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username = new_user_form.cleaned_data['username'], 
                password = new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            files = request.FILES
            if whois == '1':
                empl = Candidate.create(new_user, request.POST.get('phone', ''),
                request.POST.get('addition_contacts', ''), request.POST.get('description', ''), file_)
                empl.save()
            else:
                comp = Company.create(new_user, request.POST.get('name_company', ''), request.POST.get('FIO_CEO', ''),
                    request.POST.get('Phone_CEO', ''), request.POST.get('Email_CEO', ''), request.POST.get('FIO_Contact', ''), request.POST.get('Phone_Contact', ''), 
                    request.POST.get('Email_Contact', ''),
                    request.POST.get('description', ''), file_, request.POST.get('place', ''))
                comp.save()
            return redirect('/test')
        else:
            if whois == 1:
                d['form_for_candidate'] = new_user_form
            else:
                d['form_for_company'] = new_user_form
    return render(request, 'signup.html', d)