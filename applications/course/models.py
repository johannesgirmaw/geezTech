from distutils.command.upload import upload
import uuid
from django.db import models
from applications.course.validations import Validations
from applications.category.models import Category
from commons.utils.enums import COURSE_LEVEL, COURSE_STATUS, COURSE_TYPE, CART_STATUS, RATING_VALUES
from elearning_backend.settings import get_env_variable
from django.urls import reverse
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
        # url = get_env_variable("DOMAIN_NAME") + relative_url
        url = 'https://geeztech-production.up.railway.app' + relative_url
        return url


class Course(CommonsModel):
    def uploadFiles(instance, file_name):
        url = f"course/course_image/{instance}/{file_name}"
        return url

    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)

    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50, null=True)
    course_image = models.ImageField(
        upload_to=uploadFiles, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    course_description = models.CharField(
        max_length=100, default="description")
    course_price = models.FloatField(
        validators=[Validations.validate_price], default=0.0)
    instructor = models.ManyToManyField(
        CustomUser)
    catagory = models.ManyToManyField(
        Category)
    course_type = models.IntegerField(
        choices=COURSE_TYPE.choices, default=COURSE_TYPE.FREE)
    course_level = models.IntegerField(
        choices=COURSE_LEVEL.choices, default=COURSE_LEVEL.BEGINNER)
    course_status = models.IntegerField(
        choices=COURSE_STATUS.choices, default=COURSE_STATUS.CREATED)

    class Meta:
        ordering = ('course_name',)
        default_permissions = ('add', 'change', 'delete')

    def __str__(self):
        return self.course_name

    def created_at(self):
        return self.create_date

    def get_absolute_url(self):
        relative_url = reverse('course_detail', args=[self.id])
        # url = get_env_variable("DOMAIN_NAME") + relative_url
        url = 'https://geeztech-production.up.railway.app' + relative_url
        return url


class Course_Cart(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users_cart')
    course = models.ForeignKey(
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
    course = models.ManyToManyField(
        Course, related_name='reviewer_course')
    comment = models.TextField(max_length=200, default="review note")
    rating = models.IntegerField(choices=RATING_VALUES)
    review_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        relative_url = reverse('course_review_detail', args=[self.id])
        url = get_env_variable("DOMAIN_NAME") + relative_url
        return url


class InstructorShare(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    min_price = models.FloatField(
        validators=[Validations.validate_price], default=0.0)
    share_percent = models.IntegerField()

    def __str__(self):
        return self.min_price
