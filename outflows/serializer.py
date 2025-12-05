from . import models
from rest_framework import serializers


class OutflowSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = models.Outflow
        fields = '__all__'