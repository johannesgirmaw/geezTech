from rest_framework import generics
from commons.permission.permissions import CustomPermission
from applications.chapters.models import Chapter
from applications.chapters.serializers import ChapterSerializer
from rest_framework import filters


class DetailChapter(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class ListChapter(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['chapter_name', 'Chapter_title', 'chapter_number']
    ordering_fields = ['chapter_name', 'Chapter_title', 'chapter_number']

    def get(self, request, *args, **kwargs):
        # print("self:", self.check_permissions, "request:", dir(request),
        #       "args:", *args, "**args", **kwargs)
        pk = kwargs.get("pk")
        print("pk:", pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
