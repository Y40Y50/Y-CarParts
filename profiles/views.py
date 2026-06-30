from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .forms import RegisterForm


def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()

    return render(
        request,
        'profiles/register.html',
        {'form': form}
    )

@login_required
def profile(request):

    orders = Order.objects.filter(
        email=request.user.email
    )

    return render(
        request,
        'profiles/profile.html',
        {
            'orders': orders
        }
    )