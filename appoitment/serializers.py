from .models import Appoitment
from rest_framework import serializers


class Appoitment_seria(serializers.ModelSerializer):
    class Meta:
        model = Appoitment
        fields = '__all__'