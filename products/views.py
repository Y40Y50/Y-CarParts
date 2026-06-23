from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Product, Category

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(
        request,
        'products/product_list.html',
        {
            'products': products,
            'categories': categories,
        }
    )

def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        pk=product_id
    )

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )

