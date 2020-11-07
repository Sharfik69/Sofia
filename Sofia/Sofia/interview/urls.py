from . import views
from django.conf.urls import url


urlpatterns = [
    url('new/ajax/', views.ajax_new_interview, name='ajax_new_interview'),
    url('new/', views.new_interview, name='new_interview'),
    url(r'answer/$', views.get_form_for_interview, name='get_form_for_interview'),
    url('answer/ajax/', views.ajax_answer_interview, name='ajax_answer_interview'),
]