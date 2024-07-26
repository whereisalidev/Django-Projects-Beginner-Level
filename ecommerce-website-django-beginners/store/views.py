from django.shortcuts import render
from .models import *
from django.http import HttpResponseBadRequest, JsonResponse
import json

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_items.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    product = Product.objects.all()
    return render(request, 'store/store.html', {'products': product, 'cartItems': cartItems})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_items.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    return render(request, 'store/cart.html', {'items': items, 'order': order, 'cartItems':cartItems})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_items.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']
    return render(request, 'store/checkout.html', {'items':items, 'order':order, 'cartItems': cartItems})


def updateItem(request):
    try:
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
    except KeyError as e:
        return HttpResponseBadRequest(f'Missing key: {e}')
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON')

    print('Action:', action)
    print('ProductId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    cartItems = order.get_cart_items
    return JsonResponse({'cartItems': cartItems}, safe=False)