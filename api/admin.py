from django.contrib import admin
from .models import CandidatoMedio


# Register your models here.
class CandidatoMedioAdmin(admin.ModelAdmin):
    fields = ('titulo', 'url','medio','tipo','fecha','jne_idhojavida')

admin.site.register(CandidatoMedio, CandidatoMedioAdmin)