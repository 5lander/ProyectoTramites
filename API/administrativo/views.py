from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect,HttpRequest,HttpResponse

# Create your views here.
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .forms import *
from .serializers import TramiteSerializers
from .models import Tramite

class Tramite_APIView(APIView):
    def get(self, request,format =None, *args, **Kwargs):
        tramites= Tramite.objects.all()
        serializer= TramiteSerializers(tramites,many=True)    
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=TramiteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class Tramite_APIView_Detalles(APIView):
    def get_object(self, tramite_id):
        try:
            return Tramite.objects.get(id=tramite_id)
        except Tramite.DoesNotExist:
            raise Http404

    def get(self,request,id_tramite,format=None):
        tramite = self.get_object(id_tramite)
        serializer= TramiteSerializers(tramite)
        return Response(serializer.data)

    def post(self,request,format=None, *args,**kwargs):
            print(request.data)
            data ={
                'nombres':request.data.get('nombres'),
                'apellidos':request.data.get('apellidos'),
                'cedula':request.data.get('cedula'),
                'celular':request.data.get('celular'),
                'nacionalidad':request.data.get('nacionalidad'),
                'correo':request.data.get('correo'),
                'edad':request.data.get('edad'),
                'descripcion':request.data.get('descripcion'),
                'tramite':request.data.get('tramite'),
            }
            print(data)
            
            serializer=TramiteSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    