from django.contrib import admin

# Register your models here.
from .models import Estudiante,Prestamo,Devolucion
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display=('name','last_name','id')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display=('book','student','date')

#admin.site.register(Estudiante)
#admin.site.register(Prestamo)
admin.site.register(Devolucion)