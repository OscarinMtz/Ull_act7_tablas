# app_servicios/urls.py (Crear este archivo)

from django.urls import path
from . import views

urlpatterns = [
    # READ: Lista todos los servicios
    path('', views.index, name='inicio'), 
    # CREATE: Muestra el formulario y procesa la creación
    path('agregar/', views.agregar_servicio, name='agregar_servicio'),
    # UPDATE: Muestra el formulario prellenado y procesa la actualización
    path('editar/<int:id>/', views.editar_servicio, name='editar_servicio'),
    # DELETE: Muestra la confirmación y procesa el borrado
    path('borrar/<int:id>/', views.borrar_servicio, name='borrar_servicio'),
]