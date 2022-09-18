from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, ListCreateAPIView
from .models import *
from .serializers import *

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer

class UserList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer

