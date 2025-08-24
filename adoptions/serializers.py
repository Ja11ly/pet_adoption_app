from rest_framework import serializers
from .models import AdoptionRequest

class AdoptionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionRequest
        fields = ['id', 'user', 'pet', 'status', 'request_date']
        read_only_fields = ['status', 'request_date', 'user']  # user is set automatically
