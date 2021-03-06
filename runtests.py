import os
import sys

import django

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


if django.VERSION >= (1, 7):
    django.setup()


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
