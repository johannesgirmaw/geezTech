from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializer import CustomRegisterSerializer, UserSerializer
from rest_framework import generics
from .models import CustomUser
from rest_framework import filters

# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from dj_rest_auth.registration.views import SocialLoginView

# class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
#     client_class = OAuth2Client

# class GoogleLogin(SocialLoginView): # if you want to use Implicit Grant, use this
#     adapter_class = GoogleOAuth2Adapter


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
