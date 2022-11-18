from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from .models import CustomUser
from django.contrib.auth.models import Group, Permission


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.save()
        return user


class AdminRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.is_staff = True
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):

    # groups = serializers.SlugRelatedField(
    #     queryset=Group.objects.all(), slug_field='name')
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    user_permissions = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "last_name", "email", "is_staff", "is_active",
                  "is_superuser", "last_login", "date_joined", 'groups', 'user_permissions')

