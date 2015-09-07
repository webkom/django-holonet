# -*- coding: utf8 -*-

from django.apps import AppConfig


class HolonetDjangoConfig(AppConfig):
    name = 'holonet_django'

    def ready(self):
        import holonet_django.signals  # noqa
