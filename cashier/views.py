from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from orders.models import Order 
from menu.models import MenuItem


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
    
    panding_orders = Order.objects.filter(status="PENDING").count()
    total_menu = MenuItem.objects.count()
    
    return render(request,"cashier/dashboard.html",
                {"panding_orders":panding_orders,"total_menu":total_menu}
                )

def cashier_logout(request):
    logout(request)
    return redirect("cashier_login")
    

def cashier_order_detail(request, order_id):
    if not request.user.groups.filter(name="Cashier").exists():
        return redirect("/")

    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        order.status = "COMPLETED"
        order.save()
        return redirect("cashier_dashboard")

    return render(request, "cashier/order_detail.html", {
        "order": order
    })

