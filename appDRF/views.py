from rest_framework import viewsets
from .models import CustomUser, SMEProfile
from .serializers import CustomUserSerializer, SMEProfileSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    

class SMEProfileViewSet(viewsets.ModelViewSet):
    queryset = SMEProfile.objects.all()
    serializer_class = SMEProfileSerializer