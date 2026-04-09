from rest_framework import serializers,pagination
from .models import Autor, Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        #Serializamos el modelo Autor
        model=Autor
        #Especificamos los campos a serializar
        #fields=('name','last_name','country')
        fields=('__all__')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Libro
        fields=('titulo','autor','date')
#serializador para paginar listas
class PaginationSerializer(pagination.PageNumberPagination) :
    page_size=3 #bloques
    max_page_size=50 #bloques en memoria