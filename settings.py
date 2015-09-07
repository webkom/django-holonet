# -*- coding: utf8 -*-

DEBUG = True
USE_TZ = True
SECRET_KEY = 'just_testing'
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
ROOT_URLCONF = "holonet.urls",
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "holonet_django",
    "tests",
]
MIDDLEWARE_CLASSES = []
SITE_ID = 1
NOSE_ARGS = ['-s']

HOLONET_API_CLIENT_ID = 'test_client_id'
HOLONET_API_CLIENT_SECRET = 'test_client_secret'
HOLONET_API_URL = 'http://127.0.0.1:8000/'
