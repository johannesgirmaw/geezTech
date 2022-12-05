import uuid
from django.db import models
from applications.chapters.models import Chapter
from rest_enumfield import EnumField
from commons.utils.enums import CONTENT_TYPE
from commons.utils.model_utils import CommonsModel
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.


class Content(CommonsModel):
    chapter_id = models.OneToOneField( Chapter, on_delete=models.PROTECT)
    content_number = models.IntegerField(default=0, unique=True)
    content_title = models.CharField(max_length=50)
    image_url = models.ImageField(
        upload_to="course/content/content_image/", blank=True, null=True)
    doc_url = models.FileField(
        upload_to="course/content/content_document/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content_description = models.CharField(
        max_length=100, default="description")
    video_url = models.FileField(upload_to="course/content/content_video/",
                                 null=True,  default=" ")
    content_creator_id = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="content_creator", null=True)
    content_type = models.IntegerField(choices=CONTENT_TYPE, default=100)

    class Meta:
        ordering = ('content_title',)

    def __str__(self):
        return self.content_title
