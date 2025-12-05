from . import models
from rest_framework import serializers


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Supllier
        fields = '__all__'