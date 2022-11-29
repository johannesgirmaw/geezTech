from rest_framework import serializers
from applications.chapters.models import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    chapter_number = serializers.FloatField(read_only = True)
    detail_url = serializers.HyperlinkedIdentityField(view_name = 'chapter-detail',lookup_field = 'pk')
    class Meta:
        model = Chapter
        fields = ['detail_url','id','chapter_name', 'chapter_title','course_id','chapter_number']
