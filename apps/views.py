from django.shortcuts import render
from .models import Category, Product, User
from .serializers import CategoryModelSerializer, ProductModelSerializer, UserModelSerializer

from rest_framework.generics import ListCreateAPIView, UpdateAPIView


class CategoryApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class UserApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer