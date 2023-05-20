"""
Django settings for backend project.
"""

import os
from json import loads
from pathlib import Path

import dotenv

from common.utils import str_to_bool


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Read the configuration from .env file
dotenv.read_dotenv(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str_to_bool(os.getenv("DEBUG", "true"))

ALLOWED_HOSTS = loads(os.getenv("ALLOWED_HOSTS"))

# CSRF configurations
CSRF_TRUSTED_ORIGINS = loads(os.getenv("CSRF_TRUSTED_ORIGINS", "[]"))

# Build urls inside the project
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

# Projects informations
SITE_NAME = os.getenv("SITE_NAME")
API_URI = os.getenv("API_URI").rstrip("")
APP_URI = os.getenv("APP_URI").rstrip("")
DOMAIN = os.getenv("DOMAIN").rstrip("")
FRENTEND_BASE_URL = os.getenv("FRENTEND_BASE_URL")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRDPARTY_APPS = [
    "corsheaders",
]

LOCAL_APPS = [
]

INSTALLED_APPS = DEFAULT_APPS + THIRDPARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DB_CONNECTION = os.getenv("DB_CONNECTION", "sqlite3")
DB_DATABASE = os.getenv("DB_DATABASE", "db.sqlite3")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends." + DB_CONNECTION,
        "NAME": os.path.join(BASE_DIR, DB_DATABASE)
    }
}

if DB_CONNECTION != "sqlite3":
    DATABASES["default"].update({
        "NAME": DB_DATABASE,
        "USER": os.getenv("DB_USERNAME"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT", ""),
    })


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cross-Origin Resource Sharing

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://localhost:3000$",
    r"^http://localhost:8080$",
]

# SMTP configuration

DJANGO_SMTP_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", DJANGO_SMTP_BACKEND)
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_USE_TLS = str_to_bool(os.getenv("EMAIL_USE_TLS", "true"))

# Stripe configurations

STRIPE_PK_KEY = os.getenv("STRIPE_PK_KEY")
STRIPE_SK_KEY = os.getenv("STRIPE_SK_KEY")
STRIPE_WEBHOOK_SK = os.getenv("STRIPE_WEBHOOK_SK")
