from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class CustomUser(AbstractUser):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    middle_name = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.first_name
