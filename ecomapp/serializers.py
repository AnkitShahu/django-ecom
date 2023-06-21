from rest_framework import routers, serializers, viewsets
from .models import ProductDetails
from django.contrib.auth.models import User


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'

# class CartViewSerialize(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CartView
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']