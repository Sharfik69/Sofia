"""Sofia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('test_system.urls')),
    path('open-form/', include('open_form.urls')),
    path('q_test/', include("tests.urls")),
    path('auth/', include('authsystem.urls')),
    path('informpage/', include('inform_page.urls')),
    path('interview/', include('interview.urls')),
    path('add_stage/', include('vacancy.urls'))
]
