
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "instructor_id",
            "course_name",
            "description",
            "course_code",
            "course_image",
            "created_at",
            "updated_at"
        )
        model = Course
