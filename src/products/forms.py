from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    # def clean_<variable name>
    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price > 5:
            return price
        else:
            raise forms.ValidationError("Raise price so that it should be above 5")


class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price > 5:
            return price
        else:
            raise forms.ValidationError("Raw form Raise price so that it should be above 5")
