from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product, RawProductForm

from .forms import ProductForm

def product_view(request, *args, **kwargs):
    return HttpResponse("<h1>Product View</h1>")

def product_detail_view(request):
    product = Product.objects.get(id = 1)
    context = {
        'product': product
    }
    return render(request, "products/product_detail.html", context)

def product_new_view(request, *args, **kwargs):
    context = {
        "name": "Kumanoit",
        "title": "Software Engineer",
        "vehicles": ['Royal Enfield', "Lamborghini", "Audi", 2343],
    }
    return render(request, "home.html", context)

def product_creation_form(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'products/create.html', context)

def product_creation_html_form(request):
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_price = request.POST.get('price')
        new_summary = request.POST.get('summary')
        Product.objects.create(title = new_title, description = new_description,
                               price = new_price, summary = new_summary)
    context = {}
    return render(request, "products/create_html_form.html", context)

def product_creation_raw_django_form(request):
    if request.method == "POST":
        form = RawProductForm(request.POST)
        Product.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            price=request.POST.get("price")
        )
    form = RawProductForm(request.GET)
    context = {
        'form' : form
    }
    return render(request, "products/create_product_raw_form.html", context)

