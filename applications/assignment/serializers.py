from rest_framework import serializers
from .models import Answers, Questions, Options

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(read_only=True, many=True)
    class Meta:
        model = Questions
        fields = ['id','question_num','question','content_id','options']

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'