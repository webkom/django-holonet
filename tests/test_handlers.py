# -*- coding: utf8 -*-

from django.test import TestCase
from mock import Mock

from holonet_django import api, handlers
from holonet_django.exceptions import HolonetConfigrationError
from tests.models import Mapping1, TestRecipientModel


class HandlersTestCase(TestCase):

    def test_recipient_handler(self):

        self.assertRaises(HolonetConfigrationError, handlers.handle_recipient_change, None, False,
                          None)

        test_object = TestRecipientModel(email='test@holonet.no')
        self.assertRaises(HolonetConfigrationError, handlers.handle_recipient_change, test_object,
                          False, None)  # No pk

        api.change_recipient = Mock()
        test_object.save()
        api.change_recipient.assert_called_once_with(test_object.pk, test_object.email)

        api.change_recipient = Mock()
        test_object.email = 'test@holonet.no'
        handlers.handle_recipient_change(test_object, True, None)
        api.change_recipient.assert_called_once_with(test_object.pk, test_object.email)

    def test_mapping_handler(self):
        self.assertFalse(handlers.handle_mapping_change(None, False, None))

    def test_recipient_delete(self):

        test_object = TestRecipientModel(email='test@holonet.no')
        self.assertRaises(HolonetConfigrationError, handlers.handle_recipient_delete, test_object)

        api.change_recipient = Mock()
        api.delete_recipient = Mock()
        test_object.save()
        api.change_recipient.assert_called_once_with(test_object.pk, test_object.email)
        old_pk = test_object.pk
        test_object.delete()
        api.delete_recipient.assert_called_once_with(old_pk)

    def test_mapping_delete(self):
        mapping = Mapping1()

        api.delete_mapping = Mock()
        handlers.handle_mapping_delete(mapping)

        api.delete_mapping.assert_called_once_with(mapping)
