#aqui van a ir las funciones

from rest_framework import generics
from django.shortcuts import render,redirect
from django.db import Error
import os
from appTienda.models import Categoria, Producto
from appTienda.serializers import CategoriaSerializer, ProductoSerializer

# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def vistaCategorias(request):
    return render(request, "frmCategoria.html")

def agregarCategoria(request):
    nombre = request.POST["txtNombre"]
    try:
        categoria=Categoria(catNombre=nombre)
        categoria.save()
        mensaje="Categoria agregada"
        
    except Error as error:
        mensaje=f"problemas al agregar la categoria{error}"

    retorno = {"mensaje": mensaje}    
    return render(request,"frmCategoria.html",retorno)

def listarProductos(request):
    try:
        productos = Producto.objects.all()
        mensaje=""
        print(productos)       
    
    except:
        mensaje="problemas al  obtener los productos"
    retorno={"mensaje":mensaje, "listaProductos":productos}    
    return render(request,"listarProductos.html", retorno)


def vistaProducto(request):
    try:
        categorias= Categoria.objects.all()
        mensaje=""
    except:
        mensaje="Problemas al obtener las categorias"
    retorno ={"mensaje":mensaje,"listaCategorias":categorias, "producto":None}
    return render(request, "frmRegistrarProducto.html",retorno)


#Ahora vamos a crear función que nos permite 
# agregar un producto a la base de datos:

def agregarProducto(request):
    nombre = request.POST["txtNombre"] #name del formulario
    codigo = int(request.POST["txtCodigo"])
    precio = int(request.POST["txtPrecio"])
    idCategoria = int (request.POST["cbCategoria"])
    archivo = request.FILES.get("fileFoto", False)
    try:
        #obtener la categoria de acuerdo a su id
        categoria=Categoria.objects.get(id=idCategoria)
        #crear el producto
        producto = Producto (proNombre = nombre,proCodigo=codigo,
                            proPrecio=precio, proCategoria=categoria,
                            proFoto = archivo)
        
        #registrarlo en la base de datos
        producto.save()
        mensaje = "Producto agregado"
        return redirect("/listarProductos/")
    except Error as error:
        mensaje = f"Problemas al realizar el proceso de agregar el producto. {error}"
        
    #obtener las categorias
    categorias = Categoria.objects.all()
    retorno = {"mensaje": mensaje, "listaCategorias":categorias, "producto":producto}
    return render(request,"frmRegistrarProducto.html", retorno)

def consultarProducto(request,id):
    try:
        producto = Producto.objects.get(id=id)
        categorias = Categoria.objects.all()
        mensaje =""
    except Error as error:
        mensaje = f"Problemas{error}"
        
    retorno={"mensaje": mensaje, "producto":producto,
            "listaCategorias":categorias}
    return render(request,"frmEditarProducto.html", retorno)

                            
def actualizarProducto(request):
    idProducto = int(request.POST["idProducto"])
    nombre =request.POST["txtNombre"] #name del formulario
    codigo =int(request.POST["txtCodigo"])
    precio =int(request.POST["txtPrecio"])
    idCategoria = int (request.POST["cbCategoria"])
    archivo = request.FILES.get("fileFoto", False)

    try:
        #obtener la categoria de acuerdo a su id
        categoria = Categoria.objects.get(id=idCategoria)
        #actualizar el producto. PRIMERO SE CONSULTA
        producto = Producto.objects.get(id =idProducto)
        producto.proNombre=nombre
        producto.proPrecio=precio        
        producto.Categoria=categoria
        producto.proCodigo=codigo
        #si el campo de foto tiene datos actualiza foto
        if(archivo!= ''):
            producto.proFoto =archivo
        producto.save()
        mensaje="Producto actualizado"
        return redirect("/listarProductos/")
    except Error as error:
        mensaje=f"problemas al actualizar {error}"
        categorias =Categoria.objects.all()
        retorno = {"mensaje":mensaje, "listaCategorias":categorias,"producto":producto}
        return render(request,"frmEditarProducto.html",retorno)

def eliminarProducto(request,id):
    try:
        producto = Producto.objects.get(id=id)
        if producto.proFoto:
            if os.path.exists(producto.proFoto.path):
                os.remove(producto.proFoto.path)
            producto.proFoto.delete()
        producto.delete()
        mensaje="Producto eliminado"
        
    except Error as error:
        mensaje=f"problemas al eliminar {error}"
    
    retorno = {"mensaje":mensaje}
    return redirect("/listarProductos/",retorno)


#VISTAS DE LA API

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class ProductoList(generics.ListCreateAPIView):
    queryset= Producto.objects.all()
    serializer_class= ProductoSerializer
    
class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Producto.objects.all()
    serializer_class = ProductoSerializer
    
