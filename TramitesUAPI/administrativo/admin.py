from django.contrib import admin
from .models import  Rol, Facultad, Carrera,TipoTramite,Tramite,Tramitante,PedidoTramite
# Register your models here.
admin.site.register(Rol)
admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(TipoTramite)
admin.site.register(Tramite)
admin.site.register(Tramitante)
admin.site.register(PedidoTramite)
