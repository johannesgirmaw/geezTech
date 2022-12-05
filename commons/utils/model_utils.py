import uuid
from django.db import models

class CommonsModel(models.Model):
    id = models.CharField(primary_key=True, unique=True,default=uuid.uuid4, editable=False, max_length=36)
    create_date = models.DateField(auto_now = True)
    
    class Meta:
        abstract = True
        # ordering = ('create_date')
    