
from commons.utils.permissions import CustomPermission
from rest_framework import authentication, permissions
from rest_framework import generics
from .models import Content
from .serializer import ContentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ContentListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    # permission_classes = [IsStaffEditorPermission]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content_title']
    ordering_fields = ['content_title', 'content_description']


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
