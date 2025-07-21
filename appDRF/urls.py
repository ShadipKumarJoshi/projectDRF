from django.urls import path
from django.conf import settings
from .views import (RegisterView, LogoutView, ChangePasswordView, UserProfileView, UserProfileEditView,
                    PasswordResetRequestView, SetNewPasswordView
                    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/edit/', UserProfileEditView.as_view(), name='edit-profile'),
    path('auth/request-reset-password/', PasswordResetRequestView.as_view(), name='request-reset-password'),
    path('auth/reset-password-confirm/', SetNewPasswordView.as_view(), name='reset-password-confirm'),
]

