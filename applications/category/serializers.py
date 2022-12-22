from applications.course.serializers import CourseSerializer
from rest_framework import serializers
from applications.category.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id",'category_name', 'description','detail_url')
