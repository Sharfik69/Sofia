from . import views
from django.conf.urls import url


urlpatterns = [
    url('login/', views.auth_login, name='test'),
    url('logout/', views.auth_logout, name='test'),
     url('registration/', views.sign_up, name='test'),
]