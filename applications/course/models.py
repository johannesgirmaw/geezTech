from distutils.command.upload import upload
from pydoc import describe
import uuid
from django.db import models
from django.conf import settings

# Create your models here.


class Course(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    instructor_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # reviewer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    description = models.TextField()
    course_code = models.CharField(max_length=50)
    course_image = models.ImageField(
        upload_to="uploads/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name
