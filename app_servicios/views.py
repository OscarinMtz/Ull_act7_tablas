# app_servicios/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio 

# 1. LISTAR SERVICIOS (READ)
def index(request):
    servicios = Servicio.objects.all() # Obtiene todos los objetos
    return render(request, 'listar_servicios.html', {'servicios': servicios})

# 2. AGREGAR SERVICIO (CREATE)
def agregar_servicio(request):
    if request.method == 'POST':
        # Mapea los campos del formulario POST a los campos del modelo
        Servicio.objects.create(
            nombre_ser=request.POST['nombre_ser'],
            desc=request.POST['desc'],
            precio=request.POST['precio'],
            duracion=request.POST['duracion'],
            tipo_de_serv=request.POST['tipo_de_serv']
        )
        return redirect('inicio') # Redirige a la lista principal después de guardar
    return render(request, 'agregar_servicio.html')

# 3. EDITAR SERVICIO (UPDATE)
def editar_servicio(request, id):
    # Busca el servicio por su ID o devuelve error 404
    servicio = get_object_or_404(Servicio, id=id) 
    if request.method == 'POST':
        # Actualiza los atributos del objeto con los datos del POST
        servicio.nombre_ser = request.POST['nombre_ser']
        servicio.desc = request.POST['desc']
        servicio.precio = request.POST['precio']
        servicio.duracion = request.POST['duracion']
        servicio.tipo_de_serv = request.POST['tipo_de_serv']
        servicio.save() # Guarda los cambios en la base de datos
        return redirect('inicio')
    # Envía el objeto actual al template para prellenar el formulario
    return render(request, 'editar_servicio.html', {'servicio': servicio})

# 4. BORRAR SERVICIO (DELETE)
def borrar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if request.method == 'POST':
        servicio.delete() # Borra el objeto
        return redirect('inicio')
    # Muestra la página de confirmación
    return render(request, 'borrar_servicio.html', {'servicio': servicio})