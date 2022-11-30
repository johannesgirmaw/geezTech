import uuid
from django.db import models
from commons.utils.model_utils import CommonsModel

# Create your models here.


class Category(CommonsModel):
    parent= models.ForeignKey("self",on_delete=models.DO_NOTHING,null=True,related_name='parent_category')
    category_name =models.CharField(max_length=50)
    description =  models.CharField( max_length=50)
    category_image = models.ImageField(upload_to="category/", height_field=None, width_field=None, max_length=None)
    class Meta:
        ordering = ('category_name', 'description')

    def __str__(self) -> str:
        return self.category_name
