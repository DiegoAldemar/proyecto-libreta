from rest_framework import  serializers
from contactos.models import Contactos
from django.contrib.auth.models import User

class HelloSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class ContactosSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
        fields = ('name_user', 'first_name', 'last_name', 'phone_number', 'email')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']