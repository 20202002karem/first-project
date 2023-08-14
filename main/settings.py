"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = []
if DEBUG is False:
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS')



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "storages",
    'django_htmx',
    # 'book',
    'user',
    'recipes',
    'search',
    'articale',
]
# python manage.py startapp user
# python manage.py makemigration user
# python manage.py makemigrate  > Error 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Mysql
# install xampp, or wamp
# pip install mysqlclient
# تحتاج تنزيلها منيول  mysqlclient في حال ما نزلت 
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

#  mysql تعريف الجانكو لتاتابيز البتراضية وسوف نستخدم داتا بيز اخرا وهي 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, 'db.sqlite3')),
    }
}
# رن سيرفير > HOST > PORT > USERandPASSWORD > databases يبحث عن اسم 
# DATABASES = {
#     'default':{
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'project_1',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': ''
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfile-cdn')

# https://trydjango3.nyc3.digitaloceanspaces.com


from .cdn.conf import *  # noqa

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfile-cdn/uploads')




AUTH_USER_MODEL = 'user.User'
# app.moddel


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'









