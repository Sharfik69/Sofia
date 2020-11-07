from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.show_open_form, name = 'form'),
    url('write_openForm_ans/', views.write_openForm_ans, name = 'ans'),
    url(r'edit-open-form/(?P<id>\d+)/$', views.edit_open_form, name = 'edit'),
    url('save_form_edition/', views.save_form_edition, name = 'save_edition')
]
