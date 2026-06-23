from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    return render(request, 'home.html')

def product_list(request):
    category_id = request.GET.get('category')

    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

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

