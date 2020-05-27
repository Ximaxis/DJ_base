from django.urls import path

import adminapp.views as adminapp

from .apps import AdminappConfig

app_name = AdminappConfig.name

urlpatterns = [
    path("", adminapp.admin_main, name="admin_main"),
    path("users/create/", adminapp.user_create, name="user_create"),
    path("users/read/", adminapp.users, name="users"),
    path("users/update/<int:pk>/", adminapp.user_update, name="user_update"),
    path("users/delete/<int:pk>/", adminapp.user_delete, name="user_delete"),
    path("categories/create/", adminapp.category_create, name="category_create"),
    path("categories/read/", adminapp.categories, name="categories"),
    path("categories/update/<slug:slug>/", adminapp.category_update, name="category_update"),
    path("categories/delete/<slug:slug>/", adminapp.category_delete, name="category_delete"),
    path("products/create/category/<slug:slug>/", adminapp.product_create, name="product_create"),
    path("products/read/category/<slug:slug>/", adminapp.products, name="products"),
    path("products/read/<slug:slug>/", adminapp.product_read, name="product_read"),
    path("products/update/<slug:slug>/", adminapp.product_update, name="product_update"),
    path("products/delete/<slug:slug>/", adminapp.product_delete, name="product_delete"),
]