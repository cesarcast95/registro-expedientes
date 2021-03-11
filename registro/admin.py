from django.contrib import admin
from .models import Expediente
# Register your models here.


class ExpedienteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo',
                    'numero_folio', 'user')
    list_filter = ['user', 'created']
    search_fields = ['codigo',]

admin.site.register(Expediente, ExpedienteAdmin)
