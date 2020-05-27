from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.urls import reverse
import datetime
from adminapp.forms import ProductCategoryEditForm, ShopUserAdminEditForm
from authnapp.forms import ShopUserRegisterForm
from authnapp.models import ShopUser
from mainapp.models import Products, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def admin_main(request):
    response = redirect("my_admin:users")
    return response


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = "Admin/Users"
    users_list = ShopUser.objects.all().order_by("-is_active", "-is_superuser", "-is_staff", "username")
    content = {"title": title, "objects": users_list, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/users.html", content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = "Users/создание"

    if request.method == "POST":
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("my_admin:users"))
    else:
        user_form = ShopUserRegisterForm()

    content = {"title": title, "update_form": user_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/user_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = "Users/редактирование"

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("my_admin:user_update", args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {"title": title, "update_form": edit_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/user_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = "Users/DELETE"

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == "POST":
        # user.delete()
        # Instead delete we will set users inactive
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse("my_admin:users"))

    content = {"title": title, "user_to_delete": user, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/user_delete.html", content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = "Admin/Category"
    categories_list = ProductCategory.objects.all()
    content = {"title": title, "objects": categories_list, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/categories.html", content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = "Category/создание"

    if request.method == "POST":
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse("my_admin:categories"))
    else:
        category_form = ProductCategoryEditForm()

    content = {"title": title, "update_form": category_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/category_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, slug):
    title = "Category/редактирование"

    edit_category = get_object_or_404(ProductCategory, slug=slug)
    if request.method == "POST":
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("my_admin:category_update", args=[edit_category.slug]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {"title": title, "update_form": edit_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/category_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, slug):
    title = "Category/Delete"

    category = get_object_or_404(ProductCategory, slug=slug)

    if request.method == "POST":
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse("my_admin:categories"))

    content = {"title": title, "category_to_delete": category, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/category_delete.html", content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, slug):
    title = "Admin/Product"
    category = get_object_or_404(ProductCategory, slug=slug)
    products_list = Products.objects.filter(category__slug=slug).order_by("slug")
    content = {"title": title, "category": category, "objects": products_list, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/products.html", content)


def product_create(request, slug):
    response = redirect("my_admin:categories")
    return response


def product_read(request, slug):
    response = redirect("my_admin:categories")
    return response


def product_update(request, slug):
    response = redirect("my_admin:categories")
    return response


def product_delete(request, slug):
    response = redirect("my_admin:categories")
    return response