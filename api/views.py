from rest_framework import viewsets,views, generics, mixins
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .serializers import ProcesoSerializer, CargoSerializer , \
    OrganizacionPoliticaSerializer , CandidatoSerializer, \
    UbigeoSerializer, OrgPolComboSerializer , \
    IndicadorCategoriaSerializer, IndicadorCategoriaOrganizacionSerializer, \
    CandidatoDetailSerializer
from .models import Proceso, Cargo , OrganizacionPolitica , Candidato, Ubigeo, \
IndicadorCategoria, IndicadorCategoriaOrganizacion
from rest_framework.response import Response


class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all().order_by('nombre')
    serializer_class = ProcesoSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all().order_by('cargo')
    serializer_class = CargoSerializer

class IndicadorCategoriaViewSet(viewsets.ModelViewSet):
    queryset = IndicadorCategoria.objects.all().order_by('order')
    serializer_class = IndicadorCategoriaSerializer

class IndicadorCategoriaOrganizacionViewSet(viewsets.ModelViewSet):
    queryset = IndicadorCategoriaOrganizacion.objects.filter(estado=1).order_by("indicador_id")
    serializer_class = IndicadorCategoriaOrganizacionSerializer
    
class UbigeoViewSet(viewsets.ModelViewSet):
    queryset = Ubigeo.objects.all()
    serializer_class = UbigeoSerializer

class OrgPolComboViewSet(viewsets.ModelViewSet):
    queryset = OrganizacionPolitica.objects.all()
    serializer_class = OrgPolComboSerializer
    
class OrganizacionPoliticaViewSet(viewsets.ModelViewSet):
    queryset = OrganizacionPolitica.objects.filter(estado=1).order_by('nombre')
    serializer_class = OrganizacionPoliticaSerializer
    def retrieve(self, request, pk=None):
        queryset = self.queryset
        org = get_object_or_404(queryset, pk=pk)
        serializer = OrganizacionPoliticaSerializer(org)
        return Response(serializer.data)

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

    
    def retrieve(self, request, pk=None):
        queryset = self.queryset
        candidato = get_object_or_404(queryset, pk=pk)
        serializer = CandidatoDetailSerializer(candidato)
        return Response(serializer.data)