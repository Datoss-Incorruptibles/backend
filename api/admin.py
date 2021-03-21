from django.contrib import admin
from .models import CandidatoMedio


# Register your models here.
class CandidatoMedioAdmin(admin.ModelAdmin):
    fields = ('titulo', 'url','medio','tipo','fecha','jne_idhojavida')
    list_display = ('titulo', 'medio', 'tipo','jne_idhojavida','fecha')
    list_filter = ['fecha','jne_idhojavida']
    search_fields = ['titulo']

admin.site.register(CandidatoMedio, CandidatoMedioAdmin)