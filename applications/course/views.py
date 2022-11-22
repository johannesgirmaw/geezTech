
from commons.permission.permissions import CustomPermission
from rest_framework import generics
from .models import Course, Course_Cart, Enrollement
from .serializers import CourseSerializer, CourseCartSerializer, EnrollementSerializer
from rest_framework import filters
from commons.paginations import CustomCursorPagination


class CourseListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomCursorPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['course_name']
    # ordering_fields = ['course_name', 'course_description']


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
