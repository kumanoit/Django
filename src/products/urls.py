from django.urls import path

from products.views import (
    product_list_view,
    product_new_view,
    product_detail_view,
    product_creation_form,
    product_creation_html_form,
    product_creation_raw_django_form,
    product_creation_initial_form,
    get_product_details
)

app_name = 'products'
urlpatterns = [
    path('', product_list_view, name="product_home"),
    path('product_detail', product_detail_view, name="product_detail"),
    path('products/<product_id>/', get_product_details, name="product_detail"),
    path('new_product/', product_new_view, name="product_new_home"),
    path('create_product/', product_creation_form, name="product_creation_form"),
    path('create_product_html_form/', product_creation_html_form, name="product_creation_html_form"),
    path('create_product_raw_form/', product_creation_raw_django_form, name="product_creation_raw_django_form"),
    path('create_product_initial_form/', product_creation_initial_form, name="product_creation_initial_form"),
]
