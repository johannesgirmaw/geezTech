from django.db import models

from commons.utils.model_utils import CommonsModel
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Feedbacks(CommonsModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    @property
    def submission_date(self):
        return self.create_date

    @property
    def username(self):
        return self.user.first_name + ' ' + self.user.middle_name + ' ' + self.user.last_name

