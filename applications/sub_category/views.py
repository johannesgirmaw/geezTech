from rest_framework import generics
from .models import SunCategory
from .serializers import SubCategorySerializer


class SubCategoryList(generics.ListCreateAPIView):
    queryset = SunCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SunCategory.objects.all()
    serializer_class = SubCategorySerializer
