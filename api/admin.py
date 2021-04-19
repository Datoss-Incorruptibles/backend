from django.contrib import admin
from .models import Candidato, CandidatoMedio, OrganizacionPolitica


# Register your models here.
class CandidatoMedioAdmin(admin.ModelAdmin):
    fields = ('titulo', 'url','medio','imagen','tipo','fecha','jne_idhojavida')
    list_display = ('titulo', 'medio', 'tipo','jne_idhojavida','fecha')
    list_filter = ['fecha','jne_idhojavida']
    search_fields = ['titulo']



class OrganizacionPoliticaAdmin(admin.ModelAdmin):
    fields = ('nombre','electo')
    list_display = ('nombre','electo')


class CandidatoAdmin(admin.ModelAdmin):
    fields = ('electo',)
    list_display = ('jne_idhojavida','nombres','apellido_paterno','apellido_materno','electo')

admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(CandidatoMedio, CandidatoMedioAdmin)
admin.site.register(OrganizacionPolitica, OrganizacionPoliticaAdmin)
