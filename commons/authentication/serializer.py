from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from .models import CustomUser, Group, UserPermission, GroupPermission
from django.contrib.auth.password_validation import validate_password
from difflib import SequenceMatcher
import json

# from  


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

    def validate_password2(self,value):
        if value != self.context.get('request').data.get('password1'):
            raise serializers.ValidationError("password fields didn't match.")
        return value
    def validate_password1(self,value):
        user_attributes = ("username", "first_name", "last_name", "email")
        data = self.context.get('request').data
        password  = value.lower()
        for attribute in user_attributes:
            if SequenceMatcher(a=data.get(attribute,"").lower(), b=password).ratio()>0.5:
                raise serializers.ValidationError(f"The password is too similar to the {attribute}.")
        validate_password(password)
        return value
            
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

class GroupPermissionSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        queryset =ContentType.objects.all(),
        slug_field='model'
    )
    class Meta:
        model = GroupPermission
        fields = ['group','content_type','can_view','can_change','can_create','can_delete']

class UserPermissionSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        queryset =ContentType.objects.all(),
        slug_field='model'
    )
    class Meta:
        model = UserPermission
        fields = ['id', 'user', 'content_type','can_view','can_change','can_create','can_delete']
class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    group_permission = GroupPermissionSerializer(read_only = True, many = True)
    class Meta:
        model = Group
        fields = ['id','name','group_permission','no_of_users']
class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    user_permission = serializers.SerializerMethodField(read_only = True)



    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "last_name", "email", "is_staff", "is_active",
                  "is_superuser", "last_login", "date_joined","groups",'user_permission')
    
    def get_user_permission(self ,obj):
        return   json.loads(json.dumps(list(obj.user_permission_list))) + (json.loads(json.dumps(list(obj.group_permission_list))))


