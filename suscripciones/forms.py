from django import forms
from django.forms import ModelForm
from .models import Auto, Servicio,  Mecanico, Suscripcion

class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['patente','marca','anno','color']
        
class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombreservicio','precio','imagen']

class SuscripcionForm(ModelForm):
    class Meta:
        model = Suscripcion
        fields = ['nombret','numerot','mest','annot','cvv',]

class MecanicoForm(ModelForm):
    class Meta:
        model = Mecanico
        fields = ['rutMecanico','nombreMecanico','telefonoMecanico','correoMecanico']
