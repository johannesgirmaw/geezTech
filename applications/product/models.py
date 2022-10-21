from django.db import models
from applications.sub_category.models import SunCategory

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    sub_category_id = models.ForeignKey(SunCategory, on_delete=models.CASCADE)
    total_price = models.FloatField()
    actual_price = models.FloatField()
    delivery_price = models.FloatField()
    quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='media/% Y/% m/% d/')

    def __str__(self):
        return self.product_name
