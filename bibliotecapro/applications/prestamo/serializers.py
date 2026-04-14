from dataclasses import fields

from rest_framework import serializers
from .models import Estudiante, Prestamo, Devolucion


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        # fields=('__all__')
        #! para poder usar este serializer con la vista CreateAPIView es necesario especificar los campos y no __all__
        fields = ("book", "student", "description")




class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        #! django sabe que a pesar de que id (campo automatico) esta especificado en el serializador, este no es requerido al momento del create.
        fields = ("id","dni", "name", "last_name", "date_birth")

class DevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Devolucion
        fields=('id','loan',)