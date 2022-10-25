from django.test import TestCase
from .models import Course

class CourseTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.course = Course.objects.create(
    course_name="A good title",
    description="Nice body content",
    )

  def test_post_model(self):
    self.assertEqual(self.course.course_name, "Java Programming")
    self.assertEqual(self.course.description, 12)
    self.assertEqual(str(self.course), "Java Programming")