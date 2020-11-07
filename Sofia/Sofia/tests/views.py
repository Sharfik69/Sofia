from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
import json

from .models import Test, TestQuestion, ResultsTest
from vacancy.models import Vacancy
from authsystem.models import Candidate


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
                  {'test': str(queryset_test.id),
                   'vac': str(queryset_test.vacancy.id),
                   'questions': res,
                   'order': str(queryset_test.order),
                   'isCompany': '0'})


def edit_the_test(request, id_test):

    return render(request, 'index.html',
                  {'test': id_test, 'questions': '',
                   'isCompany': '1'})


def post_the_test(request, id_test):
    print(request.POST.dict())
    for i in range(int(request.POST.dict()['len'])):
        values = request.POST.dict()
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
    return render(request, 'index.html')


def post_the_result(request, id_test):
    # print(request.POST.dict())
    print(request.POST.dict())
    queryset_questions = TestQuestion.objects.filter(id_test=request.POST.dict()['id_test'])
    for i in range(int(request.POST.dict()['len'])):
        values = request.POST.dict()
        val = dict()
        val['id_test'] = Test.objects.filter(id=values['id_test']).first()
        # val['candidate'] = Candidate.objects.filter(id=values['candidate']).first()
        val['candidate'] = Candidate.objects.all().first()
        val['vacancy'] = Vacancy.objects.filter(id=values['vacancy']).first()
        val['ans'] = values['ans' + str(i)]
        val['order'] = values['order']

        accuracy = 0
        if queryset_questions[i].jsn_is_true == val['ans']:
            accuracy += 1
        # accuracy = int(request.POST.dict()['len']) / accuracy * 100
        print(queryset_questions[i].jsn_is_true, val['ans'])

        val['accuracy'] = accuracy
        print(val)
        # if val:
        #     ResultsTest.objects.create(**val)

    return render(request, 'index.html')


