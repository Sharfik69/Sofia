from django.shortcuts import render

# Create your views here.

def new_interview(request):

    return render(request, 'new-interview.html', {})
