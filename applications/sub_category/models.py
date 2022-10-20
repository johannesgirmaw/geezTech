from django.db import models
from applications.category.models import Category

# Create your models here.


class SunCategory(models.Model):
    sub_category_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name
