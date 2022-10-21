from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "product_name",
            "description",
            "sub_category_id",
            "total_price",
            "actual_price",
            "delivery_price",
            "quantity",
            "product_image",
        )

        model = Product
