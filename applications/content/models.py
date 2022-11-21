import uuid
from django.db import models
from commons.authentication.models import CustomUser
from applications.chapters.models import Chapter
from rest_enumfield import EnumField
from commons.enums import ContentType
# Create your models here.


class Content(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    chapter_id = models.OneToOneField(
        Chapter, on_delete=models.PROTECT)

    content_number = models.IntegerField(default=0, unique=True)

    content_title = models.CharField(max_length=50)

    image_url = models.ImageField(
        upload_to="course/content/content_image/", blank=True, null=True)

    doc_url = models.FileField(
        upload_to="course/content/content_document/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    content_description = models.CharField(
        max_length=100, default="description")

    video_url = models.FileField(upload_to="course/content/content_video/",
                                 null=True,  default=" ")

    content_creator_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name="content_creator", null=True)

    content_type = EnumField(choices=ContentType, to_choice=lambda x: (
        x.value, x.name), to_repr=lambda x: x.value)

    class Meta:
        ordering = ('content_title',)

    def __str__(self):
        return self.content_title
