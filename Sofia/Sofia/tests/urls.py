from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('cd/<id_test>', views.take_the_test),
    path('t/<id_test>', views.take_the_test),
    # path('e/<id_test>', views.edit_the_test),
    path('cp_post/<id_test>', views.post_the_test),
    path('cd_post/<id_test>', views.post_the_result),
]