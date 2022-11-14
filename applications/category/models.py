import uuid
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.CharField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, max_length=36)
    parent_id= models.ForeignKey("self",on_delete=models.DO_NOTHING,null=True,related_name='parent_category')
    category_name =models.CharField(max_length=50)
    description =  models.CharField( max_length=50)
    category_image = models.ImageField(upload_to="category/", height_field=None, width_field=None, max_length=None)
    
    def __str__(self) -> str:
        return self.category_name