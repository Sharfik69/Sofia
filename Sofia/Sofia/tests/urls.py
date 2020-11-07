from django.urls import path
from . import views

urlpatterns = [
    path('cd/<id_test>', views.take_the_test),
    path('cp/<id_test>', views.edit_the_test),
    path('cp_post/<id_test>', views.post_the_test),
    path('cd_post/<id_test>', views.post_the_result),
]