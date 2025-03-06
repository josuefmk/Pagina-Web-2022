
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render,redirect
from .procesosub import totalpagosub
from .suscripcion import SuscripcionesMant
from .models import Servicio, TipoSuscripcion
from .forms import ServicioForm, SuscripcionForm


        

# Create your views here.

def home(request):
    return render(request,'suscripciones/index.html')

def detalles(request):
    TipoSuscripciones = TipoSuscripcion.objects.all()
    return render(request, "suscripciones/detalles.html", {'TipoSuscripciones':TipoSuscripciones})

        
def formularioo(request):
    return render(request,'suscripciones/formulariocontacto.html')

def sesion(request):
  
    return render(request,'suscripciones/iniciosesion.html')

def pagosuscripcion(request):
    datos = {
        'form3': SuscripcionForm()
    }
    if request.method == 'POST':
        formulario = SuscripcionForm(request.POST)
        if formulario.is_valid():
            compra = formulario.save(commit=False)
            compra.usuario=request.user
            compra.precio=totalpagosub(request)['totalpagosub']
            compra.save()
            datos['mensaje1'] = 'Suscripcion realizada, Le enviaremos un correo con su resivo!'
        else:
                 datos['mensaje2'] = 'Suscripcion fallida'
    return render (request,'suscripciones/pagosuscripcion.html',datos)


def agregar_suscripciones(request, tiposuscripcion_id):
    suscripciones = SuscripcionesMant(request)
    tipoSuscripcion = TipoSuscripcion.objects.get(id=tiposuscripcion_id)
    suscripciones.agregarr(tipoSuscripcion)
    return redirect("detalles")

def eliminar_suscripciones(request, producto_id):
        suscripciones = SuscripcionesMant(request)
        tipoSuscripcion = TipoSuscripcion.objects.get(id=producto_id)
        suscripciones.eliminar(tipoSuscripcion)
        return redirect("detalles") 

def limpiar(request):
    suscripciones = SuscripcionesMant(request)
    suscripciones.limpiar()
    return redirect("detalles")



@login_required
def tienda(request):
    return render (request,'suscripciones/tienda.html')
       

@login_required
@user_passes_test(lambda u: u.is_staff, redirect_field_name=None)
def administracionweb(request):  
    return render(request,'suscripciones/administracionweb.html')
    
@login_required
@user_passes_test(lambda u: u.is_staff, redirect_field_name=None)
def listarapi(request):

    return render(request,'suscripciones/listarapi.html')


@login_required
@user_passes_test(lambda u: u.is_staff, redirect_field_name=None)
def form_lista(request):
    servicio=Servicio.objects.all()
    datos={
        'servicios':servicio
    }
    return render(request,'suscripciones/form_lista.html',datos)


@login_required
@user_passes_test(lambda u: u.is_staff, redirect_field_name=None)
def form_servicio(request):
    datos = {
        'form': ServicioForm()
    }

    if request.method == 'POST':
        formulario = ServicioForm(request.POST,request.FILES)

        if formulario.is_valid():
            formulario.save() #AGREGAR a la BD
            datos['mensaje1'] = 'Se guardó el Servicio'
        else:
            datos['mensaje2'] = 'NO se guardó Servicio'
 
    return render(request,'suscripciones/form_servicio.html',datos)
@login_required
@user_passes_test(lambda u: u.is_staff, redirect_field_name=None)
def form_mod_servicio(request, id):
    servicio = Servicio.objects.get(idservicio=id)
    

    datos = {
        'form':ServicioForm(instance = servicio)
    }

    if request.method == 'POST':
        formulario = ServicioForm(request.POST, request.FILES,instance = servicio)

        if formulario.is_valid():
            formulario.save() #MODIFICA a la BD
            datos['mensaje3'] = 'Se modifico la tabla Servicio'
        else:
            datos['mensaje4'] = 'NO se modifico la tabla Servicio'

    return render(request,'suscripciones/form_mod_servicio.html',datos)   

@login_required
@user_passes_test(lambda u: u.is_staff, redirect_field_name=None)
def form_del_servicio(request, id):
       servicio = Servicio.objects.get(idservicio=id)
       servicio.delete()
       return redirect(to='form_lista')
   
    
