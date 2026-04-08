from django.urls import path,register_converter
from .views import ListaAutores,FiltroAutores,LibrosPosteriores
from .converters import ValidYearsConvert
#! este archivo tiene que ser referenciado en el archivo urls.py principal del proyecto que es el unico que reconoce python.
app_name='libro_app'
class TwoDigitsNumber():
        regex='[0-9]+'
        def to_python(self,value):
            #convierte el valor que ingresaron a entero
            
            number=int(value)
            if number > 15:
                return number
            else:
                raise ValueError('error de numero')
            return value
        def to_url(self,value):
            return value
register_converter(TwoDigitsNumber,'nn')
register_converter(converters.ValidYearsConvert,'')
urlpatterns = [
    #definimos la ruta y llamamos a la vista ListaAutores
    path('api/autor/list',ListaAutores.as_view()),
    #path('api/autor/filter/<int:id>/',FiltroAutores.as_view())
    #path('api/autor/filter/<pais>/',FiltroAutores.as_view())
    path('api/autor/filter/<nn:edad>/<pais>',FiltroAutores.as_view()),
    path('api/libro/posteriores/<year>/',LibrosPosteriores.as_view())
    
]