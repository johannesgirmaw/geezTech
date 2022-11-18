from dj_rest_auth.registration.views import RegisterView
from .serializer import CustomRegisterSerializer, UserSerializer, AdminRegisterSerializer
from django.contrib.auth.base_user import BaseUserManager
from rest_framework import generics
from .models import CustomUser
from rest_framework import filters
from rest_framework.permissions import IsAdminUser

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



class CustomUserManager(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminRegisterSerializer