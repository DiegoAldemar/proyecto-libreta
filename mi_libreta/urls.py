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
from django.contrib import admin
from django.urls import path, include
from aplications.contactos import views

from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('aplications.contactos.api.urls'), name='api'),
    path('', include('aplications.contactos.urls'), name='contactos'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contactos/', views.get_contactos, name='view_contactos'),
    path('contactos/register/', views.register_contacts, name='register_contactos'),
    path('contactos/edit/<int:id>/', views.edit_contact, name='edit_contacto'),
    path('contactos/delete/<int:id>/', views.delete_contacto, name='delete_contacto'),
    path('contactos/guardado/', views.get_contactos, name='guardado_contactos'),
    path('register-user/', views.register_user, name='register_user'),
] 
