from applications.course.serializers import CourseSerializer
from rest_framework import serializers
from applications.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    courses_in_category = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('category_name', 'description',
                  'category_image', 'parent_id', 'courses_in_category')
