# -*- coding: utf8 -*-

from django.test import TestCase

from holonet_django.handlers import (handle_mapping_change, handle_mapping_delete,
                                     handle_recipient_change, handle_recipient_delete)
from tests.models import TestRecipientModel


class HandlersTestCase(TestCase):

    def test_recipient_handler(self):
        self.assertRaises(RuntimeError, handle_recipient_change, None, False, None)

        test_object = TestRecipientModel(email='test@holonet.no')
        self.assertRaises(RuntimeError, handle_recipient_change, test_object, False, None)  # No pk

        test_object.save()
        self.assertEquals(handle_recipient_change(test_object, True, None), (test_object.pk,
                                                                             test_object.email))

        test_object.email = 'test@holonet.no'
        self.assertEquals(handle_recipient_change(test_object, True, None), (test_object.pk,
                                                                             test_object.email))

    def test_mapping_handler(self):
        self.assertFalse(handle_mapping_change(None, False, None))

    def test_recipient_delete(self):

        test_object = TestRecipientModel(email='test@holonet.no')
        self.assertRaises(RuntimeError, handle_recipient_delete, test_object)

        test_object.save()
        self.assertEqual(handle_recipient_delete(test_object), test_object.pk)

    def test_mapping_delete(self):
        self.assertTrue(handle_mapping_delete(True))
