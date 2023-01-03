from rest_framework import serializers
from .models import Concessionnaire

class ConcessionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = ['nom', 'code_postal']