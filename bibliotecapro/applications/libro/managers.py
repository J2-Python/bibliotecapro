from turtle import title

from django.db import models

# Managers


class AutorManager(models.Manager):
    def listar_autores_pais(self, pais):
        return self.filter(country=pais)


class LibroManager(models.Manager):
    def lista_libros_posteriores(self, year):
        #__year significa solo el anio en la fecha o sea 20260408 -> 2026
        return self.filter(date__year__gt=year)

    def libros_por_titulos(self, kword):
        return self.filter(titulo__icontains=kword).order_by("titulo")

    def filtrar_libros(self, titulo, anio):
        #__year significa solo el anio en la fecha o sea 20260408 -> 2026
        return self.filter(titulo__icontains=titulo, date__year__gt=anio).order_by(
            "titulo"
        )
