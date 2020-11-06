from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
import json

from .models import Test, TestQuestion


def take_the_test(request, id_test):
    queryset_test = Test.objects.filter(id=id_test).first()
    # queryset_test = Test.objects.all().first()
    queryset_questions = TestQuestion.objects.filter(id_test=queryset_test.id)
    print(queryset_test.id)
    res = []
    for question in queryset_questions:
        ans = []
        if question.type != 2:
            ans = list(json.loads(question.jsn_ans)['ans'])
        res.append({'quest': question.quest, 'ans': ans, 'type': question.type})
    print(res)

    return render(request, 'index.html',
                  {'test': queryset_test, 'questions': res,
                   'isCompany': '0'})


def edit_the_test(request, id_test):

    return render(request, 'index.html',
                  {'test': id_test, 'questions': '',
                   'isCompany': '1'})


def post_the_test(requset, id_test):
    l = requset.POST
    print(l)
    return render(requset, 'index.html')


