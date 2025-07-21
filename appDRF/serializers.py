from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str, smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

# ------------------------------
# Register
# ------------------------------

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user


# ------------------------------
# Profile
# ------------------------------
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'profile_picture']
        read_only_fields = ['id', 'username', 'email'] 

# ------------------------------
# Password Reset
# ------------------------------

User = get_user_model()


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            uid = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_link = f"http://127.0.0.1:8000/api/auth/reset-password-confirm/{uid}/{token}/"  
            send_mail(
                subject="Reset Your Password",
                message=f"Click the link to reset your password: {reset_link}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[value],
                fail_silently=False,
            )
        except User.DoesNotExist:
            pass 
        return value


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=6)
    token = serializers.CharField(write_only=True)
    uid = serializers.CharField(write_only=True)

    def validate(self, attrs):
        try:
            uid = smart_str(urlsafe_base64_decode(attrs['uid']))
            user = User.objects.get(id=uid)
            if not PasswordResetTokenGenerator().check_token(user, attrs['token']):
                raise serializers.ValidationError("Token is invalid or expired")
            user.set_password(attrs['password'])
            user.save()
            return attrs
        except (User.DoesNotExist, DjangoUnicodeDecodeError):
            raise serializers.ValidationError("Invalid UID or token")
