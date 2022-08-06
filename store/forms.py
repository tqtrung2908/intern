from django.forms import ModelForm
from django.forms import fields
from django import forms
from .models import Product, Category, Image
#so 7 wednesday lam form


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'category',
            'description',
            'price',
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title', 'parent'
        ]


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label="Image")

    class Meta:
        model = Image
        fields = ['image']

