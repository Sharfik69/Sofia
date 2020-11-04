from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json

def test(request):
    return render(request, 'user_page/index.html', {})
    #return HttpResponse('<h1> Ti sosal chlen </h1>')
