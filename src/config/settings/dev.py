from .base import *  # noqa
from .base import env

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
DEBUG = env.bool("DJANGO_DEBUG")
