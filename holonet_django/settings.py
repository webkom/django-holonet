# -*- coding: utf8 -*-

import sys

from django.conf import settings

from .exceptions import HolonetConfigrationError


class Settings(object):

    CONFIGS = {
        'API_HOST': None,
        'API_KEY': None,
        'TESTING': 'test' in sys.argv,
        'RECIPIENT_MODEL': settings.AUTH_USER_MODEL,
        'RECIPIENT_UNIQUE_IDENTIFIER_FIELD': 'pk',
        'RECIPIENT_EMAIL_FIELD': 'email',
        'MAPPING_MODELS': {
        }
    }

    def __getattr__(self, item):
        default_value = self.CONFIGS.get(item, None)
        settings_value = getattr(settings, 'HOLONET_%s' % item, None)

        if settings_value is not None:
            return settings_value

        if default_value is not None:
            return default_value

        raise HolonetConfigrationError('Please set HOLONET_%s in your project settings.' % item)

holonet_settings = Settings()
