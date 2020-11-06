from . import views
from django.conf.urls import url


urlpatterns = [
    url('new/', views.new_interview, name='new_interview'),
]