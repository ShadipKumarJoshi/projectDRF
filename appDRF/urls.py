from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, SMEProfileViewSet, LogoutView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'smeprofiles', SMEProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', LogoutView.as_view(), name='logout'),
]
