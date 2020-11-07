from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'all_vacancies/$', views.all_vacancies, name='all_vacancies'),
    url(r'my_vac/$', views.my_vac, name='my_vac'),
    url(r'create_vac/$', views.create_vac, name='create_vac'),
    url(r'create_vac/add_vac$', views.add_new_vac, name='create_vac'),
]