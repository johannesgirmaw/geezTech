
from rest_framework import serializers
from .models import Course, Course_Cart,Enrollement


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