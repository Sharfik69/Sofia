from django.contrib import admin

from .models import Interview, InterviewAnswer, InterviewQuestion, InterviewTags

admin.site.register(Interview)
admin.site.register(InterviewAnswer)
admin.site.register(InterviewQuestion)
admin.site.register(InterviewTags)