from django.urls import path
from .views import *
from django.conf.urls import url


urlpatterns = [
    path('', main, name='main'),

    path('shop/<slug:slug>/', products, name='products'),
    path('contacts', contacts, name='contacts'),
    path('blog/blogsingle', blogsingle, name='blogsingle'),
    path('blog', blog, name='blog'),
    path('about', about, name='about'),
    path('shop/', shop, name='shop'),
    path('shop/category/<int:pk>/', shop, name='category'),
    path('shop/category/<int:pk>/page/<int:page>/', shop, name='page'),
    # path('shop/category/page/<int:page>/', shop, name='page'),
    path('checkout', about, name='checkout'),
]