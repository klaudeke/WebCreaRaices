from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True,verbose_name='Id Categoria')
    descripCategoria = models.CharField(max_length=100,verbose_name='Descrip Categoria')
    
    def __str__(self):
        return self.descripCategoria


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True,verbose_name='Id Producto')
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripProducto = models.CharField(max_length=100,verbose_name='Descrip Producto')
    glosaProducto = models.CharField(max_length=1000,verbose_name='Glosa Producto')
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(upload_to="productos",null=True,default=None, verbose_name='Imagen Producto')

    def __str__(self):
        return self.descripProducto


