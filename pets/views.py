from django.shortcuts import render
from rest_framework import viewsets, permissions, filters 
from .models import Pet
from .serializers import PetSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['breed', 'location', 'availability']
    search_fields = ['name', 'species', 'breed']

    # Only admin can create/update/delete pets
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
