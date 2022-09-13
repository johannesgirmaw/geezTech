from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    # first_name=models.CharField(max_length=200)
    # last_name=models.CharField(max_length=200)

    age=models.IntegerField(null =True)
    def __str__(self):
        return self.first_name