from django.urls import path
from .views import *
from django.urls import path, include

app_name='administrativo'




urlpatterns = [
    path('api/tramites',Tramite_APIView.as_view(),name='listadoTramites'),                         
]
