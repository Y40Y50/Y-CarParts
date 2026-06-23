from django.shortcuts import render, redirect
from .models import Order

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