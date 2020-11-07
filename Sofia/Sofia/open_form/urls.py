from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.show_open_form, name = 'form'),
    url('write_openForm_ans/', views.write_openForm_ans, name = 'ans'),
    url(r'edit-open-form/(?P<id>\d+)/$', views.edit_open_form, name = 'edit'),
    url('save_form_edition/', views.save_form_edition, name = 'save_edition'),
    url(r'check_open_form/(?P<id>\d+)/$', views.check_open_form, name = 'check'),
    url('write_mark_to_tast/', views.write_mark_to_tast, name = 'mark'),
    url('create_open_form/', views.create_open_form, name = 'create'),
    url('create_open_form_show/', views.create_open_form_show, name = 'create1')
]
