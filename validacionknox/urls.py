from .views import RegisterAPI 
from django.urls import path
from knox import views as knox_views
from .views import *

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout2'),
    path('api/login2/', LoginAPIGET.as_view(), name='login2'),
    path('valida-form/', LoginAPIPOST.as_view(), name='login-valida'),
    path('api/registro/', RegistroAPIGET.as_view(), name='registro'),
    path('valida-form-registro/', RegistroAPIPOST.as_view(), name='registro-valida'),
]