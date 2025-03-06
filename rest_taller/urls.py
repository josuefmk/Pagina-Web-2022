from django.urls import path
from rest_taller.views import lista_servicio, detalle_servicio

urlpatterns = [
    path('lista_servicio', lista_servicio, name="lista_servicio"),
    path('detalle_servicio/<id>', detalle_servicio, name="detalle_servicio"),

]