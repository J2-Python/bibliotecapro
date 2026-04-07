from rest_framework import serializers
from .models import Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        #Serializamos el modelo Autor
        model=Autor
        #Especificamos los campos a serializar
        #fields=('name','last_name','country')
        fields=('__all__')
        