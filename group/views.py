from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import GroupSerializer
from django.http import Http404
from .models import GroupModel
from rest_framework import status, permissions

# Create your views here.

class GroupView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        serializer=GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(group_creator=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get (self,request):
        groups=GroupModel.objects.all()
        serializer=GroupSerializer(groups,many=True)
        return Response(serializer.data)
    

class SingleGroupView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,id):
        single_group=GroupModel.objects.filter(id=id)
        if single_group.exists():
            serializer=GroupSerializer(single_group,many=True)
            return Response(serializer.data)
        return Response("NO data found")
    
    