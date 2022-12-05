from rest_framework import serializers
from applications.chapters.models import Chapter
from rest_framework.validators import UniqueTogetherValidator


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = ['id', 'chapter_name', 'chapter_title',
                  'chapter_number', 'course', 'get_absolute_url']
        validators = [
            UniqueTogetherValidator(
                queryset=Chapter.objects.all(),
                fields=['chapter_name', 'chapter_title', 'course', ]
            )
        ]
