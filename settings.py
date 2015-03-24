# -*- coding: utf8 -*-

DEBUG = True
USE_TZ = True
SECRET_KEY = 'justtesting'
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

HOLONET_RECIPIENT_MODEL = 'tests.TestRecipientModel'
HOLONET_MAPPING_MODELS = {
    'tests.Mapping1': {
        'recipient_relations': ['recipients']
    },
    'tests.Mapping2': {}
}

HOLONET_API_HOST = 'http://127.0.0.1:8000/api'
HOLONET_API_KEY = 'testing'
