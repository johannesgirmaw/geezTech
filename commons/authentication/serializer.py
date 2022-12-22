from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from .models import CustomUser, Group, UserPermission, GroupPermission, EducationalBackground
from .validator import validate_password1, validate_password2
import json
# from


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=200)
    middle_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200, default="")
    date_of_birth = serializers.DateField()

    def validate_password2(self, value):
        return validate_password2(self, value)

    def validate_password1(self, value):
        return validate_password1(self, value)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.middle_name = self.data.get('middle_name')
        user.date_of_birth = self.data.get('date_of_birth')
        user.save()
        return user


class AdminRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=200)
    middle_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200, default="")
    date_of_birth = serializers.DateField()

    def validate_password2(self, value):
        return validate_password2(self, value)

    def validate_password1(self, value):
        return validate_password1(self, value)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.middle_name = self.data.get('middle_name')
        user.date_of_birth = self.data.get('date_of_birth')
        user.is_superuser = True
        user.save()
        return user


class GroupPermissionSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(),
        slug_field='model'
    )

    class Meta:
        model = GroupPermission
        fields = ['group', 'content_type', 'can_view',
                  'can_change', 'can_create', 'can_delete']


class UserPermissionSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(),
        slug_field='model'
    )

    class Meta:
        model = UserPermission
        fields = ['id', 'user', 'content_type', 'can_view',
                  'can_change', 'can_create', 'can_delete']


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    group_permission = GroupPermissionSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'group_permission', 'no_of_users']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "middle_name", "last_name", "email", "profile_pic", "is_active",
                  "last_login")


class EducationalBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalBackground
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    user_permission = serializers.SerializerMethodField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    educational_background = EducationalBackgroundSerializer(
        read_only=True, many=True)

    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "middle_name", "last_name", "email", "date_of_birth", "profile_pic", "is_superuser", "is_active",
                  "last_login", "date_joined", "educational_background", 'user_permission', 'groups')

    def get_user_permission(self, obj):
        return json.loads(json.dumps(list(obj.user_permission_list))) + (json.loads(json.dumps(list(obj.group_permission_list))))
