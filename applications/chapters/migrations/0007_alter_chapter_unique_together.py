# Generated by Django 4.1.1 on 2022-11-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_course_course_level_course_course_type_and_more'),
        ('chapters', '0006_alter_chapter_chapter_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together={('course_id', 'chapter_number', 'chapter_name', 'chapter_title')},
        ),
    ]
