from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet
from . import views

router = DefaultRouter()
router.register(r'pets', PetViewSet, basename='pets')

urlpatterns = [
    path('', include(router.urls)),
]
