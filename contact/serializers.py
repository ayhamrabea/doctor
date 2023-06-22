from .models import modelcontact
from rest_framework import serializers


class contact_seria(serializers.ModelSerializer):
    class Meta:
        model = modelcontact
        fields = '__all__'