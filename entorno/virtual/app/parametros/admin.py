from django.contrib import admin

# Register your models here.

from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import TipoEstu
from .models import TipoLogr
from .models import Empleos

class EtniaModelAdmin(admin.ModelAdmin):
    list_display = ["NombEtni"]
    search_fields = ["NombEtni"]
    list_filter =["NombEtni"]

    class Meta:
        model = Etnia
        
admin.site.register(Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(TipoEstu)
admin.site.register(TipoLogr)
admin.site.register(Empleos)