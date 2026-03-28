from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import User
from django.db import IntegrityError
# Create your views here.

class RegisterView(APIView):
    parser_classes = [JSONParser]

    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                user=User.objects.get(username=request.data['username'])
                token=Token.objects.create(user=user)
                return Response(  {'User credentials':serializer.data,"token":token.key},status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "User with this username or email already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)