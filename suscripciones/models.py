
from contextlib import nullcontext
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Carrito.models import Compra

class Mecanico(models.Model):
    rutMecanico = models.IntegerField(primary_key=True,verbose_name='RUT')
    dvMecanico = models.CharField(max_length=1,verbose_name='DV')
    nombreMecanico = models.CharField(max_length=50,verbose_name='Nombre')
    telefonoMecanico = models.IntegerField(null=True, blank=True, verbose_name='Telefono')
    correoMecanico = models.CharField(max_length=20,null=True, blank=True, verbose_name='Correo')
    

    def __str__(self):
        return self.rutMecanico

class Auto(models.Model):
    patente = models.CharField(max_length=6,primary_key=True,verbose_name='Patente')
    marca = models.CharField(max_length=20,verbose_name='Marca')
    anno = models.IntegerField(verbose_name='Año')  
    color = models.CharField(max_length=20,verbose_name='Color')
    
    def __str__(self):
        return  self.patente

class Servicio(models.Model):
    idservicio = models.AutoField(primary_key=True,verbose_name='#')
    nombreservicio = models.CharField(max_length=50, verbose_name='Nombre Servicio ')
    precio = models.IntegerField(null=True, blank=True, verbose_name='Precio $')
    imagen = models.ImageField(upload_to="servicios",null=True)
    
    
    def __str__(self):
        return  self.nombreservicio
            

    def __str__(self):
        return self.nombre
class Suscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario= models.ForeignKey(User,on_delete=models.CASCADE)
    fecha =  models.DateField(default=timezone.now,verbose_name="Fecha Compra")
    nombret =  models.CharField(max_length=150,verbose_name="Nombre Tarjeta")
    numerot = models.IntegerField(verbose_name="Número Tarjeta")
    mest =  models.IntegerField(verbose_name="Mes Exp")
    annot =  models.IntegerField(verbose_name="Año Exp")
    cvv =  models.IntegerField(verbose_name="CVV")
    precio = models.IntegerField(verbose_name="Precio")
    def __str__(self):
        return f'{self.fecha} -> {self.usuario}' 
    
class TipoSuscripcion(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=100000)
    precio = models.IntegerField(verbose_name='$ ')
    imagen = models.ImageField(null=True, blank=True)
    def __str__(self):
            return f'{self.nombre} -> {self.precio}'
    

