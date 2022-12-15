import uuid
from django.db import models
from elearning_backend.settings import get_env_variable
from django.urls import reverse
from commons.authentication.models import CustomUser
from applications.chapters.models import Chapter
from commons.utils.enums import CONTENT_TYPE
from commons.utils.model_utils import CommonsModel
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.


class Content(CommonsModel):
    def uploadFiles(instance, file_name):
        print(instance, file_name)
        if instance.content_type == CONTENT_TYPE.VIDEO:
            url = f"course/course_video/{instance}/{file_name}"
        elif instance.content_type == CONTENT_TYPE.DOCUMENT:
            url = f"course/document/{instance}/{file_name}"
        elif instance.content_type == CONTENT_TYPE.IMAGE:
            url = f"course/image/{instance}/{file_name}"
        elif instance.content_type == CONTENT_TYPE.QUESTION:
            url = " "
        return url

    def uploadYoutubeUrl(instance, file_name):
        if instance.content_type == CONTENT_TYPE.YOUTUBE_VIDEO:
            url = f"course/youtube_url/{instance}/{file_name}"
        else:
            url = " "
        return url

    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    chapter = models.ForeignKey(
        Chapter, related_name="contents_in_chapter", on_delete=models.PROTECT)

    content_number = models.IntegerField(default=0)

    content_title = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)
    content_description = models.CharField(
        max_length=100, default="description")
    url = models.FileField(upload_to=uploadFiles, blank=True, null=True)
    youtube_url = models.URLField(
        max_length=1000, blank=True, null=True)
    content_creator = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name="content_creator",)

    content_type = models.IntegerField(
        choices=CONTENT_TYPE.choices, default=CONTENT_TYPE.VIDEO)

    class Meta:
        ordering = ('content_title',)
        constraints = [
            models.UniqueConstraint(fields=[
                                    "content_number", "chapter_id"], name='content should be only in single chapter'),
        ]

    def __str__(self):
        return self.content_title

    def get_absolute_url(self):
        relative_url = reverse('content_Update', args=[self.pk])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url
