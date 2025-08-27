from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import AdoptionRequest
from .serializers import AdoptionRequestSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class AdoptionRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AdoptionRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = AdoptionRequest.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["status", "user", "pet"]
    ordering_fields = ["request_date"]
    ordering = ["-request_date"]

    def get_queryset(self):
        # Admins see all, users see their own
        user = self.request.user
        if user.is_staff:
            return AdoptionRequest.objects.all()
        return AdoptionRequest.objects.filter(user=user)

    def perform_create(self, serializer):
        # Save with logged-in user
        serializer.save(user=self.request.user)
