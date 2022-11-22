from django.db import models
from commons.utils.model_utils import CommonsModel
from applications.content.models import Content

# Create your models here.
class Questions(CommonsModel):
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    question_num = models.FloatField()
    question = models.TextField()
class Options(CommonsModel):
    question_id =models.ForeignKey(Questions,related_name='options', on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

class Answers(CommonsModel):
    question_id = models.OneToOneField(Questions,  on_delete=models.CASCADE)
    answer = models.ForeignKey(Options, on_delete=models.CASCADE)