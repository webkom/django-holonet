# -*- coding: utf8 -*-

from django.test import TestCase

from holonet_django.exceptions import HolonetConfigurationError
from holonet_django.handlers import handle_recipient_change, handle_recipient_delete
from tests.models import TestRecipientModel


class HandlersTestCase(TestCase):

    def test_recipient_handler(self):
        self.assertRaises(HolonetConfigurationError, handle_recipient_change, None, False, None)

        test_object = TestRecipientModel(email='test@holonet.no')
        self.assertRaises(HolonetConfigurationError, handle_recipient_change, test_object, False,
                          None)  # No pk

    def test_recipient_delete(self):

        test_object = TestRecipientModel(email='test@holonet.no')
        self.assertRaises(HolonetConfigurationError, handle_recipient_delete, test_object)
