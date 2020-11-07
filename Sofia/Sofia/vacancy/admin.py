from django.contrib import admin
from .models import Tag, Vacancy, users_vacancy

admin.site.register(Tag)
admin.site.register(Vacancy)
admin.site.register(users_vacancy)

