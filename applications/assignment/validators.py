from rest_framework import serializers
from .models import Questions


def validate_question_num(value):
    if value <= 0:
        return serializers.ValidationError(f"{value} is less than zero")
    obj = Questions.objects.filter(question_num__exact = value)

    if obj.exists():
        return serializers.ValidationError(f"{value} is already exists")