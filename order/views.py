from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Regular_Pizza, Shopping_Cart



# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    regular_pizza=Regular_Pizza.objects.all()
    shopping_cart=Shopping_Cart.objects.all()

    context = {
        "regular_pizza": regular_pizza,
        "shopping_cart":shopping_cart
            }
    return render(request, "users/user.html", context)

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            context = {
                "user": request.user

            }
            return render(request, "users/user.html", context)
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {'form': form})

def cart(request,item,price, category):
    print("hello1",item, price, category)
    cart=Shopping_Cart(user=request.user, item=item, price=price, category=category, status="initiated")
    cart.save();


    regular_pizza=Regular_Pizza.objects.all()
    shopping_cart=Shopping_Cart.objects.all()

    context = {
        "regular_pizza": regular_pizza,
        "shopping_cart":shopping_cart
            }
    return render(request, "users/user.html", context)
