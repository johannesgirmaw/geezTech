
from rest_framework import generics
from commons.authentication.permissions import CustomPermission
from .models import Answers, Options, Questions
from .serializers import AnswersSerializer, QuestionsSerializer, OptionsSerializer
from rest_framework import filters
from commons.utils.paginations import CustomCursorPagination
# Create your views here.
class DetailAnswers(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class ListAnswers(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

class DetailOptions(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer


class ListOptions(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Options.objects.order_by('?')
    serializer_class = OptionsSerializer

class DetailQuestions(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class ListQuestions(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Questions.objects.order_by('?')
    pagination_classs = CustomCursorPagination
    serializer_class = QuestionsSerializer

class OptionsOfQuestions(generics.ListAPIView):
    permission_classes = [CustomPermission]
    serializer_class = OptionsSerializer
    def get_queryset(self):
        return Options.objcets.get(id = self.kwargs.get('id')).order_by('?')
    

