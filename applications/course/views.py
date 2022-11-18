
from commons.authentication.permissions import CustomPermission
from rest_framework import authentication, permissions
from rest_framework import generics
from .models import Course, Course_Cart, Enrollement
from .serializers import CourseSerializer, CourseCartSerializer, EnrollementSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CourseListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['course_name']
    ordering_fields = ['course_name', 'course_description']


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseCartListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Course_Cart.objects.all()
    serializer_class = CourseCartSerializer

class CourseCartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Course_Cart.objects.all()
    serializer_class = CourseCartSerializer

class EnrollementListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Enrollement.objects.all()
    serializer_class = EnrollementSerializer

class EnrollementDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Enrollement.objects.all()
    serializer_class = EnrollementSerializer