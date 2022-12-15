"""
Django settings for elearning_backend project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path
from django.conf import settings

import django_heroku
import environ
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
env = environ.Env()
environ.Env.read_env()

DEBUG = True

if DEBUG == True:
    def get_env_variable(var_name):
        try:
            return os.getenv(var_name)
        except KeyError:
            error_msg = "set the %s environment variable" % var_name
            raise ImproperlyConfigured(error_msg)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ql8^uxw*@k5rhmq)f7ae3=4mtsy4bjr^31+99r(7096&4h(*$1'

# SECURITY WARNING: don't run with debug turned on in production!


# ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # 3rd-party apps
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'allauth.socialaccount.providers.google',
    'corsheaders',
    "drf_spectacular",
    "django_filters",
    'rest_framework_simplejwt.token_blacklist',
    # Local
    'commons.authentication.apps.AuthenticationConfig',
    'applications.course.apps.CourseConfig',
    'applications.category.apps.CategoryConfig',
    'commons.message_util.apps.MessageUtilConfig',
    'applications.chapters.apps.ChaptersConfig',
    'applications.content.apps.ContentConfig',
    'applications.assignment.apps.AssignmentConfig',
    'applications.course_progress.apps.CourseProgressConfig',
    'commons.feedback.apps.FeedbackConfig'
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "commons.utils.exceptions.api_exception_handler",
    'DEFAULT_PAGINATION_CLASS': 'commons.utils.paginations.CustomPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'elearning_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# CORS_ALLOWED_ORIGINS = (
#     "http://localhost:3000",
#     "http://localhost:8000",
# )
CORS_ALLOW_ALL_ORIGINS = True
# CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]
# CSRF_TRUSTED_ORIGINS = ["*"]

# dependencies = [
#     # migrations.swappable_dependency(settings.AUTH_USER_MODEL),
# ]

WSGI_APPLICATION = 'elearning_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elearning',
        'USER': "etech",
        "PASSWORD": "etech",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

REST_USE_JWT = True
# JWT_AUTH_COOKIE = 'my-app-auth'
# JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # new
STATIC_ROOT = BASE_DIR / "staticfiles"  # new

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# new
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
LOGIN_URL = "commons/authorize/login"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "http://localhost:3000/user/activate/12"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = None
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "elearningegeez@gmail.com"
EMAIL_HOST_PASSWORD = "qkjrcmhvqibijaio"

ACCOUNT_EMAIL_REQUIRED = True

AUTH_USER_MODEL = 'authentication.CustomUser'

SPECTACULAR_SETTINGS = {
    "TITLE": "eLearning API Project",
    "DESCRIPTION": "eLearning platform build for geezTech",
    "VERSION": "1.0.0",
    # OTHER SETTINGS
}
RESET_PASSWORD_VERIFICATION_URL = "https://geez-elearning.herokuapp.com/reset_pwd"
URL_FRONT = "https://geez-elearning.herokuapp.com/"
ACCOUNT_ADAPTER = 'commons.utils.authenticaton_utils.DefaultAccountAdapterCustom'
REGISTER_VERIFICATION_URL = "http://localhost:3000/user/activate"


REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'commons.authentication.serializer.UserSerializer',
}
# Managing refresh tokens
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=3),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    # "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=0.5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(minutes=2),
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
django_heroku.settings(locals())
