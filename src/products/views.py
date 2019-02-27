from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product

from .forms import ProductForm, RawProductForm

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
        if form.is_valid():
            Product.objects.create(
                **form.cleaned_data
            )
        else:
            print(form.errors)
    form = RawProductForm(request.GET)
    context = {
        'form' : form
    }
    return render(request, "products/create_product_raw_form.html", context)

# to create product with default initial
def product_creation_initial_form(request):
    initial_data = {
        "title":"This is default title"
    }
    form = ProductForm(request.POST or None, initial = initial_data)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, "products/create_product_initial_data.html", context)

def get_product_details(request, product_id):
    try:
        object = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "product": object
    }
    return render(request, "products/product_detail.html", context)

## to return list of products
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "product_list": queryset
    }
    return render(request, "products/product_list.html", context)