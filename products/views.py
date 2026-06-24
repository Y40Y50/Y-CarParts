from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    selected_category = request.GET.get('category')
    search_query = request.GET.get('search')

    if selected_category:
        products = products.filter(
            category_id=selected_category
        )

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    return render(
        request,
        'products/product_list.html',
        {
            'products': products,
            'categories': categories,
            'selected_category': selected_category,
            'search_query': search_query,
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

