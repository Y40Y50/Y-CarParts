from django.contrib import admin
from django.urls import path
from cart.views import add_to_cart
from cart.views import cart_view
from products.views import (
    home,
    product_list,
    product_detail,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path(
        'products/',
        product_list,
        name='products'
    ),
    path(
        'products/<int:product_id>/',
        product_detail,
        name='product_detail'
    ),
    path(
        'cart/add/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),
    path(
        'cart/',
        cart_view,
        name='cart'
    ),
]

