from django.shortcuts import render , redirect
from .models import Order, OrderItem
from menu.models import MenuItem
from django.http import JsonResponse
import json
from menu.models import MenuItem
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def add_to_cart(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    cart = request.session.get('cart', {})

    #print(item_id)
    item_id = str(item_id)

    if item_id in cart:
        cart[item_id]['quantity'] += 1
    else:
        cart[item_id] = {
            'name': item.name,
            'price': float(item.price),
            'quantity': 1,
            'image': item.img_url
        }


    request.session['cart'] = cart

    # calculate totals
    total_items = sum(i['quantity'] for i in cart.values())
    total_price = sum(i['price'] * i['quantity'] for i in cart.values())

    return JsonResponse({
        'cart': cart,
        'total_items': total_items,
        'total_price': total_price
    })

def get_cart(request):
    cart = request.session.get('cart', {})
    return JsonResponse(cart_response(cart))


def cart_response(cart):
    total_items = sum(i['quantity'] for i in cart.values())
    total_price = sum(i['price'] * i['quantity'] for i in cart.values())

    return {
        'cart': cart,
        'total_items': total_items,
        'total_price': total_price
    }

def increase_quantity(request, item_id):
    cart = request.session.get('cart', {})
    item_id = str(item_id)

    if item_id in cart:
        cart[item_id]['quantity'] += 1

    request.session['cart'] = cart
    return JsonResponse(cart_response(cart))

def decrease_quantity(request, item_id):
    cart = request.session.get('cart', {})
    item_id = str(item_id)

    if item_id in cart:
        cart[item_id]['quantity'] -= 1
        if cart[item_id]['quantity'] <= 0:
            del cart[item_id]

    request.session['cart'] = cart
    return JsonResponse(cart_response(cart))

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    item_id = str(item_id)

    if item_id in cart:
        del cart[item_id]

    request.session['cart'] = cart
    return JsonResponse(cart_response(cart))

def order_bill(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/bill.html', {'order': order})

def checkout_page(request):
    return render(request, 'orders/checkout.html')

@csrf_exempt
def checkout_confirm(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    cart = request.session.get('cart')
    if not cart:
        return JsonResponse({"error": "Cart empty"}, status=400)

    data = json.loads(request.body)

    customer_name = data.get("customer_name", "Guest")
    phone = data.get("phone", "")

    order = Order.objects.create(
        customer_name=customer_name,
        total_amount=0
    )

    total = 0
    for item in cart.values():
        OrderItem.objects.create(
            order=order,
            item_name=item['name'],
            price=item['price'],
            quantity=item['quantity']
        )
        total += item['price'] * item['quantity']

    order.total_amount = total
    order.save()

    request.session['cart'] = {}

    return JsonResponse({"order_id": order.id})
