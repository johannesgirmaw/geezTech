# Generated by Django 4.1.1 on 2022-11-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0008_alter_chapter_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='chapter_title',
            field=models.CharField(max_length=50),
        ),
    ]