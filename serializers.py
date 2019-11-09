from rest_framework import serializers
from .models import Continent  # LANGUAGE_CHOICES, STYLE_CHOICES


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['name']
