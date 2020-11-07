from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
import json

from .models import Test, TestQuestion, ResultsTest
from vacancy.models import Vacancy
from authsystem.models import Candidate, Company


def take_the_test(request, id_test):
    try:
        user = Company.objects.get(user=auth.get_user(request))
    except Company.DoesNotExist:
        user = Candidate.objects.get(user=auth.get_user(request))
    if not user.is_company:

        queryset_test = Test.objects.filter(id=id_test).first()
        queryset_questions = TestQuestion.objects.filter(id_test=queryset_test.id)
        print(queryset_test.id)
        res = []
        for question in queryset_questions:
            ans = []
            if question.type != 2:
                ans = list(json.loads(question.jsn_ans)['ans'])
            if str(question.img) != "NUL":
                img_url = str(question.img)[6:]
            else:
                img_url = "static/default.png"
            res.append({'quest': question.quest, 'ans': ans, 'type': question.type, 'img': img_url})
        print(res)
        return render(request, 'test_page.html',
                      {'test': str(queryset_test.id),
                       'vac': str(queryset_test.vacancy.id),
                       'questions': res,
                       'order': str(queryset_test.order),
                       'isCompany': '0'})
    exist = 0
    try:
        id_vac, order = str(id_test).split('_')
        print(id_vac, order)
        res = []
    except Exception:
        if Test.objects.filter(id=id_test).count() > 0:
            exist = 1
            queryset_test = Test.objects.get(id=id_test)
            queryset_questions = TestQuestion.objects.filter(id_test=queryset_test.id)
            res = []
            for question in queryset_questions:
                ans = list(json.loads(question.jsn_ans)['ans'])
                ans_tr = list(json.loads(question.jsn_is_true)['ans'])
                res.append({'quest': question.quest, 'ans': ans, 'ans_tr': ans_tr, 'type': question.type})
            id_vac, order = id_test, 0

    return render(request, 'test_page.html',
                  {'test': id_vac, 'questions': '',
                   'isCompany': '1', 'order': order,
                   'exist_field': res,
                   'exist_check': exist})


# def edit_the_test(request, id_test):
#     queryset_test = Test.objects.get(id=id_test)
#     queryset_questions = TestQuestion.objects.filter(id_test=queryset_test.id)
#     res = []
#     for question in queryset_questions:
#         ans = list(json.loads(question.jsn_ans)['ans'])
#         res.append({'quest': question.quest, 'ans': ans, 'type': question.type})
#     return render(request, 'edit_table.html',
#                   {'test': id_test, 'questions': res,
#                    'isCompany': '1', 'test_info': queryset_test})


def post_the_test(request, id_test):
    if request.POST.dict()['order'] == '-5':
        for qq in TestQuestion.objects.filter(id_test=id_test):
            qq.delete()
    for i in range(int(request.POST.dict()['len'])):
        values = request.POST.dict()
        print(values)
        order = values['order']
        try:
            values['quest'+str(i)+'.id_test'] = Test.objects.get(id=values['quest'+str(i)+'.id_test'])
            print('YA TUT')
        except Test.DoesNotExist:
            d = dict()
            d['vacancy'] = Vacancy.objects.filter(id=id_test).first()
            d['order'] = order
            Test.objects.create(**d)
            values['quest' + str(i) + '.id_test'] = Test.objects.get(vacancy=d['vacancy'], order=d['order'])
            print('values', values)
        val = dict()
        val['id_test'] = values['quest' + str(i) + '.id_test']
        val['quest'] = values['quest' + str(i) + '.quest']
        val['type'] = values['quest' + str(i) + '.type']
        val['jsn_ans'] = values['quest' + str(i) + '.jsn_ans']
        val['jsn_is_true'] = values['quest' + str(i) + '.jsn_is_true']
        try:
            val['img'] = request.FILES['quest' + str(i) + '.img']
        except(KeyError):
            val['img'] = "NUL"

        print(val)
        if val:
            obj = TestQuestion.objects.create(**val)
            obj.save()
    # return redirect('../cd/' + str(id_tst))
    return render(request, 'test_page.html')


def post_the_result(request, id_test):
    # print(request.POST.dict())
    print(request.POST.dict())
    queryset_questions = TestQuestion.objects.filter(id_test=request.POST.dict()['id_test'])
    try:
        user = Company.objects.get(user=auth.get_user(request))
    except Company.DoesNotExist:
        user = Candidate.objects.get(user=auth.get_user(request))
    for i in range(int(request.POST.dict()['len'])):
        values = request.POST.dict()
        val = dict()
        val['id_test'] = Test.objects.filter(id=values['id_test']).first()
        # val['candidate'] = Candidate.objects.filter(id=values['candidate']).first()
        val['candidate'] = user
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
        if val:
            ResultsTest.objects.create(**val)

    return render(request, 'test_page.html')


