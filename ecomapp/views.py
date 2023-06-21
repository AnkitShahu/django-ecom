from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import ProductDetails, UserDetails, CartViews
from .serializers import ProductSerializer, UserViewSerialize, CartViewSerialize,UserSerializer
from rest_framework import viewsets, generics
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    queryset = ProductDetails.objects.all()
    return render(request, 'index.html', {'products': queryset})

@login_required()
def my_account(request):
    return render(request, 'myaccount.html')

def cart(request):
    cart_products = request.session.get('cart', [])
    products = ProductDetails.objects.filter(product_id__in=cart_products)
    return render(request, 'cart.html', {'products': products})

def add_to_cart(request, product_id):
    cart_products = request.session.get('cart', [])
    cart_products.append(product_id)
    request.session['cart'] = cart_products
    messages.success(request, "Product is Successfully Added to Your Card Page!")
    return redirect('home')
    # messages.success(request, "please check card page")

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invaild Username')

        user = authenticate(username= username, password= password)

        if user is None:
            messages.error(request, 'Invalid Password')
        else: 
            login(request, user)
            #messages.success(request, "loginin")
            return redirect('my_account')

    return render(request, 'login.html')
    
def logout_page(request):
    logout(request)
    return redirect ('login')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, 'This User Name is Already Used! Please try Anther')
        else:
            user = User.objects.create(first_name = first_name, last_name= last_name, username= username, email=email)
            print(user)
            user.set_password(password)
            user.save()
            messages.success(request, "User is Successfully Register ! Please Login")
    return render(request, 'register.html')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductSerializer



class CartViewSet(viewsets.ModelViewSet):
    queryset = CartViews.objects.all()
    serializer_class = CartViewSerialize

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserViewSerialize
    
    
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
# class CompanyViewSet (viewsets. ModelViewSet):
# queryset= Company.objects.all()
# serializer_class=CompanySerializer
