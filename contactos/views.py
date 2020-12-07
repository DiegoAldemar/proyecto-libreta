from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from contactos import serializers

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