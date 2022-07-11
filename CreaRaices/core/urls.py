
from re import template
from django.contrib import admin
from xml.etree.ElementInclude import include
from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import home, productos, mantenedor_productos, nuevo_producto, mod_producto, del_producto, login


urlpatterns = [
    path('', home, name="home"),
    path('productos', productos, name="productos"),
    path('home', home, name="home"),
    path('mantenedor', mantenedor_productos, name="mantenedor"),
    path('nuevo_usuario', nuevo_producto, name="nuevo_usuario"),
    path('mod_usuario/<id>', mod_producto, name="mod_usuario"),
    path('del_usuario/<id>', del_producto, name="del_usuario"),
    path('login', login, name="login"),
    path('logout', logout_then_login, name="logout"),
]
