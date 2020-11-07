from django.conf.urls import url
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('page/<id_vac>', views.index, name='test'),
    url('send_text/', views.add_text, name='send_text_to_server'),
    url('get_text/', views.get_text, name='get_text'),
]