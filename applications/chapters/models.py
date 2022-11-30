import uuid
from django.db import models

from applications.course.models import Course
from commons.utils.model_utils import CommonsModel
# Create your models here.


class Chapter(CommonsModel):
    chapter_name = models.CharField(max_length=50 )
    chapter_title = models.CharField(max_length=50)
    chapter_number = models.FloatField(null=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
        ordering = ('chapter_name', 'chapter_title')
        unique_together =  ('course_id','chapter_number')
        unique_together = ('course_id','chapter_name')
        unique_together = ('course_id','chapter_title')

    def __str__(self) -> str:
        return self.chapter_name
