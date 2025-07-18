from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, SMEProfileViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'smeprofiles', SMEProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
