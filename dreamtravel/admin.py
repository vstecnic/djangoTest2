from django.contrib import admin
from .models import Aerolinea, Categorias, Destinos, Localidad, MetodoPago, ObraSocial, Usuario

# Register your models here.

class AerolineaAdmin(admin.ModelAdmin):
    list_display = ('id_aerolinea', 'nombreaerolinea',)

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombrecategoria',)

admin.site.register(Aerolinea)
admin.site.register(Categorias)
admin.site.register(Destinos)
admin.site.register(Localidad)
admin.site.register(MetodoPago)
admin.site.register(ObraSocial)
admin.site.register(Usuario)
