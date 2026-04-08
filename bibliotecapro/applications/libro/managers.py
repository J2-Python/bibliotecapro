from django.db import models

# Managers


class AutorManager(models.Manager):
    def listar_autores_pais(self, pais):
        return self.filter(country=pais)


class LibroManager(models.Manager):
    def lista_libros_posteriores(self,year):
        return self.filter(
            date__year__gt=year
        )