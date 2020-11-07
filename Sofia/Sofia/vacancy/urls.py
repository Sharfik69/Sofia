from django.conf.urls import url
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'add_by_number', views.add_by_number, name='add_by_number'),
    path('<id_vac>', views.create_stage, name='create_stage'),
]