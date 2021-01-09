from rest_framework import viewsets,views, generics, mixins
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProcesoSerializer, CargoSerializer , \
    OrganizacionPoliticaSerializer , CandidatoSerializer, UbigeoSerializer
from .models import Proceso, Cargo , OrganizacionPolitica , Candidato, Ubigeo


class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all().order_by('nombre')
    serializer_class = ProcesoSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all().order_by('cargo')
    serializer_class = CargoSerializer


class UbigeoViewSet(viewsets.ModelViewSet):
    queryset = Ubigeo.objects.all()
    serializer_class = UbigeoSerializer
class OrganizacionPoliticaViewSet(viewsets.ModelViewSet):
    queryset = OrganizacionPolitica.objects.all().order_by('id')
    serializer_class = OrganizacionPoliticaSerializer

    
class OrganizacionPoliticaDetailViewSet(viewsets.ModelViewSet):
    queryset = OrganizacionPolitica.objects.all().order_by('id')
    serializer_class = OrganizacionPoliticaSerializer


class CandidatoViewSet(viewsets.ModelViewSet):

    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organizacion_politica_id','region']

    def get_queryset(self):
        queryset = self.queryset
        cargo_ids = self.request.query_params.get('cargo_ids', [])
        if cargo_ids:
            queryset = queryset.filter(cargo_id__in=cargo_ids.split(","))
        return queryset