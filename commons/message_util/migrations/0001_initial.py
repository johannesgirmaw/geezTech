# Generated by Django 4.1.1 on 2022-11-14 05:18

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('subject', models.CharField(max_length=200)),
                ('message_body', models.TextField()),
                ('recievers', models.ManyToManyField(related_name='recievers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
