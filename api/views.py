from rest_framework import viewsets

from .serializers import ProcesoSerializer, CargoSerializer , OrganizacionPoliticaSerializer
from .models import Proceso, Cargo , OrganizacionPolitica


class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all().order_by('nombre')
    serializer_class = ProcesoSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all().order_by('cargo')
    serializer_class = CargoSerializer


class OrganizacionPoliticaViewSet(viewsets.ModelViewSet):
    queryset = OrganizacionPolitica.objects.all().order_by('id')
    serializer_class = OrganizacionPoliticaSerializer

    