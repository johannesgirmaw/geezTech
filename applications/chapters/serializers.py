from applications.course_progress.serializers import ChapterProgressSerializer
from applications.content.serializer import ContentSerializer
from rest_framework import serializers
from applications.chapters.models import Chapter
from rest_framework.validators import UniqueTogetherValidator


class ChapterSerializer(serializers.ModelSerializer):
    contents_in_chapter = ContentSerializer(many=True, read_only=True)
    chapter_progresses_in_chapter = ChapterProgressSerializer(
        many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'chapter_name', 'chapter_title',
                  'chapter_number', 'course', 'get_absolute_url', 'contents_in_chapter', 'chapter_progresses_in_chapter']
        validators = [
            UniqueTogetherValidator(
                queryset=Chapter.objects.all(),
                fields=['chapter_name', 'chapter_title', 'course', ]
            )
        ]
