from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Prestamo
from .serializers import PrestamoSerializer
# Create your views here.

class ListarPrestamos(ListAPIView):
    serializer_class=PrestamoSerializer
    
    def get_queryset(self):
        return Prestamo.objects.listar_prestamo_fecha('2026-04-7')
        #return super().get_queryset()