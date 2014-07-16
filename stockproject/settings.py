"""
Django settings for stockproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^ihtgspjf5k^%+=#6t#$rp)=34al7+6%sqcs*4mo$v^juiz$8l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
CRISPY_TEMPLATE_PACK = 'bootstrap3'

AUTH_USER_MODEL = 'stocks.User'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'companies'


# SEND MAIL

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'winnie.rocketu@gmail.com'
EMAIL_HOST_PASSWORD = 'testingaccount'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'winnie.rocketu@gmail.com'

# Application definition

INSTALLED_APPS = (
    'stocks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'crispy_forms',
    'debug_toolbar',
    'django.contrib.humanize',
    'actstream',
)

# ACTSTREAM_SETTINGS = {
#     'MANAGER': 'stocks.streams.MyActionManager',
#     'FETCH_RELATIONS': True,
#     'USE_PREFETCH': True,
#     'USE_JSONFIELD': True,
#     'GFK_FETCH_DEPTH': 1,
# }

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'stockproject.urls'

WSGI_APPLICATION = 'stockproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Static images files
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", *MEDIA_URL.strip("/").split("/"))


try:
    from local_settings import *
except ImportError:
    pass