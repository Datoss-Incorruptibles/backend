from rest_framework import viewsets

from .serializers import ProcesoSerializer, CargoSerializer , OrganizacionPoliticaSerializer, UbigeoSerializer
from .models import Proceso, Cargo , OrganizacionPolitica, Ubigeo


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

    
