from django.forms import ModelForm, CharField
from .models import Contactos
from django import forms
from django.contrib.auth.models import User
from django.core import validators

class ContactosForm(ModelForm):
    class Meta:
        model = Contactos
        fields = ['name_user', 'first_name', 'last_name', 'phone_number', 'email']


class Register_UserForm(ModelForm):
    #username = CharField(validators = [validators.RegexValidator('[A-Za-z0-9]', message='solo letras y numeros')])
    password = CharField(widget=forms.PasswordInput, validators= [validators.MinLengthValidator(6, 'mas de 6 caracteres')])
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        

