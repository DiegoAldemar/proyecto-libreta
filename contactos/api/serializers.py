from rest_framework import  serializers
from contactos.models import Contactos
from django.contrib.auth.models import User

class HelloSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class ContactosSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'name_user_id')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']