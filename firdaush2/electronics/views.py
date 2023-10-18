from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from electronics.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *

from django.contrib.auth import login as auth_login

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == "POST": 
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username invalid ! Please try some other username.")
            return redirect('login')
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.error(request, "password invalid ! Please try some other username.")
            return redirect('login')
        
        else:
            auth_login(request, user)
            messages.error(request, "User logged in .")
            return redirect('home')

    return render(request, 'login.html')

@login_required(login_url="login")
def home(request):
    return render(request,'home.html')

@login_required(login_url="login")
def about(request):
    return render(request,'about.html')

@login_required(login_url="login")

def product(request):
    return render(request,'product.html')

@login_required(login_url="login")

def deal(request):
    return render(request,'topdeals.html')


def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact( email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def register(request):
    if request.method == "POST":     
    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        
        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some other username")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register')
        

        user = User.objects.create(
            email = email,
            username = username,
            first_name=fname,
            last_name=lname,
        )
        user.set_password(password)
        user.save()

        messages.success(request, "Your Account has been created succesfully!!.Login Now.")
        
        
        return redirect('login')
    
    return render(request, 'register.html')







def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')