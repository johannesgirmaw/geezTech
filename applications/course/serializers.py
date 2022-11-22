
from rest_framework import serializers
from .models import Course, Course_Cart, CoursePrice, Enrollement, Reviewer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


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
