from datetime import datetime
from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Prestamo, Devolucion, Estudiante
from .serializers import PrestamoSerializer, DevolucionSerializer, EstudianteSerializer
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
            # Devolvemos el json con el mensaje de error personalizado
            raise ValidationError(
                {"error": "Datos no validos", "text": serializer.errors}
            )

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
    serializer_class = DevolucionSerializer
    queryset = Devolucion.objects.all()
    # antes de crear ejecuta el perform para obtener la fecha

    def handle_exception(self, exc):
        # si axc es unainstancia de ValidationError
        if isinstance(exc, ValidationError):
            print(exc.detail)
            # error_detail=exc.detail
            #! para que no de error error_detail.items(): mas abajo
            error_detail = cast(Mapping, exc.detail)
            errores_personalizados = {
                "required": "Este campo es requerido",
                "invalid": "El valor ingresado no es valido",
                "does_not_exist": "el objeto no existe",
            }
            response_data = {}
            for field, errors in error_detail.items():
                fields_erros = []
                for error in errors:
                    error_code = error.code
                    msj_error = errores_personalizados.get(error_code, str(error))
                    fields_erros.append(msj_error)
                response_data[field] = fields_erros
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        return super().handle_exception(exc)

    def perform_create(self, serializer):
        date = datetime.now().date()
        serializer.save(date=date)


class RegistrarEstudiante(CreateAPIView):
    serializer_class = EstudianteSerializer
    queryset = Estudiante.objects.all()


class UpdateEstudiante(UpdateAPIView):
    # para buscar por otro campo en lugar de <pk> se puede usar lookup_field=<id>
    # lookup_field='id'
    serializer_class = EstudianteSerializer
    queryset = Estudiante.objects.all()
    #! despues de validar los datos con el serializer al momento de recibir lso datos, se ejecuta el perform_update que es un metodo de la vista UpdateAPIView

    # def update(self, request, *args, **kwargs):
    #     #esto es redundante porque el metodo update del UpdateAPIVien ya sabe que se registro se esta consultando para actualizarce: get() es parte del manager del objeto estidiante 'pk' es lo que se envia desde la url como param
    #     #instance_estudiante=Estudiante.objects.get(id=self.kwargs['pk'])
    #     #! obtenemos el objeto que se esta actualizando
    #     instance_estudiante=self.get_object()
    #     print(instance_estudiante.name.upper())
    #     return super().update(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)

    #     serializer.vlidated_data['last_name']=serializer.validated['last_name'].upper()
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

    #! ejemplo de como restringir solo el uso de put
    def update(self, request, *args, **kwargs):
        # rechazamos patch
        if self.request.method == "PATCH":
            return Response(
                {"error": "Metodo no permitido"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().update(request, *args, **kwargs)

    def get_object(self):
        return super().get_object()

    def perform_update(self, serializer, *args, **kwargs):
        # cambiamos a mayuscula
        serializer.validated_data["name"] = serializer.validate_data["name"].upper()
        print(serializer.validated_data["name"])
        # serializer.save()
        return super().perform_update(serializer)
class DeleteDevolucion(DestroyAPIView):
    serializer_class=DevolucionSerializer
    #queryset=Devolucion.objects.all()
    lookup_field='pk'
    def get_queryset(self):
        #return super().get_queryset()
        return Devolucion.objects.all()
    def destroy(self, request, *args, **kwargs):
        #copiado desde https://www.cdrf.co/3.13/rest_framework.generics/DestroyAPIView.html
        instance = self.get_object()
        #imprime el usuario autenticado de djangoadmin
        print(request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
        #return super().destroy(request, *args, **kwargs)
    
    def perform_destroy(self, instance):
        print(instance.loan.student.name)
        return super().perform_destroy(instance)
    