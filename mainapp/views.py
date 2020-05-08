from django.shortcuts import render
import datetime

# Create your views here.


def main(request):
    title = "Главная"
    visit_date = datetime.datetime.now()
    content = {"title": title, "visit_date": visit_date}
    return render(request, 'mainapp/index.html', content)


def products(request):
    return render(request, 'mainapp/product-single.html')


def contacts(request):
    return render(request, 'mainapp/contact.html')


def blogsingle(request):
    return render(request, 'mainapp/blog-single.html')


def blog(request):
    return render(request, 'mainapp/blog.html')


def cart(request):
    return render(request, 'mainapp/cart.html')


def about(request):
    return render(request, 'mainapp/about.html')


