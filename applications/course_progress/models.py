import uuid
from django.db import models
from applications.chapters.models import Chapter
from applications.content.models import Content

from applications.course.models import Course
from commons.authentication.models import CustomUser
from commons.enums import PROGRESS_STATUS
# Create your models here.


class UserCourseProgress(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)

    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='course_id')
    user = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='course_user')
    course_progress_status = models.IntegerField(
        choices=PROGRESS_STATUS.choices, default=PROGRESS_STATUS.STARTED)

    class Meta:
        db_table = "user_course_progress"


class UserChapterProgress(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)

    chapter = models.ForeignKey(
        Chapter, on_delete=models.PROTECT, related_name='chapter_id')
    user = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='chapter_user')
    chapter_progress_status = models.IntegerField(
        choices=PROGRESS_STATUS.choices, default=PROGRESS_STATUS.STARTED)

    class Meta:
        db_table = "user_chapter_progress"


class UserContentProgress(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)

    content = models.ForeignKey(
        Content, on_delete=models.PROTECT, related_name='content_id')
    user = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='content_user')
    content_progress_status = models.IntegerField(
        choices=PROGRESS_STATUS.choices, default=PROGRESS_STATUS.STARTED)

    class Meta:
        db_table = "user_content_progress"
