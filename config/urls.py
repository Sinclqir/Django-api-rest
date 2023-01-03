"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from api.views import ConcessionnaireViewSet
from api.views import VoitureViewSet


router = routers.SimpleRouter()
router.register(r'concessionnaire', ConcessionnaireViewSet)

concessionnaireRouter = routers.NestedSimpleRouter(router, r'concessionnaire', lookup='concessionnaire')
concessionnaireRouter.register(r'voitures', VoitureViewSet, basename='concessionnaire_voiture')

concessionnaireRouter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(r'', include(concessionnaireRouter.urls)),
]