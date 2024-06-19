from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SweetViewSet, OrderViewSet, OrderStatusUpdateViewSet, UserRegistrationView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'sweets', SweetViewSet)
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-status', OrderStatusUpdateViewSet, basename='order-status')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
