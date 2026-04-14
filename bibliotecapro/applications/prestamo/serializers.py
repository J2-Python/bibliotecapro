from dataclasses import fields

from rest_framework import serializers
from .models import Estudiante, Prestamo, Devolucion


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        # fields=('__all__')
        #! para poder usar este serializer con la vista CreateAPIView es necesario especificar los campos y no __all__
        fields = ("book", "student", "description")


class DevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devolucion
        fields = "loan"


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ("dni", "name", "last_name", "date_birth")
