from django.shortcuts import render
from rest_framework import generics, permissions
from applications.category.models import Category
from applications.category.serializers import CategorySerializer
from rest_framework import filters
# Create your views here.


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCategory(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Category.objects.all().filter(category_name = 'food')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name', 'description']
