from django.contrib import admin
from .models import Usuarios, Experiencia, Educacion, Habilidades, Experiencia, Logros
# Register your models here.

class UsuariosModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "IdUsuario", "ImagUsua", "EstaUsua")
    search_fields = ('IdUsuario','GeneUsua','CeluUsua', 'TeleUsua')
    list_filter = ('IdUsuario', 'GeneUsua')
    readonly_fields = ('RegiUsua')

    class Meta:
        model = Usuarios

admin.site.register(Usuarios, UsuariosModelAdmin)

class ExperienciaModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "CargExpe", "EmprExpe", "FechInic", "FechaFin", "SopoExpe")
    search_fields = ('CargExpe', 'EmprExpe')
    list_filter = ('CargExpe', 'FechaFin')
    readonly_fields = ('EstaExpt')

    class Meta:
        model = Experiencia

admin.site.register(Experiencia, ExperienciaModelAdmin)

class EducacionModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "TipoEstu", "TituloEst", "FechGrado", "Instituto", "SoporteEs")
    search_fields = ('TituloEst', 'TipoEstu')
    list_filter = ('TipoEstu', 'FechGrado')
    readonly_fields = ('EstaEstu')

    class Meta:
        model = Educacion

admin.site.register(Educacion, EducacionModelAdmin)

class LogrosModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "NombLogr", "FechLogr", "NombTiLo")
    search_fields = ('NombLogr', 'NombTiLo', 'FechLogr')
    list_filter = ('NombTiLo', 'FechLogr', 'NombLogr')

    class Meta:
        model = Logros

admin.site.register(Logros, LogrosModelAdmin)

class HabilidadesModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "NombHabil", "NiveHabil")
    search_fields = ('NombHabil', 'NiveHabil')
    list_filter = ('NiveHabil', 'NombHabil')

    class Meta:
        model = Habilidades

admin.site.register(Habilidades, HabilidadesModelAdmin)