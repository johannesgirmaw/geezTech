# Generated by Django 4.1.1 on 2022-11-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0005_alter_chapter_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='chapter_title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]