from django.db import models
from commons.utils.model_utils import CommonsModel
from applications.content.models import Content
from applications.course.models import Course
from django.conf import settings
from django.urls import reverse


User = settings.AUTH_USER_MODEL

# Create your models here.


class Questions(CommonsModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    question_num = models.FloatField(null=True)
    question = models.TextField()

    def __str__(self):
        return self.question


class Options(CommonsModel):
    question = models.ForeignKey(
        Questions, related_name='options', null=True, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.value

    class Meta:
        ordering = (('?'),)


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

    def __str__(self):
        return self.user


class UserQuizeResults(CommonsModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    result = models.FloatField()
    is_passed = models.BooleanField()

    def __str__(self):
        return self.user


class Certificates(CommonsModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=(
        "course"), on_delete=models.CASCADE)
    certificate_url = models.CharField(max_length=200)
    description = models.TextField()
    result = models.FloatField()

    def __str__(self):
        return f"{self.user} {self.course}"

    @property
    def certificate_date(self):
        return self.create_date

    def get_absolute_url(self):
        return reverse("certificate-detail", kwargs={"pk": self.id})

    @property
    def detail_url(self):
        return self.get_absolute_url()

    @property
    def username(self):
        return self.user.username
