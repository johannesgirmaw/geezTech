# Generated by Django 4.1.1 on 2022-11-22 05:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('create_date', models.DateField(auto_now=True)),
                ('question_num', models.FloatField()),
                ('question', models.TextField()),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.content')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('create_date', models.DateField(auto_now=True)),
                ('value', models.CharField(max_length=200)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.questions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('create_date', models.DateField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.options')),
                ('question_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assignment.questions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]