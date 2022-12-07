from rest_framework import serializers, reverse
from .models import Answers, Questions, Options, UserAnswers, UserQuizeResults, Certificates
from .validators import validate_question_num
class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(read_only = True, many = True) 
    # url= serializers.SerializerMethodField(read_only = True)
    # permission = serializers.SerializerMethodField(read_only = True)
    url_hyperLink = serializers.HyperlinkedIdentityField(view_name = 'questions-detail', lookup_field='pk')
     
    
    class Meta:
        model = Questions
        fields = ['url_hyperLink','id',"content_id",'question','options']
    # def validate_question_num(self,value):
    #     print(value)
    #     obj = Questions.objects.filter(question_num__exact = value)
    #     if obj.exists():
    #         raise serializers.ValidationError(f"{value} is already exist")
            
    # def get_url(self,obj):
    #     print(self.context)
    #     print(obj)
    #     # print(obj.get_required_permissions)
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse.reverse("questions-detail", kwargs={"pk":obj.id},request=request)
    # # def get_permission(self,obj,mothod,model_cls):
    # #     # print(obj.get_required_permissions)
    # #     return obj.get_required_permissions(method, model_cls)

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'

class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = '__all__'

class UserQuizeResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuizeResults
        fields = '__all__'

class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = ['id','certificate_date','result','certificate_url','description','user','course','detail_url']