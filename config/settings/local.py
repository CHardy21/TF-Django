
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+b0m2dqye41p-#9wd8+x8#_$$*wxeae&6cc(t7p0%l3o%zftvc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'mydb.sqlite3',
    }
}
# cuando use mysql cargar dato en el archivo my_config
# from . import my_config
# DATABASES = my_config