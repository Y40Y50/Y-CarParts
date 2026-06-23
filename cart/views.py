from django.shortcuts import render
from django.shortcuts import redirect
from products.models import Product

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('products')

def cart_view(request):
    cart = request.session.get('cart', {})

    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)

        products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })

        total += product.price * quantity

    return render(
        request,
        'cart/cart.html',
        {
            'products': products,
            'total': total
        }
    )

def cart_count(request):
    cart = request.session.get('cart', {})

    count = sum(cart.values())

    return {
        'cart_count': count
    }