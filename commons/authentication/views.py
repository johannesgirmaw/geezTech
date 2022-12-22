from dj_rest_auth.registration.views import RegisterView
from .serializer import CustomRegisterSerializer, UserSerializer, AdminRegisterSerializer, GroupSerializer, UserPermissionSerializer, EducationalBackgroundSerializer, UserDetailSerializer
from django.contrib.auth.base_user import BaseUserManager
from rest_framework import generics
from .models import CustomUser, Group, UserPermission, EducationalBackground
from rest_framework import filters
from ..utils.permissions import IsSystemAdminUser


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


class ListUser(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'first_name', 'last_name']
    ordering_fields = ['username', 'first_name', 'last_name']


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ListGroup(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DetailGroup(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CustomUserManager(generics.CreateAPIView):
    permission_classes = [IsSystemAdminUser]
    serializer_class = AdminRegisterSerializer


class ListUserPermission(generics.ListAPIView):
    permission_classes = [IsSystemAdminUser,]
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer


class DetailUserPermission(generics.RetrieveAPIView):
    permission_classes = [IsSystemAdminUser]
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer


class ListEducationalBackground(generics.ListCreateAPIView):
    permission_classes = [IsSystemAdminUser,]
    queryset = EducationalBackground.objects.all()
    serializer_class = EducationalBackgroundSerializer


class DetailEducationalBackground(generics.RetrieveAPIView):
    permission_classes = [IsSystemAdminUser]
    queryset = EducationalBackground.objects.all()
    serializer_class = EducationalBackgroundSerializer
 
class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer