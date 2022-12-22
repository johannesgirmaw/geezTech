from applications.course.models import Course
from applications.course.serializers import CourseSerializer
from rest_framework import serializers
from applications.category.models import Category


class CategoryCourseSerializer(CourseSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_code', 'course_image',
                  'course_description', 'course_price', 'get_absolute_url']


class CategorySerializer(serializers.ModelSerializer):
    courses_in_category = CategoryCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'category_name', 'description',
                  'category_image', 'detail_url', 'courses_in_category',)
