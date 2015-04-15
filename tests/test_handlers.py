# -*- coding: utf8 -*-
from unittest import mock

from django.test import TestCase

from holonet_django import handlers
from holonet_django.exceptions import HolonetConfigrationError
from tests.models import Mapping1, TestRecipientModel


class HandlersTestCase(TestCase):

    @mock.patch('holonet_django.api.change_recipient')
    def test_recipient_handler(self, mock_change_recipient):

        with self.assertRaises(HolonetConfigrationError):
            handlers.handle_recipient_change(None, False, None)

        test_object = TestRecipientModel(email='test@holonet.no')
        with self.assertRaises(HolonetConfigrationError):
            handlers.handle_recipient_change(test_object, False, None)  # No pk

        test_object.save()

        test_object.email = 'test2@holonet.no'
        handlers.handle_recipient_change(test_object, True, None)
        mock_change_recipient.assert_has_calls([
            mock.call(1, 'test@holonet.no'),
            mock.call(1, 'test2@holonet.no'),
        ])

    @mock.patch('holonet_django.api.delete_recipient')
    @mock.patch('holonet_django.api.change_recipient')
    def test_recipient_delete(self, mock_change_recipient, mock_delete_recipient):

        test_object = TestRecipientModel(email='test@holonet.no')
        self.assertRaises(HolonetConfigrationError, handlers.handle_recipient_delete, test_object)

        test_object.save()
        mock_change_recipient.assert_called_once_with(test_object.pk, test_object.email)
        old_pk = test_object.pk
        test_object.delete()
        mock_delete_recipient.assert_called_once_with(old_pk)

    @mock.patch('holonet_django.api.delete_mapping')
    def test_mapping_delete(self, mock_delete_mapping):
        mapping = Mapping1()
        handlers.handle_mapping_delete(mapping)
        mock_delete_mapping.assert_called_once_with(mapping)

    @mock.patch('holonet_django.api.change_mapping')
    def test_mapping_change(self):
        self.assertFalse(handlers.handle_mapping_change(None, False, None))

