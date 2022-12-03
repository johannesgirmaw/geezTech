# Generated by Django 4.1.1 on 2022-12-03 09:45

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('middle_name', models.CharField(default='', max_length=200)),
            ],
            options={
                'ordering': ('username', 'first_name', 'last_name'),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('create_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('create_date', models.DateField(auto_now=True)),
                ('can_view', models.BooleanField(default=False, verbose_name='can_views')),
                ('can_change', models.BooleanField(default=False)),
                ('can_delete', models.BooleanField(default=False)),
                ('can_create', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='content type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_permission', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPermission',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('create_date', models.DateField(auto_now=True)),
                ('can_view', models.BooleanField(default=False)),
                ('can_change', models.BooleanField(default=False)),
                ('can_delete', models.BooleanField(default=False)),
                ('can_create', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='content type')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_permission', to='authentication.group', verbose_name='group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='group',
            name='group_permissions',
            field=models.ManyToManyField(blank=True, related_name='group_set', related_query_name='group', through='authentication.GroupPermission', to='contenttypes.contenttype', verbose_name='group permission'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='authentication.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', through='authentication.UserPermission', to='contenttypes.contenttype', verbose_name='user permissions'),
        ),
    ]
