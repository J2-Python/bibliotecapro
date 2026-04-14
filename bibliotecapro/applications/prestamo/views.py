from datetime import datetime
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView
from .models import Prestamo,Devolucion,Estudiante
from .serializers import PrestamoSerializer,DevolucionSerializer,EstudianteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from typing import cast
from collections.abc import Mapping
# Create your views here.


class ListarPrestamos(ListAPIView):
    serializer_class = PrestamoSerializer

    def get_queryset(self):
        return Prestamo.objects.listar_prestamo_fecha("2026-04-7")
        # return super().get_queryset()


class RegistrarPrestamo(CreateAPIView):
    serializer_class = PrestamoSerializer
    queryset = Prestamo.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        #! es util para depuriar
        if serializer.isvalid():
            print("========es valido '=====")
            #! solo se ejecuta el perfomr_create siempre y cuando el serializador is_valid=True
            self.perform_create(serializer)
        else:
            print("*******")
            print(serializer.errors)
            #Devolvemos el json con el mensaje de error personalizado
            raise ValidationError({"error":"Datos no validos","text":serializer.errors})
        
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    # antes de crear ejecuta el perform para obtener la fecha
    def perform_create(self, serializer):
        # now() solo tevuelve la fecha y hora
        # now().date() devuelve la fecha 2026-04-10
        date = datetime.now().date()
        # en serializer ya esta todo lo que envio en cliente en la peticion
        # guarda el dato que falta que en este caso es el campo date del modelo Prestamo
        serializer.save(date=date)

class RegistrarDevolucion(CreateAPIView):
    serializer_class=DevolucionSerializer
    queryset=Devolucion.objects.all()
     # antes de crear ejecuta el perform para obtener la fecha
     
    def handle_exception(self, exc):
        #si axc es unainstancia de ValidationError
        if isinstance(exc,ValidationError) :
            print(exc.detail)
            #error_detail=exc.detail
            #! para que no de error error_detail.items(): mas abajo
            error_detail = cast(Mapping, exc.detail)
            errores_personalizados={'required':'Este campo es requerido',
                                    'invalid':'El valor ingresado no es valido',
                                    'does_not_exist':'el objeto no existe'}
            response_data={}
            for field,errors in error_detail.items():
                fields_erros=[]
                for error in errors:
                    error_code=error.code
                    msj_error=errores_personalizados.get(error_code,str(error))
                    fields_erros.append(msj_error)
                response_data[field]=fields_erros
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)
                
        return super().handle_exception(exc)
    
    
    def perform_create(self, serializer):
        date = datetime.now().date()
        serializer.save(date=date)
        

class RegistrarEstudiante(CreateAPIView):
    serializer_class=EstudianteSerializer
    queryset=Estudiante.objects.all()

class UpdateEstudiante(UpdateAPIView):
    serializer_class=EstudianteSerializer
    queryset=Estudiante.objects.all()