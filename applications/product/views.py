from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class SubCategoryList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
