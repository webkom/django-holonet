# -*- coding: utf8 -*-

import sys

from django.conf import settings

from .exceptions import HolonetConfigurationError


class Settings(object):

    CONFIGS = {
        'TESTING': 'test' in sys.argv,
        'API_CLIENT_ID': None,
        'API_CLIENT_SECRET': None,
        'API_URL': None,
    }

    def __init__(self):
        """
        This function does a config test.
        :raises: ´holonet_django.exceptions.HolonetConfigurationError´
        :return: None
        """

        for key, value in self.CONFIGS.items():
            getattr(self, key)

    def __getattr__(self, item):
        if item not in self.CONFIGS.keys():
            raise HolonetConfigurationError('%s is not a valid django-holonet setting. This is '
                                            'probably a problem with the django-holonet module '
                                            'itself.' % (item, ))

        default_value = self.CONFIGS.get(item)
        settings_value = getattr(settings, 'HOLONET_%s' % item, None)

        if settings_value is not None:
            return settings_value

        if default_value is not None:
            return default_value

        raise HolonetConfigurationError('Please set HOLONET_%s in your project settings.' % item)

holonet_settings = Settings()
