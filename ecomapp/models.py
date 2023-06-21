from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductDetails(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_image1 = models.ImageField(upload_to='product_images/', blank=True)
    product_image2 = models.ImageField(upload_to='product_images/', blank=True)
    product_image3 = models.ImageField(upload_to='product_images/', blank=True)
    product_name = models.CharField(max_length=100, blank=True)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField()
    product_details = models.TextField(blank=True)
    
    def __str__(self):
        return self.product_name

class UserDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)


# class CartView(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
    
class CartViews(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)