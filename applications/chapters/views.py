from rest_framework import generics,serializers, filters
from commons.utils.permissions import CustomPermission
from applications.chapters.models import Chapter
from applications.chapters.serializers import ChapterSerializer
import math


class DetailChapter(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def perform_update(self, serializer,*args, **kwards):
        id = self.kwargs.get('pk')
        current_chapter =Chapter.objects.get(id=id)
        chapter_num = current_chapter.chapter_number
        if self.request.query_params.get('method') == "reorder":
            previous_chapter_id = self.request.query_params.get('previous_chapter_id')
            if previous_chapter_id is not None:
                previous_chapter = Chapter.objects.get(id = previous_chapter_id) 
                next_chapter = Chapter.objects.filter(course_id=previous_chapter.course_id, chapter_number__gt = previous_chapter.chapter_number).order_by('chapter_number').first()
                if next_chapter is None:
                    chapter_num = math.floor(previous_chapter.chapter_number) + 1
                elif current_chapter != next_chapter:
                    chapter_num = (previous_chapter.chapter_number + next_chapter.chapter_number)/2
        serializer.save(chapter_number = chapter_num)

class ListChapter(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['chapter_name', 'Chapter_title']
    ordering_fields = ['chapter_name', 'Chapter_title']
    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id is None:
            raise Exception('course_id is not found on parms')
        return Chapter.objects.order_by('chapter_number').filter(course_id=course_id)
    def perform_create(self, serializer):
        course_id = serializer.validated_data.get('course_id')
        last_chapter = Chapter.objects.filter(course_id = course_id).order_by('chapter_number').last()
        chapter_number = 1
        if last_chapter is not None:
            chapter_number = last_chapter.chapter_number + 1
        serializer.save(chapter_number = chapter_number)
