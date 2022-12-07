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
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    chapter = models.ForeignKey(
        Chapter,null=True, on_delete=models.PROTECT)

    content_number = models.IntegerField(default=0)

    content_title = models.CharField(max_length=50)
    image_url = models.ImageField(
        upload_to="course/content/content_image/", blank=True, null=True)
    doc_url = models.FileField(
        upload_to="course/content/content_document/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content_description = models.CharField(
        max_length=100, default="description")
    video_url = models.FileField(upload_to="course/content/content_video/",
                                 default=" ")

    content_creator = models.ForeignKey(
        User, null=True, on_delete=models.PROTECT, related_name="content_creator",)

    content_type = models.IntegerField(
        choices=CONTENT_TYPE, default=100)

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
