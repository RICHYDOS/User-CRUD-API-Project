from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = Customers.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CustomersListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CustomersListSerializer(queryset, many=True)
        return Response(serializer.data)
