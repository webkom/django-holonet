# -*- coding: utf8 -*-

from django.core.management.base import BaseCommand

from holonet.settings import CLIENT_ID


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Hello holonet user! Client ID: %s' % CLIENT_ID)
