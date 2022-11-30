from distutils.command.upload import upload
import uuid
from django.db import models
from applications.course.validations import Validations
from applications.category.models import Category
from commons.enums import COURE_LEVEL, COURSE_TYPE, CART_STATUS, RATING_VALUES

from commons.utils.model_utils import CommonsModel
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Course(CommonsModel):
    instructor_id = models.ForeignKey(
        User, on_delete=models.PROTECT)
    reviewer_id = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="reviewer")
    catagory_id = models.ForeignKey(Category, on_delete=models.PROTECT, )
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    course_image = models.ImageField(
        upload_to="course/course_image/"+ str(course_name), blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    course_description = models.CharField(
        max_length=100, default="description")
    course_video = models.FileField(upload_to="course/course_video/",
                                    null=True,  default=" ")
    course_price_id = models.CharField(max_length=100,  default=" ")
    assisitant_instructor_id = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="assistant", null=True)
    course_type = models.IntegerField(choices=COURSE_TYPE, default=100)
    course_level = models.IntegerField(choices=COURE_LEVEL, default=100)

    class Meta:
        ordering = ('course_name',)

    def __str__(self):
        return self.course_name


class Course_Cart(CommonsModel):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users_cart')
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, default=None, related_name="course_carts")
    status = models.IntegerField(choices=CART_STATUS)

    def __str__(self):
        return self.user_id


class Enrollement(CommonsModel):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users_enroll')
    course_id = models.ForeignKey(
        Course, default=None, null=True, on_delete=models.CASCADE, related_name="course_enroll")
    enroll_start_date = models.DateField(auto_now=True)
    enroll_end_date = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Enrollement_detail", kwargs={"pk": self.pk})


class Reviewer(CommonsModel):
    reviewer_id = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='users_review')
    course_id = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='courses_review')
    comment = models.TextField(max_length=200, default="review note")
    rating = models.IntegerField(choices=RATING_VALUES)
    review_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment


class CoursePrice(CommonsModel):
    course_id = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='courses_price')
    price = models.FloatField(
        validators=[Validations.validate_price], default=0.0)
    instructor_price = models.FloatField(
        validators=[Validations.validate_price])
