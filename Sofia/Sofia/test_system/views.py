from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth

import json

def test(request):
    d = {}
    d['param1'] = 'Я купил цветы'
    d['param2'] = 'Задний привод'
    d['param3'] = 'Camry - Машина богов'

    d['numbers'] = [x for x in range(1, 10, 2)]
    d['kitty'] = [{
        'Dimas' : 'когда-нибудь я стану казекаге',
        'Iriska' : 'kill me'
    },
    {
        'Dimas' : 'когда-нибудь я стану ХОКАГЕ',
        'Iriska' : 'pls ebni menya'
    }]

    d['status'] = 'ERROR2'
    
    d['username'] = auth.get_user(request).username

    return render(request, 'user_page/index.html', d)
    #return HttpResponse('<h1> Ti sosal chlen </h1>')
