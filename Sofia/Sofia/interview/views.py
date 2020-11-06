from django.shortcuts import render

# Create your views here.

def new_interview(request):

    return render(request, 'new-interview.html', {})


def ajax_new_interview(request):
    print(request.POST)
    return render(request, 'new-interview.html', {})