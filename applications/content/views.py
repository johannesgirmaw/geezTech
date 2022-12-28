
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

    def perform_create(self, serializer):
        print(self.request.data["chapter"])

        last_content = Content.objects.filter(
            chapter=self.request.data["chapter"]).order_by("content_number").last()
        # print("last_content:", last_content.content_number)
        if last_content != None:
            last_content = last_content.content_number
        if last_content != None:
            last_content = last_content + 1
        else:
            last_content = 1

        # Since data in request is immutable, It should be copied and updated
        # print("content:------->:", content)
        print("content:-------", self.request.data)
        content = self.request.data.copy()
        print("content:-------", content)
        content["content_number"] = last_content

        content_serializer = ContentSerializer(data=content)
        if content_serializer.is_valid():
            content_serializer.save()


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
