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
    print(requset.POST.dict())
    for i in range(int(requset.POST.dict()['len'])):
        values = requset.POST.dict()
        print(values)
        # values_new = json.dumps(values.replase("\\\\", ""))
        # print(values_new['i'])
        id_tst = values['quest'+str(i)+'.id_test']
        values['quest'+str(i)+'.id_test'] = Test.objects.filter(id=values['quest'+str(i)+'.id_test']).first()
        val = dict()
        val['id_test'] = values['quest' + str(i) + '.id_test']
        val['quest'] = values['quest' + str(i) + '.quest']
        val['type'] = values['quest' + str(i) + '.type']
        val['jsn_ans'] = values['quest' + str(i) + '.jsn_ans']
        val['jsn_is_true'] = values['quest' + str(i) + '.jsn_is_true']
        print(val)
        if val:
            TestQuestion.objects.create(**val)
    # return redirect('../cd/' + str(id_tst))
    return render(requset, 'index.html')


