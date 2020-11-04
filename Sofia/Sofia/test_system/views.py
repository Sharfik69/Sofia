from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json

def test(request):
    #Здесь пишем логику, сбор данные и все такое
    #Все данные, которые нам нужно отдать на страницу мы забиваем в словарь и передаем
    #3 параметром в render (Сейчас там просто пустой массив)
    #Как это работает, покажу потом
    return render(request, 'user_page/index.html', {})
    #return HttpResponse('<h1> Ti sosal chlen </h1>')
