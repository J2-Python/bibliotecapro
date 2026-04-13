from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import AutorSerializer, LibroSerializer, PaginationSerializer,EditorialSerializer
from .models import Autor, Libro,Editorial
from typing import cast

# Create your views here.

# Serializador


class ListaAutores(ListAPIView):
    # queryset=Autor.objects.all()

    # se asigna la referencia de la clase porque DRF la usara despues
    # Las configuraciones en drf se manejan usando referencias a clases
    serializer_class = AutorSerializer

    #!interceptamos la request
    def get(self, request, *args, **kwargs):
        print("*******")
        print(request)
        print(request.path)
        return self.list(request, *args, **kwargs)

    # sobreescribimos el metodo get_queryset
    def get_queryset(self):
        # query=Autor.objects.all()
        # query=Autor.objects.filter(country='España')
        return Autor.objects.listar_autores_pais("Colombia")
        # return super().get_queryset()


class FiltroAutores(ListAPIView):
    # queryset=Autor.objects.all()

    # se asigna la referencia de la clase porque DRF la usara despues
    # Las configuraciones en drf se manejan usando referencias a clases
    serializer_class = AutorSerializer

    # sobreescribimos el metodo get_queryset
    def get_queryset(self):
        edad = self.kwargs["edad"]
        pais = self.kwargs["pais"]

        print(f"{edad} - {pais}")
        return Autor.objects.listar_autores_pais(pais)
        # return super().get_queryset()


class LibrosPosteriores(ListAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        year = self.kwargs["year"]
        print(year)
        queryset = Libro.objects.lista_libros_posteriores(year)
        return queryset


class LibrosPorTitulo(ListAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        # kword request.query_params.get("titulo", "") da error de pylance
        request = cast(Request, self.request)
        kword = request.query_params.get("titulo", "")
        # kword = self.request.GET.get("titulo",'')
        print(kword)
        return Libro.objects.libros_por_titulos(kword)


class FiltrarLibros(ListAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        request = cast(Request, self.request)
        titulo = request.query_params.get("titulo", "")
        anio = request.query_params.get("anio", 1990)
        return Libro.objects.filtrar_libros(titulo, anio)


class LibrosAutor(ListAPIView):
    serializer_class = LibroSerializer
    # Paginar de 3 maximo 50 paginas
    pagination_class = PaginationSerializer

    def get_queryset(self, request: Request):
        # request = cast(Request, self.request)
        autor = request.query_params.get("autor_name", "")
        print(autor)
        page = request.query_params.get("page", "")
        return Libro.objects.por_autor(autor)


class DetailAutor(RetrieveAPIView):
    serializer_class = AutorSerializer

    # Se ejecuta para buscar los datos
    def get_queryset(self):
        return Autor.objects.filter(country="españa")

    # Para validar quien puede ver o definir como se puede mostrar la informacion
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SaludosPostman(APIView):
    # sobreescribimos el metodo get y post
    def get(self, request):
        print("Estamos en en el get")
        print(request)
        return Response({"status": "ok GET"})

    def post(self, request):
        print("Estamos en en el post")
        print(request)
        # request = cast(Request, request)
        print(request.data)
        print(request.data.get("nombres", ""))
        return Response({"status": "ok post"})

    # def delete(self,request):
    #    print("Estamos en en el delete")
    #    print(request)
    #    return Response({'status':'ok delete'})


class GuardarEditorial(APIView):
    
    def post(self, request):
        print("Estamos en en el post")
        print(request)
        # request = cast(Request, request)
        print(request.data)
        print(request.data.get("name", ""))
        name=request.data.get("name","")
        
        Editorial.objects.create(name=name)
        return Response({"status": "ok post"})
    
#grabar usando la vista generica CreateAPIView
class RegistrarEditorial(CreateAPIView):
    serializer_class=EditorialSerializer
    queryset=Editorial.objects.all()