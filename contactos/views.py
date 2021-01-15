from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ContactosForm, Register_UserForm
from contactos.models import Contactos
from django.forms import BaseModelFormSet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Contactos
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('view_contactos')
        else:
            messages.error(request, 'Usuario Erroneo')
    return render(request, 'base.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def get_contactos(request):
    ver_contactos = Contactos.objects.filter(name_user_id=request.user).order_by('first_name')
    numero_contanctos = ver_contactos.count()
    print(request.user.id)
    return render(request, 'view_contactos.html', {'ver_contactos':ver_contactos,
                                                    'numero_contactos':numero_contanctos})


@login_required
def register_contacts(request):
    if request.method == 'POST':
        save_contact = Contactos(name_user_id=request.user.id)
        form = ContactosForm(request.POST, instance=save_contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contacto Guardado!!!!')
            return redirect('view_contactos')
    else:
        form = ContactosForm()
    return render(request, 'register_contactos.html', {'form':form})

@login_required
def edit_contact(request, id):
    contacto_editar = Contactos.objects.filter(id=id).values()
    if request.method == 'POST':
        contacto_editado = Contactos.objects.get(id=id)
        contacto_editado.first_name = request.POST['first_name']
        contacto_editado.last_name = request.POST['last_name']
        contacto_editado.phone_number = request.POST['phone_number']
        contacto_editado.email = request.POST['email']
        contacto_editado.save()
        messages.success(request, 'Contacto Actualizado!!!')
        print('guardar contacto')
        return redirect('view_contactos')
    return render(request, 'edit_contacto.html', {'contacto_editar': contacto_editar})


@login_required
def delete_contacto(request, id):
    delete_contacto = Contactos.objects.get(id=id)
    delete_contacto.delete()
    messages.warning(request, '¿Desea Eliminar Contacto?')
    return redirect('view_contactos')

def register_user(request):
    if request.method == 'POST':
        form = Register_UserForm(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            username = data_form.get('username')
            email = data_form.get('email')
            first_name = data_form.get('first_name')
            last_name = data_form.get('last_name')
            password = data_form.get('password')
            password_confirmation = request.POST['password_confirmation']
            if password == password_confirmation:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                messages.success(request, 'Registro Exitoso!!!')
                return render(request, 'base.html')
            else:
                redirect('register_user.html')
    else:
        form = Register_UserForm()
    return render(request, 'register_user.html', {'form': form})