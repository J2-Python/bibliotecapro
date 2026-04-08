from rest_framework import serializers
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
        