import uuid
from django.db import models
from applications.chapters.models import Chapter
from applications.content.models import Content
from django.urls import reverse
from applications.course.models import Course
from commons.authentication.models import CustomUser
from commons.utils.enums import PROGRESS_STATUS
from elearning_backend.settings import get_env_variable


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

    def get_absolute_url(self):
        relative_url = reverse('course_progress_detail', args=[self.id])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url


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

    def get_absolute_url(self):
        relative_url = reverse('chapter_progress_detail', args=[self.id])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url


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

    def get_absolute_url(self):
        relative_url = reverse('content_progress_detail', args=[self.id])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url
