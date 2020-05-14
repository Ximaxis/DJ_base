from django.shortcuts import render
import datetime
from .models import ProductCategory, Products

# Create your views here.


def main(request):
    title = "Главная"
    visit_date = datetime.datetime.now()
    products = Products.objects.all()[:4]
    content = {"title": title, "visit_date": visit_date, 'products': products}

    return render(request, 'mainapp/index.html', content)


def products(request):
    title = "Страница товара"
    content = {"title": title}
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


def cart(request):
    title = "Корзина"
    content = {"title": title}
    return render(request, 'mainapp/cart.html', content)


def shop(request):
    title = "Каталог товаров"
    content = {"title": title}
    return render(request, 'mainapp/shop.html', content)


def checkout(request):
    title = "Хз как назвать"
    content = {"title": title}
    return render(request, 'mainapp/checkout.html', content)


def about(request):
    title = "О нас"
    content = {"title": title}
    return render(request, 'mainapp/about.html', content)


