import uuid
from django.db import models

from applications.course.models import Course
from elearning_backend.settings import get_env_variable
from django.urls import reverse
from commons.utils.model_utils import CommonsModel

# Create your models here.


class Chapter(CommonsModel):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)

    chapter_name = models.CharField(max_length=50)
    chapter_title = models.CharField(max_length=50)
    chapter_number = models.IntegerField(default=0)
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='chapters_in_courses', null=True)

    class Meta:
        ordering = ('chapter_name', 'chapter_title')

    def __str__(self) -> str:
        return self.chapter_name

    def get_absolute_url(self):
        relative_url = reverse('chapter_detail', args=[self.pk])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url
