from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets, permissions
from rest_framework.parsers import JSONParser


from aplications.contactos.api import serializers


from aplications.contactos.models import Contactos
from django.forms import BaseModelFormSet

from django.contrib.auth.models import User
from aplications.contactos.api.serializers import ContactosSerealizer





class HelloAPI(APIView):
    serializer_class = serializers.HelloSerializers
    #prueba api view
    def get(self, request, format=None):
        #retornar lista de caracteristicas del api view
        lista_apiview = [
            'hola hellen',
            'esta es mi primer api',
            'vamos a probarla',
            'esto me gusta mucho'
        ]

        return Response({
            'message': 'hello world',
            'lista_apiview': lista_apiview,
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({
                'message': message,
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):

        return Response({'method': 'DELETE'})

@csrf_exempt
def contactos_list(request):
    if request.method == 'GET':
        contactos = Contactos.objects.all()
        serializers = ContactosSerealizer(contactos, many=True)
        return JsonResponse(serializers.data, safe=False)


""" class ContactosList(generics.ListCreateAPIView):
    queryset = Contactos.objects.all()
    serializer_class = serializers.ContactosSerealizer

class ContactoDetail(APIView):
    def get_object(self, nameuser):
        try:
            return Contactos.objects.filter(name_user_id=nameuser)
        except Contactos.DoesNotExist:
            raise Http404

    def get(self, request, nameuser, format=None):
        contactos = self.get_object(nameuser)
        serializers = ContactosSerealizer(contactos)
        return Response(serializers.data)
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_class = [permissions.IsAuthenticated] """
    