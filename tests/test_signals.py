# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.utils import override_settings
from mock import Mock, patch

from holonet_django import validators
from holonet_django.exceptions import HolonetConfigurationError
from holonet_django.signals import (add_signal_listeners, pre_save_mapping_check,
                                    pre_save_recipient_check)
from tests.models import Mapping1, TestRecipientModel


class SignalsTestCase(TestCase):

    @patch('holonet_django.handlers.handle_recipient_change')
    def test_recipient_signal(self, mock_handler):

        test_object = TestRecipientModel(username='test', email='test@holonet.no')
        test_object.save()

        mock_handler.assert_called_once_with(test_object, True, None)

    @patch('holonet_django.handlers.handle_mapping_change')
    def test_mapping_signal(self, mock_handler):
        mapping1 = Mapping1(mail_prefix='holonet_test')
        mapping1.save()
        mock_handler.assert_called_once_with(mapping1, created=True, updated_fields=None)

    @patch('holonet_django.handlers.handle_recipient_delete')
    def test_recipient_delete_signal(self, mock_handler):
        test_object = TestRecipientModel(username='test', email='test@holonet.no')
        test_object.save()
        test_object.delete()

        mock_handler.assert_called_once_with(test_object)

    def test_mapping_recipient_list_change(self):
        mapping1 = Mapping1(mail_prefix='holonet_test')
        mapping1.save()

        test_object = TestRecipientModel(username='test', email='test@holonet.no')
        test_object.save()

        mapping1.recipients.add(test_object)

    @patch('holonet_django.handlers.handle_mapping_delete')
    def test_mapping_delete_signal(self, mock_handler):
        mapping = Mapping1(mail_prefix='holonet_test')
        mapping.save()
        mapping.delete()

        mock_handler.assert_called_once_with(mapping)

    @override_settings(HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': False
        }
    })
    def test_mapping_init_no_list(self):
        self.assertRaisesMessage(
            HolonetConfigurationError,
            'recipient_relations needs to be a list of strings.',
            add_signal_listeners
        )

    @override_settings(HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': [False]
        }
    })
    def test_mapping_init_no_string_list(self):
        self.assertRaisesMessage(
            HolonetConfigurationError,
            'Each item in recipient_relations need to be a string.',
            add_signal_listeners
        )

    @override_settings(HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': ['does_not_excist_field']
        }
    })
    def test_mapping_init_list_not_field(self):
        self.assertRaisesMessage(
            HolonetConfigurationError,
            'Could not find the relation_field on the model.',
            add_signal_listeners
        )

    @override_settings(HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': ['invalid_test_field']
        }
    })
    def test_mapping_init_no_list_invalid_field(self):
        self.assertRaisesMessage(
            HolonetConfigurationError,
            'The relation field needs to be of type models.ManyToManyField',
            add_signal_listeners
        )

    def test_recipient_pre_validator(self):
        self.assertIsNone(pre_save_recipient_check(TestRecipientModel(email='test@holonet.no')))

        self.assertRaises(validators.ValidationError, pre_save_recipient_check,
                          TestRecipientModel())

    def test_mapping_pre_validation(self):
        validators.is_prefix_unique = Mock(side_effect=lambda x, y: True)

        self.assertIsNone(pre_save_mapping_check(Mapping1(mail_prefix='holonet_test')))
        self.assertRaises(validators.ValidationError, pre_save_mapping_check, Mapping1())
