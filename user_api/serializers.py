from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username")

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name")

class CustomersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ("id", "username", "email", "date_created")

class CustomersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ("username", "email", "first_name", "last_name")