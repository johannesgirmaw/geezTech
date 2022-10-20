from rest_framework import serializers
from .models import SunCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "sub_category_name",
            "category_id"
        )

        model = SunCategory
