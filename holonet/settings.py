# -*- coding: utf8 -*-

from django.conf import settings


CLIENT_ID = getattr(settings, 'HOLONET_CLIENT_ID', None)
