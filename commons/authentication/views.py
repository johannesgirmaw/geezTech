from dj_rest_auth.registration.views import RegisterView
from .serializer import CustomRegisterSerializer, UserSerializer
from rest_framework import generics
from .models import CustomUser

class CustomRegisterView(RegisterView):
    serializer_class=CustomRegisterSerializer

class ListUser(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

