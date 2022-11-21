from django.db import models
from commons.authentication.models import CustomUser
import uuid

# Create your models here.
class EmailMessage(models.Model):
    id = models.CharField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, max_length=36)
    subject = models.CharField(max_length= 200)
    message_body = models.TextField()
    recievers = models.ManyToManyField(CustomUser , related_name='recievers')

    def __str__(self):
        return self.subject


