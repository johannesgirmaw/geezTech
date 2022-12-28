
from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'chapter', 'content_number', 'content_title', 'updated_at', 'content_description', 'content_type', 'url',
                  'youtube_url', 'content_creator')
