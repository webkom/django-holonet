# -*- coding: utf8 -*-

from django.test import TestCase

from holonet_django.handlers import handle_recipient_change


class HandlersTestCase(TestCase):

    def test_recipient_handler(self):
        self.assertFalse(handle_recipient_change(None))
