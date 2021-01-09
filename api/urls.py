from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'procesos', views.ProcesoViewSet)
router.register(r'cargos', views.CargoViewSet)
router.register(r'organizacionpolitica', views.OrganizacionPoliticaViewSet)
<<<<<<< HEAD
router.register(r'organizacionpolitica/{pk}/$', views.OrganizacionPoliticaDetailViewSet)
# candidato?cargo=x&orgpoli=Y traer la info por query params
router.register(r'candidato', views.CandidatoViewSet)
router.register(r'candidato/{pk}/$', views.CandidatoViewSet)

=======
router.register(r'ubigeo', views.UbigeoViewSet)
>>>>>>> master

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]