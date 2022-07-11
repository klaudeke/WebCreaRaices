from pyexpat import model
from rest_framework import serializers
from core.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idCategoria','descripProducto','glosaProducto','precio','stock','imagen']
        