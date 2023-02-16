from django.db import models
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.db.models.deletion import CASCADE
from django.db.models import Avg

class Rol(models.Model):

    nombre = models.CharField(verbose_name='Ingresar el nombre del rol', max_length=80, help_text='Ingrese el nombre del rol')
    descripcion = models.TextField(verbose_name='Ingrese una descrición detallada del rol', help_text='Descripcion del rol')

    class Meta:
        verbose_name = 'Permiso del sistema'
        verbose_name_plural = 'Permisos para usuarios'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        permisos_defecto = ['add', 'change', 'delete', 'view']
        if not self.id:
            nuevo_grupo, creado = Group.objects.get_or_create(name=f'{self.nombre}')
            for permiso_temp in permisos_defecto:
                permiso, creado = Permission.objects.update_or_create(
                    name = f'Can {permiso_temp} {self.nombre} ',
                    content_type = ContentType.objects.get_for_model(Rol),
                    codename = f'{permiso_temp}_{self.nombre}'
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
            super().save(*args, **kwargs)
        else:
            rol_antiguo = Rol.objects.filter(id=self.id).values('nombre').first()
            if rol_antiguo['nombre'] == self.nombre:
                super().save(*args, **kwargs)
            else:
                Group.objects.filter(name=rol_antiguo['nombre'].update(name=f'{self.nombre}'))
                for permiso_temp in permisos_defecto:
                    Permission.objects.filter(codename=f"{permiso_temp}_{rol_antiguo['nombre']}").update(
                        codename = f'{permiso_temp}_{self.nombre}',
                        name= f'Can {permiso_temp} {self.nombre}'
                    )
                super().save(*args, **kwargs)


class Persona(models.Model):
    nombres = models.CharField(verbose_name="Nombres Completos",max_length=100)
    apellidos = models.CharField(verbose_name="Apellidos Completos",max_length=100)
    cedula =models.CharField(verbose_name="Cedula",max_length=10)
    celular = models.CharField(verbose_name="Nro celular",max_length=10)
    nacionalidad= models.CharField(verbose_name="Nacionalidad",max_length=100)
    correo = models.EmailField(verbose_name="Correo electronico",max_length=100)
    edad= models.IntegerField(verbose_name="Edad")

    def duplicidadCedula(self):
        persona= Persona.objects.all() 
        for persona in persona:
            if persona.cedula == self.cedula:
                print("Existe la cedula")
                self.nombres= persona.nombres
            else:
                print("La cedula no coincide")

    def __str__(self):
        return self.apellidos + " "+self.nombres


class Facultad(models.Model):
    nombreF=models.CharField(verbose_name="Nombre de la Facultad",max_length=100)
    def __str__(self):
        return self.nombreF


class Carrera(models.Model):
    nombreC = models.CharField(verbose_name="Nombre de la carrera",max_length=200)
    facultad =models.ForeignKey(Facultad,on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombreC

class TipoTramite(models.Model):
    nombrett= models.CharField(verbose_name="Tipo de tramite",max_length=100)
    descripcion=models.TextField(verbose_name="Que contempla este tramite")

class Tramite(models.Model):
    nombreT=models.CharField(verbose_name="Nombre del tramite",max_length=100)
    tipoTramite=models.ForeignKey(TipoTramite,verbose_name="Tipo de Tramite",on_delete=models.DO_NOTHING)
    descripcion= models.TextField(verbose_name="Para quienes va dirigido")
    tiempoestimado=models.IntegerField(verbose_name="Tiempo que demora el tramite")
    necesidad=models.TextField(verbose_name="Que necesita para solicitar este tramite")
    costo=models.FloatField()

class Tramitante(Persona):
    carrera=models.ManyToManyField(Carrera,verbose_name="Carrera")

class PedidoTramite(Persona):
    tramite=models.OneToOneField(Tramite,verbose_name="Tramite",on_delete=models.RESTRICT)
    descripcion=models.TextField(verbose_name="Motivo Del Pedido",blank=True, null=True)