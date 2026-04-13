from django.urls import path, register_converter
from .views import (
    DetailAutor,
    ListaAutores,
    FiltroAutores,
    LibrosPosteriores,
    LibrosPorTitulo,
    FiltrarLibros,
    LibrosAutor,
    SaludosPostman,
    GuardarEditorial,
    RegistrarEditorial,
)
from .converters import ValidYearsConvert, TwoDigitsNumber

#! este archivo tiene que ser referenciado en el archivo urls.py principal del proyecto que es el unico que reconoce python.
app_name = "libro_app"

register_converter(TwoDigitsNumber, "nn")
register_converter(ValidYearsConvert, "yyyy")
urlpatterns = [
    # definimos la ruta y llamamos a la vista ListaAutores
    path("api/autor/list/", ListaAutores.as_view()),
    # path('api/autor/filter/<int:id>/',FiltroAutores.as_view())
    # path('api/autor/filter/<pais>/',FiltroAutores.as_view())
    path("api/autor/filter/<nn:edad>/<pais>/", FiltroAutores.as_view()),
    path("api/libro/posteriores/<yyyy:year>/", LibrosPosteriores.as_view()),
    path("api/libro/por-titulo/", LibrosPorTitulo.as_view()),
    path("api/libro/filtrar/", FiltrarLibros.as_view()),
    path("api/libro/por-autor/", LibrosAutor.as_view()),
    path("api/autor/detail/<pk>/", DetailAutor.as_view()),
    path("api/postman/", SaludosPostman.as_view()),
    path("api/editorial/save/", GuardarEditorial.as_view()),
    path("api/editorial/register/", RegistrarEditorial.as_view()),
]
