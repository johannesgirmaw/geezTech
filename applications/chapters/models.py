import uuid
from django.db import models

# Create your models here.


class Chapter(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    chapter_name = models.CharField(max_length=50)
    Chapter_title = models.CharField(max_length=50)
    chapter_number = models.IntegerField(default=0, unique=True)

    class Meta:
        ordering = ('chapter_name', 'Chapter_title')

    def __str__(self) -> str:
        return self.chapter_name

    def save(self, *args, **kwargs):
        self.chapter_number = self.chapter_number + 1
        super().save(*args, **kwargs)
