from django.urls import path, include
from . import views
from  ecomapp.views import ProductViewSet, UserViewSet, CartViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart-view', CartViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', views.home, name='home' ),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('login/', views.login_page, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_page, name="logout"),
    path('my-account/', views.my_account, name="my_account"),
    path('api/', include(router.urls)),
]
