from lib2to3.pgen2.tokenize import TokenError
from pstats import Stats
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login,logout
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .serializers import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import knox_settings
from rest_framework.views import APIView
from django.contrib.auth.signals import user_logged_in, user_logged_out



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
     
class RegistroAPIGET(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registro.html'
 

    def get(self, request, format=None):

        serializer = RegisterSerializer()
        return Response({'serializer': serializer})  
    
class RegistroAPIPOST(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = RegisterSerializer
    template_name = 'registro.html'

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'url': '/knox/api/login2/'})
        else:
           
            return JsonResponse({'mensaje': 'Error en los datos de registro!'})
        
##########################################################################################
        
# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
class LoginAPIGET(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request, format=None):

        serializer = LoginSerializer()
        return Response({'serializer': serializer})

class LoginAPIPOST(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = LoginSerializer
    template_name = 'login.html'

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token = AuthToken.objects.create(user)[1]
            response = JsonResponse({'url': '/'})
            response.set_cookie('sessiontoken', token)
            return response
        else:
            return JsonResponse({'mensaje': "Error en los datos ingresados"})
        
        
        
        
    ############################################
class LogoutView(generics.GenericAPIView):
    renderer_classes =  [TemplateHTMLRenderer]
    template_name = '/'

    def get (self, request ,format=None):
      token = AuthToken.objects.filter(user=request.user)
      token.delete()
      logout(request)
      response = redirect('home')
      response.delete_cookie('sessiontoken')
      return response