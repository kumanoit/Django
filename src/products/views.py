from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product_view(*args, **kwargs):
    return HttpResponse("<h1>Product View</h1>")