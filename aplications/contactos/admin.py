from django.contrib import admin
from .models import Contactos
# Register your models here.

class Contactos_admin(admin.ModelAdmin):
    list_display = ('name_user',
                    'first_name',
                    'last_name',
                    'phone_number',
                    'email')
    

admin.site.register(Contactos, Contactos_admin)




    
