from django.contrib import admin
from django.urls import path, include
from cart.views import add_to_cart
from cart.views import cart_view, remove_from_cart
from django.conf import settings
from django.conf.urls.static import static


from products.views import (
    home,
    product_list,
    product_detail,
)

from cart.views import (
    cart_view,
    add_to_cart,
    remove_from_cart,
    increase_quantity,
    decrease_quantity,
)

from checkout.views import (
    checkout,
    payment_success,
    payment_cancel,
    create_checkout_session,
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
    path(
        'cart/remove/<int:product_id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),
    path(
        'cart/increase/<int:product_id>/',
        increase_quantity,
        name='increase_quantity'
    ),

    path(
        'cart/decrease/<int:product_id>/',
        decrease_quantity,
        name='decrease_quantity'
    ),
    path(
        'checkout/',
        checkout,
        name='checkout'
    ),
    path('', include('django.contrib.auth.urls')),
    path('', include('profiles.urls')),

    path(
        'success/',
        payment_success,
        name='payment_success'
    ),

    path(
        'cancel/',
        payment_cancel,
        name='payment_cancel'
    ),
    path(
        'create-checkout-session/',
        create_checkout_session,
        name='create_checkout_session'
    ),

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATICFILES_DIRS[0]
    )