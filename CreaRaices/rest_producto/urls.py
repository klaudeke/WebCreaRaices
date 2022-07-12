from django.urls import path
from rest_producto import views
from rest_producto.viewslogin import loginApi


urlpatterns = [
    path('api_productos',views.api_productos,name="api_productos"),
    path('loginApi',loginApi,name="loginApi"),
]