from rest_framework import serializers
from .models import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        # fields=('__all__')
        #! para poder usar este serializer con la vista CreateAPIView es necesario especificar los campos y no __all__
        fields = ("book", "student", "description")
