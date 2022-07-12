from django.urls import path
from rest_producto import views
from rest_producto.viewsLogin import login


urlpatterns = [
    path('api_productos',views.api_productos,name="api_productos"),
    path('login',login,name="login"),
]