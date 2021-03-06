"""mi_libreta URL Configuration

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
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
        
        path('hello-api/', views.HelloAPI.as_view()),
        path('contactos/', views.contactos_list),
        #path('contactos/', views.ContactosList.as_view()),
        #path('contactos/<int:nameuser>/', views.ContactoDetail.as_view()),
        #path('users/', views.UserViewSet.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)