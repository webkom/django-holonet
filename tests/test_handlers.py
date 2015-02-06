# -*- coding: utf8 -*-

from django.test import TestCase

from holonet_django.handlers import handle_mapping_change, handle_recipient_change
from tests.models import TestRecipientModel


class HandlersTestCase(TestCase):

    def test_recipient_handler(self):
        self.assertRaises(RuntimeError, handle_recipient_change, None)

        test_object = TestRecipientModel()
        self.assertRaises(RuntimeError, handle_recipient_change, test_object)  # No pk

        test_object.save()
        self.assertEquals(handle_recipient_change(test_object), (test_object.pk, test_object.email))

        test_object.email = 'test@holonet.no'
        self.assertEquals(handle_recipient_change(test_object), (test_object.pk, test_object.email))

    def test_mapping_handler(self):
        self.assertFalse(handle_mapping_change(None))
