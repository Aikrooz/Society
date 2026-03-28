from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer,UserSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import User
from django.db import IntegrityError
# Create your views here.

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})



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