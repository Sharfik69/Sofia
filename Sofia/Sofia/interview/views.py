from django.shortcuts import render

# Create your views here.

def new_interview(request):
    data = {
        'idInterview': 'qqq'
    }
    return render(request, 'new-interview.html', data)


def ajax_new_interview(request):
    print(request.POST)
    return render(request, 'new-interview.html', {})