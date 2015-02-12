import sys

from django.conf import settings

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    ROOT_URLCONF="holonet.urls",
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "holonet_django",
        "tests",
    ],
    MIDDLEWARE_CLASSES=[],
    SITE_ID=1,
    NOSE_ARGS=['-s'],

    HOLONET_RECIPIENT_MODEL='tests.TestRecipientModel',
    HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': ['recipients']
        },
        'tests.Mapping2': {}
    }
)

try:
    import django
    setup = django.setup
except AttributeError:
    pass
else:
    setup()


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    from django.test.runner import DiscoverRunner
    test_runner = DiscoverRunner()

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
