from http.client import CREATED
from lib2to3.pgen2 import token
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
#from .models import Usuario


@api_view(['POST'])
def login(request):
    
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario incorrecto")
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Password incorrecto")
    
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)




# Create your views here.
