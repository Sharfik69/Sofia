from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.test, name = 'test'),
    url('write_openForm_ans/', views.write_openForm_ans, name = 'ans')
]
