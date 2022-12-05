from rest_framework import generics, serializers, filters
from commons.utils.permissions import CustomPermission
from applications.chapters.models import Chapter
from applications.chapters.serializers import ChapterSerializer
from rest_framework import filters
from rest_framework.response import Response

from rest_framework import serializers
import math


class DetailChapter(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def perform_update(self, serializer, *args, **kwards):
        id = self.kwargs.get('pk')
        current_chapter = Chapter.objects.get(id=id)
        chapter_num = current_chapter.chapter_number
        if self.request.query_params.get('method') == "reorder":
            previous_chapter_id = self.request.query_params.get(
                'previous_chapter_id')
            if previous_chapter_id is not None:
                previous_chapter = Chapter.objects.get(id=previous_chapter_id)
                next_chapter = Chapter.objects.filter(
                    course_id=previous_chapter.course_id, chapter_number__gt=previous_chapter.chapter_number).order_by('chapter_number').first()
                if next_chapter is None:
                    chapter_num = math.floor(
                        previous_chapter.chapter_number) + 1
                elif current_chapter != next_chapter:
                    chapter_num = (previous_chapter.chapter_number +
                                   next_chapter.chapter_number)/2
        serializer.save(chapter_number=chapter_num)


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
