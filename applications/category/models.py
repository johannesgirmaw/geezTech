import uuid
from django.db import models
from commons.utils.model_utils import CommonsModel

# Create your models here.


class Category(models.Model):
    def uploadFiles(instance, file_name):
        url = f"category/{instance}/{file_name}"
        return url

    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, related_name='parent_category')
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category_image = models.FileField(upload_to=uploadFiles, blank=True)

    class Meta:
        ordering = ('category_name', 'description')

    def __str__(self) -> str:
        return self.category_name
