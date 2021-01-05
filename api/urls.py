from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'procesos', views.ProcesoViewSet)
router.register(r'cargos', views.CargoViewSet)
router.register(r'organizacionpolitica', views.OrganizacionPoliticaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]