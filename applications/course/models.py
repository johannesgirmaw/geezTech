from distutils.command.upload import upload
import uuid
from django.db import models
from applications.course.validations import Validations
from applications.category.models import Category
from commons.utils.enums import COURE_LEVEL, COURSE_TYPE, CART_STATUS, RATING_VALUES
from elearning_backend.settings import get_env_variable
from django.urls import reverse
from commons.utils.enums import COURE_LEVEL, COURSE_TYPE, CART_STATUS, RATING_VALUES
from commons.utils.model_utils import CommonsModel
from django.conf import settings
from commons.authentication.models import CustomUser
User = settings.AUTH_USER_MODEL


class CoursePrice(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    price = models.FloatField(
        validators=[Validations.validate_price], default=0.0)
    instructor_price = models.FloatField(
        validators=[Validations.validate_price])

    def get_absolute_url(self):
        relative_url = reverse('course_progress_detail', args=[self.id])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url


class Course(models.Model):
    def uploadFiles(instance, file_name):
        url = f"course/course_image/{instance}/{file_name}"
        return url

    def uploadVideoFiles(instance, file_name):
        url = f"course/course_video/{instance}/{file_name}"
        return url

    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)

    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    course_image = models.ImageField(
        upload_to=uploadFiles, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    course_description = models.CharField(
        max_length=100, default="description")
    course_video = models.FileField(upload_to=uploadVideoFiles)
    course_price = models.ForeignKey(
        CoursePrice, on_delete=models.PROTECT, related_name='course_price')
    assisitant_instructor_id = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="assistant", null=True)
    instructor = models.ForeignKey(
        User, on_delete=models.PROTECT)
    reviewer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="reviewer")
    catagory = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="category", null=True)
    course_type = models.IntegerField(choices=COURSE_TYPE, default=100)
    course_level = models.IntegerField(choices=COURE_LEVEL, default=100)

    class Meta:
        ordering = ('course_name',)
        default_permissions = ('add', 'change', 'delete')

    def __str__(self):
        return self.course_name

    def created_at(self):
        return self.create_date

    def get_absolute_url(self):
        relative_url = reverse('course_detail', args=[self.id])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url


class Course_Cart(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users_cart')
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, default=None, related_name="course_carts")
    status = models.IntegerField(choices=CART_STATUS)

    def __str__(self):
        return self.user_id

    def get_absolute_url(self):
        relative_url = reverse('course_progress_detail', args=[self.id])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url


class Enrollement(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='users_enroll')
    course = models.ForeignKey(
        Course, default=None, null=True, on_delete=models.CASCADE, related_name="course_enroll")
    enroll_start_date = models.DateField(auto_now=True)
    enroll_end_date = models.DateField()

    def get_absolute_url(self):
        relative_url = reverse('course_enroll_detail', args=[self.id])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url


class Reviewer(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    reviewer = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='users_review')
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='courses_review')
    comment = models.TextField(max_length=200, default="review note")
    rating = models.IntegerField(choices=RATING_VALUES)
    review_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        relative_url = reverse('course_review_detail', args=[self.id])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url
