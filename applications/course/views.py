
from commons.authentication.permissions import CustomPermission
from rest_framework import authentication, permissions
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CourseListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    # permission_classes = [IsStaffEditorPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['course_name']
    filter_backends = [filters.SearchFilter]
    search_fields = ['course_name']

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
    permission_classes = [CustomPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
