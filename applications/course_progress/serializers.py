
from rest_framework import serializers
from .models import UserChapterProgress, UserContentProgress, UserCourseProgress


class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseProgress
        fields = '__all__'


class ChapterProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChapterProgress
        fields = '__all__'


class ContentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContentProgress
        fields = '__all__'
