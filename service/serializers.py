from .models import service
from rest_framework import serializers


class service_seria(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = '__all__'