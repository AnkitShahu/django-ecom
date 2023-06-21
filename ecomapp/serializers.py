from rest_framework import routers, serializers, viewsets
from .models import ProductDetails, UserDetails, CartViews
from django.contrib.auth.models import User


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'

class CartViewSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartViews
        fields = '__all__'
        
class UserViewSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']