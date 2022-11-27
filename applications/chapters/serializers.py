from rest_framework.reverse import reverse
from rest_framework import serializers
from applications.chapters.models import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Chapter
        fields = ['chapter_name', 'url']

    def get_url(self, obj):
        request = self.context.get("request")
        print("request", request.__dict__)
        return f"/applications/chapters/"
