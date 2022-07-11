from django.urls import path
from rest_producto.viewsLogin import login
from rest_producto.views import api_productos

urlpatterns = [
    path('api_productos',api_productos,name="api_productos"),
    path('login',login,name="login"),
]