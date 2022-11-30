from distutils.command.upload import upload
import uuid
from django.db import models
from applications.course.validations import Validations
from commons.authentication.models import CustomUser
from applications.category.models import Category
from commons.enums import COURE_LEVEL, COURSE_TYPE, CART_STATUS, RATING_VALUES


class CoursePrice(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    price = models.FloatField(
        validators=[Validations.validate_price], default=0.0)
    instructor_price = models.FloatField(
        validators=[Validations.validate_price])


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
    course_price = models.ForeignKey(
        CoursePrice, on_delete=models.PROTECT, related_name='course_price')
    assisitant_instructor_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name="assistant", null=True)
    course_type = models.IntegerField(choices=COURSE_TYPE, default=100)
    course_level = models.IntegerField(choices=COURE_LEVEL, default=100)

    class Meta:
        ordering = ('course_name',)

    def __str__(self):
        return self.course_name


class Course_Cart(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='users_cart')
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, default=None, related_name="course_carts")
    status = models.IntegerField(choices=CART_STATUS)

    def __str__(self):
        return self.user_id


class Enrollement(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='users_enroll')
    course = models.ForeignKey(
        Course, default=None, null=True, on_delete=models.CASCADE, related_name="course_enroll")
    enroll_start_date = models.DateField(auto_now=True, auto_now_add=False)
    enroll_end_date = models.DateField(auto_now=False, auto_now_add=False)

    def get_absolute_url(self):
        return reverse("Enrollement_detail", kwargs={"pk": self.pk})


class Reviewer(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    reviewer_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='users_review')
    course_id = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='courses_review')
    comment = models.TextField(max_length=200, default="review note")
    rating = models.IntegerField(choices=RATING_VALUES)
    review_time = models.TimeField(auto_now=True)
    review_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment
