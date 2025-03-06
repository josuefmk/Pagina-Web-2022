from django.contrib import admin
from .models import Mecanico, Auto, Servicio, Suscripcion, TipoSuscripcion
# Register your models here.
admin.site.register(Mecanico)
admin.site.register(Auto)
admin.site.register(Servicio)
admin.site.register(Suscripcion)
admin.site.register(TipoSuscripcion)


