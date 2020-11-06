from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
#Это я тсчу кое что
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
    d['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username = new_user_form.cleaned_data['username'], 
                password = new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/test')
        else:
            d['form'] = new_user_form
    return render(request, 'signup.html', d)