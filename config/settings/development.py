from .base import *

# DB接続情報
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'app',
    'USER': 'root',
    'PASSWORD': 'password',
    'HOST': 'host.docker.internal',
    'PORT': '53306',
    'ATOMIC_REQUESTS': True,
  }
}