from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Producto

class productosForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'idCategoria',
            'descripProducto',
            'glosaProducto',
            'precio',
            'stock',
            'imagen'
            ]