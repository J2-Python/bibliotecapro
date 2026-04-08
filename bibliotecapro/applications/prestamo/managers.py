from django.db import models

class PrestamoManager(models.Manager):
    def listar_prestamo_fecha(self,fecha):
        #date__lte  el campo dates es menor o igual a 
        return self.filter(date__lte=fecha,)