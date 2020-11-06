from django.contrib import admin

from .models import Tag, Candidate, Education, WorkExperience

admin.site.register(Tag)
admin.site.register(Candidate)
admin.site.register(Education)
admin.site.register(WorkExperience)
