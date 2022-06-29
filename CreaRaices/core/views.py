from django.shortcuts import render, redirect
from core.forms import productosForm
from core.models import Producto
#from .models import Usuario

# Create your views here.


def home(request):
    return render(request,'core/home.html')

def login(request):
    return render(request,'core/login.html')


def productos(request):
    return render(request,'core/productos.html')
   
def mantenedor_productos(request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request,'core/mantenedor.html', datos)

def nuevo_producto(request):

    datos = {
        'form': productosForm()
    }

    if request.method=='POST':
        formulario= productosForm(request.POST, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']= "producto creado correctamente"
        else :
            datos["form"] = formulario

    return render(request,'core/nuevo_usuario.html',datos)

def mod_producto(request,id):

    id_producto = Producto.objects.get(idProducto=id)

    datos = {
        'form': productosForm(instance=id_producto)
    }

    if request.method=='POST':
        formulario= productosForm(data=request.POST,instance=id_producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']= "producto modificado correctamente"
    

    return render(request,'core/mod_usuario.html',datos)    

def del_producto(request,id):

    id_producto = Producto.objects.get(idProducto=id)
  
    id_producto.delete()

    return redirect(to="home")       