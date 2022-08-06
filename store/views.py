from django.http import HttpResponseRedirect
from .forms import ProductForm, CategoryForm, ImageForm
from django.shortcuts import render, redirect
from .models import Product, Category, Image
from django.core.paginator import Paginator
from django.contrib import messages
#classview
#middleware section
#validate in form

def product_delete(request, product_id):
    product = Product.objects.filter(pk=product_id)
    product.delete()
    return redirect('/products')


def category_delete(request, category_id):
    category = Category.objects.filter(pk=category_id)
    category.delete()
    return redirect('/categories')


def product_update(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/products')

    return render(request, 'store/product_update.html',
                  {'product': product,
                   'form': form})


def category_update(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('/categories')

    return render(request, 'store/category_update.html',
                  {'category': category,
                   'form': form})


def all_products(request):
    product_list = Product.objects.all()
    #Set up paginator
    #p = Paginator(Product.objects.all(), 3)
    #page = request.GET.get('page')

    return render(request, 'store/product_list.html',
                      {'product_list': product_list})


def all_categories(request):
    category_list = Category.objects.filter(parent__isnull=True)
    return render(request, 'store/category_list.html',
                  {'category_list': category_list})


def product_show(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'store/product_show.html',
                  {'product': product})


def category_show(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'store/category_show.html',
                  {'category': category})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        files = request.FILES.getlist("image")
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            for i in files:
                Image.objects.create(product=f, image=i)
            messages.success(request, "Product was successfully created!!!!")
            return redirect('/products')
    else:
        form = ProductForm()
        imageform = ImageForm()

    return render(request, 'store/add_product.html',
                  {'form': form, 'imageform': imageform})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/categories')
    else:
        form = CategoryForm()

    return render(request, 'store/add_category.html',
                  {'form': form})