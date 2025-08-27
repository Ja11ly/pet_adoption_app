from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Review
from .serializers import ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["rating", "pet", "user"]
    ordering_fields = ["created_at", "rating"]
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

