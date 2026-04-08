from django.db import models

# Managers


class AutorManager(models.Manager):
    def listar_autores_pais(self, pais):
        return self.filter(country=pais)