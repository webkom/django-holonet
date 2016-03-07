# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.utils import override_settings

from holonet_django.exceptions import HolonetConfigurationError
from holonet_django.settings import holonet_settings


class TestHolonetSettings(TestCase):

    def test_item_getter_no_setting(self):
        try:
            holonet_settings.ENDPOINT
        except HolonetConfigurationError as e:
            self.assertIsInstance(e, HolonetConfigurationError)

    @override_settings(HOLONET_API_URL='http://127.0.0.1/')
    def test_setting_getter(self):
        self.assertEquals(holonet_settings.API_URL, 'http://127.0.0.1/')
