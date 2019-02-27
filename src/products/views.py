from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product

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