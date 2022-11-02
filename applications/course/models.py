from distutils.command.upload import upload
from pydoc import describe
import uuid
from django.db import models
from commons.authentication.models import CustomUser
from applications.category.models import Category

# Create your models here.


class Course(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    instructor_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT)
    reviewer_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name ="reviewer")
    catagory_id = models.ForeignKey(Category, on_delete=models.PROTECT, )
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    course_image = models.ImageField(
        upload_to="course/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name
