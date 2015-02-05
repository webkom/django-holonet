# -*- coding: utf8 -*-

import sys

from django.conf import settings


class Settings(object):

    CONFIGS = {
        'API_ENDPIONTS': {
            'sender_blacklist': '/sender-blacklist/',
            'domain_blacklist': '/domain-blacklist/',
        },
        'TESTING': 'test' in sys.argv
    }

    def __getattr__(self, item):
        asked_attribute = self.CONFIGS.get(item, None)
        if asked_attribute is None:
            asked_attribute = getattr(settings, 'HOLONET_%s' % item, None)
            if asked_attribute is None:
                raise AttributeError('Please set HOLONET_%s in your project settings.' % item)
        return asked_attribute

holonet_settings = Settings()
