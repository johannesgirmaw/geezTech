
from commons.authentication.serializer import UserSerializer
from rest_framework import serializers

from applications.course_progress.serializers import CourseProgressSerializer
from .models import Course, Course_Cart, CoursePrice, Enrollement, Reviewer


class CourseSerializer(serializers.ModelSerializer):
    course_progress = CourseProgressSerializer(many=True, read_only=True)
    # categorys = CategorySerializer(many=True, read_only=True)
    instructors = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        # fields = ['id',  'instructors',   'course_name', 'course_code', 'course_image',
        #           'updated_at', 'course_description',   'course_price', 'course_progress', 'get_absolute_url']


class CourseCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Cart
        fields = '__all__'


class EnrollementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollement
        fields = ('id', 'user', 'course', 'enroll_start_date',
                  'enroll_end_date', 'get_absolute_url')


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        verbose_name = 'Reviewer'
        verbose_name_plural = 'Reviewers'
        fields = ('id', 'reviewer', 'course', 'comment',
                  'rating', 'review_time', 'review_date', 'get_absolute_url')


class CoursePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePrice
        verbose_name = 'CoursePrice'
        verbose_name_plural = 'CoursePrices'
        fields = ('id', 'price', 'instructor_price', 'get_absolute_url')
