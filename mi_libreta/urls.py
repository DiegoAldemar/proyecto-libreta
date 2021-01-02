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
from contactos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('contactos.api.urls'), name='api'),

    path('login/', views.login_view, name='login'),

    path('contactos/', views.get_contactos, name='view_contactos'),
    path('contactos/register/', views.register_contacts, name='register_contactos'),
    path('contactos/guardado/', views.get_contactos, name='guardado_contactos'),
    path('register-user/', views.register_user, name='register_user'),
]
