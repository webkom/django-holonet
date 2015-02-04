# -*- coding: utf8 -*-

import sys

from django.conf import settings

TESTING = 'test' in sys.argv

ENDPOINT = getattr(settings, 'HOLONET_ENDPOINT', None)
CLIENT_ID = getattr(settings, 'HOLONET_CLIENT_ID', None)
CLIENT_SECRET = getattr(settings, 'HOLONET_CLIENT_SECRET', None)

API_ENDPIONTS = {
    'sender_blacklist': '/sender-blacklist/',
    'domain_blacklist': '/domain-blacklist/',
    'lists': '/lists/',
    'recipients': '/recipients/'
}
