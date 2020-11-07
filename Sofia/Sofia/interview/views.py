from django.shortcuts import render
from django.db import models
from django.http import HttpResponse

import json

from vacancy.models import Vacancy
from .models import Interview, InterviewQuestion, InterviewTags, InterviewAnswer
from authsystem.models import Candidate
# Create your views here.

def new_interview(request):
    data = {}
    if (request.GET):
        if (request.GET['interview']):
            data['idInterview'] = request.GET['interview']
            interview = Interview.objects.get(id = request.GET['interview'])
            data['interviewName'] = interview.name
            arr = []
            questions = InterviewQuestion.objects.filter(interview = interview)
            cnt = 0
            for question in questions:
                tags = InterviewTags.objects.filter(question = question)
                tag1 = []
                cntTag = 0
                for tag in tags:
                    tag1.append({
                        'num': cntTag,
                        'id': tag.id,
                        'text': tag.text
                    })
                    cntTag += 1
                arr.append({
                    'num': cnt,
                    'questionId': question.id,
                    'questionText': question.question,
                    'tags': tag1
                })
                cnt += 1
            data['questions'] = arr
        # print(arr)

    return render(request, 'new-interview.html', data)


def ajax_new_interview(request):

    print(request.POST)

    idInterview = request.POST['idInterview']

# !!!!!!!!!!!!!!!!!!! потом получать нужную вакансию 
    id_vacancy = 1

    vacancy = Vacancy.objects.get(id=id_vacancy)

    order = 1
    name = request.POST['interviewName']
    if (idInterview == ''):
        interview = Interview(
            vacancies = vacancy,
            order = order,
            name = name
        )
        interview.save()
    else:
        interview = Interview.objects.get(id=idInterview)
        interview.name = name
        interview.save()
        questions = InterviewQuestion.objects.filter(
            interview = interview
        )
        for question in questions:
            question.delete()
    
    
    request_questions = dict(request.POST)
    questions = {}
    tags = {}

    for key in request_questions:
        if key.find("interview_question") == 0:
            num = key[key.find('[') + 1:][:-1]
            questions[num] = request_questions[key]
        if key.find("tags") == 0:
            num = key[key.find('[') + 1:][:-1]
            tags[num] = request_questions[key]
    
    for key in questions:
        name = questions[key][0]
        if name == '':
            continue
        new_question = InterviewQuestion(
            question = name,
            interview = interview,
            order = key
        )
        new_question.save()
        if key in tags:
            for tag in tags[key]:
                if tag == '':
                    continue
                new_tag = InterviewTags(
                    text = tag,
                    question = new_question
                )
                new_tag.save()
        
    # print(list(Vacancy.objects.all())[0].id)
    return HttpResponse(
        json.dumps({
            'answer': 'Сохранено',
            'status': 'ok',
            'id': interview.id,
        }),
        content_type="application/json"
    )
    

def ajax_answer_interview(request):
    data = {}
    if (request.POST):
        arr = dict(request.POST)
        id_candidate = arr['idCandidate'][0]
        id_interview = arr['idInterview'][0]
        candidate = Candidate.objects.get(id = id_candidate)
        
        if (candidate == None):
            return HttpResponse("Случилась ошибка")

        for key in arr:

            if key.find("answer") == 0:
                num = key[key.find('[') + 1:][:-1]
                question = InterviewQuestion.objects.get(id = num)
                ans = InterviewAnswer.objects.filter(
                    question=question,
                    respondent=candidate
                )
                if (ans):
                    ans[0].answer = arr[key][0]
                    ans[0].save()
                else:
                    ans = InterviewAnswer(
                        question = question,
                        respondent = candidate,
                        answer = arr[key][0]
                    )
                    ans.save()
    return HttpResponse("Сохранено")

def get_form_for_interview(request):
    data = {}
    if (request.GET):
        if 'interview' in request.GET:
            id_interview = request.GET['interview']
        if 'candidate' in request.GET:
            id_candidate = request.GET['candidate']

        if (id_candidate and id_interview):
            data['idInterview'] = id_interview
            interview = Interview.objects.get(id = id_interview)
            # print(id_candidate)
            candidate = Candidate.objects.get(id = id_candidate)
            if (interview and candidate):
                data['interviewName'] = interview.name
                data['candidateName'] = candidate.user.first_name + '' + candidate.user.last_name + ' (' + candidate.user.username + ')'
                arr = []
                questions = InterviewQuestion.objects.filter(interview = interview)
                cnt = 0
                for question in questions:
                    tags = InterviewTags.objects.filter(question = question)
                    tag1 = []
                    cntTag = 0
                    for tag in tags:
                        tag1.append({
                            'id': tag.id,
                            'text': tag.text
                        })
                    ans = ''
                    ans_ = InterviewAnswer.objects.filter(
                        question=question,
                        respondent=candidate
                    )
                    if (ans_):
                        ans = ans_[0].answer

                    arr.append({
                        'num': cnt,
                        'questionId': question.id,
                        'questionText': question.question,
                        'tags': tag1,
                        'answer': ans,
                    })
                    cnt += 1
                data['questions'] = arr

                data['idInterview'] = id_interview
                data['idCandidate'] = id_candidate


    return render(request, 'answer-interview.html', data)

