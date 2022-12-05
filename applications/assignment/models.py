from django.db import models
from commons.utils.model_utils import CommonsModel
from applications.content.models import Content
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class Questions(CommonsModel):
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    question_num = models.FloatField()
    question = models.TextField()

    def __str__(self):
        return self.question


class Options(CommonsModel):
    question_id = models.ForeignKey(
        Questions, related_name='options', on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.value


class Answers(CommonsModel):
    question = models.OneToOneField(Questions,  on_delete=models.CASCADE)
    answer = models.ForeignKey(Options, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class UserAnswers(CommonsModel):
    question = models.OneToOneField(Questions,  on_delete=models.CASCADE)
    answer = models.ForeignKey(Options, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_correct = models.BooleanField()


class UserQuizeResults(CommonsModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    result = models.FloatField()
    is_passed = models.BooleanField()
