from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+b0m2dqye41p-#9wd8+x8#_$$*wxeae&6cc(t7p0%l3o%zftvc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['chardy.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'mydb.sqlite3',
    }
}