from rest_framework import viewsets,views, generics, mixins, filters
from django.db.models import Q, Count
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
    queryset = OrganizacionPolitica.objects.filter(estado=1).order_by('nombre')
    serializer_class = OrgPolComboSerializer
    
class OrganizacionPoliticaViewSet(viewsets.ModelViewSet):
    queryset = OrganizacionPolitica.objects.filter(estado=1)
    serializer_class = OrganizacionPoliticaSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['nombre', 'fundacion_fecha','sentencias']
    ordering = ['nombre']


    def get_queryset(self):
        queryset = self.queryset.annotate(sentencias=Count('indicadorescategoriaorg', \
            filter=(Q(indicadorescategoriaorg__indicador=8) | Q(indicadorescategoriaorg__indicador=9)))) 
        return queryset
    def retrieve(self, request, pk=None):
        queryset = self.queryset
        org = get_object_or_404(queryset, pk=pk)
        serializer = OrganizacionPoliticaSerializer(org)
        return Response(serializer.data)

class CandidatoViewSet(viewsets.ModelViewSet):
    
    queryset = Candidato.objects \
                .exclude(Q(jne_estado_lista='INADMISIBLE') | Q(jne_estado_lista='IMPROCEDENTE')) \
                .exclude(Q(jne_estado_expediente='INADMISIBLE') | Q(jne_estado_expediente='IMPROCEDENTE')) \
                .order_by('distrito_electoral','jne_organizacion_politica','jne_posicion')
    serializer_class = CandidatoSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['documento_identidad','apellido_paterno','apellido_materno','nombres']

    filterset_fields = ['organizacion_politica_id','region','ubigeo_postula']

    def get_queryset(self):
        queryset = self.queryset
        cargo_ids = self.request.query_params.get('cargo_ids', [])
        if cargo_ids:
            queryset = queryset.filter(cargo_id__in=cargo_ids.split(","))
        indicadores = self.request.query_params.get('indicador_ids', [])
        if indicadores:
            queryset = queryset.annotate(indicadores=Count('indicadores_categoria_candidato', \
                filter=(Q(indicadores_categoria_candidato__indicador__in=indicadores.split(","))))) \
                .filter(indicadores__gt=0)
    
        max_estudios = self.request.query_params.get('max_estudios_ids', [])
        if max_estudios:
            queryset = queryset.filter(nivel_estudio_id_max__in=max_estudios.split(","))
        return queryset

    
    def retrieve(self, request, pk=None):
        queryset = self.queryset
        candidato = get_object_or_404(queryset, pk=pk)
        serializer = CandidatoDetailSerializer(candidato)
        return Response(serializer.data)