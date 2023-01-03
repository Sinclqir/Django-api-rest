from rest_framework import viewsets
from api.serializers import ConcessionnaireSerializer
from api.serializers import VoitureSerializer
from .models import Concessionnaire
from .models import Voiture

class ConcessionnaireViewSet(viewsets.ModelViewSet):
    queryset = Concessionnaire.objects.all()
    serializer_class = ConcessionnaireSerializer

class VoitureViewSet(viewsets.ModelViewSet):
    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer