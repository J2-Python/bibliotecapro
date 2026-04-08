from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import AutorSerializer,LibroSerializer
from .models import Autor,Libro
# Create your views here.

#Serializador

class ListaAutores(ListAPIView):
    #queryset=Autor.objects.all()
    
    #se asigna la referencia de la clase porque DRF la usara despues
    #Las configuraciones en drf se manejan usando referencias a clases
    serializer_class=AutorSerializer
    
    #!interceptamos la request
    def get(self,request,*args,**kwargs):
        print('*******')
        print(request)
        print(request.path)
        return self.list(request,*args,**kwargs)
    
    
    #sobreescribimos el metodo get_queryset
    def get_queryset(self):
        #query=Autor.objects.all()
        #query=Autor.objects.filter(country='España')
        return Autor.objects.listar_autores_pais('Colombia')
        #return super().get_queryset()
        
class FiltroAutores(ListAPIView):
    #queryset=Autor.objects.all()
    
    #se asigna la referencia de la clase porque DRF la usara despues
    #Las configuraciones en drf se manejan usando referencias a clases
    serializer_class=AutorSerializer
    
    #sobreescribimos el metodo get_queryset
    def get_queryset(self):
        edad=self.kwargs['edad']
        pais=self.kwargs['pais']
        
        print(f"{edad} - {pais}")
        return Autor.objects.listar_autores_pais(pais)
        #return super().get_queryset()

class LibrosPosteriores(ListAPIView):
    serializer_class=LibroSerializer
    
    def get_queryset(self):
        year=self.kwargs['year']
        queryset=Libro.objects.lista_libros_posteriores(year)
        return queryset