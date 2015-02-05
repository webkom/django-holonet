# -*- coding: utf8 -*-
try:
    from django.core.exceptions import AppRegistryNotReady

    try:
        from holonet_django import signals
    except AppRegistryNotReady:
        default_app_config = 'holonet_django.apps.HolonetDjangoConfig'

except ImportError:
    AppRegistryNotReady = None
    from holonet_django import signals


