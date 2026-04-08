from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import AutorSerializer
from .models import Autor
# Create your views here.

#Serializador

class ListaAutores(ListAPIView):
    #queryset=Autor.objects.all()
    
    #se asigna la referencia de la clase porque DRF la usara despues
    #Las configuraciones en drf se manejan usando referencias a clases
    serializer_class=AutorSerializer
    
    #sobreescribimos el metodo get_queryset
    def get_queryset(self):
        #query=Autor.objects.all()
        #query=Autor.objects.filter(country='España')
        return Autor.objects.listar_autores_pais('Colombia')
        #return super().get_queryset()
