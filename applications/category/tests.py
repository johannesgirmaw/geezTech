from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Category
# Create your tests here.


class CategoryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # cls.user = get_user_model().objects.create_user(
        #   username = 'testuser',
        #   email = 'test@email.com',
        #   password='secret',
        # )

        cls.category = Category.objects.create(
            category_name="Electronics"
        )

    def test_category_model(self):
        self.assertEqual(self.category.category_name, "Electronics")
