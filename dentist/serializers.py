from .models import doctor
from rest_framework import serializers


class dentist_seria(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = '__all__'