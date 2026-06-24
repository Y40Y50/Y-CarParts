import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY
from django.shortcuts import render, redirect
from .models import Order
from django.http import JsonResponse

def checkout(request):

    if request.method == 'POST':

        Order.objects.create(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            total=0
        )

        return redirect('products')

    return render(
        request,
        'checkout/checkout.html'
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

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': 'Y-CarParts Order',
                    },
                    'unit_amount': 1000,
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel/',
    )

    return redirect(session.url)