from django.contrib import admin
from .models import Autor, Libro, Editorial


# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor")


admin.site.register(Autor)
# admin.site.register(Libro)
admin.site.register(Editorial)
