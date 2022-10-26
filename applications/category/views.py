from django.shortcuts import render
from rest_framework import generics,permissions
from applications.category.models import Category
from applications.category.serializers import CategorySerializer

# Create your views here.
class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer