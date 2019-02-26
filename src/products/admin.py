from django.contrib import admin
from .models import Product

# Register your models here.
# registering product app so that it is visible on UI
admin.site.register(Product)