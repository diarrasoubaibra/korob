from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_viewsets.artisan_viewset import ArtisanViewSet
from .api_viewsets.cart_viewset import CartViewSet
from .api_viewsets.cartItem_viewset import CartItemViewSet
from .api_viewsets.customer_viewset import CustomerViewSet 
from .api_viewsets.product_viewset import ProductViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'artisan', ArtisanViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
