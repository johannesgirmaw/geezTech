from rest_framework import generics
from commons.permission.permissions import CustomPermission
from applications.chapters.models import Chapter
from applications.chapters.serializers import ChapterSerializer
from rest_framework import filters
from rest_framework.response import Response

from rest_framework import serializers


class DetailChapter(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class ListChapter(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['chapter_name', 'Chapter_title', 'chapter_number']
    ordering_fields = ['chapter_name', 'Chapter_title', 'chapter_number']

    def list(self, request):
        if self.request.GET.get("course_id"):
            queryset = Chapter.objects.filter(course=self.request.GET.get(
                "course_id")).order_by('chapter_number').all()
            serailizer = ChapterSerializer(queryset, many=True)
            return Response(serailizer.data)
        else:
            queryset = Chapter.objects.order_by('chapter_number').all()
            serailizer = ChapterSerializer(queryset, many=True)
            return Response(serailizer.data)

    def perform_create(self, serializer):

        if self.request.GET.get("course_id") or self.request.data["course"]:

            last_chapter = Chapter.objects.filter(course=self.request.POST.get(
                "course")).order_by("chapter_number").last()
            chapter = self.request.data
            if last_chapter != None:
                chapter_number = last_chapter.chapter_number + 1
            else:
                chapter_number = 1
            # Since get post methods return immutable dictionary
            chapter = chapter.copy()
            chapter["chapter_number"] = chapter_number

            serializer = ChapterSerializer(data=chapter)
            if serializer.is_valid():
                return super().perform_create(serializer)
        else:
            raise serializers.ValidationError(
                ('Course id is already enrolled'))
