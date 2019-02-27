"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products.views import product_list_view, product_new_view, product_detail_view, product_creation_form
from products.views import product_creation_html_form, product_creation_raw_django_form
from products.views import product_creation_initial_form, get_product_details


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_list_view, name="product_home"),
    path('product_detail', product_detail_view, name="product_detail"),
    path('products/<product_id>/', get_product_details, name="product_detail"),
    path('new_product/', product_new_view, name="product_new_home"),
    path('create_product/', product_creation_form, name="product_creation_form"),
    path('create_product_html_form/', product_creation_html_form, name="product_creation_html_form"),
    path('create_product_raw_form/', product_creation_raw_django_form, name="product_creation_raw_django_form"),
    path('create_product_initial_form/', product_creation_initial_form, name="product_creation_initial_form"),
]
