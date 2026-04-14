from django.urls import path
from .views import ListarPrestamos,RegistrarPrestamo,RegistrarDevolucion,RegistrarEstudiante,UpdateEstudiante
#! este archivo tiene que ser referenciado en el archivo urls.py principal del proyecto que es el unico que reconoce python.
app_name='prestamo_app'
urlpatterns = [
    #definimos la ruta y llamamos a la vista ListaAutores
    path('api/prestamo/list-fecha/',ListarPrestamos.as_view()),
    path('api/prestamo/create/',RegistrarPrestamo.as_view()),
    path('api/devolucion/create/',RegistrarDevolucion.as_view()),
    path('api/estudiante/create/',RegistrarEstudiante.as_view()),
    path('api/estudiante/update/<pk>/',UpdateEstudiante.as_view())
]