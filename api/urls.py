from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'procesos', views.ProcesoViewSet)
router.register(r'cargos', views.CargoViewSet)
router.register(r'organizacionpolitica', views.OrganizacionPoliticaViewSet)
router.register(r'candidato', views.CandidatoViewSet)
router.register(r'ubigeo', views.UbigeoViewSet)
router.register(r'orgpolcombo', views.OrgPolComboViewSet,basename='orgpolcombo')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('plan/<int:organizacion_politica_id>/<int:tipo_eleccion>/', views.OrganizacionPlanViewSet.as_view(), name='planes'),
    path('', include(router.urls)),
]