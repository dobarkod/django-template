from uuid import uuid4
from .base import *  # noqa

DEBUG = True
SECRET_KEY = uuid4().hex

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
