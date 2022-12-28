
from rest_framework import serializers
from .models import UserChapterProgress, UserContentProgress, UserCourseProgress


class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseProgress
        fields = ('id', 'course', 'user',
                  'course_progress_status')


class ChapterProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChapterProgress
        fields = ('id', 'chapter', 'user',
                  'chapter_progress_status')


class ContentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContentProgress
        fields = ("id", "content", "user",
                  "content_progress_status")
