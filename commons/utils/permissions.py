from rest_framework import permissions, serializers
from commons.authentication.models import UserPermission, GroupPermission                                        
class CustomPermission(permissions.BasePermission):
    perms_map = {
        'GET': 'can_view',
        'OPTIONS': [],
        'HEAD': [],
        'POST': 'can_create',
        'PUT': 'can_change',
        'PATCH': 'can_change',
        'DELETE': 'can_delete',
    }

    def _user_permissions(self,permissions_filter):
        users_permission = UserPermission.objects.filter( **permissions_filter)
        return users_permission.exists()

    def _group_permision(self, permissions_filter):
        permissions_filter["group__user"] = permissions_filter.pop("user")
        group_permission = GroupPermission.objects.filter(**permissions_filter)
        return group_permission.exists()


    def _permission_query(self,request_param,user,model_name):
        permissions_filter = {
            "user": user,
            request_param: True,
            'content_type__model':model_name
        }
        if self._user_permissions(permissions_filter) or self._group_permision(permissions_filter):
            return True
        return False
    def _check_permission(self, request_param,queryset, user):
        model_name = queryset.model._meta.model_name
        if isinstance(request_param, str):
            return self._permission_query(request_param, user, model_name)
        elif isinstance(request_param, list):
            if len(request_param) == 0:
                return True
            for param in request_param:
                if self._check_permission(param, queryset, user):
                    return True
        return False

    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True
        if request.method not in self.perms_map:
            raise serializers.ValidationError("The method is not allowed")
        request_param = self.perms_map[request.method]
        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
        elif hasattr(view, 'queryset'):
            queryset=view.queryset
        assert queryset is not None, (
                '{}.get_queryset() and {}.queryset returned None'.format(view.__class__.__name__,view.__class__.__name__)
        )
        return self._check_permission(request_param, queryset, user)



class IsSystemAdminUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
