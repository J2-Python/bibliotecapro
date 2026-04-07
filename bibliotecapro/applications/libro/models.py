from os import name
from tabnanny import verbose

from django.db import models

# Managers


class AutorManager(models.Manager):
    def listar_autores_pais(self, pais):
        return self.filter(country=pais)


# Create your models here.
class Autor(models.Model):
    name = models.CharField("Nombres", max_length=20)
    last_name = models.CharField("Apellidos", max_length=20)
    country = models.CharField("Pais", max_length=30)
    #! Objetos del modelo que se pueden utilizar conocidos como manager
    objects = AutorManager()

    class Meta:
        verbose_name = "Autor"  # Singular
        verbose_name_plural = "Autores"  # Plural

    # sobreescribimos el metodo __str__
    def __str__(self):
        return f"{self.name} {self.last_name}"


class Editorial(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

    # sobreescribimos el metodo __str__
    def __str__(self):
        return f"{self.name}"


class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    Editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    # campo opcional
    date = models.DateField(blank=True, null=True)
    # front
    front = models.ImageField("Portada", upload_to="libro", blank=True, null=True)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    # sobreescribimos el metodo __str__
    def __str__(self):
        return f"{self.titulo}"
