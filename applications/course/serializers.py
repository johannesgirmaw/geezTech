
from rest_framework import serializers

from applications.course_progress.serializers import CourseProgressSerializer
from .models import Course, Course_Cart, CoursePrice, Enrollement, Reviewer


class CourseSerializer(serializers.ModelSerializer):
    course_progress = CourseProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'instructor_id', 'reviewer_id', 'catagory_id', 'course_name',
                  'course_code', 'course_image', 'created_at', 'updated_at', 'course_description',
                  'course_video', 'course_price', 'assisitant_instructor_id', 'course_type', 'course_level', 'course_progress')


class CourseCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Cart
        fields = '__all__'


class EnrollementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollement
        fields = '__all__'


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        verbose_name = 'Reviewer'
        verbose_name_plural = 'Reviewers'
        fields = '__all__'


class CoursePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePrice
        verbose_name = 'CoursePrice'
        verbose_name_plural = 'CoursePrices'
        fields = '__all__'
