from django.contrib import admin
from .models import CustomUser, Group,GroupPermission,UserPermission


# class CustomUserAdmin(admin.ModelAdmin):
#     # list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',
#     #                 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions')

#     list_display = [
#         field.name for field in CustomUser._meta.get_fields() if not field.many_to_many]


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Group)
admin.site.register(GroupPermission)
admin.site.register(UserPermission)
