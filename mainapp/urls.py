from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='main'),

    path('shop/products', products, name='products'),
    path('contacts', contacts, name='contacts'),
    path('blog/blogsingle', blogsingle, name='blogsingle'),
    path('blog', blog, name='blog'),
    path('cart', cart, name='cart'),
    path('about', about, name='about'),
    path('shop', shop, name='shop'),
    path('checkout', about, name='checkout'),
]