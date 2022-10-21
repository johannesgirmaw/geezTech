from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'sub_category_id', 'total_price',
                    'actual_price', 'delivery_price', 'quantity', 'product_image')


# Register your models here.
admin.site.register(Product, ProductAdmin)
