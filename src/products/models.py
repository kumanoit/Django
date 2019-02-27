from django.db import models
# Create your models here.
from django import forms

class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    summary = models.TextField(default="summay not given")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()