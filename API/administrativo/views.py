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

    def put(self,request,id_tramite, format=None):
        tramite=self.get_object(id_tramite)
        serializer= TramiteSerializers(tramite,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
