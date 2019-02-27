from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product_view(request, *args, **kwargs):
    return HttpResponse("<h1>Product View</h1>")

def product_new_view(request, *args, **kwargs):
    return render(request, "home.html", {})