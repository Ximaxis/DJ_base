from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from .models import Basket
from mainapp.models import Products


def basket(request):
    title = "Корзина"
    content = {"title": title}
    return render(request, 'mainapp/cart.html', content)


def basket_add(request, slug):
    product = get_object_or_404(Products, slug=slug)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_remove(request):
    content = {}
    return render(request, "mainapp/cart.html", content)
