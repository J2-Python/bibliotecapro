from django.urls import path
from .views import ListarPrestamos
#! este archivo tiene que ser referenciado en el archivo urls.py principal del proyecto que es el unico que reconoce python.
app_name='prestamo_app'
urlpatterns = [
    #definimos la ruta y llamamos a la vista ListaAutores
    path('api/prestamo/list-fecha',ListarPrestamos.as_view())
]