from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ContactosForm, Register_UserForm
from contactos.models import Contactos
from django.forms import BaseModelFormSet
from django.contrib.auth.models import User


def login(request):
    
    return render(request, 'base.html')


def get_contactos(request):
    return render(request, 'view_contactos.html')

def register_contacts(request):
    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid():
            form.save()
            guardado = 'Contacto Guardado'
            return redirect('view_contactos')
    else:
        form = ContactosForm()
    return render(request, 'register_contactos.html', {'form':form})


def register_user(request):
    if request.method == 'POST':
        form = Register_UserForm(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            username = data_form.get('username')
            email = data_form.get('email')
            first_name = data_form.get('first_name')
            last_name = data_form.get('last_name')
            password = request.POST['password']
            password_confirmation = request.POST['password_confirmation']
            if password == password_confirmation:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return render(request, 'base.html')
            else:
                redirect('register_user.html')
    else:
        form = Register_UserForm()
    return render(request, 'register_user.html', {'form': form})