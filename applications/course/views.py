from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class CourseDetailRetrieveView(generics.RetrieveAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     lookup_field = "pk"


# class CourseDetailUpdateView(generics.UpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     lookup_field = "pk"


# class CourseDetailDestroyView(generics.DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     lookup_field = "pk"

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
