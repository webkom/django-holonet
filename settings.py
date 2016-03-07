# -*- coding: utf8 -*-

DEBUG = True
USE_TZ = True
SECRET_KEY = 'secret'
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
HOLONET_API_USERNAME = 'test'
HOLONET_API_PASSWORD = 'test'
HOLONET_API_URL = 'http://127.0.0.1:8000/'
HOLONET_DEFAULT_DOMAINS = [1]

HOLONET_RECIPIENT_MODEL = 'tests.TestRecipientModel'
HOLONET_MAPPING_MODELS = {
    'tests.Mapping1': {
        'recipient_relations': ['recipients']
    },
    'tests.Mapping2': {}
}
