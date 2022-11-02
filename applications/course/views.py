from .permissions import IsStaffEditorPermission
from rest_framework import authentication, permissions
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    permission_classes = [
        permissions.DjangoModelPermissions, IsStaffEditorPermission]
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
    permission_classes = [
        permissions.DjangoModelPermissions]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
