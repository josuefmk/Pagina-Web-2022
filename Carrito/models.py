from pyexpat import model

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Producto(models.Model):
   
    nombre = models.CharField(max_length=64)
    precio = models.IntegerField(verbose_name='$ ')
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    usuario= models.ForeignKey(User,on_delete=models.CASCADE)
    fecha =  models.DateField(default=timezone.now,verbose_name="Fecha Compra")
    nombret =  models.CharField(max_length=150,verbose_name="Nombre Tarjeta")
    numerot = models.IntegerField(verbose_name="Número Tarjeta")
    mest =  models.IntegerField(verbose_name="Mes Exp")
    annot =  models.IntegerField(verbose_name="Año Exp")
    cvv =  models.IntegerField(verbose_name="CVV")
    total = models.IntegerField(verbose_name="Total")
    def __str__(self):
        return f'{self.fecha} -> {self.usuario}' 
