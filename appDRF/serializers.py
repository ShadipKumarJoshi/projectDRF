from rest_framework import serializers
from .models import CustomUser, SMEProfile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'address']
        
class SMEProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMEProfile
        fields = '__all__'