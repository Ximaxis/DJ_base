from django.shortcuts import render, get_object_or_404
from django.conf import settings
import datetime
from .models import ProductCategory, Products
from basketapp.models import Basket

# Create your views here.


def main(request):
    title = "Главная"
    visit_date = datetime.datetime.now()
    products = Products.objects.all()[:5]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {"title": title, "visit_date": visit_date, 'products': products, "basket": basket}

    return render(request, 'mainapp/index.html', content)


def products(request, slug):
    title = "Страница товара"
    same_products = Products.objects.all()
    get_product = get_object_or_404(Products, slug=slug)
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        "title": title,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        "get_product": get_product,
        "basket": basket,
    }
    return render(request, 'mainapp/product-single.html', content)


def contacts(request):
    title = "Контактные данные"
    content = {"title": title}
    return render(request, 'mainapp/contact.html', content)


def blogsingle(request):
    title = "Запись в блоге"
    content = {"title": title}
    return render(request, 'mainapp/blog-single.html', content)


def blog(request):
    title = "Блог"
    content = {"title": title}
    return render(request, 'mainapp/blog.html', content)


def shop(request):
    title = "Каталог товаров"
    products = Products.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {"title": title, 'products': products, 'basket': basket}
    return render(request, 'mainapp/shop.html', content)


def checkout(request):
    title = "Хз как назвать"
    content = {"title": title}
    return render(request, 'mainapp/checkout.html', content)


def about(request):
    title = "О нас"
    content = {"title": title}
    return render(request, 'mainapp/about.html', content)


