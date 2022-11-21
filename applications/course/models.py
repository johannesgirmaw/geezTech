from distutils.command.upload import upload
from pydoc import describe
import uuid
from django.db import models
from commons.authentication.models import CustomUser
from applications.category.models import Category
from rest_enumfield import EnumField
from commons.enums import CourseLevel, CourseType
# Create your models here.


class Course(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    instructor_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT)
    reviewer_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name="reviewer")
    catagory_id = models.ForeignKey(Category, on_delete=models.PROTECT, )
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    course_image = models.ImageField(
        upload_to="course/course_image/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_description = models.CharField(
        max_length=100, default="description")
    course_video = models.FileField(upload_to="course/course_video/",
                                    null=True,  default=" ")
    course_price_id = models.CharField(max_length=100,  default=" ")
    assisitant_instructor_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name="assistant", null=True)
    course_type = EnumField(choices=CourseType, to_choice=lambda x: (
        x.value, x.name), to_repr=lambda x: x.value)
    course_level = EnumField(choices=CourseLevel, to_choice=lambda x: (
        x.value, x.name), to_repr=lambda x: x.value)

    class Meta:
        ordering = ('course_name',)

    def __str__(self):
        return self.course_name
