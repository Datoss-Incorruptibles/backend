from rest_framework import viewsets

from .serializers import ProcesoSerializer, CargoSerializer, PartidoPoliticoSerializer
from .models import Proceso, Cargo, PartidoPolitico


class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all().order_by('nombre')
    serializer_class = ProcesoSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all().order_by('cargo')
    serializer_class = CargoSerializer


class PartidosPoliticosViewSet(viewsets.ModelViewSet):
    queryset = PartidoPolitico.objects.all().order_by('nombre')
    serializer_class = PartidoPoliticoSerializer
