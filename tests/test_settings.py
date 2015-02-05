#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from django.test.utils import override_settings

from holonet_django.settings import holonet_settings


class TestHolonetSettings(unittest.TestCase):

    def test_item_getter_no_setting(self):
        try:
            holonet_settings.ENDPOINT
        except AttributeError as e:
            self.assertIsInstance(e, AttributeError)

    @override_settings(HOLONET_ENDPOINT='test_endpoint')
    def test_setting_getter(self):
        self.assertEquals(holonet_settings.ENDPOINT, 'test_endpoint')
