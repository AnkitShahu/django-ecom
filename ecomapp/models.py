from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductDetails(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    

    
# class CartView(models.Model):
#     user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)