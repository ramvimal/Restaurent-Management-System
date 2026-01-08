from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from orders.models import Order


def cashier_login(request):
    if request.method == "POST":  
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user and user.groups.filter(name="Cashier").exists():
            print("success")
            login(request, user)
            return redirect("cashier_dashboard")

        return render(request, "cashier/login.html", {
            "error": "Invalid credentials or not a cashier"
        })

    return render(request, "cashier/login.html")


def cashier_dashboard(request):
    if not request.user.groups.filter(name="Cashier").exists():
        return redirect("cashier_login")
    return render(request,"cashier/dashboard.html")
    

def cashier_logout(request):
    logout(request)
    return redirect("cashier_login")
    

