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
    filterset_fields = ['organizacion_politica_id']

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Candidato.objects.all().order_by('id')
        # queryset = Purchase.objects.all()
        # cargo = self.request.query_params.get('cargo', None)
        org_politica_id = self.request.query_params.get('org_politica_id', None)

        if org_politica_id is not None:
            queryset = queryset.filter(organizacion_politica_id=org_politica_id)
        return queryset
