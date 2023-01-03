from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from api.views import ConcessionnaireViewSet
from api.views import VoitureViewSet

router = routers.SimpleRouter()

concessionnaireRouter = routers.NestedSimpleRouter(router, r'concessionnaire', lookup='concessionnaire')
concessionnaireRouter.register(r'voiture', VoitureViewSet ,basename='concessionnaire_voiture')

router.register(r'concessionnaire', ConcessionnaireViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(r'', include(concessionnaireRouter.urls))
]