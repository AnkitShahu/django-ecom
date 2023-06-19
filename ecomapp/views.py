from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get ('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, 'invail username')
            return redirect('/')
        
        user = User.objects.create(first_name = first_name, last_name= last_name, username= username)
        print(user)
        user.set_password(password)
        user.save()
        print('User Save')
    return render(request, 'register.html')