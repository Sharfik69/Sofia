from . import views
from django.conf.urls import url


urlpatterns = [
    url('page/', views.index, name='test'),
    url('send_text/', views.add_text, name='send_text_to_server'),
    url('get_text/', views.get_text, name='get_text'),
]