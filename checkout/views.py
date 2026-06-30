import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY
from django.shortcuts import render, redirect
from .models import Order
from django.http import JsonResponse
from products.models import Product

def checkout(request):

    cart = request.session.get('cart', {})
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total += product.price * quantity

    if request.method == 'POST':

        Order.objects.create(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            total=total
        )

        return redirect('products')

    return render(
        request,
        'checkout/checkout.html',
        {'total': total}
    )

def payment_success(request):
    return render(
        request,
        'checkout/success.html'
    )


def payment_cancel(request):
    return render(
        request,
        'checkout/cancel.html'
    )

def create_checkout_session(request):
    cart = request.session.get('cart', {})

    line_items = []

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)

        line_items.append({
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100),
            },
            'quantity': quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )

    return redirect(session.url)