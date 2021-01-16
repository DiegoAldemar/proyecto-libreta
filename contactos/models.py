from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contactos(models.Model):
    name_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.first_name}  {self.phone_number}  {self.name_user}'


    class Meta:
        ordering = ['name_user']
