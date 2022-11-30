import uuid
from django.db import models

from applications.course.models import Course

# Create your models here.


class Chapter(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)

    chapter_name = models.CharField(max_length=50)
    chapter_title = models.CharField(max_length=50)
    chapter_number = models.IntegerField(default=0)
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='courses_id', null=True)

    class Meta:
        ordering = ('chapter_name', 'chapter_title')

    def __str__(self) -> str:
        return self.chapter_name
