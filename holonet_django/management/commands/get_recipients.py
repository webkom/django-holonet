# -*- coding: utf8 -*-

from django.core.management.base import BaseCommand

from holonet_django.settings import API_ENDPIONTS


class Command(BaseCommand):

    def print_result(self, res):
        print(res)

    def handle(self, *args, **options):
        self.print_result(API_ENDPIONTS['lists'])
