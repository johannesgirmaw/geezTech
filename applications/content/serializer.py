
from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'chapter', 'content_number', 'content_title', 'image_url',
                  'doc_url', 'created_at', 'updated_at', 'content_description', 'video_url',
                  'content_creator', 'content_type', 'get_absolute_url')
