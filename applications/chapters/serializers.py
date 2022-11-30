from rest_framework import serializers
from applications.chapters.models import Chapter
from rest_framework.validators import UniqueTogetherValidator


class ChapterSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'chapter_name', 'chapter_title',
                  'chapter_number', 'course', 'url']
        validators = [
            UniqueTogetherValidator(
                queryset=Chapter.objects.all(),
                fields=['chapter_name', 'chapter_title', 'course', ]
            )
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return f"/applications/chapters/"
