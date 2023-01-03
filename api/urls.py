from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from VoitureViewSet import viewsets as voiture_viewsets
from concessionnaire import viewsets as concessionnaire_viewsets

router = DefaultRouter()
router.register(r'voiture', voiture_viewsets.VoitureViewSet)
router.register(r'concessionnaire', concessionnaire_viewsets.ConcessionnaireViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]