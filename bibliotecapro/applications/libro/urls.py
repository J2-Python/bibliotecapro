from django.urls import path
from .views import ListaAutores
#! este archivo tiene que ser referenciado en el archivo urls.py principal del proyecto que es el unico que reconoce python.
app_name='libro_app'
urlpatterns = [
    #definimos la ruta y llamamos a la vista ListaAutores
    path('api/autor/list',ListaAutores.as_view())
]