import uuid
from django.db import models
from commons.utils.model_utils import CommonsModel
from django.urls import reverse

# Create your models here.


class Category(CommonsModel):
    def uploadFiles(instance, file_name):
        url = f"category/{instance}/{file_name}"
        return url
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"pk": self.pk})
    

    def detail_url(self):
        return self.get_absolute_url()

    class Meta:
        ordering = ('category_name', 'description')

    def __str__(self) -> str:
        return self.category_name
