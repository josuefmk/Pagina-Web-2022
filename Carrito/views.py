from django.shortcuts import render,redirect
from .car import Carrito
from .forms import CompraForm
from .proceso import total_carrito
from .models import Producto
from django.contrib.auth.decorators import login_required


@login_required
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})
@login_required
def checkout(request):
    datos = {
        'form1': CompraForm()
    }
    if request.method == 'POST':
        formulario = CompraForm(request.POST)
        if formulario.is_valid():
            compra = formulario.save(commit=False)
            compra.usuario=request.user
            compra.total=total_carrito(request)['total_carrito']
            compra.save()
            datos['mensaje1'] = 'Pago Realizado,Le enviaremos un correo con los datos para realizar el servicio!'
        else:
            datos['mensaje2'] = 'Pago rechazado'
 
    return render(request,"checkout.html",datos)


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")
