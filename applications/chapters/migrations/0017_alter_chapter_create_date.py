# Generated by Django 4.1.1 on 2022-12-02 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0016_remove_chapter_create_dated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
    ]