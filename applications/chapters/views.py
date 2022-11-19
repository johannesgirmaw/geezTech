from rest_framework import generics
from commons.authentication.permissions import CustomPermission
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
